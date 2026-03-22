# Attest42

**Don’t trust AI agents. Verify them.**

![Status](https://img.shields.io/badge/status-prototype-blue)
![Backend](https://img.shields.io/badge/backend-FastAPI-green)
![Frontend](https://img.shields.io/badge/frontend-React-blue)
![Execution](https://img.shields.io/badge/execution-TEE--ready-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 What It Does

Attest42 is a verification layer for AI agent execution. It generates cryptographic attestations that prove what an AI system did, ensuring outputs are verifiable, policy-compliant, and tamper-evident.

- Executes AI tasks under defined policies  
- Generates cryptographic attestations:
  - input/output hashes  
  - policy constraints  
  - execution proof  
- Enables independent verification of results  

👉 Shifts AI from **trust-based → verification-based**

---

## 🔁 Flow

Input → Execution → Attestation → Verification

---

## 🧱 Tech Stack

- **Backend:** Python, FastAPI  
- **Frontend:** React, Vite, Tailwind  
- **Execution Layer:** Isolated runtime (TEE-ready)  
- **Attestation:** Hashing + signed receipts  
- **TEE Integration:** dstack (in progress)

---

## ⚙️ Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
````

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🔍 API

* `POST /run` → execute task + generate attestation
* `POST /verify` → verify attestation

---

## ✅ Status

* [x] End-to-end execution → attestation → verification flow
* [x] Policy-based execution control
* [x] Cryptographic attestation model (hash + signature)
* [x] Verification endpoint with integrity checks
* [x] Interactive frontend for execution + inspection
* [x] Full API integration between frontend and backend
* [x] Isolated execution layer (TEE-ready architecture)
* [x] Initial dstack setup and integration exploration

---

## 🗺️ Future Roadmap

* [ ] Full dstack-backed execution (real TEE integration)
* [ ] On-chain attestation registry
* [ ] Stronger signature schemes (BLS / aggregated proofs)
* [ ] Policy marketplace and reusable rule sets
* [ ] Multi-agent execution and cross-verification
* [ ] Real-time monitoring and audit dashboards

---

## 💡 Why It Matters

AI systems are increasingly handling sensitive data and critical actions.
Attest42 ensures their behavior is **verifiable, auditable, and trustworthy**.

---


**We prove what AI did.**
