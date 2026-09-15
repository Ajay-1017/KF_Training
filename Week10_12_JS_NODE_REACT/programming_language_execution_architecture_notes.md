# How Programming Languages Run --- Computer Architecture Mental Model

## 1. The Big Picture

When we write a program in a high-level programming language, the CPU
cannot directly understand Python, JavaScript, Java, or C syntax.

The general idea is:

```text
Human-readable source code
        ↓
Compiler / Interpreter / Engine / Runtime
        ↓
Bytecode or Machine Code
        ↓
Operating System
        ↓
CPU
```

The exact pipeline depends on the language and its implementation.

---

# 2. Important Terms

## Programming Language

A **programming language** is the language in which we write programs.

Examples:

- Python
- JavaScript
- Java
- C

A language itself is not necessarily the program that executes your
code.

For example:

```text
Python       → language
CPython      → implementation of Python
JavaScript   → language
V8           → JavaScript engine
Java         → language
JVM          → Java Virtual Machine
```

---

## Implementation

An **implementation** is a program/system that actually implements the
rules and behavior of a programming language.

For Python:

```text
Python language
       ↓
Different implementations
       ├── CPython
       ├── PyPy
       ├── Jython
       └── IronPython
```

CPython is the most widely used Python implementation.

---

## Runtime Environment

A **runtime environment** is the environment that provides what is
needed to execute a program while it is running.

It can provide things such as:

- execution of code
- memory management
- object management
- module loading
- exception handling
- interaction with the operating system
- runtime APIs

For example:

```text
Python program
      ↓
CPython runtime
      ↓
OS
      ↓
CPU
```

A useful definition:

> A runtime environment is the environment/program machinery that
> provides everything needed to execute a program while it is running.

---

## Compiler

A **compiler** translates source code into another form.

For example:

```text
C source code
      ↓
C compiler
      ↓
Machine code
```

For CPython:

```text
Python source
      ↓
CPython compiler
      ↓
Python bytecode
```

The output of a compiler does not always have to be machine code.

---

## Interpreter

An **interpreter** executes instructions instead of requiring the source
language to be directly converted into a native executable first.

In CPython:

```text
Python source
      ↓
Python bytecode
      ↓
Bytecode interpreter
      ↓
Execution
```

The interpreter executes **bytecode instructions**, not literally Python
source lines.

---

## Bytecode

Bytecode is an intermediate set of instructions designed for a virtual
machine or runtime.

For Python:

```text
Python source
      ↓
Python bytecode
      ↓
PVM / bytecode interpreter
```

Bytecode is different from CPU machine code.

---

## Machine Code

Machine code consists of native instructions that the CPU can execute.

Conceptually:

```text
High-level code
      ↓
Machine code
      ↓
CPU
```

The CPU ultimately executes native machine instructions.

---

## JIT --- Just-In-Time Compilation

A JIT compiler compiles code into native machine code **during program
execution**.

For example:

```text
Bytecode / intermediate representation
              ↓
          JIT compiler
              ↓
       Native machine code
              ↓
             CPU
```

Modern JavaScript engines and the JVM use JIT compilation.

---

# 3. Python --- CPython Architecture

The most common Python implementation is **CPython**.

Mental model:

```text
Python source code
        ↓
CPython
        ↓
CPython compiler
        ↓
Python bytecode
        ↓
PVM / Bytecode Interpreter
        ↓
CPython's native C implementation
        ↓
Machine instructions
        ↓
Operating System
        ↓
CPU
```

## Step-by-step

Suppose we write:

```python
a = 45
print(a)
```

### Step 1 --- Source code

We write normal Python code:

```python
a = 45
print(a)
```

### Step 2 --- CPython compiler

CPython compiles the Python source into Python bytecode.

Conceptually:

```text
Python source
      ↓
CPython compiler
      ↓
Python bytecode
```

### Step 3 --- PVM

The bytecode is given to CPython's bytecode execution machinery,
commonly called the **Python Virtual Machine (PVM)**.

The PVM executes bytecode instructions.

It does **not** literally execute Python source code line by line.

It executes **bytecode instructions instruction by instruction**.

---

# 4. What Is the PVM?

PVM means:

> **Python Virtual Machine**

In the context of CPython, it is the bytecode execution machinery inside
the Python runtime/interpreter.

A simplified view:

```text
                  PVM
        ┌─────────────────────┐
        │                     │
        │  Bytecode reader    │
        │         ↓           │
        │  Evaluation loop    │
        │         ↓           │
        │  Instruction        │
        │  handlers           │
        │         ↓           │
        │  Python object      │
        │  operations         │
        │                     │
        └─────────────────────┘
```

