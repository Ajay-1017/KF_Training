# JavaScript  User Input, Readline, Callback, Promise & Async/Await

## 1. Input and Output in JavaScript

### Input

Input means **getting data from the user**.

Browser JavaScript can use:

```javascript
let name = prompt("Enter your name: ");
```

But `prompt()` is normally available in the **browser**, not Node.js.

When JavaScript runs with Node.js:

```bash
node main.js
```

we commonly use the built-in `readline` module for terminal input.

### Output

In Node.js, output is usually:

```javascript
console.log("Hello");
```

Internally:

```text
process.stdout → terminal
```

---

## 2. Python vs JavaScript Input

Python:

```python
name = input("Enter your name: ")
```

Browser JavaScript:

```javascript
let name = prompt("Enter your name: ");
```

Node.js:

```javascript
let name = await ask("Enter your name: ");
```

The reason Node.js looks more complicated is that its I/O model is designed around **asynchronous/event-driven operations**.

Python's `input()` already handles waiting for terminal input for you.

---

# 3. What is `readline`?

`readline` is a **built-in Node.js module** used to read input from the terminal.

```javascript
const readline = require("readline");
```

`require()` means:

> Load the module so we can use it.

Create a terminal interface:

```javascript
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
```

### Important terms

```text
process.stdin   → standard input → keyboard
process.stdout  → standard output → terminal
rl              → interface used to communicate with the terminal
```

So:

```javascript
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
```

basically means:

> Create an interface that receives input from the keyboard and communicates with the terminal.

---

# 4. `rl.question()`

`rl.question()` asks the user for input.

```javascript
rl.question("Enter your name: ", (answer) => {
    console.log(answer);
});
```

Flow:

```text
rl.question()
     ↓
Ask user
     ↓
Wait for input
     ↓
User enters "Ajay"
     ↓
Callback function runs
     ↓
answer = "Ajay"
```

The function:

```javascript
(answer) => {
    console.log(answer);
}
```

is called a **callback function**.

---

# 5. What is a Callback?

A **callback** is:

> A function passed to another function so that it can be called later when some work is completed.

Example:

```javascript
function greet(name, callback) {
    console.log("Hello " + name);

    callback();
}

function sayBye() {
    console.log("Bye!");
}

greet("Ajay", sayBye);
```

Output:

```text
Hello Ajay
Bye!
```

Here:

```javascript
greet("Ajay", sayBye);
```

passes `sayBye` to `greet`.

Inside `greet()`:

```javascript
callback();
```

calls `sayBye()`.

So:

```text
greet()
   ↓
does its work
   ↓
callback()
   ↓
sayBye() runs
```

### Why is it called a callback?

Because you are basically saying:

> "When you're done, call this function back."

---

# 6. Why do we use Promise?

`rl.question()` normally uses a callback:

```javascript
rl.question("Enter name: ", (answer) => {
    console.log(answer);
});
```

But we want to write code in a cleaner style using:

```javascript
let name = await ask("Enter name: ");
```

For `await` to work, `ask()` needs to return a **Promise**.

A Promise represents:

> A result that is not available yet, but will be available later.

Think:

```text
Promise
   ↓
"I don't have the answer yet."
   ↓
User enters input
   ↓
Answer becomes available
   ↓
Promise is completed
```

---

# 7. What is `resolve()`?

A Promise is commonly created like this:

```JavaScript
new Promise((resolve) => {
    // work
});
```

`resolve()` means:

> "The result is ready."

Example:

```javascript
new Promise((resolve) => {
    resolve("Ajay");
});
```

The Promise is now completed with:

```text
"Ajay"
```

---

# 8. Converting `readline` Callback to Promise

We can create an `ask()` function:

```javascript
function ask(question) {
    return new Promise((resolve) => {
        rl.question(question, resolve);
    });
}
```

The important line is:

```javascript
rl.question(question, resolve);
```

Normally:

```javascript
rl.question(question, callback);
```

So here:

```javascript
resolve
```

is being passed as the **callback**.

When the user enters something, `readline` effectively does:

```javascript
resolve(answer);
```

Example:

```text
User enters:
Ajay

        ↓

readline gets "Ajay"

        ↓

resolve("Ajay")

        ↓

Promise completed with "Ajay"
```

---

# 9. What is `async`?

`async` is used when a function needs to work with asynchronous operations and, especially, when we want to use `await` inside it.

Example:

