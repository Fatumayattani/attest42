import { useState } from "react";
import InputForm from "./components/InputForm";
import ResultCard from "./components/ResultCard";
import VerificationPanel from "./components/VerificationPanel";
import { runPipeline } from "./services/api";

export default function App() {
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleRun = async (data: any) => {
    setLoading(true);
    const res = await runPipeline(data);
    setResult(res);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-950 to-gray-900 text-white flex items-center justify-center p-6">
      <div className="w-full max-w-3xl space-y-8">

        {/* Header */}
        <div className="text-center space-y-2">
          <h1 className="text-5xl font-bold tracking-tight bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
            Attest42
          </h1>
          <p className="text-gray-400 text-lg">
            Don’t trust AI agents. Verify them.
          </p>
        </div>

        <InputForm onRun={handleRun} loading={loading} />
        <ResultCard result={result} />
        <VerificationPanel attestation={result?.attestation} />

      </div>
    </div>
  );
}