The most important part to understand is the **evaluation loop**.

It repeatedly:

```text
Get next bytecode instruction
          ↓
Determine what it means
          ↓
Execute the corresponding operation
          ↓
Get the next instruction
```

---

# 5. What Is Inside the PVM?

At a simplified level, the PVM contains:

1. Bytecode execution machinery
2. An evaluation loop
3. Instruction handlers
4. Python object operations
5. Support for executing Python bytecode

The bytecode interpreter is implemented mainly in **C** as part of
CPython.

For example, Python bytecode can contain instructions conceptually like:

```text
LOAD_CONST
STORE_NAME
LOAD_NAME
BINARY_OP
CALL
```

The PVM processes these instructions.

---

# 6. Does the PVM Convert Bytecode to Machine Code?

Normally, **no**.

This is a very important distinction.

In traditional CPython:

```text
Python source
      ↓
CPython compiler
      ↓
Python bytecode
      ↓
PVM / bytecode interpreter
      ↓
Executes bytecode using CPython's native implementation
      ↓
CPU
```

The bytecode interpreter is implemented mainly in C.

The CPython C code was already compiled into native machine code when
the CPython interpreter itself was built.

So:

```text
CPython C source
      ↓
C compiler
      ↓
Machine code
      ↓
CPython executable
```

Then, when we run Python:

```text
Python source
      ↓
Python bytecode
      ↓
PVM
      ↓
Already-compiled CPython native code
      ↓
CPU
```

Therefore:

> The PVM normally does not take each Python bytecode instruction and
> compile it into new machine code.

---

# 7. Why Is Python Commonly Called an Interpreted Language?

Python is commonly called an **interpreted language** because in the
usual CPython execution model, Python bytecode is executed by a bytecode
interpreter.

The more technically accurate picture is:

```text
Python source
      ↓
Compiled to bytecode
      ↓
Bytecode interpreted by PVM
      ↓
Execution
```

So Python is **not simply "never compiled."**

CPython does compile Python source into bytecode first.

The common description "interpreted language" refers to the fact that
the resulting bytecode is executed by an interpreter rather than Python
source being directly compiled into a native executable in the
traditional C sense.

Also:

> "Interpreted language" is a convenient classification, not a strict
> property of the language itself.

Different Python implementations can execute Python differently.

---

# 8. Python Objects and Memory

Python works heavily with objects.

For:

```python
a = 45
```

a useful mental model is:

```text
       a
       │
       ▼
┌───────────────┐
│ Python int    │
│               │
│ value = 45    │
└───────────────┘
```

`a` is a **name/reference** associated with a Python integer object.

Python's runtime manages:

- objects
- memory
- object lifetimes
- modules
- exceptions
- other runtime operations

---

# 9. CPython as a Runtime

A precise mental model is:

> **CPython is an implementation of the Python language that provides
> the runtime environment for executing Python programs.**

Do not think:

```text
Python = CPython
```

Instead:

```text
Python = programming language
CPython = implementation of Python
```

CPython contains the compiler, bytecode execution machinery,
runtime/object system, memory management, and other components needed to
run Python programs.

---

# 10. Python Implementations

Python is a language. There are multiple implementations.

## CPython

```text
Python
   ↓
CPython
   ↓
Python bytecode
   ↓
PVM / bytecode interpreter
```

**CPython**:

- Most widely used Python implementation
- Primarily implemented in C
- Compiles Python source to bytecode
- Executes bytecode using its interpreter/runtime

---

## PyPy

```text
Python
   ↓
PyPy
   ↓
JIT compilation
   ↓
Machine code
```

**PyPy**:

> A Python implementation with a JIT compiler.

It can compile frequently executed code into native machine code at
runtime.

---

## Jython

```text
Python
   ↓
Jython
   ↓
JVM
   ↓
Java ecosystem
```

**Jython**:

> A Python implementation designed to run on the JVM and integrate with
> Java.

---

## IronPython

```text
Python
   ↓
IronPython
   ↓
.NET / CLR
   ↓
CPU
```

**IronPython**:

> A Python implementation designed for the .NET ecosystem.

---

# 11. Python Implementations --- Very Briefly

---

  Implementation                      Very brief meaning

---

  **CPython**                         Standard/most widely used Python
                                      implementation; bytecode
                                      interpreter implemented mainly in C

  **PyPy**                            Python implementation with JIT

  **Jython**                          Python implementation running on
                                      the JVM

