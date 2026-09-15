# JavaScript Array Iteration — Short Notes

## 1. `for` loop

General-purpose loop with full control over index and condition.

```JavaScript
for (let i = 0; i < employees.length; i++) {
    console.log(employees[i].name);
}
```

**Use when:** You need index or maximum loop control.

---

## 2. `for...of`

Loops directly over array values.

```js
for (let emp of employees) {
    console.log(emp.name);
}
```

**Use when:** You want simple iteration with loop control.

- Supports `break` ✅
- Supports `continue` ✅
- No callback required

---

## 3. `forEach()`

Array method that runs a callback once for every element.

```js
employees.forEach((emp) => {
    console.log(emp.name);
});
```

**Use when:** You simply want to perform an action for every element.

- Supports `break` ❌
- Supports `continue` ❌
- Does not return a new array
- Can modify objects in place

### In-place object modification

```js
employees.forEach((emp) => {
    emp.salary += 5000;
});
```

The original objects are modified.

---

## 4. `map()`

Array method used to transform every element and return a **new array**.

```js
let names = employees.map((emp) => {
    return emp.name;
});
```

Output:

```js
["Ajay", "Ravi", "Kumar"]
```

**Use when:** You want to transform data and create a new array.

---

## Quick Comparison

| Method        | Main purpose                 | New array? | `break` / `continue` |
| ------------- | ---------------------------- | ---------- | ------------------------ |
| `for`       | General looping              | ❌         | ✅                       |
| `for...of`  | Loop through values          | ❌         | ✅                       |
| `forEach()` | Perform action for each item | ❌         | ❌                       |
| `map()`     | Transform each item          | ✅         | ❌                       |

## Easy Memory Trick

```text
for / for...of
→ I control the loop

forEach()
→ Do something for every item

map()
→ Transform every item → new array
```

### Important

`for...of` and `forEach()` can often do the same job.

The key difference is:

- `for...of` = more loop control
- `forEach()` = callback-based "do this for every item"
- `map()` = transform and return a new array
