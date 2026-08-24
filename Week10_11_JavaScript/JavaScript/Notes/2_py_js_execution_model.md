# Python and JavaScript Execution Model

## 1. Python and JavaScript are programming languages

Python and JavaScript define the **syntax and rules** for writing
programs.

A language itself does not "run."

A **language implementation/runtime** is responsible for running the
code.

---

## 2. Python

A common Python implementation is **CPython**.

```text
Python language
      ↓
CPython
      ↓
Compile Python → Bytecode
      ↓
Python Virtual Machine
      ↓
Execute bytecode
```

### In simple terms

1. You write Python source code.
2. CPython compiles the source code into bytecode.
3. The Python Virtual Machine executes the bytecode instructions.
4. Therefore, CPython handles both the compilation stage and the
   execution stage.

So:

> **Python → CPython → bytecode → execution**

---

## 3. JavaScript

JavaScript is executed by a **JavaScript engine**.

Examples:

- Chrome → V8
- Node.js → V8
- Firefox → SpiderMonkey
- Safari → JavaScriptCore

The general model is:

```text
JavaScript language
        ↓
JavaScript Engine
        ↓
Parse + Compile/Interpret + Optimize
        ↓
Execute
```

Modern JavaScript engines can use interpretation, compilation, and **JIT
(Just-In-Time) optimization**.

So:

> **JavaScript → JavaScript engine → execution**

---

## 4. Are Python and JavaScript interpreted languages?

At the beginner level, it is common to say:

> **Python and JavaScript are interpreted languages.**

However, technically, **"interpreted" and "compiled" describe how a
particular implementation executes a language**. They are not absolute
properties of the language itself.

For example, modern JavaScript engines perform compilation and JIT
optimization, while CPython compiles Python source into bytecode before
executing it.

---

## 5. Final mental model

Remember these two models:

### Python

```text
Python
  ↓
CPython
  ↓
Bytecode
  ↓
Python Virtual Machine
  ↓
Execution
```

### JavaScript

```text
JavaScript
     ↓
JavaScript Engine
     ↓
Interpret / Compile / JIT Optimize
     ↓
Execution
```

### The key conclusion

> **Python and JavaScript are programming languages. Their
> implementations/runtimes are what actually execute the code.**

> **Python → CPython → bytecode → execution**

> **JavaScript → JavaScript engine → execution**

This is the more accurate way to understand the traditional **compiled
vs. interpreted** distinction.
