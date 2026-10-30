from fastapi import FastAPI

app = FastAPI(title="Nat20")

@app.get("/health")
# Page Status
def health():
    return {"status": "ok"}
