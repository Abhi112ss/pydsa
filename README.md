# 🚀 PyDSA Engine

<p align="center">
  <img src="https://img.shields.io/pypi/v/pydsa-engine" alt="PyPI Version">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <b>A Semantic AI-Powered Data Structures & Algorithms Execution Engine</b>
</p>

---

## 🌟 Overview

**PyDSA Engine** is a next-generation Data Structures and Algorithms execution environment designed for developers, students, educators, and AI applications.

Instead of remembering exact problem names, simply describe what you're looking for and let the AI-powered routing engine find the correct algorithm instantly.

PyDSA Engine includes:

* 🧠 AI Semantic Search
* ⚡ Dynamic Algorithm Execution
* 🔍 Visual X-Ray Tracer
* 📋 Clipboard Integration
* 🌐 Built-in FastAPI Server
* 📚 3900+ Algorithm Database
* 📈 Complexity Analysis
* 🎯 Natural Language Problem Routing

---

# ✨ Features

## 🧠 AI Vector Routing

Find algorithms using natural language.

Example:

> "water container"

Automatically routes to:

> Container With Most Water

---

## ⚡ Dynamic Execution

Execute algorithms directly from the terminal with real inputs.

Supports:

* Arrays
* Strings
* Integers
* Matrices
* Graph Inputs
* Trees

---

## 🔍 X-Ray Visual Tracer

Watch your algorithm execute step-by-step.

Features:

* Local variable tracking
* Execution flow visualization
* Debugging support
* Educational learning mode

---

## 🌐 Built-in REST API

Turn PyDSA into a backend microservice instantly.

Powered by:

* FastAPI
* Swagger UI
* OpenAPI

---

## 📋 Clipboard Integration

Copy optimal solutions directly into your IDE.

---

# 📦 Installation

Install globally from PyPI:

```bash
pip install pydsa-engine
```

Verify installation:

```bash
pydsa --help
```

---

# 💻 CLI Usage

## 1️⃣ Search For A Problem

Use natural language to find algorithms.

```bash
pydsa search "water container"
```

Example Output:

```text
Found:
Container With Most Water
Difficulty: Medium
Category: Two Pointers
```

---

## 2️⃣ View Source Code

Display the optimal implementation.

```bash
pydsa solve "max water" --show-code
```

---

## 3️⃣ Copy Source Code

Copy the implementation directly to your clipboard.

```bash
pydsa solve "two sum" --copy
```

Requirements:

```bash
pip install pyperclip
```

---

## 4️⃣ Execute An Algorithm

Pass actual inputs directly.

Example:

```bash
pydsa solve "two sum" "[2,7,11,15]" "9"
```

Output:

```text
Result:
[0,1]

Time Complexity:
O(n)

Space Complexity:
O(n)
```

---

## 5️⃣ Visual X-Ray Tracing

Watch execution step-by-step.

```bash
pydsa solve "two sum" "[2,7,11,15]" "9" --trace
```

Example Output:

```text
Line 12:
num = 2
target = 9

Line 13:
lookup = {2:0}
```

Perfect for:

* Learning DSA
* Debugging
* Interview Preparation

---

# 🌐 REST API Server

PyDSA includes a production-ready FastAPI backend.

Start server:

```bash
pydsa serve --port 8000
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

Redoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Example API Request

### Endpoint

```http
POST /solve
```

### Request Body

```json
{
  "query": "two sum",
  "inputs": [
    [2,7,11,15],
    9
  ],
  "trace": true
}
```

### Response

```json
{
  "result": [0,1],
  "time_complexity": "O(n)",
  "space_complexity": "O(n)"
}
```

---

# 📚 Supported Categories

PyDSA Engine currently supports:

* Arrays
* Strings
* Linked Lists
* Trees
* Binary Trees
* Binary Search Trees
* Graphs
* Dynamic Programming
* Greedy Algorithms
* Backtracking
* Recursion
* Sliding Window
* Two Pointers
* Hash Tables
* Heaps
* Queues
* Stacks
* Tries
* Design Problems
* Math
* Bit Manipulation

And many more.

---

# 🏗 Project Architecture

```text
PyDSA Engine
│
├── CLI
├── AI Semantic Search
├── Vector Database
├── Execution Engine
├── Visual Tracer
├── FastAPI Server
├── Complexity Analyzer
└── Algorithm Database (3900+)
```

---

# 🛠 Development Setup

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/pydsa.git
```

Move into project:

```bash
cd pydsa
```

Install editable mode:

```bash
pip install -e .
```

Install testing dependencies:

```bash
pip install pytest
```

---

# ✅ Run Tests

Execute the full test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=pydsa
```

---

# 🤝 Contributing

Contributions are welcome.

You can contribute:

* New algorithms
* Bug fixes
* Documentation
* New CLI features
* Performance improvements
* AI routing enhancements

Workflow:

```bash
fork → feature branch → commit → pull request
```

---

# 📈 Roadmap

### v1

* AI Semantic Search
* Execution Engine
* FastAPI Server
* X-Ray Tracer

### v2

* Visual Graph Explorer
* Interactive Tree Renderer
* Algorithm Benchmarking
* Web Playground

### v3

* AI Tutor Mode
* LeetCode Importer
* Competitive Programming Assistant
* Algorithm Recommendation Engine

---

# 📄 License

Licensed under the MIT License.

See:

```text
LICENSE
```

for details.

---

<p align="center">
  Built with ❤️ for the Python & DSA Community
</p>

<p align="center">
  <b>PyDSA Engine — Search. Execute. Learn.</b>
</p>
