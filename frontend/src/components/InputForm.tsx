import { useState } from "react";

export default function InputForm({ onRun, loading }: any) {
  const [input, setInput] = useState("");

  return (
    <div className="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-2xl shadow-xl space-y-4 transition-all duration-300 hover:scale-[1.01]">
      <h2 className="text-xl font-semibold">Run Attest42</h2>

      <textarea
        className="w-full p-3 rounded-lg bg-gray-800 border border-gray-700"
        rows={4}
        placeholder="Enter input data..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button
        className="bg-gradient-to-r from-blue-500 to-purple-600 px-4 py-2 rounded-lg hover:opacity-90 transition"
        disabled={loading}
        onClick={() =>
          onRun({
            input_data: input,
            policy: {
              allowed_actions: ["summarize"],
              no_data_leakage: true,
            },
          })
        }
      >
        {loading ? "Running..." : "Run"}
      </button>
    </div>
  );
}