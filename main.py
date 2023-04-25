from fastapi import FastAPI

# ====================== API ==========================

app = FastAPI()  # Running on port 8000


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# ================= Playing Around Code ==================

print("Hello Lyrics!")
