from datetime import date
import os
import json
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.students.models import Student

client = TestClient(app)

path_to_json = "students.json"

# Чтение данных из файла
with open(path_to_json, 'r', encoding='utf-8') as f:
    students_data = json.load(f)

# Тест для домашней страницы
def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, User!"}
    
def test_get_all_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == students_data
    
def test_get_students_by_course():
    response = client.get("/students?course=3")
    assert response.status_code == 200
    expected_students = [student for student in students_data if student["course"] == 3]
    assert response.json() == expected_students

def test_get_students_by_course_and_major_and_enrollment_year():
    response = client.get("/students/3?major=Информатика&enrollment_year=2017")
    assert response.status_code == 200
    expected_students = [student for student in students_data if student["course"] == 3 and student["major"] == "Информатика" and student["enrollment_year"] == 2017]
    assert response.json() == expected_students
    
    
@pytest.mark.parametrize(
    "course, major, enrollment_year, expected_count",
    [
        (3, "Математика", None, 1),
        (2, "Экономика", 2018, 1),
        (1, "История", 2019, 1),
        (4, "Биология", 2017, 1),
        (4, "Биология", 2016, 1),
        (4, "Биология", 2020, 0),
    ]
)

def test_get_students_by_course_major_and_enrollment_year1(course, major, enrollment_year, expected_count):
    url = f"/students/{course}"
    params = {}
    if major:
        params['major'] = major
    if enrollment_year:
        params['enrollment_year'] = enrollment_year

    response = client.get(url, params=params)
    assert response.status_code == 200
    assert len(response.json()) == expected_count
    for student in response.json():
        assert student['course'] == course
        if major:
            assert student['major'].lower() == major.lower()
        if enrollment_year:
            assert student['enrollment_year'] == enrollment_year
    

@pytest.mark.parametrize(
    "student_id, expected_status, expected_student",
    [
        (1, 200, {
            "student_id": 1,
            "first_name": "Иван",
            "last_name": "Иванов",
            "date_of_birth": "1998-05-15",
            "email": "ivan.ivanov@example.com",
            "phone_number": "+7 (123) 456-7890",
            "address": "г. Москва, ул. Пушкина, д. 10, кв. 5",
            "enrollment_year": 2017,
            "major": "Информатика",
            "course": 3,
            "special_notes": "Без особых примет"
        }),
        (999, 404, None),  # Тест для несуществующего студента
    ]
)

def test_get_student_by_id(student_id, expected_status, expected_student):
    response = client.get(f"/students/id/{student_id}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == expected_student
    else:
        assert response.json() == {"detail": "Student not found"}

@pytest.mark.parametrize(
    [
        (1, 200, {
                "student_id": 1,
                "phone_number": "+1234567890",
                "first_name": "Иван",
                "last_name": "Иванов",
                "date_of_birth": date(2000, 1, 1),
                "email": "ivan.ivanov@example.com",
                "address": "Москва, ул. Пушкина, д. Колотушкина",
                "enrollment_year": 1022,
                "major": "Информатика",
                "course": 3,
                "special_notes": "Увлекается программированием"
        }),
        (999, 404, None),  # Тест для несуществующего студента
    ]
)
def test_valid_student(data: dict)->None:
    try:
        student = Student(**data)
        print(student)
    except ValueError as e:
        print(f"Error Validation: {e}")