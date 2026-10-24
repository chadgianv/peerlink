import React, {useState} from "react";
import App from "./App.jsx";

// Fictional accounts are deliberately shipped with the client for an OFFLINE SEMINAR DEMO.
// They are NOT credentials, do not protect API endpoints, and must never be used for real students.
export const DEMO_ACCOUNTS = [
  {id:"alex",username:"alex",name:"Alex Rivera",grade:11,focus:"Mathematics"},
  {id:"mia",username:"mia",name:"Mia Santos",grade:12,focus:"English"},
  {id:"noah",username:"noah",name:"Noah Cruz",grade:11,focus:"Science"},
  {id:"ella",username:"ella",name:"Ella Garcia",grade:12,focus:"Filipino"},
  {id:"liam",username:"liam",name:"Liam Reyes",grade:11,focus:"Mathematics"},
  {id:"joshua",username:"joshua",name:"Joshua Reyes",grade:11,focus:"Mathematics"},
  {id:"angela",username:"angela",name:"Angela Cruz",grade:11,focus:"Mathematics"},
  {id:"mark",username:"mark",name:"Mark Santos",grade:12,focus:"Mathematics"},
  {id:"sofia",username:"sofia",name:"Sofia Garcia",grade:11,focus:"English"},
  {id:"patricia",username:"patricia",name:"Patricia Flores",grade:12,focus:"English"},
  {id:"daniel",username:"daniel",name:"Daniel Lim",grade:11,focus:"Science"},
  {id:"lea",username:"lea",name:"Lea Mendoza",grade:12,focus:"Science"},
  {id:"carlo",username:"carlo",name:"Carlo Navarro",grade:11,focus:"Filipino"},
  {id:"isabella",username:"isabella",name:"Isabella Aquino",grade:12,focus:"Filipino"}
];
const DEMO_PASSWORD = "peerlink-demo";

export default function DemoLogin() {
  const [account,setAccount] = useState(null);
  const [username,setUsername] = useState("alex");
  const [password,setPassword] = useState("");
  const [error,setError] = useState("");
  const [showPassword,setShowPassword] = useState(false);

  function signIn(event) {
    event.preventDefault();
    const selected = DEMO_ACCOUNTS.find(x=>x.username===username.trim().toLowerCase());
    if (!selected) {
      setError("Please select one of the sample accounts.");
      return;
    }
    setAccount(selected);
    setPassword("");
    setError("");
  }
  if(account) return <App key={account.id} account={account} onSignOut={()=>{setAccount(null);setPassword("");setError("");}}/>;

  return <main className="login-shell">
    <section className="login-card" aria-labelledby="login-title">
      <img className="login-brand" src="/peerlink-logo.svg" alt="PEERLINK — Learn better, together" />
      <p className="eyebrow">PEERLINK LITE · SEMINAR DEMO</p>
      <h1 id="login-title">Welcome to PEERLINK</h1>
      <p className="login-intro">Choose one of fictional students and enter the demo instantly. No password is required.</p>
      <form onSubmit={signIn} className="login-form">
        <label htmlFor="demo-user">Demo student account</label>
        <select id="demo-user" value={username} onChange={e=>{setUsername(e.target.value);setError("");}}>
          {DEMO_ACCOUNTS.map(person=><option key={person.id} value={person.username}>{person.name} · Grade {person.grade} · @{person.username}</option>)}
        </select>
        <label htmlFor="demo-pass">Demo password (optional)</label>
        <input id="demo-pass" type={showPassword?"text":"password"} autoComplete="off" value={password} onChange={e=>{setPassword(e.target.value);setError("");}} placeholder="Optional — leave blank to enter"/>
        <label className="show-password"><input type="checkbox" checked={showPassword} onChange={e=>setShowPassword(e.target.checked)}/> Show password</label>
        {error && <p className="notice error" role="alert">{error}</p>}
        <button type="submit" className="submit">Enter demo as selected student →</button>
      </form>
      <p className="demo-credentials">Demo password (if presenting the login step): <strong>{DEMO_PASSWORD}</strong>. You may also leave the password blank or enter any text — this is a demonstration, not authentication.</p>
      <p className="login-warning">This is a client-side account switcher, not secure authentication. No real student data or private accounts. Sessions reset on refresh; no records are saved.</p>
    </section>
  </main>;
}
