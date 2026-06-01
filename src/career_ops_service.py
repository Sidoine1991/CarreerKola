#!/usr/bin/env python3
"""
CarreerKola Career-Ops Service
Flask application for job prospection API
Runs on Render
"""

import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# ============================================
# Health Check
# ============================================

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Career-Ops",
        "version": "1.0.0"
    }), 200

# ============================================
# Status Endpoint
# ============================================

@app.route("/api/career-ops/status", methods=["GET"])
def get_status():
    """Get system status"""
    database_url = os.getenv("DATABASE_URL", "NOT SET")
    is_configured = database_url != "NOT SET"
    
    return jsonify({
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
    }), 200

# ============================================
# Profile Endpoint
# ============================================

@app.route("/api/career-ops/profile", methods=["GET"])
def get_profile():
    """Get user career profile"""
    return jsonify({
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
        "secondary_skills": ["R", "Power BI", "Excel VBA"],
        "remote_preference": "hybrid",
        "expected_salary_min": 45000,
        "expected_salary_max": 65000
    }), 200

# ============================================
# Jobs Endpoints
# ============================================

@app.route("/api/career-ops/jobs/best-matches", methods=["GET"])
def get_best_matches():
    """Get best job matches"""
    limit = int(request.args.get("limit", 5))
    offset = int(request.args.get("offset", 0))
    
    return jsonify({
        "matches": [
            {
                "job_id": 1,
                "title": "Data Analyst - M&E",
                "company": "Mercy Corps",
                "match_score": 92.5,
                "salary_min": 45000,
                "salary_max": 60000,
                "url": "https://mercycorps.org/careers",
                "remote_type": "hybrid",
                "seniority_level": "mid",
                "location": "Remote"
            }
        ],
        "total": 1,
        "limit": limit,
        "offset": offset
    }), 200

@app.route("/api/career-ops/jobs/all", methods=["GET"])
def get_all_jobs():
    """Get all jobs"""
    limit = int(request.args.get("limit", 50))
    offset = int(request.args.get("offset", 0))
    
    return jsonify({
        "jobs": [],
        "total": 0,
        "limit": limit,
        "offset": offset
    }), 200

# ============================================
# Statistics Endpoint
# ============================================

@app.route("/api/career-ops/stats", methods=["GET"])
def get_stats():
    """Get market statistics"""
    return jsonify({
        "jobs_total": 0,
        "matches_found": 0,
        "average_match_score": 0,
        "salary_stats": {
            "average_min": 45000,
            "average_max": 65000
        }
    }), 200

@app.route("/api/career-ops/scraper-runs/recent", methods=["GET"])
def get_recent_runs():
    """Get recent scraper runs"""
    return jsonify({
        "runs": [],
        "total": 0
    }), 200

# ============================================
# Root Endpoint
# ============================================

@app.route("/", methods=["GET"])
def read_root():
    """Root endpoint"""
    return jsonify({
        "service": "CarreerKola",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "status": "/api/career-ops/status",
            "profile": "/api/career-ops/profile",
            "jobs": "/api/career-ops/jobs/best-matches",
            "stats": "/api/career-ops/stats"
        }
    }), 200

# ============================================
# Error Handlers
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# ============================================
# Main Entry Point
# ============================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8001))
    app.run(host="0.0.0.0", port=port, debug=False)
