from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.connection.db import get_db
from app.models.request_models import UserProfile as UserProfileSchema
from app.models.db_models import UserProfile as UserProfileDB
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {
        "message": "DB connected successfully"
    }

# -----------------------------
# GET ALL PROFILES
# -----------------------------

@router.get("/profiles")

def get_profiles(db: Session = Depends(get_db)):
    try:
        profiles = db.query(    UserProfileDB
        ).all()

        return profiles

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Fetch error: {str(e)}"
        )

@router.post("/profile")
def create_profile(profile:UserProfileSchema, db: Session = Depends(get_db)):
    db_profile = UserProfileDB(
        name=profile.name,
        gender=profile.gender,
        skin_tone=profile.skin_tone,
        body_shape=profile.body_shape,
        face_shape=profile.face_shape
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return {
        "message": "Profile saved"
    }

