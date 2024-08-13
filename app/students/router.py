from fastapi import APIRouter 
from app.students.schemas import SStudent
from app.students.dao import StudentDAO
from typing import List

router = APIRouter(prefix='/students', tags=['Работа со студентами'])

@router.get("/", response_model=List[SStudent], summary="Получить всех студентов")
async def get_all_students():
    return await StudentDAO.find_all_students()
    