from typing import Annotated, List
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
import schemes
import crud
from database import get_session, create_db_and_tables

logger = logging.getLogger('uvicorn')
templates = Jinja2Templates(directory="templates")
SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_and_tables()
    yield
    # Shutdown


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}_{route.name}"


app = FastAPI(
    title="FastAPI Tutorial",
    summary="このAPIはFastAPIのチュートリアルとして掲示板のAPIを提供します。",
    lifespan=lifespan,
    generate_unique_id_function=custom_generate_unique_id
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", description="画面表示を行います。", tags=["Root"])
async def root(request: Request, db: SessionDep):
    entries = crud.get_entries(db)
    return templates.TemplateResponse(request=request, name="entry.html", context={'entries': entries})

@app.get("/entries", description="掲示板の全エントリーを取得します。", tags=["Entries"])
async def get_entries(db: SessionDep) -> List[schemes.Entry]:
    entries = crud.get_entries(db)
    return [schemes.Entry.model_validate(entry.model_dump()) for entry in entries]

@app.post("/entries", description="掲示板にエントリーを新規追加します。", tags=["Entries"])
async def create_entry(entry: schemes.EntryRequest, db: SessionDep) -> schemes.Entry:
    logger.info(f"Received entry: {entry}")
    created_entry = crud.create_entry(db, entry)
    return schemes.Entry.model_validate(created_entry.model_dump())

@app.patch("/entries/{entry_id}", description="IDを指定して掲示板のエントリーを更新します。", tags=["Entries"])
async def update_entry(entry_id: int, entry: schemes.EntryRequest, db: SessionDep) -> schemes.Entry:
    try:
        updated_entry = crud.update_entry(db, entry_id, entry)
    except AttributeError:
        logger.error(f"Entry {entry_id} not found")
        raise HTTPException(status_code=404, detail=f"Entry {entry_id} not found")
    logger.info(f"Entry {entry_id} updated")
    return schemes.Entry.model_validate(updated_entry.model_dump())

@app.delete("/entries/{entry_id}", description="IDを指定して掲示板のエントリーを削除します。", tags=["Entries"])
async def delete_entry(entry_id: int, db: SessionDep) -> schemes.MessageResponse:
    try:
        crud.delete_entry(db, entry_id)
    except AttributeError:
        logger.error(f"Entry {entry_id} not found")
        raise HTTPException(status_code=404, detail=f"Entry {entry_id} not found")
    logger.info(f"Entry {entry_id} deleted")
    return {"message": f"Entry {entry_id} deleted"}
