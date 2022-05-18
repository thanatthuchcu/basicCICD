from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def hello():
    return "Hello Spy"

if __name__ == "__main__":
    uvicorn.run(app)