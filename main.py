from fastapi import FastAPI, Depends, HTTPException
import logging
import schemes
import crud
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Tutorial",
    summary="このAPIはFastAPIのチュートリアルとして掲示板のAPIを提供します。",
)
logger = logging.getLogger('uvicorn')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=schemes.MessageResponse, description="接続確認用のAPIです。")
async def root():
    return {"message": "Hello World"}

@app.post("/entry", response_model=schemes.MessageResponse, description="掲示板にエントリーを新規追加します。")
async def create_entry(entry: schemes.EntryRequest, db: Session = Depends(get_db)):
    logger.info(f"Received entry: {entry}")
    crud.create_entry(db, entry)
    return {"message": "Entry created"}

@app.delete("/entry/{entry_id}", response_model=schemes.MessageResponse, description="IDを指定して掲示板のエントリーを削除します。")
async def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    try: 
        crud.delete_entry(db, entry_id)
    except AttributeError:
        logger.error(f"Entry {entry_id} not found")
        raise HTTPException(status_code=404, detail=f"Entry {entry_id} not found")
    logger.info(f"Entry {entry_id} deleted")
    return {"message": f"Entry {entry_id} deleted"}
