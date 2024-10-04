from PIL import Image, ImageFilter, ImageOps

# Открываем изображение с использованием абсолютного пути
image = Image.open('C:\\Users\\bdv\\PycharmProjects\\pythonProject36\\IMG_3921.JPG')

# 1. Изменяем размер изображения
resized_image = image.resize((800, 600))

# 2. Применяем эффект черно-белого изображения
bw_image = resized_image.convert('L')

# 3. Применяем размытие
blurred_image = bw_image.filter(ImageFilter.BLUR)

# 4. Добавляем рамку
bordered_image = ImageOps.expand(blurred_image, border=30, fill='red')

# 5. Поворачиваем изображение на 45 градусов
rotated_image = bordered_image.rotate(45, expand=True)

# 6. Сохраняем изображение в другом формате
rotated_image.save('C:\\Users\\bdv\\PycharmProjects\\pythonProject36\\output.png')

# Показываем обработанное изображение
rotated_image.show()


import pandas as pd

# 1. Считываем данные из файла с использованием абсолютного пути и указанием кодировки
df = pd.read_csv('C:\\Users\\bdv\\PycharmProjects\\pythonProject36\\Данные продаж 23 год.csv', encoding='cp1251', sep=';')

# 2. Выполняем простой анализ данных

# Выводим первые 5 строк данных
print("Первые 5 строк данных:")
print(df.head())
print()

# Выводим статистику данных
print("Статистика данных:")
print(df.describe())
print()

# Выводим топ-5 продуктов по продажам
top_products = df.groupby('Товар')['Продажи'].sum().nlargest(5)
print("Топ-5 продуктов по продажам:")
print(top_products)
print()

# 3. Выводим результаты в консоль


import requests


# Вставляем  API-ключ выданный на сайте OpenWeather c привязкой к городу где живем
API_KEY = '075692edd08ed0d05c2174f15274fc36'
CITY = 'Chelyabinsk'

# вводим URL для запроса данных о погоде
url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Увеличиваем время  ожидания до 20 секунд так как меньше недостаточно для соединения
timeout = 20

# Количество попыток тоже минимальное для улучшения контакта с сайтом
max_retries = 3

for attempt in range(max_retries):
    try:
        # Отправляем  GET-запрос с увеличенным временем ожидания
        response = requests.get(url, timeout=timeout)

        # Проверяем статуса ответа
        if response.status_code == 200:
            # Преобразуем ответ в JSON
            data = response.json()

            # Извлекаем  нужные нам  данные
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Выводим  данные в консоль
            print(f"Погода в городе {CITY}:")
            print(f"Описание: {weather}")
            print(f"Температура: {temperature}°C")
            print(f"Влажность: {humidity}%")
            print(f"Скорость ветра: {wind_speed} м/с")
            break
        else:
            print(f"Ошибка при запросе данных: {response.status_code}")
            break
    except requests.exceptions.RequestException as e:
        if attempt < max_retries - 1:
            print(f"Ошибка при выполнении запроса: {e}. Попытка {attempt + 1} из {max_retries}.")
        else:
            print(f"Ошибка при выполнении запроса: {e}. Все попытки исчерпаны.")