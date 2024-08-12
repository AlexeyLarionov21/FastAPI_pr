import json
from json_db_lite import JSONDatabase


def dict_list_to_json(dict_list, filename):
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


# def json_to_dict_list(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             json_str = file.read()
#             dict_list = json.loads(json_str)
#         return dict_list
#     except (TypeError, ValueError, IOError) as e:
#         print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
#         return None
    

small_db = JSONDatabase(file_path='students.json')


def json_to_dict_list():
    return small_db.get_all_records()


def add_student(student: dict):
    student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
    small_db.add_records(student)
    return True


def upd_student(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


def dell_student(key: str, value: str):
    print(f"Удаляю запись с ключом {key} и значением {value}")
    small_db.delete_record_by_key(key, value)
    print("Запись удалена")
    return True