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

# 1. Считтываем данные из файла с использованием абсолютного пути и указанием кодировки
df = pd.read_csv('C:\\Users\\bdv\\PycharmProjects\\pythonProject36\\Данные продаж 23 год.csv', encoding='cp1251', sep=';')

# 2. Выполняем простой анализ данных

# Выводим первые 5 строк данных
print("Первые 5 строк данных:")
print(df.head())
print()

# Выводим  статистику данных
print("Статистика данных:")
print(df.describe())
print()

# Выводим топ-5 продуктов по продажам
top_products = df.groupby('Товар')['Продажи'].sum().nlargest(5)
print("Топ-5 продуктов по продажам:")
print(top_products)
print()

# 3. Выводим результаты в консоль
