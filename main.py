from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr, field_validator
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re
from datetime import date
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Abhiram123@127.0.0.1:3306/fastapi_users"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        logger.info("Database connection successful")
except Exception as e:
    logger.error(f"Database connection failed: {str(e)}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    address = Column(String(200))
    gender = Column(Enum('male', 'female'))
    phone_number = Column(String(20))

Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    address: str
    gender: str
    phone_number: str

class UserCreate(UserBase):
    pass

@app.post("/adduser")
async def create_user(user: UserCreate):
    logger.info(f"Received user data: {user.dict()}")
    db = SessionLocal()
    try:
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        logger.info(f"User created with ID: {db_user.id}")
        return {"message": "User created", "user_id": db_user.id}
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/getallusers")
async def get_all_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    finally:
        db.close()

@app.get("/")
async def read_root():
    return FileResponse('templates/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
