from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from lib import crud, models, schemas
from lib.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI(description="""
Une super api pour API HOUR !
""")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/personnes/", response_model=schemas.User, tags=["Personnes"])
def creer_une_personne(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Créer une personne"""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/personnes", response_model=List[schemas.User], tags=["Personnes"])
def lister_les_personnes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lister les personnes"""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/personnes/{user_id}", response_model=schemas.User, tags=["Personnes"])
def chercher_une_personne(user_id: int, db: Session = Depends(get_db)):
    """Chercher une personne"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/personnes/{user_id}/boissons/", response_model=schemas.Item, tags=["Boissons"])
def associer_une_personne_et_une_boisson(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    """Associer une personne et une boisson"""
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/boissons", response_model=List[schemas.Item], tags=["Boissons"])
def lister_les_boissons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lister les boissons"""
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/")
async def dit_bonjour():
    """Message de bienvenue :-)"""
    return {"message": "Bonjour API Hour !"}
