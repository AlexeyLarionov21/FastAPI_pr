from fastapi import FastAPI
from app.students.router import router as router_students


app = FastAPI(debug=True)


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_students)

# @app.get('/students')
# def get_all_students(course: int | None = None):
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     return_list = []
#     for student in students:
#         if student["course"] == course:
#             return_list.append(student)
#     return return_list
    

# @app.get("/students/{course}")
# def get_all_students_course(request_body: RBStudent = Depends()) -> List[Student]:
#     students = json_to_dict_list(path_to_json)
#     filtered_students = []
#     for student in students:
#         if student["course"] == request_body.course:
#             filtered_students.append(student)

#     if request_body.major:
#         filtered_students = [student for student in filtered_students if
#                              student['major'].lower() == request_body.major.lower()]
#     if request_body.enrollment_year:
#         filtered_students = [student for student in filtered_students if
#                              student['enrollment_year'] == request_body.enrollment_year]
#     return filtered_students 


# @app.get("/student/{student_id}")
# def get_student_from_param_id(student_id: int)->Student:
#     students = json_to_dict_list(path_to_json)
#     for student in students:
#         if student["student_id"] == student_id:
#             return student


# ################ POST #################

# @app.post("/add_student")
# def add_student_handler(student: Student):
#     student_dict = student.dict()
#     check = add_student(student_dict)
#     if check:
#         return {"message": "Successfull added"}
#     else:
#         return {"message": "Error adding student"}
    

# @app.put("/update_student")
# def update_student_handler(filter_student: SUpdateFilter, new_data: StudentUpdate):
#     check = upd_student(filter_student.dict(), new_data.dict())
#     if check:
#         return {"message": "Info updated successfully"}
#     else:
#         raise HTTPException(status_code=400, detail="Error updating student information")
    
# @app.delete("/delete_student")
# def delete_student_handler(filter_student: SDeleteFilter):
#     check = dell_student(filter_student.key, filter_student.value)
#     if check:
#         return {"message": "Student deleted successfully"}
#     else:
#         raise HTTPException(status_code=400, detail="Error deleting student")
    
# # uvicorn app.main:app --reload