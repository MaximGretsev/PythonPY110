Синтаксис выражения-генератора
```python
(expression for x in iterable)
```
Поэтому нет такого понятия как tuple comprehension

Найдем сумму первых 999999 натуральных чисел и сравним размер занимаемой памяти выражения-генератора и list comprehension.  
Для этого воспользуемся функцией из модуля `sys`:
```python
import sys

sys.getsizeof(some_obj)  # размер в байтах некоторого объекта some_obj
```
