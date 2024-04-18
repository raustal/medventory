from fastapi import APIRouter
from ..models.models import Campus
from ..db.database import session

router = APIRouter()

@router.get('/campuses')
def get_campuses():
    '''Get a list of all campuses.'''
    campuses = session.query(Campus).all()
    return campuses

@router.post('/campus/add')
def add_campus(campus: Campus) -> Campus:
    '''Add a new campus to the database.'''
    session.add(campus)
    session.commit()
    return campus

