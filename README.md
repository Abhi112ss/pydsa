# PyDSA Engine 🚀

![PyPI - Version](https://img.shields.io/pypi/v/pydsa-engine)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**PyDSA Engine** is a semantic, AI-powered Data Structures and Algorithms execution environment. 

It features a massive database of over 3,900 algorithms, a local AI vector search for fuzzy routing, a real-time execution engine, an X-Ray visual tracer for debugging, and a built-in FastAPI REST server.

## ✨ Features

* **🧠 AI Vector Routing:** Find the right algorithm even if you don't know the exact name (e.g., search for "water container" to find "Container With Most Water").
* **⚡ Dynamic Execution:** Pass actual inputs directly from your terminal and watch the engine calculate the optimal output, time complexity, and space complexity.
* **🔍 Visual Tracer (X-Ray):** Watch the Python interpreter step through the algorithm line-by-line and track local variables in real-time.
* **🌐 Built-in REST API:** Instantly transform the CLI tool into a FastAPI backend microservice with a single command.
* **📋 Clipboard Integration:** Instantly copy optimal, syntax-highlighted solutions directly to your system clipboard.

---

## 📦 Installation

Install globally via the Python Package Index (PyPI):

pip install pydsa-engine

---

## 💻 CLI Usage

### 1. Search for a Problem
Don't know the exact name? Ask the AI Brain to find it for you using natural language:

pydsa search "water container"


### 2. View and Copy Source Code
Bypass execution to instantly view the syntax-highlighted optimal code in your terminal, or copy it directly to your clipboard:

# View the code in the terminal
pydsa solve "max water" --show-code

# Copy the code directly to your IDE (requires pyperclip)
pydsa solve "two sum" --copy


### 3. Execute an Algorithm
Pass your inputs directly via the CLI. The engine will safely parse arrays, strings, and integers, run the optimal algorithm, and display the complexities.
*(Note: Array inputs must be wrapped in quotes)*

pydsa solve "two sum" "[2, 7, 11, 15]" "9"


### 4. The Visual Tracer (Step-by-Step)
Append the `--trace` flag to watch the algorithm execute line-by-line and print a table of the local variable states:

pydsa solve "two sum" "[2, 7, 11, 15]" "9" --trace


---

## 🌐 API Server Usage

PyDSA Engine includes a production-ready FastAPI server. You can spin it up locally to serve algorithm executions to your web or mobile apps.

Start the server:

pydsa serve --port 8000


Once running, navigate to `http://127.0.0.1:8000/docs` in your browser to access the interactive Swagger UI and test the endpoints.

**Example API Request (`POST /solve`):**
{
  "query": "two sum",
  "inputs": [
    [2, 7, 11, 15],
    9
  ],
  "trace": true
}

---

## 🛠️ Development & Testing

Want to contribute to the engine or add new algorithms? 

1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/pydsa.git
cd pydsa

2. Install in editable mode with testing dependencies:

pip install -e .
pip install pytest

3. Run the test suite to ensure the AI routing and engine are stable:

pytest


## 📄 License
This project is licensed under the MIT License.
