from fastapi import FastAPI
import logging
import schemes

app = FastAPI()
logger = logging.getLogger('uvicorn')


@app.get("/", response_model=schemes.MessageResponse)
async def root():
    return {"message": "Hello World"}

@app.post("/entry", response_model=schemes.MessageResponse)
async def create_entry(entry: schemes.Entry):
    logger.info(f"Received entry: {entry}")
    return {"message": "Entry created"}

@app.delete("/entry/{entry_id}", response_model=schemes.MessageResponse)
async def delete_entry(entry_id: int):
    logger.info(f"Entry {entry_id} deleted")
    return {"message": f"Entry {entry_id} deleted"}
