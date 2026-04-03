# DocuPilot

> **AI-powered agent that reads documentation step by step, executes instructions with Ansible, learns from human feedback, and maintains a running summary.**

---

## ✨ Features

* 📖 Iteratively reads documents (3–4 lines at a time) to avoid the **lost-in-the-middle problem and context length limitation**.
* ⚙️ Executes instructions automatically using **Ansible**.
* 🧑‍🤝‍🧑 Human-in-the-loop support — asks for help when uncertain.
* 🧠 Learns from human guidance and stores knowledge in a **vector database** for future reference.
* 📝 Maintains a fixed-length **execution summary** after each iteration, keeping focus on the current steps without being overwhelmed by long docs.

---

## 🚀 Why DocuPilot?

Traditional LLM-based agents struggle with **long documents full of sequential instructions** — they often:

* Forget earlier steps due to **context length limits**,
* Miss instructions in the middle (the **lost-in-the-middle problem**), or
* Get overwhelmed by trying to process everything at once.

**DocuPilot solves this by:**

1. Processing the doc **in small iterations** (3–4 lines at a time).
2. Maintaining a **fixed-length rolling summary** of past steps.
3. Storing **human-in-the-loop (HIL) learnings** in a **vector database**, enabling recall in future runs.
4. Focusing only on the **current iteration** while ensuring context continuity.

---

## 🚀 Getting Started

### Prerequisites

* [Python 3.12+](https://www.python.org/)
* [Ansible](https://docs.ansible.com/) installed and configured
* Git

### Installation

```bash
# Clone the repository
git clone https://github.com/anupamreddy/DocuPilot.git
cd DocuPilot

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # on Linux/Mac
venv\Scripts\activate     # on Windows

# Install dependencies
pip install -r requirements.txt

#Export OpenAI API Key.
export OPENAI_API_KEY=<replace your key>
```

---

## 🧑‍💻 Usage

Run DocuPilot on a document:

```bash
python main.py execute --filepath path/to/document.txt
```

* DocuPilot processes **3–4 lines at a time**.
* Executes instructions via **Ansible**.
* If uncertain, it asks the **human-in-the-loop (HIL)** for clarification.
* Stores human feedback in a **vector database** for future reference.
* Updates a running fixed-length **summary** in `summary.md`.

---

## 📂 Project Structure

```
DocuPilot/
├── main.py              # Entry point
├── agent/               # Core agent logic
├── ansible_runner/      # Ansible integration
├── vector_store/        # Vector DB for HIL learnings
├── docs/                # Example documents
├── summary.md           # Live updated execution summary
└── requirements.txt     # Dependencies
```

---

## 🛣️ Roadmap

* [ ] Support for multiple document formats (Markdown, PDF, HTML)
* [ ] Web interface for live execution view
* [ ] Knowledge base to remember past human-in-the-loop answers (vector DB v2)
* [ ] Multi-agent collaboration (doc reader + executor + verifier)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or raise an issue.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

⚡ **DocuPilot** – Automating docs, few instructions at a time.

---
