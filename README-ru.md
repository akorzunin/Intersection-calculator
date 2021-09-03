Intersection-calculator
=======================

Вычисляет координаты x и y пересечения двух прямых линий, каждая из которых определяется двумя точками.

Зачем
----------

В основном этот проект создан для нахождения Стронгхолда в игре Маинкрафт путем триангуляции по траектории полета ока Края, но такой метод имеет множество примениений и в других областях.

Как работает
-----------------------

- Программа рассчитывает кординаты точки Px и Py через определители матриц:
  ![algoritm](https://user-images.githubusercontent.com/54314123/132042127-8724c2c3-7c0e-4054-b894-55e2fe8d7ddb.png)
- Где исходные координаты выбираются по такому принципу как показано на картинке:
  ![intersection_calc_inanutshell](https://user-images.githubusercontent.com/54314123/132040968-2e79625c-a145-4818-9b91-455fcad47838.png)

Установка
------------------

1. Убедитесь что python3 установлен.
2. Используйте `pip install -r requirements.txt` для установки
   необходимых библиотек для python.

Как использовать
-------------------------------

### Использование через Jupyter Notebook

1. Откройте файл [triang_test.ipynb](https://github.com/akorzunin/Intersection-calculator/blob/main/triang_test.ipynb "triang_test.ipynb")
2. Выполние ячейки для инициализации кода

### Доступные методы:

- `calculate(self, *args, **kwargs):`
  Вычислить координаты точки.
- `update_first(self, *args, **kwargs):`
  Обновить координаты первой точки.
- `update_second(self, *args, **kwargs):`
  Обновите координаты второй точки.
- `update(self, **kwargs):`
  Обновить предыдущий расчет с помощью kwargs.
- `print_coord(self, px, py):`
  Функция выводит округленные значения, возвращает не округленные значения.

Примеры
--------------

Пример вычислений из Jupyter Notebook

```
   # example
   t.calculate(383, -1373, 385, -1385, 578, -2016, 574, -2026)
   # example with kwargs
   t.calculate(x1=380, y1=-1373, x2=385, y2=-1385, x3=587, y3=-2016, x4=574, y4=-2026)
   # update lines independently
   t.update_first(578+1, -2016+1, 574+1, -2026+1) 
   # update lines independently with kwargs 
   t.update_second(x3=578+108, y3=-2016+1, x4=574+1, y4=-2026-1)
   # upadate only certain points
   t.update(x1=0.1, y1=-1000000, x2=0, y2=0)
```

Пример из консоли python

```
	>>> from triang_calc import TriangCalcClass
	>>> t = TriangCalcClass()
	>>> t.calculate(x1=380, y1=-1373, x2=385, y2=-1385, x3=587, y3=-2016, x4=574, y4=-2026)
	Px: 633.0, Py: -1981.0
	>>> t.update(x1=0.1, y1=-1000000, x2=0, y2=0)
	Px: 0.0, Py: -2468.0
```

Лицензия
----------------

Intersection-calculator это бесплатное программное обеспечение с открытым исходным кодом под лицензией [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE).
