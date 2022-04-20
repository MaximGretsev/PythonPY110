Из заданного списка вывести только положительные элементы.

Для фильтрации элементов используйте lambda функцию

```python
def filter_positive_number(x: int) -> bool:
    return x > 0

lambda x: x > 0  # тоже самое что и filter_positive_number только через lambda функцию
```