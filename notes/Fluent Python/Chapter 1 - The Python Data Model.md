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