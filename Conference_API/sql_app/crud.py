from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas
from fastapi import HTTPException

# Get list of users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Get list of rooms
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()
    
# Get list of reservation
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

#Create User in DB
def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Create Room in DB
def create_room(db: Session, room: schemas.Room):
    db_room = models.Room(roomname=room.roomname, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

#Create Booking in DB
def create_booking(db: Session, booking: schemas.Booking):
    db_booking = models.Booking(
        user_id =booking.user_id, 
        room_id = booking.room_id,
        booked_num = booking.booked_num,
        start_datetime = booking.start_datetime,
        end_datetime = booking.end_datetime
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking