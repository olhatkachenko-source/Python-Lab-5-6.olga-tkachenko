import requests
import json
import csv

# Код показника Світового банку:
# birth, total (years) для України за 1991–2019 роки
indicator = "SP.DYN.LE00.IN"
country = "ua"
year = "1991:2019"

# Формування URL-адреси API
url = (
    f"https://api.worldbank.org/v2/country/{country}/"
    f"indicator/{indicator}?date={year}&format=json&per_page=500"
)

# Виконання HTTP-запиту
response = requests.get(url)

# Перевірка успішності запиту
if response.status_code == 200:
    print("Дані успішно отримано")

    # Отримання даних у форматі JSON
    data = response.json()

    # Збереження даних у JSON
    with open(
        "lab5.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )
    print("Створено файл lab5.json")

    # Перетворення JSON у CSV
    csv_data = []
    for item in data[1]:
        if item["value"] is not None:
            csv_data.append([
                item["country"]["value"],
                item["date"],
                item["value"]
            ])

    with open(
        "lab5.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([
            "Country",
            "Year",
            "Life Expectancy (years)"
        ])
        writer.writerows(csv_data)

    print("Створено файл lab5.csv")

    # Виведення JSON на екран
    print("\nЗміст JSON:")
    print("-" * 50)
    for item in data[1][:5]:
        print(json.dumps(
            item,
            ensure_ascii=False,
            indent=4
        ))
        print()

    # Виведення CSV на екран
    print("\nЗміст CSV:")
    print("-" * 50)
    print("Country, Year, Life Expectancy (years)")
    for row in csv_data[:5]:
        print(f"{row[0]}, {row[1]}, {row[2]}")

else:
    print("Помилка отримання даних:", response.status_code)
