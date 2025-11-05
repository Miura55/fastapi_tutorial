from sqlmodel import Session, select
from models import Entry
import schemes


def get_entries(db: Session):
    statement = select(Entry)
    return db.exec(statement).all()

def create_entry(db: Session, entry: schemes.EntryRequest):
    db_entry = Entry(
        title=entry.title,
        content=entry.content,
        user_name=entry.user_name
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def update_entry(db: Session, entry_id: int, entry: schemes.EntryRequest):
    statement = select(Entry).where(Entry.id == entry_id)
    db_entry = db.exec(statement).first()
    if db_entry is None:
        raise AttributeError(f"Entry {entry_id} not found")
    db_entry.title = entry.title
    db_entry.content = entry.content
    db_entry.user_name = entry.user_name
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_entry(db: Session, entry_id: int):
    statement = select(Entry).where(Entry.id == entry_id)
    db_entry = db.exec(statement).first()
    if db_entry is None:
        raise AttributeError(f"Entry {entry_id} not found")
    db.delete(db_entry)
    db.commit()
    return db_entry
