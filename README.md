simplestruct
============

Struct-like classes with attribute type checking.

Getting Started
---------------

### Installation

You can install it from pip.

```
$ pip install simplestruct
```

### Basic Usage

Here's a simple an example.

```python
import simplestruct

class Person(simplestruct.Struct):
    name = str

p = Person(name="Jesse")

# Assigning a value of a different type to an attribute 
# will raise a `TypeError` exception.
p.name = 1  # Raises a `TypeError` Exception

# And durning instantiation.
Person(name=1)  # Raises a `TypeError` Exception
```

Type Support
------------

Simplestruct supports all python standard types and user-defined
types.

```python
from datetime import datetime


class Person(simplestruct.Struct):
    name = str            # This would require `str`.
    age = int             # This would require `int`.
    birthday = datetime   # This would require `datetime`.
```

Composable
----------

You can compound structs after structs.

```python
class Address(simplestruct.Struct):
    country = str


class Telephone(simplestruct.Struct):
    number = str


class Person(simplestruct.Struct):
    address = Address
    telephone = Telephone

Person(
    address=Address(country="PH"),
    telephone=Telephone(number="+6302111111")
)
```

Typed List
----------

You can define typed lists where the value of items in a list
must be of the defined type.

```python
class Address(simplestruct.Struct):
    ...

class Person(simplestruct.Struct):
    addresses = [Address]


Person(addresses=[Address(), Address(), Address()])

# This however would raise a `TypeError` exception.
Person(addresses=[Address(), "wat"])
```

Typed Tuple
-----------

You can define tuples as attributes and each of the tuples item's
attribute.

```python
class Person(simplestruct.Struct):
    age_and_gender = (int, str)

Person(age_and_gender=(10, "M"))
```
