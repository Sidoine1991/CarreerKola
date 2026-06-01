# CarreerKola API Reference

**Base URL:** `https://career-ops-xxxxx.onrender.com`

## Endpoints

### GET /health
Health check endpoint
**Response:** `{"status": "healthy", "service": "Career-Ops"}`

### GET /api/career-ops/status
System status and profile info
**Response includes:** database status, profile info, job counts, last scrape time

### GET /api/career-ops/profile
User career profile
**Response includes:** skills, experience, salary expectations, remote preferences

### GET /api/career-ops/jobs/best-matches?limit=5&offset=0
Top job matches for the user
**Response includes:** ranked jobs with match scores (0-100)

### GET /api/career-ops/jobs/all?limit=100&offset=0
All jobs in database (paginated)
**Query params:** limit, offset, sort

### GET /api/career-ops/stats
Market statistics and trends
**Response includes:** salary ranges, remote breakdown, top skills, company distribution

### GET /api/career-ops/scraper-runs/recent?limit=10
Recent scraper execution logs
**Response includes:** timestamp, jobs scraped, duration, sources

### POST /api/career-ops/jobs/save
Save new job to database
**Body:** job details (title, company, url, salary, location, etc.)

### POST /api/career-ops/matches/save
Save job match score
**Body:** job_id, profile_id, match_score, reasoning

---

## Examples

**cURL — Get top 5 matches:**
```bash
curl https://career-ops-xxxxx.onrender.com/api/career-ops/jobs/best-matches?limit=5
```

**Python — Get statistics:**
```python
import requests
url = "https://career-ops-xxxxx.onrender.com/api/career-ops/stats"
stats = requests.get(url).json()
print(f"Jobs: {stats['jobs_total']}, Avg Match: {stats['average_match_score']}%")
```

**JavaScript — Save job:**
```javascript
fetch('https://career-ops-xxxxx.onrender.com/api/career-ops/jobs/save', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    title: "Data Analyst",
    company: "Mercy Corps",
    url: "https://example.com/job/123",
    salary_min: 45000,
    salary_max: 60000,
    location: "Remote"
  })
})
```

---

## Error Responses

- **400** Bad Request — Missing required fields
- **404** Not Found — Resource not found
- **500** Server Error — Database or processing error

---

Last updated: 2026-06-01
