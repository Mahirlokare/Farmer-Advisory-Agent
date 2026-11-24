# System architecture

## Current MVP boundary
- React + Vite browser client.
- FastAPI application with versioned REST endpoints.
- Open-Meteo forecast adapter (no API key required for the public endpoint; observe provider terms and rate limits).
- Advisory service currently returns an explicit knowledge-base-pending response. It does not fabricate crop prescriptions.
- Disease upload endpoint validates MIME type and size, but intentionally does not diagnose until a validated model is integrated.

## Target production architecture
1. Web/PWA client with offline-first cached language packs and low-bandwidth image upload.
2. API gateway, authentication, farmer consent and rate limiting.
3. FastAPI domain services: advisory orchestration, weather, mandi, schemes, soil, disease inference and expert escalation.
4. Retrieval layer: curated ICAR, state agricultural university, KVK and government publications; document metadata, region/crop/date filters, citations and expiry.
5. PostgreSQL for users, farms, consent, sessions, advisories and audit events; pgvector or Qdrant for embeddings; object storage for consented media; Redis for cache/queues.
6. Specialist model services: crop disease vision model, retrieval-grounded language generation, speech recognition and speech synthesis. Keep model versions and evaluation sets tracked.
7. Observability: structured logs, latency/error metrics, model/data lineage, safety incident review and feedback.

## Trust and safety
- Every recommendation must cite source, region, crop, publication date and confidence.
- Separate general education from regulated pesticide/fertilizer instructions.
- Never generate chemical dosage without a verified label/source and local applicability.
- Low-confidence, out-of-distribution or severe disease cases must escalate to a human expert.
- Obtain consent before storing farmer identity, location, voice or crop images.
