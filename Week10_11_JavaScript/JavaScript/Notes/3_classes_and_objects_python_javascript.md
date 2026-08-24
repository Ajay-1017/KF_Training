# Classes and Objects --- Python & JavaScript

## 1. Class

A class is a blueprint or design for creating objects.

It defines:

- What data an object can have
- What actions an object can perform

Think of a class as a **design/template**.

---

## 2. Object

An **object** is an instance created from a class.

Each object follows the design defined by the class, but can contain its
**own data**.

### Mental model

```text
             CLASS
          ┌───────────┐
          │  Person   │
          │           │
          │ name      │
          │ age       │
          │ greet()   │
          └─────┬─────┘
                │
        ┌───────┴───────┐
        ↓               ↓
     OBJECT 1        OBJECT 2
   name = Ajay      name = Rahul
   age = 21         age = 25
```

Both objects follow the same class design, but their data can be
different.

---

## 3. Python Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello", self.name)


person1 = Person("Ajay", 21)
person2 = Person("Rahul", 25)
```

Here:

- `Person` → class
- `person1` → object
- `person2` → object
- `name` and `age` → attributes
- `greet()` → method

```python
person1.name       # Ajay
person1.age        # 21

person2.name       # Rahul
person2.age        # 25

person1.greet()
```

---

## 4. JavaScript Example

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log("Hello", this.name);
    }
}

const person1 = new Person("Ajay", 21);
const person2 = new Person("Rahul", 25);
```

Here:

- `Person` → class
- `person1` → object
- `person2` → object
- `name` and `age` → properties
- `greet()` → method

---

## 5. Attribute vs Property

The terminology is slightly different between Python and JavaScript.

  Concept                              Python      JavaScript

---

  Data associated with an object       Attribute   Property
  Function associated with an object   Method      Method
  Blueprint                            Class       Class
  Instance of a class                  Object      Object

A useful learning mapping is:

```
Python                  JavaScript

attribute      ≈        property
method         =        method
class          =        class
object         =        object
```

---

## 6. Dot Notation

The `.` is called **dot notation**.

It is used to access properties/attributes and methods of an object.

### Python

```python
person1.name
person1.greet()
```

### JavaScript

```javascript
person1.name
person1.greet()
```

So:

```text
object.property
object.method()
```

In JavaScript, a method is essentially a property whose value is a
function.

---

## 7. Important Mental Model

```text
CLASS
  │
  │ creates instances
  ↓
OBJECT
  │
  ├── data
  │     └── Python: attributes
  │         JavaScript: properties
  │
  └── behavior
        └── methods
```

### Simple definition to remember

> **A class is a blueprint/design that defines what an object should
> have and what it can do. An object is an instance created from that
> class, containing its own data.**