**IronPython**                      Python implementation for the .NET
                                      ecosystem
-----------------------------------------------

---

# 12. C Architecture

C has a much more direct traditional compilation model.

```text
C source code
      ↓
C compiler
(GCC / Clang)
      ↓
Machine code
      ↓
Executable
      ↓
Operating System
      ↓
CPU
```

The important point:

> C is traditionally compiled directly into native machine code before
> execution.

Example:

```text
main.c
  ↓
gcc
  ↓
executable
  ↓
CPU
```

---

# 13. Java Architecture

Java uses the JVM.

```text
Java source code
       ↓
     javac
       ↓
 Java bytecode
    (.class)
       ↓
      JVM
       │
       ├── Interpreter
       │
       └── JIT Compiler
                ↓
        Native machine code
                ↓
               CPU
```

## Important terms

```text
Java       = programming language
javac      = Java compiler
Bytecode   = intermediate instructions
JVM        = Java Virtual Machine
JIT        = Just-In-Time compiler
```

The JVM can interpret bytecode and JIT-compile frequently executed code
into native machine code.

---

# 14. JavaScript Architecture

Modern JavaScript engines such as V8 use a combination of interpretation
and JIT compilation.

Simplified mental model:

```text
JavaScript source code
          ↓
         V8
          ↓
    Parse / Compile
          ↓
       Bytecode
          ↓
      Interpreter
          ↓
     JIT Compiler
          ↓
    Machine Code
          ↓
         CPU
```

Modern engines have multiple internal compilation and optimization
stages, so the diagram is simplified.

The key idea is:

> JavaScript engines can JIT-compile frequently executed ("hot") code
> into optimized native machine code.

---

# 15. V8

**V8** is a JavaScript engine.

It is used by:

- Google Chrome
- Node.js

A simplified model:

```text
JavaScript
     ↓
    V8
     ↓
Bytecode / intermediate representations
     ↓
Interpreter + JIT
     ↓
Machine code
     ↓
CPU
```

Do not confuse:

```text
JavaScript = language
V8         = JavaScript engine
Node.js    = runtime built around V8
```

---

# 16. Node.js Architecture

Node.js is not a programming language.

It is a **JavaScript runtime** that allows JavaScript to run outside the
browser.

Simplified architecture:

```text
JavaScript code
       ↓
     Node.js
       │
       ├───────────────┐
       ↓               ↓
      V8           Node.js APIs
       │               │
       │          File System
       │          Networking
       │          Timers
       │          Processes
       │          etc.
       │
       ▼
 Interpreter + JIT
       │
       ▼
 Machine Code
       │
       ▼
      CPU
```

## Important relationship

```text
JavaScript = Language

V8 = JavaScript Engine

Node.js = Runtime built around V8
```

Node.js uses V8 to execute JavaScript and provides additional runtime
APIs that allow JavaScript programs to interact with the operating
system.

---

# 17. Browser vs Node.js

This was an important distinction.

## JavaScript in a Browser

```text
JavaScript
     ↓
Browser
     ↓
JavaScript Engine
     ↓
CPU
```

The browser provides:

- JavaScript engine
- DOM
- Web APIs
- `fetch()`
- `localStorage`
- timers
- browser-specific functionality

For Chrome:

```text
JavaScript
     ↓
Chrome
     ↓
V8 + Browser APIs
```

---

## JavaScript with Node.js

```text
JavaScript
     ↓
Node.js
     ↓
V8 + Node APIs
     ↓
Operating System
     ↓
CPU
```

Node.js provides APIs for things such as:

- file system
- networking
- HTTP servers
- processes
- environment variables
- timers

Therefore:

> Node.js allows JavaScript to run outside the browser.

Node.js does not replace JavaScript and does not replace V8.

It uses V8.

---

# 18. Browser vs Node.js --- Simple Comparison

```text
                 JavaScript
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
       Browser               Node.js
          │                     │
          ▼                     ▼
 JavaScript Engine       V8 JavaScript Engine
 + Browser APIs          + Node.js APIs
          │                     │
          ▼                     ▼
        CPU / OS             OS / CPU
```

The environment changes, but the JavaScript language remains the same.

---

# 19. C vs Python vs Java vs JavaScript vs Node.js

## C

```text
C source
   ↓
C compiler
   ↓
Machine code
   ↓
CPU
```

**Main idea:** Direct native compilation.

---

## Python / CPython

```text
Python source
     ↓
CPython compiler
     ↓
Python bytecode
     ↓
PVM / bytecode interpreter
     ↓
CPython native implementation
     ↓
CPU
```

