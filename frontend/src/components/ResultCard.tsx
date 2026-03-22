export default function ResultCard({ result }: any) {
  if (!result) return null;

  return (
    <div className="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-2xl shadow-xl space-y-4 transition-all duration-300 hover:scale-[1.01]">

      <h2 className="text-xl font-semibold">Result</h2>

      <div>
        <p className="text-gray-400 text-sm">Output</p>
        <p className="bg-black/40 border border-white/10 p-3 rounded-lg">
          {result.output}
        </p>
      </div>

      <div className="flex items-center gap-2">
        <span className="text-gray-400 text-sm">Status:</span>
        <span className={result.blocked ? "text-red-400" : "text-green-400"}>
          {result.blocked ? "Blocked" : "Allowed"}
        </span>
      </div>

      <div>
        <p className="text-gray-400 text-sm mb-1">Attestation</p>
        <pre className="bg-black/60 border border-white/10 p-4 rounded-xl text-xs overflow-auto max-h-64">
          {JSON.stringify(result.attestation, null, 2)}
        </pre>
      </div>

    </div>
  );
}