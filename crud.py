from sqlalchemy.orm import Session
import models
import schemes


def get_entries(db: Session):
    return db.query(models.Entry).all()

def create_entry(db: Session, entry: schemes.EntryCreate):
    db_entry = models.Entry(
        title=entry.title,
        content=entry.content,
        user_name=entry.user_name
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_entry(db: Session, entry_id: int):
    db_entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
    db.delete(db_entry)
    db.commit()
    return db_entry