**Main idea:** Source is compiled to bytecode, then bytecode is
interpreted.

---

## Java

```text
Java source
     ↓
javac
     ↓
Java bytecode
     ↓
JVM
     ↓
Interpreter + JIT
     ↓
Machine code
     ↓
CPU
```

**Main idea:** Bytecode runs on the JVM, with JIT compilation.

---

## JavaScript

```text
JavaScript source
       ↓
JavaScript engine
       ↓
Bytecode / IR
       ↓
Interpreter + JIT
       ↓
Machine code
       ↓
CPU
```

**Main idea:** Modern engines use interpretation and JIT compilation.

---

## Node.js

```text
JavaScript
     ↓
Node.js
     ↓
V8 + Node.js runtime APIs
     ↓
Interpreter + JIT
     ↓
Machine code
     ↓
CPU
```

**Main idea:** Node.js is a runtime that uses V8 to execute JavaScript
outside the browser.

---

# 20. Master Comparison Table

---

  Technology              What is it?              Main execution idea

---

  **C**                   Programming language     Compiler → native machine
                                                   code

  **Python**              Programming language     Python implementation
                                                   executes Python

  **CPython**             Python                   Source → bytecode →
                          implementation/runtime   bytecode interpreter

  **PyPy**                Python implementation    JIT compilation

  **Jython**              Python implementation    Runs on JVM

  **IronPython**          Python implementation    Runs on .NET/CLR

  **Java**                Programming language     Source → bytecode → JVM

  **JVM**                 Virtual machine/runtime  Interpreter + JIT

  **JavaScript**          Programming language     Engine
                                                   interprets/JIT-compiles

  **V8**                  JavaScript engine        Interpreter + JIT

  **Node.js**             JavaScript runtime       V8 + Node APIs/runtime

**PVM**                 CPython bytecode         Executes Python bytecode
                          execution machinery
---------------------------------------------

---

# 21. The Most Important Mental Model

Remember this:

```text
             PROGRAMMING LANGUAGE
                      │
                      ▼
          IMPLEMENTATION / ENGINE / RUNTIME
                      │
                      ▼
             BYTECODE / NATIVE CODE
                      │
                      ▼
                INTERPRETER / JIT
                      │
                      ▼
               MACHINE CODE
                      │
                      ▼
                    CPU
```

Different languages take different paths.

---

# 22. Final Mental Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    YOUR SOURCE CODE                         │
│                                                             │
│     C          Python        Java       JavaScript           │
└─────┬────────────┬────────────┬────────────┬────────────────┘
      │            │            │            │
      ▼            ▼            ▼            ▼
  C Compiler    CPython       javac         V8
      │            │            │            │
      │            ▼            ▼            ▼
      │         Bytecode    Bytecode    Bytecode / IR
      │            │            │            │
      │            ▼            ▼            ▼
      │          PVM          JVM       Interpreter + JIT
      │            │            │            │
      ▼            │            └────┬───────┘
 Machine Code      │                 │
      │            ▼                 ▼
      │       CPython native     Machine Code
      │            │                 │
      └────────────┴─────────────────┘
                   │
                   ▼
            Operating System
                   │
                   ▼
                  CPU
```

For Node.js:

```text
JavaScript
    ↓
 Node.js
    │
    ├── V8
    │    ↓
    │ Interpreter + JIT
    │    ↓
    │ Machine Code
    │
    └── Node APIs
         ↓
    OS interaction
         ↓
        CPU
```

---

# 23. The Five Sentences to Memorize

### C

> **C compiler compiles C source directly into native machine code.**

### Python

> **CPython compiles Python source into bytecode, and its PVM/bytecode
> interpreter executes that bytecode.**

### Java

> **`javac` compiles Java source into bytecode, and the JVM interprets
> or JIT-compiles that bytecode.**

### JavaScript

> **A JavaScript engine such as V8 executes JavaScript and can
> JIT-compile frequently executed code into native machine code.**

### Node.js

> **Node.js is a JavaScript runtime built around V8 that allows
> JavaScript to run outside the browser and provides APIs for
> interacting with the operating system.**

---

# 24. The One Big Question Behind Everything

Whenever you learn a new language/runtime, ask:

1. **What is the language?**
2. **What implementation/engine runs it?**
3. **Does it produce bytecode?**
4. **Who executes the bytecode?**
5. **Does it use interpretation?**
6. **Does it use JIT compilation?**
7. **How does it ultimately reach the CPU?**

If you can answer those seven questions, you understand the basic
execution architecture of that language.
