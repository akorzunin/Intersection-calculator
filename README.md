Intersection-calculator
=======================

Calculates the x and y coordinates of the intersection of two straight lines, each defined by two points.

Why
---

Basically this project was created to find Stronghold in the game Minecraft by triangulating the flight path of the Edge, but this method has many applications in other areas as well.

How it works
------------

- The program calculates the coordinates of point Px and Py through the determinants of matrices:
  ![algoritm](https://user-images.githubusercontent.com/54314123/132042127-8724c2c3-7c0e-4054-b894-55e2fe8d7ddb.png)
- Where the initial coordinates are chosen as shown in the picture:
  ![intersection_calc_inanutshell](https://user-images.githubusercontent.com/54314123/132040968-2e79625c-a145-4818-9b91-455fcad47838.png)
- More about [line–line intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Formulas).

Setup
-----

1. Make sure python3 is installed.
2. Use `pip install -r requirements.txt` to install
   required libraries for python.

How to use
----------

### Using via Jupyter Notebook

1. Open the file [triang_test.ipynb](https://github.com/akorzunin/Intersection-calculator/blob/main/triang_test.ipynb "triang_test.ipynb")
2. Execute cells to initialize code

### Available methods:

- `calculate(self, *args, **kwargs):`
  Calculate point coordinates.
- `update_first(self, *args, **kwargs):`
  Update the coordinates of the first point.
- `update_second(self, *args, **kwargs):`
  Update the coordinates of the second point.
- `update(self, **kwargs):`
  Update the previous calculation with kwargs.
- `print_coord(self, px, py):`
  Function outputs rounded values, returns unrounded values.

Examples
--------

Example calculations from Jupyter Notebook

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

Example from the python console

```
	>>> from triang_calc import TriangCalcClass
	>>> t = TriangCalcClass()
	>>> t.calculate(x1=380, y1=-1373, x2=385, y2=-1385, x3=587, y3=-2016, x4=574, y4=-2026)
	Px: 633.0, Py: -1981.0
	>>> t.update(x1=0.1, y1=-1000000, x2=0, y2=0)
	Px: 0.0, Py: -2468.0
```

License
-------

Intersection-calculator is free and open source software under the [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE).

Intersection-calculator
=======================

Calculates the x and y coordinates of the intersection of two straight lines, each defined by two points.

Why
---

Basically this project was created to find Stronghold in the game Minecraft by triangulating the flight path of the Edge, but this method has many applications in other areas as well.

How it works
------------

- The program calculates the coordinates of point Px and Py through the determinants of matrices:
  ![algoritm](https://user-images.githubusercontent.com/54314123/132042127-8724c2c3-7c0e-4054-b894-55e2fe8d7ddb.png)
- Where the initial coordinates are chosen as shown in the picture:
  ![intersection_calc_inanutshell](https://user-images.githubusercontent.com/54314123/132040968-2e79625c-a145-4818-9b91-455fcad47838.png)
- More about [line–line intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Formulas).

Setup
-----

1. Make sure python3 is installed.
2. Use `pip install -r requirements.txt` to install
   required libraries for python.

How to use
----------

### Using via Jupyter Notebook

1. Open the file [triang_test.ipynb](https://github.com/akorzunin/Intersection-calculator/blob/main/triang_test.ipynb "triang_test.ipynb")
2. Execute cells to initialize code

### Available methods:

- `calculate(self, *args, **kwargs):`
  Calculate point coordinates.
- `update_first(self, *args, **kwargs):`
  Update the coordinates of the first point.
- `update_second(self, *args, **kwargs):`
  Update the coordinates of the second point.
- `update(self, **kwargs):`
  Update the previous calculation with kwargs.
- `print_coord(self, px, py):`
  Function outputs rounded values, returns unrounded values.

Examples
--------

Example calculations from Jupyter Notebook

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

Example from the python console

```
	>>> from triang_calc import TriangCalcClass
	>>> t = TriangCalcClass()
	>>> t.calculate(x1=380, y1=-1373, x2=385, y2=-1385, x3=587, y3=-2016, x4=574, y4=-2026)
	Px: 633.0, Py: -1981.0
	>>> t.update(x1=0.1, y1=-1000000, x2=0, y2=0)
	Px: 0.0, Py: -2468.0
```

License
-------

Intersection-calculator is free and open source software under the [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE).
