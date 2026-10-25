import csv
import os

flag = False

# Перевірка відкриття файлу та виведення вихідних даних
try:
    csvfile = open("lab5.csv", "r", encoding="utf-8")
    reader = csv.DictReader(csvfile)
    print("Зміст вихідного файлу lab5.csv:")
    print("-" * 60)
    for row in reader:
        print(row['Country'], ": ", row['Year'], " - ", row['Life Expectancy (years)'])
    csvfile.close()
except:
    print("Файл lab5.csv не знайдено!")

# Пошук даних у заданому користувачем діапазоні років та збереження результатів
try:
    csvfile = open("lab5.csv", "r", encoding="utf-8")
    reader = csv.DictReader(csvfile)

    print("\n" + "=" * 60)
    start_year = input("Введіть початковий рік діапазону (наприклад, 2000): ")
    end_year = input("Введіть кінцевий рік діапазону (наприклад, 2010): ")

    # Перевірка, щоб введені значення були числами
    while not (start_year.isdigit() and end_year.isdigit()):
        print("Помилка! Роки повинні бути числами.")
        start_year = input("Введіть початковий рік ще раз: ")
        end_year = input("Введіть кінцевий рік ще раз: ")

    start_year = int(start_year)
    end_year = int(end_year)

    print(f"\nРезультати пошуку для діапазону років {start_year}–{end_year}:")
    print("-" * 60)

    for row in reader:
        current_year = int(row['Year'])
        # Перевірка потрапляння року у визначений діапазон
        if start_year <= current_year <= end_year:
            flag = True
            print(row['Country'], ": ", row['Year'], " - ", row['Life Expectancy (years)'])

            # Додавання знайденого запису у новий CSV-файл
            with open("lab6.csv", "a", newline="", encoding="utf-8") as csvfile2:
                writer = csv.writer(csvfile2)
                writer.writerow([row['Country'], row['Year'], row['Life Expectancy (years)']])

    csvfile.close()

    if flag == False:
        print(f"Даних у заданому діапазоні років ({start_year}–{end_year}) не знайдено.")
    else:
        print("\nРезультати пошуку успішно збережено у файл lab6.csv")

except:
    print("Файл lab5.csv не знайдено!")
