# AI Outreach Engine

## 📦 Prerequisites

* Python 3.10+
* Virtual environment (recommended)

---

## 🔧 Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd ai-outreach-engine
```

2. Create and activate a virtual environment:

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\Activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run with Uvicorn (Recommended)

From the project root:

```bash
uvicorn src.api.main:app --reload
```

* `--reload` enables auto-restart on code changes
* App will be available at: http://127.0.0.1:8000

---

## ▶️ Run with Python Module

Alternatively, you can run the app directly:

```bash
python3 -m src.api.main
```

---

## 📁 Project Structure

```text
project/
├── src/
│   ├── api/
│   │   ├── main.py          # Entry point (FastAPI app)
│   │   └── routes/          # API route definitions
│   ├── services/            # Business logic layer
│   ├── db/                  # Database models / connections
│   └── gemini/              # AI / LLM integration layer
│
├── tests/                   # Unit and integration tests
├── requirements.txt
└── README.md
```

---

## ⚠️ Notes

* Always run commands from the **project root directory**
* Ensure `src/` contains `__init__.py` so it is recognized as a package
* Use **absolute imports** (e.g., `from src.services...`) throughout the project

---

## 🧪 Development Tips

* Use Uvicorn with `--reload` during development
* Keep business logic in `services/` and API logic in `api/`
* Avoid running files directly (e.g., `python src/api/main.py`) as it breaks imports

---

## 📬 API Docs

Once running, access interactive docs at:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## ✅ Summary

| Method  | Command                             | Use Case           |
| ------- | ----------------------------------- | ------------------ |
| Uvicorn | `uvicorn src.api.main:app --reload` | Development (best) |
| Python  | `python3 -m src.api.main`           | Simple execution   |

---
