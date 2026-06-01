# CarreerKola Deployment Guide

Complete step-by-step deployment instructions for Render + Windows Task Scheduler.

---

## ⚡ Quick Start (5 minutes)

### 1. Clone Repository
```bash
git clone https://github.com/Sidoine1991/CarreerKola.git
cd CarreerKola
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your AWS RDS credentials
```

### 4. Test Locally
```bash
python src/career_ops_service.py
# Curl in another terminal: curl http://localhost:8001/health
```

---

## 🌐 Deploy to Render (10 minutes)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Initial CarreerKola deployment"
git push origin main
```

### Step 2: Create Render Service
1. Go to [https://dashboard.render.com](https://dashboard.render.com)
2. Click **New Web Service**
3. Configure:
   - **Name:** career-ops
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python src/career_ops_service.py`

### Step 3: Add Environment Variables
In Render Dashboard → Environment:

```env
DATABASE_URL=postgresql://dbadmin:PASSWORD@trading-db.cq9suk2wcwxh.us-east-1.rds.amazonaws.com:5432/postgres
PSYCHOBOT_URL=https://psychobot-1si7.onrender.com
WHATSAPP_PHONE=+2290196911346
EMAIL_ADDRESS=syebadokpo@gmail.com
PORT=8001
LOG_LEVEL=INFO
```

### Step 4: Deploy
1. Select GitHub repo: `Sidoine1991/CarreerKola`
2. Branch: `main`
3. Auto-deploy: ON
4. Click **Create Web Service**

Render will deploy automatically (2-3 minutes).

### Step 5: Verify
```bash
# Check health
curl https://career-ops-xxxxx.onrender.com/health

# Check status
curl https://career-ops-xxxxx.onrender.com/api/career-ops/status
```

---

## 🤖 Schedule Daily Execution (Windows)

### Step 1: Create PowerShell Script
File: `D:\Dev\TradBOT\career_ops_scheduler.ps1`

```powershell
# Run daily job prospection
python D:\Dev\TradBOT\career_ops_scheduler_rds.py
```

### Step 2: Create Windows Task
1. Open **Task Scheduler**
2. **Create Basic Task**
3. Configure:
   - **Name:** CarreerKola Daily Prospection
   - **Trigger:** Daily at 06:00
   - **Action:** Start program
     - Program: `C:\Python39\python.exe`
     - Arguments: `D:\Dev\TradBOT\career_ops_scheduler_rds.py`

### Step 3: Test
```bash
# Manual test
python D:\Dev\TradBOT\career_ops_scheduler_rds.py
```

Check output:
- Jobs scraped: ~150-200
- Jobs matched: ~40-50
- Word report generated
- WhatsApp message sent

---

## 🔧 Troubleshooting

### "Database connection failed"
```bash
# Test RDS connection
psql postgresql://dbadmin:PASSWORD@trading-db.cq9suk2wcwxh.us-east-1.rds.amazonaws.com:5432/postgres
```

### "No jobs found"
- Check scraper sources are accessible
- Verify LinkedIn/Indeed not blocked
- Check logs for 403/429 errors

### "WhatsApp message not delivered"
- Verify PSYCHOBOT_URL in .env
- Check PsychoBot service is running
- Test: `curl https://psychobot-1si7.onrender.com/health`

### "Slow scraping (>5 min)"
- Reduce `MAX_JOBS_PER_SOURCE` in .env
- Increase `RATE_LIMIT_DELAY` if getting 429 errors
- Consider splitting into multiple schedules

---

## 📊 Monitoring

### Render Logs
```
https://dashboard.render.com → career-ops → Logs
```

Monitor for:
- Startup errors
- Database connection issues
- API request patterns

### Database Queries
```sql
-- Check recent scraper runs
SELECT * FROM career_ops.scraper_runs
ORDER BY run_timestamp DESC
LIMIT 10;

-- Check job matches
SELECT * FROM career_ops.job_matches
ORDER BY created_at DESC
LIMIT 10;
```

---

## 🚀 Production Checklist

- [ ] Environment variables set in Render
- [ ] Database URL tested and working
- [ ] PsychoBot service running and connected
- [ ] Windows Task Scheduler configured
- [ ] Manual test run successful
- [ ] WhatsApp message received
- [ ] Render logs monitored for errors
- [ ] Daily execution verified (overnight test)

---

## 🔄 Continuous Deployment

Render auto-deploys on every push to `main`:

```bash
git commit -m "feat: Add new job source"
git push origin main
# Render automatically redeploys within 1-2 minutes
```

---

## 📞 Support

- Email: syebadokpo@gmail.com
- WhatsApp: +229 01 96 91 13 46
- GitHub Issues: https://github.com/Sidoine1991/CarreerKola/issues

---

Last updated: 2026-06-01
