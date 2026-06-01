#!/usr/bin/env python3
"""
CarreerKola Career-Ops Service
FastAPI application for job prospection API
Runs on Render (port 8001)
"""

import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="CarreerKola",
    description="Autonomous job prospection & AI-powered career intelligence",
    version="1.0.0"
)

# ============================================
# Health Check
# ============================================

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Career-Ops",
        "version": "1.0.0"
    }

# ============================================
# Status Endpoint
# ============================================

@app.get("/api/career-ops/status", tags=["Status"])
def get_status():
    """Get system status and database information"""
    try:
        # Check environment
        database_url = os.getenv("DATABASE_URL", "NOT SET")
        is_configured = database_url != "NOT SET"
        
        return {
            "service": "Career-Ops",
            "database": "connected" if is_configured else "not configured",
            "profile": {
                "name": "Sidoine Yeba Dokpo",
                "experience_years": 4.5,
                "current_role": "Data Analyst + MEAL Specialist"
            },
            "jobs_total": 0,
            "matches_total": 0,
            "last_scrape": None,
            "configured": is_configured
        }
    except Exception as e:
        return {
            "service": "Career-Ops",
            "status": "error",
            "error": str(e)
        }

# ============================================
# Profile Endpoint
# ============================================

@app.get("/api/career-ops/profile", tags=["Profile"])
def get_profile():
    """Get user career profile"""
    return {
        "id": 1,
        "name": "Sidoine Yeba Dokpo",
        "email": os.getenv("EMAIL_ADDRESS", "syebadokpo@gmail.com"),
        "current_role": "Data Analyst + MEAL Specialist",
        "experience_years": 4.5,
        "primary_skills": [
            "Python",
            "SQL",
            "Data Analysis",
            "Monitoring & Evaluation"
        ],
        "secondary_skills": [
            "R",
            "Power BI",
            "Excel VBA"
        ],
        "remote_preference": "hybrid",
        "expected_salary_min": 45000,
        "expected_salary_max": 65000
    }

# ============================================
# Jobs Endpoints
# ============================================

@app.get("/api/career-ops/jobs/best-matches", tags=["Jobs"])
def get_best_matches(limit: int = 5, offset: int = 0):
    """Get best job matches for the user"""
    return {
        "matches": [
            {
                "job_id": 1,
                "title": "Data Analyst - M&E",
                "company": "Mercy Corps",
                "match_score": 92.5,
                "salary_min": 45000,
                "salary_max": 60000,
                "url": "https://mercycorps.org/careers/data-analyst",
                "remote_type": "hybrid",
                "seniority_level": "mid",
                "location": "Remote"
            }
        ],
        "total": 1,
        "limit": limit,
        "offset": offset
    }

@app.get("/api/career-ops/jobs/all", tags=["Jobs"])
def get_all_jobs(limit: int = 50, offset: int = 0):
    """Get all jobs (paginated)"""
    return {
        "jobs": [],
        "total": 0,
        "limit": limit,
        "offset": offset
    }

# ============================================
# Statistics Endpoint
# ============================================

@app.get("/api/career-ops/stats", tags=["Stats"])
def get_stats():
    """Get market statistics"""
    return {
        "jobs_total": 0,
        "matches_found": 0,
        "match_rate_percentage": 0,
        "average_match_score": 0,
        "salary_stats": {
            "average_min": 45000,
            "average_max": 65000
        },
        "remote_breakdown": {
            "remote": 0,
            "hybrid": 0,
            "onsite": 0
        }
    }

# ============================================
# Scraper Runs Endpoint
# ============================================

@app.get("/api/career-ops/scraper-runs/recent", tags=["Scraper"])
def get_recent_runs(limit: int = 10):
    """Get recent scraper execution logs"""
    return {
        "runs": [],
        "total": 0
    }

# ============================================
# Root Endpoint
# ============================================

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint - API information"""
    return {
        "service": "CarreerKola",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "status": "/api/career-ops/status",
            "profile": "/api/career-ops/profile",
            "jobs": "/api/career-ops/jobs/best-matches"
        }
    }

# ============================================
# Error Handlers
# ============================================

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": str(exc)
        }
    )

# ============================================
# Main Entry Point
# ============================================

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8001))
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
