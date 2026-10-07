from sqlalchemy import Column, Integer, String, JSON
from app.connection.db import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    skin_tone = Column(String)

    body_shape = Column(String)

    face_shape = Column(String)

    gender = Column(String)

    height = Column(String)

    weight_range = Column(String)

    style_preference = Column(String)

    occasion = Column(String)

    preferred_colors = Column(JSON)

    avoid_colors = Column(JSON)

    footwear = Column(JSON)

    accessories = Column(JSON)