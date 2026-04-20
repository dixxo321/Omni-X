/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export default function App() {
  return (
    <div className="bg-[#0A0A0A] text-zinc-400 font-sans min-h-screen w-full overflow-hidden flex flex-col border-8 border-[#1A1A1A]">
      <header className="h-20 border-b border-zinc-800/50 flex items-center justify-between px-10 bg-[#0C0C0C]">
        <div className="flex items-center gap-4">
          <div className="w-8 h-8 bg-zinc-100 rounded-sm flex items-center justify-center">
            <div className="w-4 h-4 border-2 border-zinc-900"></div>
          </div>
          <h1 className="text-zinc-100 text-xl font-serif tracking-tight italic">OmniMesh X</h1>
          <span className="text-[10px] uppercase tracking-[0.2em] bg-zinc-800 text-zinc-400 px-2 py-1 rounded">OS Kernel v0.1.0</span>
        </div>
        <div className="flex items-center gap-8 text-[11px] uppercase tracking-widest font-medium">
          <a href="#" className="hover:text-zinc-100 transition-colors">Cognition</a>
          <a href="#" className="hover:text-zinc-100 transition-colors">Agents</a>
          <a href="#" className="text-zinc-100 border-b border-zinc-100 pb-1">Architecture</a>
          <button className="bg-zinc-100 text-zinc-950 px-5 py-2 hover:bg-zinc-200 transition-colors">Launch API</button>
        </div>
      </header>

      <main className="flex-1 flex p-10 gap-10">
        <div className="w-1/4 flex flex-col gap-6">
          <div className="p-6 border border-zinc-800 bg-[#0E0E0E] rounded-lg">
            <h3 className="text-zinc-100 font-serif italic text-lg mb-2">System Pulse</h3>
            <div className="space-y-4">
              <div className="flex justify-between items-end">
                <span className="text-[10px] uppercase tracking-tighter">Active Nodes</span>
                <span className="text-zinc-100 font-mono">48</span>
              </div>
              <div className="h-1 bg-zinc-800 w-full rounded-full overflow-hidden">
                <div className="h-full bg-emerald-500 shadow-[0_0_10px_#10b981] w-full"></div>
              </div>
              <div className="flex justify-between items-end">
                <span className="text-[10px] uppercase tracking-tighter">Engine State</span>
                <span className="text-emerald-500 font-mono text-[10px]">PRODUCTION (GLOBAL)</span>
              </div>
              <div className="flex justify-between items-end">
                <span className="text-[10px] uppercase tracking-tighter">Active Traces</span>
                <span className="text-zinc-100 font-mono">14,204</span>
              </div>
            </div>
          </div>
          <div className="flex-1 border border-zinc-800/50 p-6 rounded-lg bg-[#0E0E0E]/50">
            <h4 className="text-[10px] uppercase tracking-[0.2em] mb-4">Safety Protocol</h4>
            <ul className="space-y-3 text-xs leading-relaxed italic">
              <li className="flex gap-3"><span className="text-zinc-600 font-mono">01</span> Strict Action Gate approval for risky tools.</li>
              <li className="flex gap-3"><span className="text-zinc-600 font-mono">02</span> Memory boundary enforcement isolated by tenant.</li>
              <li className="flex gap-3"><span className="text-zinc-600 font-mono">03</span> Pre-execution structural verification of task plans.</li>
            </ul>
          </div>
        </div>

        <div className="flex-1 flex flex-col gap-8">
          <div className="flex justify-between items-end">
            <h2 className="text-4xl text-zinc-100 font-serif">Intelligence Architecture</h2>
            <p className="text-xs max-w-[300px] text-right text-zinc-500 italic uppercase leading-relaxed">
              Progressive build layers for a planetary-scale, multimodal agentic AI framework.
            </p>
          </div>

          <div className="grid grid-cols-3 gap-6 flex-1">
            <div className="border border-zinc-800 p-8 rounded-xl flex flex-col hover:border-zinc-500 transition-all cursor-default bg-[#0C0C0C]">
              <span className="text-[10px] font-mono mb-4 text-zinc-600 uppercase tracking-widest">Completed</span>
              <h3 className="text-zinc-100 font-serif italic text-2xl mb-4 underline underline-offset-8 decoration-zinc-800">Foundation</h3>
              <p className="text-sm leading-relaxed mb-6 flex-1">
                Interface layout, API bootstrapping, base abstractions, schemas, and provider routing logic constructed entirely inside the monorepo workspace.
              </p>
              <div className="flex gap-2 flex-wrap">
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Python 3.11</span>
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">FastAPI</span>
              </div>
            </div>

            <div className="border border-zinc-800 p-8 rounded-xl flex flex-col hover:border-zinc-500 transition-all cursor-default bg-[#0C0C0C]">
              <span className="text-[10px] font-mono mb-4 text-emerald-500 uppercase tracking-widest">Completed</span>
              <h3 className="text-zinc-100 font-serif italic text-2xl mb-4 underline underline-offset-8 decoration-zinc-800">Cognition</h3>
              <p className="text-sm leading-relaxed mb-6 flex-1">
                Planner heuristics, verifiable task contracts, memory abstractions, and strict action-gate governor policies instantiated securely.
              </p>
              <div className="flex gap-2 flex-wrap">
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Safety</span>
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Memory</span>
              </div>
            </div>

            <div className="border border-zinc-800 p-8 rounded-xl flex flex-col hover:border-zinc-500 transition-all cursor-default bg-[#0C0C0C]">
              <span className="text-[10px] font-mono mb-4 text-emerald-500 uppercase tracking-widest">Completed</span>
              <h3 className="text-zinc-100 font-serif italic text-2xl mb-4 underline underline-offset-8 decoration-zinc-800">Ecosystem</h3>
              <p className="text-sm leading-relaxed mb-6 flex-1">
                Independent specialist agents equipped, telemetry traces logged dynamically, eval harnesses deployed, and internal release gates locked.
              </p>
              <div className="flex gap-2 flex-wrap">
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Agents</span>
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Evals</span>
                <span className="px-2 py-1 bg-zinc-900 border border-zinc-800 text-[9px] uppercase">Gov</span>
              </div>
            </div>
          </div>
        </div>
      </main>

      <footer className="h-12 border-t border-zinc-800/50 flex items-center px-10 justify-between bg-[#0C0C0C]">
        <div className="flex gap-6 items-center">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-emerald-500"></div>
            <span className="text-[9px] uppercase tracking-widest">Orchestrator: Online</span>
          </div>
          <div className="w-px h-3 bg-zinc-800"></div>
          <span className="text-[9px] uppercase tracking-widest">Environment: Local Dev</span>
        </div>
        <div className="text-[9px] uppercase tracking-widest text-zinc-600">
          © 2026 OmniMesh Open Intelligence Lab — Built with discipline.
        </div>
      </footer>
    </div>
  );
}
