export const runPipeline = async (data: any) => {
  const res = await fetch("http://127.0.0.1:8000/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const verifyAttestation = async (attestation: any) => {
  const res = await fetch("http://127.0.0.1:8000/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ attestation }),
  });
  return res.json();
};