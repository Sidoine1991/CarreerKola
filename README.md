# 🚀 CarreerKola — Autonomous Job Prospection & AI-Powered Career Intelligence

> **An intelligent, autonomous job discovery and analysis system powered by AI, real-time market scraping, and advanced scoring algorithms. Built for professionals seeking meaningful career opportunities.**

---

## 🎯 What Is CarreerKola?

CarreerKola is a **standalone microservice** that automates daily job prospection across multiple sources, scores opportunities against your professional profile, and delivers personalized insights via WhatsApp.

**Key Features:**
- 🔍 **Multi-source scraping** — 11+ job boards with intelligent pagination
- 🧠 **AI-powered scoring** — 8-factor weighted algorithm matching jobs to profile
- 📊 **Real-time data** — AWS RDS persistence, complete audit trail
- 🤖 **Autonomous execution** — Windows Task Scheduler at 06:00 WAT daily
- 💬 **WhatsApp delivery** — Formatted reports + job recommendations
- 🏢 **Enterprise focus** — MEAL (Monitoring & Evaluation), Data Science roles

---

## 🛠️ Quick Start

### Installation

```bash
git clone https://github.com/Sidoine1991/CarreerKola.git
cd CarreerKola
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your AWS RDS credentials
```

### Run

```bash
# Start API service
python src/career_ops_service.py

# Or run scheduler (separate terminal)
python src/career_ops_scheduler_rds.py
```

---

## 📊 Job Scoring (8 Factors)

- **40%** — Skills match
- **15%** — Experience years
- **15%** — Remote fit
- **10%** — Seniority level
- **10%** — Salary range
- **5%** — Semantic match
- **3%** — Recency
- **2%** — Source priority

---

## 🔄 Data Flow

```
06:00 WAT (Daily)
    ↓
Scrape 11 job sources
    ↓
Score against profile
    ↓
Generate Word report
    ↓
Send via WhatsApp
```

---

## 🌐 Job Sources (11)

**Tier 1 — MEAL/M&E:**
Mercy Corps, IFAD, FAO, Global Fund, GiveDirectly, Oxfam, World Bank

**Tier 2 — General:**
LinkedIn, Indeed, AngelList, RemoteOK

---

## 📈 API Endpoints

```
GET  /health
GET  /api/career-ops/status
GET  /api/career-ops/profile
GET  /api/career-ops/jobs/best-matches
GET  /api/career-ops/jobs/all
GET  /api/career-ops/stats
POST /api/career-ops/jobs/save
```

---

## 🔐 Security

✅ Environment-based credentials  
✅ No API keys required  
✅ No payment fees  
✅ Private AWS RDS storage  

---

## 📚 Documentation

- [Full README](./README_FULL.md)
- [API Reference](./docs/API_REFERENCE.md)
- [Contributing](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)

---

## 📞 Support

📧 syebadokpo@gmail.com  
💬 +229 01 96 91 13 46  
🐙 [@Sidoine1991](https://github.com/Sidoine1991)

---

**v1.0.0 — Production Ready** ✅

Built with ❤️ for career seekers who want intelligent automation
