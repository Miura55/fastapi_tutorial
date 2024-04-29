from fastapi import FastAPI
import logging
import schemes

app = FastAPI(
    title="FastAPI Tutorial",
    summary="このAPIはFastAPIのチュートリアルとして掲示板のAPIを提供します。",
)
logger = logging.getLogger('uvicorn')


@app.get("/", response_model=schemes.MessageResponse, description="接続確認用のAPIです。")
async def root():
    return {"message": "Hello World"}

@app.post("/entry", response_model=schemes.MessageResponse, description="掲示板にエントリーを新規追加します。")
async def create_entry(entry: schemes.EntryRequest):
    logger.info(f"Received entry: {entry}")
    return {"message": "Entry created"}

@app.delete("/entry/{entry_id}", response_model=schemes.MessageResponse, description="IDを指定して掲示板のエントリーを削除します。")
async def delete_entry(entry_id: int):
    logger.info(f"Entry {entry_id} deleted")
    return {"message": f"Entry {entry_id} deleted"}
