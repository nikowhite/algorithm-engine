
# 🧠 Algorithmic Problem Engine

**Algorithmic Problem Engine** is a command-line engine for running and evaluating algorithmic problem solutions, similar to the core of platforms like LeetCode or Codeforces. It is designed to automatically validate user-submitted code in multiple programming languages (Python, Java, C++).

## 🚀 Features

- 📦 Load problems from JSON (description, input/output)
- 🧪 Execute solutions against multiple test cases
- ⌛ Enforce time and memory limits (via a sandbox)
- 🧩 Multi-language support (Python, Java, C++)
- 🔧 Modular and extensible architecture
- 🖥️ Command-line interface

## 📁 Example Problem Format

```json
{
  "id": "sum",
  "title": "Sum of Two Integers",
  "description": "Find the sum of two integers.",
  "test_cases": [
    {"input": "2 3", "output": "5"},
    {"input": "-1 4", "output": "3"}
  ],
  "time_limit": 2,
  "memory_limit": 256
}
```

## 📄 Example Python Solution (`sum.py`)

```python
a, b = map(int, input().split())
print(a + b)
```

## 🔧 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/yourusername/algorithm-engine.git
cd algorithm-engine

# Run a problem
python engine/engine.py --problem examples/sum.json --solution solutions/sum.py --lang python
```

## 👤 Who Is This For?

This project can be useful for:

- 👨‍🏫 Teachers — to automatically evaluate students’ code
- 👨‍💻 Developers — as the backend core of an online coding platform
- 🧪 Course creators — to validate and test assignments
- 💼 Freelancers — to demonstrate clean system architecture and coding skills

## 📌 Notes

- Users are responsible for writing their own solutions
- Problems can be added manually or loaded from APIs or files
- Can be integrated into a future web platform

## ✅ TODO

- [ ] Add unit and integration tests
- [ ] Add Docker sandbox for strict resource control
- [ ] Support additional languages (Rust, Go, etc.)
- [ ] Add optional web interface
