import React, { useEffect, useRef, useState } from "react";
const API = import.meta.env.VITE_API_URL || ""; // same-origin /api via Vite dev proxy
const FALLBACK_SUBJECTS = {Mathematics:["Quadratic Equations","Algebra","Statistics"],English:["Grammar","Essay Writing"],Science:["Biology","Chemistry"],Filipino:["Panitikan","Pagsulat"]};
const FALLBACK_SLOTS = ["Wednesday 3 PM","Thursday 4 PM","Friday 2 PM","Monday 3 PM"];

async function request(path, body, signal) {
  const response = await fetch(API + path, {
    method: body ? "POST" : "GET",
    headers: body ? {"Content-Type":"application/json"} : {},
    body: body ? JSON.stringify(body) : undefined,
    signal
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const details = response.status >= 500 ? "Python API unavailable (HTTP " + response.status + "). Verify FastAPI on port 8000." : (typeof data.detail === "string" ? data.detail : "Please check your selections (HTTP " + response.status + ").");
    throw new Error(details);
  }
  return data;
}
export default function App() {
  const [mode,setMode] = useState("tutor");
  const [name,setName] = useState("Alex Rivera");
  const [grade,setGrade] = useState("11");
  const [subject,setSubject] = useState("Mathematics");
  const [topic,setTopic] = useState("Quadratic Equations");
  const [time,setTime] = useState("Wednesday 3 PM");
  const [subjects,setSubjects] = useState(FALLBACK_SUBJECTS);
  const [slots,setSlots] = useState(FALLBACK_SLOTS);
  const [matches,setMatches] = useState([]);
  const [searched,setSearched] = useState(false);
  const [loading,setLoading] = useState(false);
  const [error,setError] = useState("");
  const [confirmation,setConfirmation] = useState("");
  const activeRequest = useRef(null);

  useEffect(() => {
    const controller = new AbortController();
    request("/api/options", null, controller.signal)
      .then(data => {setSubjects(data.subjects);setSlots(data.slots);})
      .catch(() => {}); // fallback choices remain available if backend is stopped
    return () => controller.abort();
  }, []);

  function reset() {
    if (activeRequest.current) activeRequest.current.abort();
    setMatches([]);setSearched(false);setLoading(false);setError("");setConfirmation("");
  }
  function changeMode(next) {setMode(next);reset();}
  function changeSubject(next) {setSubject(next);setTopic("");reset();}
  async function search(event) {
    event.preventDefault();
    reset();
    const controller = new AbortController();
    activeRequest.current = controller;
    setLoading(true);
    try {
      const result = await request("/api/match/" + (mode === "tutor" ? "tutors" : "groups"), {
        subject, topic, preferred_slot:time, grade:Number(grade)
      }, controller.signal);
      if (!controller.signal.aborted) {setMatches(result.matches);setSearched(true);}
    } catch (err) {
      if (err.name !== "AbortError") setError("Cannot contact the matching API. Start FastAPI in a second terminal on port 8000, then retry. " + err.message);
    } finally {
      if (activeRequest.current === controller) {setLoading(false);activeRequest.current=null;}
    }
  }
  function simulate(item) {
    setConfirmation(mode === "tutor" ?
      "SIMULATED tutoring request for " + item.name + ". No appointment was created and no student was notified." :
      "SIMULATED join request for " + item.name + ". No membership was created and no group was notified.");
  }

  return <div className="app">
    <header className="topbar"><div className="logo">P</div><div><b>PEERLINK Lite</b><small>Learn better, together</small></div><span className="badge">PEERLINK · DEMO</span></header>
    <main className="page">
      <section className="hero"><p className="eyebrow">STUDENT-TO-STUDENT LEARNING</p><h1>Find your people.<br/><em>Learn your way.</em></h1><p>Discover a peer tutor or a study group matched to your topic and schedule. All student profiles are fictional.</p></section>
      <div className="columns">
        <section className="panel">
          <p className="eyebrow">STEP 01 · LEARNING NEEDS</p><h2>How would you like to learn?</h2>
          <div className="modes" role="group" aria-label="Learning mode">
            {[["tutor","Find a Peer Tutor","One-on-one learning"],["group","Find a Study Group","Learn with classmates"]].map(([key,title,subtitle])=>
              <button key={key} type="button" aria-pressed={mode===key} className={mode===key?"selected":""} onClick={()=>changeMode(key)}>
                <span aria-hidden="true">{key==="tutor"?"◉":"◎"}</span><strong>{title}</strong><small>{subtitle}</small>
              </button>)}
          </div>
          <form onSubmit={search}>
            <label htmlFor="name">Learner name (fictional)</label><input id="name" required minLength={2} maxLength={60} value={name} onChange={e=>{setName(e.target.value);reset();}}/>
            <div className="formrow">
              <div><label htmlFor="grade">Grade</label><select id="grade" value={grade} onChange={e=>{setGrade(e.target.value);reset();}}><option value="11">11</option><option value="12">12</option></select></div>
              <div><label htmlFor="subject">Subject</label><select id="subject" value={subject} onChange={e=>changeSubject(e.target.value)}>{Object.keys(subjects).map(s=><option key={s} value={s}>{s}</option>)}</select></div>
            </div>
            <label htmlFor="topic">Specific topic</label><select id="topic" value={topic} onChange={e=>{setTopic(e.target.value);reset();}}><option value="">Any topic</option>{(subjects[subject]||[]).map(t=><option key={t} value={t}>{t}</option>)}</select>
            <label htmlFor="time">Preferred schedule</label><select id="time" value={time} onChange={e=>{setTime(e.target.value);reset();}}><option value="">Any time</option>{slots.map(t=><option key={t} value={t}>{t}</option>)}</select>
            <button type="submit" className="submit" disabled={loading}>{loading?"Finding matches...":"Find " + (mode==="tutor"?"peer tutors":"study groups") + " →"}</button>
          </form>
          <p className="disclaimer">Use fictional names only. PEERLINK Lite does not collect or save student accounts.</p>
        </section>
        <section className="panel results" aria-live="polite" aria-busy={loading}>
          <p className="eyebrow">STEP 02 · RECOMMENDATIONS</p><h2>{mode==="tutor"?"Peer Tutor Finder":"Study Group Finder"}</h2>
          {error && <div className="notice error" role="alert">{error}</div>}
          {confirmation && <div className="notice success" role="status">{confirmation}</div>}
          {loading && <div className="empty"><span>⏳</span><h3>Finding matches...</h3></div>}
          {!loading && !searched && <div className="empty"><span>✦</span><h3>Learning starts with a connection.</h3><p>Choose a subject and search for fictional matches from the Python backend.</p></div>}
          {!loading && searched && matches.length === 0 && <div className="empty"><span>◇</span><h3>No matches found</h3><p>Try a different subject or adjust your preferences.</p></div>}
          {!loading && searched && matches.length > 0 && <div className="match-list">
            <p className="result-count">{matches.length} {mode==="tutor"?"peer tutors":"study groups"} found · ranked by compatibility</p>
            {matches.map((item,index)=><article className="match-card" key={item.id}>
              <div className="match-heading"><div><b>{item.name}</b><small>{mode==="tutor"?"Grade "+item.grade+" · Fictional tutor":"Study group · "+item.available_seats+" seats available"}</small></div><strong className="score">{item.score}/100</strong></div>
              {index===0 && <span className="topmatch">Top match</span>}
              <p className="match-meta">{mode==="tutor"?"Topics: "+item.topics.join(", ")+" · Times: "+item.slots.join(", "):"Topic: "+item.topic+" · Time: "+item.slot+" · Members: "+item.members+"/"+item.capacity}</p>
              <div className="reasons">{item.reasons.map((reason,i)=><span key={i}>{reason}</span>)}</div>
              <button type="button" className="request-button" onClick={()=>simulate(item)}>{mode==="tutor"?"Request tutoring (demo)":"Join group (demo)"}</button>
            </article>)}
          </div>}
          <p className="disclaimer">Rankings are rule-based points, not verified ability or AI confidence. Requests are simulated only.</p>
        </section>
      </div>
    </main><footer>PEERLINK Lite · React + Python FastAPI · Seminar prototype</footer>
  </div>;
}