```javascript
async function test() {
    let name = await ask("Enter name: ");

    console.log(name);
}
```

Important rule:

```text
await → normally used inside an async function
```

---

# 10. What is `await`?

`await` means:

> Wait for the Promise to finish and give me its result.

Example:

```javascript
let name = await ask("Enter name: ");
```

Flow:

```text
ask()
 ↓
Promise
 ↓
Wait for user input
 ↓
User enters "Ajay"
 ↓
Promise resolves
 ↓
await gets "Ajay"
 ↓
name = "Ajay"
```

---

# 11. Complete Input Code

```javascript
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question) {
    return new Promise((resolve) => {
        rl.question(question, resolve);
    });
}

async function main() {
    let name = await ask("Enter your name: ");

    console.log("Hello", name);

    rl.close();
}

main();
```

### Execution flow

```text
main()
  ↓
ask("Enter your name")
  ↓
Promise created
  ↓
readline asks the user
  ↓
User enters "Ajay"
  ↓
readline calls resolve("Ajay")
  ↓
Promise completed
  ↓
await receives "Ajay"
  ↓
name = "Ajay"
  ↓
console.log()
  ↓
Hello Ajay
```

---

# 12. Why `for...of` Instead of `forEach` With `await`?

For your employee-management program, we had:

```javascript
let emp_keys = Object.keys(employees[0]);

for (let info of emp_keys) {
    let detail = await ask("Enter the " + info + ": ");
    new_employee_obj[info] = detail;
}
```

This is preferred for sequential user input.

We generally avoid:

```javascript
emp_keys.forEach(async (info) => {
    let detail = await ask(...);
});
```

because `forEach()` does not wait for the asynchronous callback to finish.

Use:

```javascript
for (let info of emp_keys) {
    let detail = await ask(...);
}
```

when you need to wait for each operation.

---

# 13. Employee Object Example

Given:

```javascript
let employees = [
    {
        id: 101,
        name: "Ajay",
        age: 21,
        department: "ECE",
        salary: 21000
    }
];
```

Get the property names using:

```javascript
Object.keys(employees[0]);
```

Result:

```text
["id", "name", "age", "department", "salary"]
```

Then:

```javascript
let new_employee_obj = {};

for (let info of Object.keys(employees[0])) {
    let detail = await ask("Enter " + info + ": ");
    new_employee_obj[info] = detail;
}

employees.push(new_employee_obj);
```

---

# 14. Important Object Concept: `obj.key` vs `obj[key]`

Suppose:

```javascript
let info = "name";
let detail = "Ajay";
```

This:

```javascript
new_employee_obj.info = detail;
```

creates:

```javascript
{
    info: "Ajay"
}
```

because `.info` means the literal property named `info`.

But:

```javascript
new_employee_obj[info] = detail;
```

creates:

```javascript
{
    name: "Ajay"
}
```

because `[info]` uses the value stored in the variable `info`.

Remember:

```javascript
object.key      // literal key "key"

object[key]     // value of variable key
```

---

# 15. Key Interview Points

### What is `readline`?

> A built-in Node.js module used to read input from the terminal.

### What is `process.stdin`?

> Standard input, usually the keyboard/terminal input.

### What is `process.stdout`?

> Standard output, usually the terminal/screen.

### What is a callback?

> A function passed to another function so it can be called later when an operation is completed.

### What is a Promise?

> An object representing the eventual result of an asynchronous operation.

### What does `resolve()` do?

> It marks a Promise as completed and provides its result.

### What does `await` do?

> It waits for a Promise to settle and gives the resolved value.

### What does `async` do?

> It marks a function as asynchronous and allows `await` to be used inside it.

### Why use `readline` in Node.js instead of `prompt()`?

> `prompt()` is a browser API. Node.js does not normally provide it, so `readline` is used for terminal input.

---

# 16. One-Line Mental Model

Remember this:

```text
readline     → talks to terminal
rl.question  → asks user
callback     → runs when input arrives
Promise      → represents future result
resolve      → says result is ready
await        → waits for result
async        → allows await
```

### Python vs Node.js

```text
Python:

input()
  ↓
wait
  ↓
value


Node.js:

readline
  ↓
rl.question()
  ↓
callback
  ↓
Promise
  ↓
resolve()
  ↓
await
  ↓
value
```

The extra concepts in Node.js come mainly from its **asynchronous/event-driven I/O model**. Python's `input()` hides much of this complexity from you.
