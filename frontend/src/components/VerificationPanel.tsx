import { useState } from "react";
import { verifyAttestation } from "../services/api";

export default function VerificationPanel({ attestation }: any) {
  const [result, setResult] = useState<any>(null);

  if (!attestation) return null;

  const handleVerify = async () => {
    const res = await verifyAttestation(attestation);
    setResult(res);
  };

  return (
    <div className="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-2xl shadow-xl space-y-4 transition-all duration-300 hover:scale-[1.01]">

      <h2 className="text-xl font-semibold">Verification</h2>

      <button
        className="bg-purple-600 px-4 py-2 rounded-lg hover:opacity-90 transition"
        onClick={handleVerify}
      >
        Verify
      </button>

      {result && (
        <div className="p-4 rounded-xl bg-black/40 border border-white/10 text-center">
          <p className="text-gray-400 text-sm">Verification Result</p>

          <p className={`text-2xl font-bold mt-2 ${
            result.valid ? "text-green-400" : "text-red-400"
          }`}>
            {result.valid ? "VALID ✓" : "INVALID ✗"}
          </p>
        </div>
      )}

    </div>
  );
}