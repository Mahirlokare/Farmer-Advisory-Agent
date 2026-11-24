# Bharat Krishi AI — Multilingual Farmer Intelligence Platform

A Pan-India, farmer-first agricultural decision-support platform. The initial repository establishes a working MVP foundation with multilingual UI, FastAPI services, weather integration, advisory workflows, and clearly marked model/data integration boundaries.

## Vision
- Text-first multilingual assistance, designed for low-bandwidth devices.
- Crop and cultivation guidance grounded in reviewed agricultural sources.
- Weather-aware planning and market information adapters.
- Image-based crop disease triage with explicit confidence and human-escalation safeguards.
- Expandable language, crop, region, and disease catalogs.

## Initial language set
English, Hindi, Marathi, Gujarati, Tamil, and Telugu. Language coverage is an interface/configuration target; all translations and agronomic content must be reviewed before production use.

## Repository layout
See `docs/ARCHITECTURE.md` and `docs/ROADMAP.md`.

## Conversational AI configuration

The advisory endpoint uses an OpenAI-compatible chat-completions provider. It generates answers from the farmer's actual question, crop, location, soil context, selected language and recent conversation history. It is not a fixed-response FAQ bot.

Configure these variables on the backend service (never expose the key in the frontend):
- `LLM_API_KEY`: API key for the selected model provider (required).
- `LLM_BASE_URL`: provider API base URL; defaults to `https://api.openai.com/v1`.
- `LLM_MODEL`: model identifier; defaults to `gpt-4o-mini`.
- `LLM_TIMEOUT_SECONDS`: request timeout; defaults to 45.

Until `LLM_API_KEY` is configured, the API deliberately returns HTTP 503 with a clear setup message instead of pretending that a model answered. A ChatGPT subscription does not automatically include API credits.

The current model integration is inference with a configured hosted model, not custom fine-tuning. A reviewed Indian agriculture knowledge base (RAG), live mandi/scheme data connectors and a separately evaluated crop-disease vision model remain future integrations. The model must not claim these sources or capabilities are active.

## Local development
Backend: `cd backend && python -m venv .venv && pip install -r requirements.txt && uvicorn app.main:app --reload`
Frontend: `cd frontend && npm install && npm run dev`

The frontend expects `VITE_API_BASE_URL` (defaults to `http://localhost:8000`). Backend configuration is documented in `backend/.env.example`.

## Safety
This is an assistive prototype, not a substitute for local agricultural extension officers, soil testing, pesticide labels, or emergency advisories. Do not apply pesticide/fertilizer dosage from an unverified model response. Disease predictions are not enabled until a validated model is supplied.

## License
TBD — choose a license before accepting external contributions.