import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return <main className="shell"><p className="eyebrow">PHASE 0 · FOUNDATION</p><h1>PEERLINK Lite</h1><p>Peer Tutor Finder + Study Group Finder</p><p className="hint">Project foundation is ready. Student forms and matching are planned for the next phases.</p></main>;
}

createRoot(document.getElementById("root")).render(<React.StrictMode><App /></React.StrictMode>);
