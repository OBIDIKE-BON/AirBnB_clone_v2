#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Column, Integer


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
