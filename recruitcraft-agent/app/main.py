from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import List, Optional
import os

app = FastAPI(title="RecruitCraft Agent API", version="0.1.0")

class JDMatch(BaseModel):
    job_title: str
    match_percentage: int = Field(ge=0, le=100)
    reason: str

class Candidate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    experience: Optional[float] = None
    role: Optional[str] = None
    skills: Optional[List[str]] = None
    education: Optional[str] = None
    location: Optional[str] = None

class AnalyzeRequest(BaseModel):
    subject: str
    resume_text: str
    # optional: a list of JD strings or references (we will plug real store later)
    jds: Optional[List[str]] = None

class AnalyzeResponse(BaseModel):
    candidate: Candidate
    top_matches: List[JDMatch]
    best_fit_jd: Optional[str] = None
    best_score: Optional[int] = None
    recommended_action: Optional[str] = None

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "recruitcraft",
        "env": {
            "LANGCHAIN_TRACING_V2": os.getenv("LANGCHAIN_TRACING_V2", "false"),
            "LANGCHAIN_PROJECT": os.getenv("LANGCHAIN_PROJECT", "")
        }
    }

@app.post("/analyze_resume", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest = Body(...)):
    """
    Placeholder implementation so infra can be verified now.
    We'll replace this with LangGraph orchestration next.
    """
    subj_lower = req.subject.lower()
    # naive “demo” scoring based on keywords just to test plumbing
    base = [
        ("SDET", 80 if "qa" in req.resume_text.lower() or "selenium" in req.resume_text.lower() else 40, "Keyword demo score"),
        ("Java Developer", 70 if "java" in req.resume_text.lower() else 35, "Keyword demo score"),
        ("UI/UX Designer", 30 if "figma" in req.resume_text.lower() else 15, "Keyword demo score"),
    ]
    # keep top-3 ≥ 0 (we’ll apply 70% filter in n8n later if desired)
    ranked = sorted(base, key=lambda x: x[1], reverse=True)[:3]
    top = [JDMatch(job_title=t, match_percentage=s, reason=r) for (t, s, r) in ranked]
    best = top[0] if top else None

    return AnalyzeResponse(
        candidate=Candidate(),
        top_matches=top,
        best_fit_jd=best.job_title if best else None,
        best_score=best.match_percentage if best else None,
        recommended_action="Shortlist for interview" if best and best.match_percentage >= 75 else "Review manually"
    )
