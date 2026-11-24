from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.schemas import AdvisoryRequest, WeatherRequest
from app.services.advisory import build_advisory
from app.services.weather import get_weather

app = FastAPI(title=settings.app_name, version="0.1.0", description="Multilingual farmer decision-support API")
origins = [x.strip() for x in settings.cors_origins.split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=["GET","POST"], allow_headers=["*"])

@app.get("/health")
async def health():
    return {"status": "ok", "service": "bharat-krishi-ai", "version": "0.1.0"}

@app.get("/api/v1/languages")
async def languages():
    return [{"code":"en","name":"English"},{"code":"hi","name":"हिन्दी"},{"code":"mr","name":"मराठी"},{"code":"gu","name":"ગુજરાતી"},{"code":"ta","name":"தமிழ்"},{"code":"te","name":"తెలుగు"}]

@app.post("/api/v1/advisory")
async def advisory(request: AdvisoryRequest):
    return build_advisory(request.crop, request.location, request.question, request.language, request.soil_type)

@app.post("/api/v1/weather")
async def weather(request: WeatherRequest):
    try:
        return await get_weather(request.latitude, request.longitude)
    except httpx_error_types() as exc:
        raise HTTPException(status_code=502, detail="Weather provider is temporarily unavailable") from exc

def httpx_error_types():
    import httpx
    return (httpx.HTTPError,)

@app.post("/api/v1/disease/triage")
async def disease_triage(image: UploadFile = File(...)):
    if image.content_type not in {"image/jpeg", "image/png", "image/webp"}:
        raise HTTPException(status_code=415, detail="Upload a JPEG, PNG, or WebP image")
    content = await image.read()
    if len(content) > 8 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Image must be 8 MB or smaller")
    # No disease model is bundled. Never return a fabricated diagnosis.
    return {"status":"model_not_configured","model_ready":False,"message":"Image received. Validated crop-disease inference is not configured yet; no diagnosis has been generated. Please consult a local agricultural expert."}
