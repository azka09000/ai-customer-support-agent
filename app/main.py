from fastapi import FastAPI

app = FastAPI(
    title="AI Customer Support Agent",
    description="An AI-powered customer support application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Customer Support Agent"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AI Customer Support Agent"
    }