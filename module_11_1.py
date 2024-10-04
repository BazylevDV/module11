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