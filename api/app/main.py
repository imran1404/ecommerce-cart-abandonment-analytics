
from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce Analytics API",
    description="API for e-commerce conversion and cart abandonment analytics.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "E-Commerce Analytics API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
