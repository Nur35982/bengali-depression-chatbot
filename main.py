from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.llm import call_model
from backend.rag.vector_store import retrieve_context
from backend.utils.phq_score import calculate_phq_score, get_depression_level

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend")

chat_history = []  # store history per session (simplified)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, user_input: str = Form(...), model: str = Form(...)):
    context = retrieve_context(user_input)
    prompt = f"User: {user_input}\n\nRelevant context: {context}\n\nAnswer in Bengali with empathy:"
    response = call_model(model, prompt)

    chat_history.append((user_input, response))

    # Simple PHQ scoring logic (simulate via keywords)
    score = calculate_phq_score(user_input)
    level = get_depression_level(score)

    final = f"আপনার ডিপ্রেশন স্কোর: {score} যা নির্দেশ করে যে: {level}"
    if len(chat_history) >= 5:
        response += f"\n\n{final}"

    return templates.TemplateResponse("index.html", {"request": request, "chat": chat_history})
