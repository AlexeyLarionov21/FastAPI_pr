from fastapi import FastAPI, HTTPException
from utils import json_to_dict_list
import os
from typing import Optional
from models import Student

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'students.json')

app = FastAPI()

@app.get('/students')
def get_all_students(course: int | None = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list
    

@app.get("/")
def home_page():
    return {"message": "Hello, User!"}

@app.get("/students/{course}")
def get_all_students_course(course: int, major: str | None = None, enrollment_year: int | None = 2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student['course'] == course:
            filtered_students.append(student)    
    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower() == major.lower()]    
    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollment_year'] == enrollment_year]
    return filtered_students    

@app.get("/student")
def get_student_by_id(student_id: Optional[int] = None):
    students = json_to_dict_list(path_to_json)
    if student_id is None:
        return students
    for student in students:
        if student['student_id'] == student_id:
            return student

@app.get("/students/id/{student_id}")
def get_student_by_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student['student_id'] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.get("/student", response_model=Student)
def get_student_from_param_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student

