# JavaScript Array Methods — Short Notes

The key is to stop memorizing syntax and instead ask:

> **"What do I want as the result?"**

| Method        | Main purpose                  | Returns                        | Think like         |
| ------------- | ----------------------------- | ------------------------------ | ------------------ |
| `forEach()` | Do something for every item   | Nothing useful (`undefined`) | **DO**       |
| `map()`     | Transform every item          | **New array**            | **CHANGE**   |
| `filter()`  | Select matching items         | **New array**            | **CHOOSE**   |
| `find()`    | Find one matching item        | **One item**             | **FIND ONE** |
| `reduce()`  | Combine items into one result | **One value**            | **COMBINE**  |

---

## 1. `forEach()` → "I just want to DO something"

Use when you don't need a new array.

```js
employees.forEach(emp => {
    console.log(emp.name);
});
```

### Ask yourself:

> "Do I just want to perform an action for every item?"

→ Use `forEach()`

---

## 2. `map()` → "I want to CHANGE / TRANSFORM every item"

Use when you want a **new array with one output for each input**.

```js
let names = employees.map(emp => emp.name);
```

If there are 5 employees:

```text
5 employees
    ↓
  map()
    ↓
5 names
```

### Ask yourself:

> "Do I need a new array where every item is transformed?"

→ Use `map()`

---

## 3. `filter()` → "I want to CHOOSE some items"

Use when you want only the items that satisfy a condition.

```js
let eceEmployees = employees.filter(
    emp => emp.department === "ECE"
);
```

```text
10 employees
     ↓
  filter()
     ↓
only ECE employees
```

### Ask yourself:

> "Do I want only the items that satisfy a condition?"

→ Use `filter()`

---

## 4. `find()` → "I want ONE matching item"

Use when you want the first item that matches a condition.

```js
let employee = employees.find(
    emp => emp.id === 103
);
```

Result:

```text
one employee object
```

### Ask yourself:

> "Do I need one matching item?"

→ Use `find()`

---

## 5. `reduce()` → "I want ONE FINAL RESULT"

Use when you want to combine many items into one result.

```js
let totalSalary = employees.reduce((total, emp) => {
    return total + emp.salary;
}, 0);
```

Result:

```text
ONE number
```

### Ask yourself:

> "Am I combining many items into one result?"

→ Use `reduce()`

---

# 🔥 Easiest Way to Remember

```text
forEach  → DO
map      → CHANGE
filter   → CHOOSE
find     → ONE
reduce   → COMBINE
```

---

# Shopping Cart Example

Suppose you have:

```js
let cart = [
    { name: "keyboard", price: 1200, quantity: 2 },
    { name: "mouse", price: 200, quantity: 3 },
    { name: "phone", price: 10000, quantity: 1 }
];
```

### Need to print every product?

```text
→ forEach()
```

### Need to calculate `item_total` for every product?

```text
→ map()
```

### Need products where price > 1000?

```text
→ filter()
```

### Need the product with id 101?

```text
→ find()
```

### Need total price of all products?

```text
→ reduce()
```

---

# ⭐ Most Important Rule

Don't ask:

> "Which method can do this?"

Many methods can technically accomplish similar tasks.

Instead ask:

> **"What result do I want?"**

```text
Action        → forEach()
New array     → map()
Subset array  → filter()
One item      → find()
One value     → reduce()
```

This distinction helps prevent **misusing JavaScript array methods**.
