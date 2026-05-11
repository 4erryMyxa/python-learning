# Функция save_report которая:
# Принимает список словарей с пользователями
# Считает средний возраст
# Сохраняет результат в report.json
import json
def save_report(users):
     total_age = 0
     for user in users:
         total_age = total_age + user["age"]  # складываем все возрасты
     average_age = total_age / len(users)    # делим на количество  # должно быть 19.5
     report = {
           "total_users": len(users),
           "average_age": average_age,
           "users": users
}
     with open("report.json", "w") as file:
         json.dump(report, file)
users = [
    {"name": "Alex", "age": 15},
    {"name": "Ilya", "age": 21},
    {"name": "Anton", "age": 17},
    {"name": "Max", "age": 25}
]
save_report(users)
print("Готово! Файл сохранён.")