# numpy中reshape的用法

这里的`reshape`有两个函数：

- `numpy.reshape(a, ...)`, 是numpy的函数，改变数组a的形状

- `numpy.ndarray.reshape(...)`, 是ndarray对象的成员函数 （与前者作用相同）

## `numpy.reshape(a, newshape, order='C')`

参数：

- a: array对象

- newshape： int或由int组成的元组。

  新的形状需要与原形状兼容。如果该参数是一个int，那么结果将是1xN的数组。如果是一个tuple，tuple中的一个元素可以为-1，在这种情况下，该位置上的值将会被自动推断。

- order：可取值'C' 'F' 'A', 可选参数

  该参数的含义较复杂，此处略过。

返回值：

- 如果可能的话，返回一个view对象。否则将会返回一个copy。

举例：

```python
In [32]: np.reshape(np.arange(6),(3,2))
Out[32]:
array([[0, 1],
       [2, 3],
       [4, 5]])
```

## `numpy.ndarray.reshape(...)`

参数：

```python
a.reshape(shape, order='C')
```

shape的含义与上一个函数相同。

另外，这个函数允许将shape以多个参数的形式提供，比如，``a.reshape(10, 11)`` 就等同于``a.reshape((10, 11))``.

举例：

```python
In [31]: np.arange(6).reshape(2,3)
Out[31]:
array([[0, 1, 2],
       [3, 4, 5]])
```
