from fastapi import FastAPI
from another_script import router  # Asume que los endpoints están definidos en 'another_script.py'

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
