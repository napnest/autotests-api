import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print("Отправка GET-запроса")
print(response.status_code)  # 200
print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print("******************************************************************")



data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print("Отправка POST-запроса")
print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью
print("******************************************************************")



data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print("Отправка данных в application/x-www-form-urlencoded")
print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}
print("******************************************************************")



headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print("Передача заголовков")
print(response.json())  # Заголовки включены в ответ
print("******************************************************************")



params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print("Работа с параметрами запроса")
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач
print("******************************************************************")



files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

print("Отправка файлов")
print(response.json())  # Ответ с данными о загруженном файле
print("******************************************************************")



with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print("Использование httpx.Client")
print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи
print("******************************************************************")


print("Добавление базовых заголовков в Client")
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://httpbin.org/get")

print(response.json())  # Заголовки включены в ответ
client.close()
print("******************************************************************")



print("Проверка статуса ответа (raise_for_status)")
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
print("******************************************************************")



print("Обработка таймаутов")
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")


