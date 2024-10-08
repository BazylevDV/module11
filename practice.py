import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    obj_module = inspect.getmodule(obj)
    if obj_module is not None:
        obj_module = obj_module.__name__
    else:
        obj_module = 'builtins'  # Для встроенных типов

    # Создаем словарь с информацией
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)


# Создаем свой класс для демонстрации
class CheckIn:

    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


# Создаем объект класса
my_obj = CheckIn(10)
my_obj_info = introspection_info(my_obj)
print(my_obj_info)