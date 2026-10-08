from fastapi import FastAPI

app = FastAPI(title="BCS 31O3 Software Engineering Backend")


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Backend is running in Docker!",
        "course": "BCS 31O3 Software Engineering",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
