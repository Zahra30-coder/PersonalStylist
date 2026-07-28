from pydantic import BaseModel
from typing import Optional, List


class UserProfile(BaseModel):

    name: Optional[str] = None
    skin_tone: Optional[str] = None
    body_shape: Optional[str] = None
    face_shape: Optional[str] = None
    gender: Optional[str] = None
    height: Optional[str] = None
    weight_range: Optional[str] = None
    style_preference: Optional[str] = None
    occasion: Optional[str] = None

    preferred_colors: Optional[List[str]] = None
    avoid_colors: Optional[List[str]] = None
    footwear: Optional[List[str]] = None
    accessories: Optional[List[str]] = None