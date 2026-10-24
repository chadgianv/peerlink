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
export default function App({account, onSignOut}) {
  const [mode,setMode] = useState("tutor");
  const [name,setName] = useState(account.name);
  const [grade,setGrade] = useState(String(account.grade));
  const [subject,setSubject] = useState(account.focus);
  const [topic,setTopic] = useState(FALLBACK_SUBJECTS[account.focus][0]);
  const [time,setTime] = useState("Wednesday 3 PM");
  const [subjects,setSubjects] = useState(FALLBACK_SUBJECTS);
  const [slots,setSlots] = useState(FALLBACK_SLOTS);
  const [matches,setMatches] = useState([]);
  const [searched,setSearched] = useState(false);
  const [loading,setLoading] = useState(false);
  const [error,setError] = useState("");
  const [confirmation,setConfirmation] = useState("");
  const [requests,setRequests] = useState([]);
  const [groupRequests,setGroupRequests] = useState([]);
  const [requestError,setRequestError] = useState("");
  const [busyRequest,setBusyRequest] = useState(false);
  const activeRequest = useRef(null);

  useEffect(() => {
    const controller = new AbortController();
    request("/api/options", null, controller.signal)
      .then(data => {setSubjects(data.subjects);setSlots(data.slots);})
      .catch(() => {}); // fallback choices remain available if backend is stopped
    return () => controller.abort();
  }, []);

  async function loadRequests() {
    try {const res=await request("/api/requests?account_id="+encodeURIComponent(account.id),null);setRequests(res.requests);setRequestError("");}
    catch(e){setRequestError("Could not load demo requests. Ensure FastAPI is running. "+e.message);}
  }
  async function loadGroupRequests(){try{const data=await request("/api/group-requests?account_id="+encodeURIComponent(account.id),null);setGroupRequests(data.requests);}catch(e){setRequestError("Could not load group requests: "+e.message);}}
  useEffect(()=>{loadRequests();loadGroupRequests();},[account.id]);
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
  async function submitTutor(item) {
    if(!time || !item.slots.includes(time)){setConfirmation("Choose a schedule offered by "+item.name+" before sending the request.");return;}
    setBusyRequest(true);setRequestError("");
    try {const result=await request("/api/requests",{learner_id:account.id,tutor_id:item.id,subject,topic,preferred_slot:time});setConfirmation("Request #"+result.id+" sent to "+item.name+". Status: pending. Sign out and sign in as @"+item.account_id+" to respond.");await loadRequests();}
    catch(e){setRequestError("Could not submit tutoring request: "+e.message);}
    finally{setBusyRequest(false);}
  }
  async function decideTutor(item,status) {
    setBusyRequest(true);setRequestError("");
    try {const response=await fetch(API+"/api/requests/"+item.id,{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify({account_id:account.id,status})});
      if(!response.ok)throw new Error("HTTP "+response.status);
      await loadRequests();setConfirmation("Request #"+item.id+" "+status+". The learner can view this updated status.");}
    catch(e){setRequestError("Could not respond: "+e.message);}
    finally{setBusyRequest(false);}
  }
  async function sendGroupRequest(item) {
    setBusyRequest(true);setRequestError("");
    try {const result=await request("/api/group-requests",{account_id:account.id,group_id:item.id});setConfirmation("Group join request #"+result.id+" is pending. Sign in as @"+item.host_id+" to review.");await loadGroupRequests();}
    catch(e){setRequestError("Could not request group membership: "+e.message);}
    finally{setBusyRequest(false);}
  }
  async function decideGroup(item,status){setBusyRequest(true);setRequestError("");try{
    const res=await fetch(API+"/api/group-requests/"+item.id,{method:"PATCH",headers:{"Content-Type":"application/json"},body:JSON.stringify({account_id:account.id,status})});
    if(!res.ok)throw new Error("HTTP "+res.status+" — capacity or request state changed");
    setConfirmation("Group request #"+item.id+" "+status+".");await loadGroupRequests();
  }catch(e){setRequestError(e.message);}finally{setBusyRequest(false);}}
  function simulate(item) {
    setConfirmation(mode === "tutor" ?
      "SIMULATED tutoring request for " + item.name + ". No appointment was created and no student was notified." :
      "SIMULATED join request for " + item.name + ". No membership was created and no group was notified.");
  }

  return <div className="app">
    <header className="topbar"><div className="logo">P</div><div><b>PEERLINK Lite</b><small>Learn better, together</small></div><div className="account-chip"><span>{account.name} · Grade {account.grade}</span><button type="button" className="signout" onClick={()=>{reset();onSignOut();}}>Sign out</button></div></header>
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
            <label htmlFor="name">Demo account name</label><input id="name" readOnly required minLength={2} maxLength={60} value={name}/>
            <div className="formrow">
              <div><label htmlFor="grade">Grade</label><select id="grade" value={grade} disabled><option value="11">11</option><option value="12">12</option></select></div>
              <div><label htmlFor="subject">Subject</label><select id="subject" value={subject} onChange={e=>changeSubject(e.target.value)}>{Object.keys(subjects).map(s=><option key={s} value={s}>{s}</option>)}</select></div>
            </div>
            <label htmlFor="topic">Specific topic</label><select id="topic" value={topic} onChange={e=>{setTopic(e.target.value);reset();}}><option value="">Any topic</option>{(subjects[subject]||[]).map(t=><option key={t} value={t}>{t}</option>)}</select>
            <label htmlFor="time">Preferred schedule</label><select id="time" value={time} onChange={e=>{setTime(e.target.value);reset();}}><option value="">Any time</option>{slots.map(t=><option key={t} value={t}>{t}</option>)}</select>
            <button type="submit" className="submit" disabled={loading}>{loading?"Finding matches...":"Find " + (mode==="tutor"?"peer tutors":"study groups") + " →"}</button>
          </form>
          <p className="disclaimer">Signed in locally as a fictional student. Account switching resets the demo view; no student records are stored.</p>
        </section>
        <section className="panel results" aria-live="polite" aria-busy={loading}>
          <p className="eyebrow">STEP 02 · RECOMMENDATIONS</p><h2>{mode==="tutor"?"Peer Tutor Finder":"Study Group Finder"}</h2>
          {error && <div className="notice error" role="alert">{error}</div>}
          {requestError && <div className="notice error" role="alert">{requestError}</div>}
          {confirmation && <div className="notice success" role="status">{confirmation}</div>}
          {loading && <div className="empty"><span>⏳</span><h3>Finding matches...</h3></div>}
          {!loading && !searched && <div className="empty"><span>✦</span><h3>Learning starts with a connection.</h3><p>Choose a subject and search for fictional matches from the Python backend.</p></div>}
          {!loading && searched && matches.length === 0 && <div className="empty"><span>◇</span><h3>No shared schedule found</h3><p>No available match was found for the selected time. Try another schedule, or choose Any time to explore alternatives.</p></div>}
          {!loading && searched && matches.length > 0 && <div className="match-list">
            <p className="result-count">{matches.length} {mode==="tutor"?"peer tutors":"study groups"} found · ranked by compatibility · shared availability required when a time is selected</p>
            {matches.map((item,index)=><article className="match-card" key={item.id}>
              <div className="match-heading"><div><b>{item.name}</b><small>{mode==="tutor"?"Grade "+item.grade+" · Fictional tutor":"Study group · "+item.available_seats+" seats available"}</small></div><strong className="score">{item.score}/100</strong></div>
              {index===0 && <span className="topmatch">Top match</span>}
              <p className="match-meta">{mode==="tutor"?"Topics: "+item.topics.join(", ")+" · Times: "+item.slots.join(", "):"Topic: "+item.topic+" · Time: "+item.slot+" · Members: "+item.members+"/"+item.capacity}</p>
              <div className="reasons">{item.reasons.map((reason,i)=><span key={i}>{reason}</span>)}</div>
              <button type="button" className="request-button" onClick={()=>mode==="tutor"?submitTutor(item):sendGroupRequest(item)} disabled={busyRequest || (mode==="tutor" && item.account_id===account.id) || (mode==="group" && item.host_id===account.id)}>{mode==="tutor"?(item.account_id===account.id?"Your tutor profile":"Send tutoring request"):(item.host_id===account.id?"Your study group":"Request to join group")}</button>
            </article>)}
          </div>}
          <p className="disclaimer">Rankings are rule-based. Tutoring requests are saved locally and can be accepted by any listed tutor account; study-group join requests are saved locally and reviewed by demo group hosts. Demo identities are not authenticated.</p>
        </section>
      </div>
      <section className="panel requests-panel" aria-live="polite">
        <div className="requests-header"><div><p className="eyebrow">STEP 03 · TUTORING REQUESTS</p><h2>{"My tutoring requests & tutor inbox"}</h2></div><button type="button" className="request-button" onClick={loadRequests}>Refresh requests</button></div>
        {requests.length===0?<p className="result-count">No tutoring requests yet. Find a tutor and send a request, then enter their demo account to respond.</p>:
          <div className="match-list">{requests.map(item=><article className="match-card" key={item.id}>
            <div className="match-heading"><div><b>Request #{item.id} · {item.subject}</b><small>{item.topic||"Any topic"} · {item.slot}</small></div><strong className="score">{item.status}</strong></div>
            <p className="match-meta">From @{item.learner_id} to @{({t1:"joshua",t2:"angela",t3:"mark",t4:"sofia",t5:"patricia",t6:"daniel",t7:"lea",t8:"carlo",t9:"isabella"})[item.tutor_id]} · {item.created_at} UTC</p>
            {item.status==="accepted" && <div className="accepted-session"><strong>Session confirmed in PEERLINK demo</strong><p>Topic: {item.subject} — {item.topic||"General review"}</p><p>Agreed schedule: {item.slot}</p><p>Next step: both students should coordinate their meeting place outside this prototype. This is not a calendar booking or notification.</p><small>Reference: Tutoring request #{item.id} · Accepted</small></div>}
            {item.status==="declined" && <div className="notice error">The tutor declined this request. Please search for another available tutor.</div>}
            {({t1:"joshua",t2:"angela",t3:"mark",t4:"sofia",t5:"patricia",t6:"daniel",t7:"lea",t8:"carlo",t9:"isabella"})[item.tutor_id]===account.id && item.status==="pending" && <div className="request-actions"><button type="button" disabled={busyRequest} className="request-button" onClick={()=>decideTutor(item,"accepted")}>Accept request</button><button type="button" disabled={busyRequest} className="request-button" onClick={()=>decideTutor(item,"declined")}>Decline request</button></div>}
          </article>)}</div>}
        <p className="disclaimer">Accepted requests display a demo session confirmation with the agreed schedule. Requests are saved in local SQLite; no notifications, meeting links or real calendar bookings are created.</p>
      </section>
      <section className="panel requests-panel" aria-live="polite">
        <div className="requests-header"><div><p className="eyebrow">STEP 04 · STUDY GROUPS</p><h2>My group memberships & join requests</h2></div><button type="button" className="request-button" onClick={loadGroupRequests}>Refresh group requests</button></div>
        {groupRequests.length===0?<p className="result-count">No group requests yet. Search a study group, request to join, and switch to its host account to approve.</p>:
          <div className="match-list">{groupRequests.map(item=><article className="match-card" key={item.id}>
            <div className="match-heading"><div><b>{item.group_name}</b><small>Request #{item.id} · From @{item.learner_id} · Host @{item.host_id}</small></div><strong className="score">{item.status}</strong></div>
            {item.status==="accepted" && <div className="accepted-session"><strong>Membership confirmed in PEERLINK demo</strong><p>You are part of this fictional study group. See its listed topic and schedule in Study Group Finder. No group chat or meeting was automatically created.</p></div>}
            {item.status==="declined" && <div className="notice error">Membership request declined. Search for another group.</div>}
            {item.host_id===account.id && item.status==="pending" && <div className="request-actions"><button type="button" disabled={busyRequest} className="request-button" onClick={()=>decideGroup(item,"accepted")}>Approve member</button><button type="button" disabled={busyRequest} className="request-button" onClick={()=>decideGroup(item,"declined")}>Decline</button></div>}
          </article>)}</div>}
        <p className="disclaimer">A demo-only locally saved membership workflow. No account authentication, messaging or real school groups.</p>
      </section>
    </main><footer>PEERLINK Lite · React + Python FastAPI · Seminar prototype</footer>
  </div>;
}
