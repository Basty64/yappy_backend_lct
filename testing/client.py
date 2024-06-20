import requests
import csv

url = 'https://localhost:8080/v1/requests/'  #Вставить нужный урл

csv_file_path = './docs/yappy_hackaton_2024_400k.csv'  # Вставить нужный урл к файлу
data = []
with open(csv_file_path, 'r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        data.append(row["link"])

        # Запросы к сервису
        # response = requests.post(url, json=data)

# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else:
#     print(f"Ошибка: {response.status_code}")