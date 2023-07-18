
## Special Methods

- There are also called **Dunder Methods** because they start with two underscores.
- These special method leverages the Python Data Model.
- Library implements the special method and is called by the special syntax attributed with it by the user of the library.
- One doesn't calls the special method by themselves, but use the special syntax around it. For example,`mycol.__len__()` is not called by the user, but instead `len(mycol)` is used.
- The special methods are only to be used by the interpreter directly.
- The special method help us to provide the common syntax or framework used by all other code to provide usage. For example, if we implemented the dunder method `__getitem__` on our collection. Then the user can use `[]` for indexing as well as all other functionality that is based on it (e.g. `random.choice`). 
- For built-in type the interpreter instead of calling special method implementation takes shortcuts to provide performance. For example, instead of calling `__len__` method on `list` it just reads the value of `ob_size` field on the C struct `PyVarObjectC` that represents any variable size built-in object in memory.
- Generally, the special method call is implicit. Meaning called internally by the interpreter for special syntax used. For example, in ```python for x in someCollection:``` the interpreter calls the `someCollection.__iter()__` implicitly.
- Special methods should only be used when doing meta-programming most of the time. For example, calling the `__init__` method on the super to invoke the initializer on the parent of the class.
- An example of usage of dunder methods:
```python
class WeirdNumbers:
	def collatz(self, x: int) -> int:
		if x % 2 == 0:
			return x // 2
		else:
			return 3 * x + 1

	def __init__(self, n: int) -> None:
		self.weirdNumbers = [n]
		while n != 1:
			n = self.collatz(n)
			self.weirdNumbers += [n]

	def __len__(self) -> int:
		return len(self.weirdNumbers)

if __name__ == '__main__':
	weird_numbers = WeirdNumbers(25)
	assert len(weird_numbers) == 24
```

- As you can see in the above example, we didn't use the special method `__len__` even in implementation but leverage the use of Python data model.
- It is usually better to call built-in functions corresponding to special methods. As they often provide other services and are faster on built-in types.
- Avoid creating arbitrary, custom attributes `__foo__` syntax because such names may acquire special meaning in the future.

## Some Dunder Methods

- `__len__`: As name suggest used for length of a collection or an object. It is used by the syntax `len(someCollection)`.
- `__getitem__`: It is used for getting a value at an index from a collection. It is used by the syntax `someCollection[2]`.
- `__repr__`: It is called by the repr built-in to get the string representation of the object for inspection. If we don't implement it the console representation would be something like `<Vector object at 0x10e100070>`. It is important because it shows the exact representation of the object instead of formatted output. It is what used by the debugger and such for outputting the evaluated expression. Whereas, ` __str__` method is used by the print method to show the formatted output. It is a good practice to implement repr such that the output representation resembles the code like `Vector(3, 4)` calling a constructor for the `Vector` class. If you only implement one of these special methods, choose __repr__, because when no custom __str__ is available, Python will call __repr__ as a fallback.
- `__add__`: It is used by the addition operator (`+`).
- `__mul__`: It is used by the multiplication operator (`*`). Both the **add** and **mul** dunder methods are commutative, meaning the order of their arguments doesn't matter.
- `__bool__`: It is used to get the Boolean value of an object. In the case of collections, if the **bool** dunder method is not implemented than interpreter will call the **len** dunder method, if it is zero then it will be considered as **falsy** else **truthy**.

## Conclusion

- Hence, in the conclusion the first chapter shows various dunder methods and how using then can leverage the Python Data model. It makes user-defined type look and feel as same as the built-in types. Hence giving the same API for both built-in and user-defined types. Being a python programmers mean to use this dunder methods properly according to one needs.