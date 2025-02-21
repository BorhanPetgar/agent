
# ReAct Chatbot with Ollama and LangChain

This project implements a **ReAct (Reasoning and Acting)** framework using **Ollama** and **LangChain**. The chatbot uses a loop of **Thought**, **Action**, **Observation**, and **Answer** to solve user queries. It supports two actions: querying **Wikipedia** and performing **calculations**.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **ReAct Framework**: The chatbot follows a structured reasoning and acting process to solve problems.
- **Ollama Integration**: Uses the Ollama language model for generating responses.
- **LangChain Support**: Leverages LangChain for prompt management and action execution.
- **Available Actions**:
  - `wikipedia: <query>`: Searches Wikipedia for information.
  - `calculate: <expression>`: Performs mathematical calculations.
- **Dynamic Prompting**: The chatbot dynamically formats prompts based on user input.

---

## Installation

### Prerequisites
- Python 3.10
- Ollama installed and running locally
- Required Python libraries

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/BorhanPetgar/agent.git
   cd agent
   ```

2. Install the required Python libraries:
   ```bash
   pip install langchain langchain-community httpx
   ```

3. Ensure Ollama is running locally. You can pull the desired model (e.g., `llama2`):
   ```bash
   ollama pull llama2
   ```

4. Run the chatbot:
   ```bash
   python main.py
   ```

---

## Usage

### Running the Chatbot
1. Start the chatbot by running:
   ```bash
   python main.py
   ```

2. The chatbot will prompt you to enter a question. For example:
   ```
   Enter your question: What is the capital of France?
   ```

3. The chatbot will follow the ReAct framework to provide an answer:
   ```
   Thought: I should look up France on Wikipedia to find its capital.
   Action: wikipedia: France
   PAUSE

   Observation: France is a country. The capital is Paris.
   Answer: The capital of France is Paris.
   ```

### Supported Actions
- **Wikipedia Query**:
  ```
  Action: wikipedia: <query>
  ```
  Example:
  ```
  Action: wikipedia: cat
  ```

- **Calculation**:
  ```
  Action: calculate: <expression>
  ```
  Example:
  ```
  Action: calculate: 0.25 * 80
  ```

---

## Code Structure

```
agent/
├── chatbot.py          # ChatBot class implementation
├── tools.py            # Action implementations (Wikipedia, calculate)
├── main.py             # Main script to run the chatbot
├── README.md           # This file
└── requirements.txt    # List of dependencies
```

### Key Files
- **`chatbot.py`**: Contains the `ChatBot` class, which implements the ReAct framework.
- **`tools.py`**: Defines the available actions (`wikipedia`, `calculate`).
- **`main.py`**: The entry point for running the chatbot.

---

## Examples

### Example 1: Wikipedia Query
**Input**:
```
What is the scientific name of a rose flower?
```

**Output**:
```
Thought: I should look up "rose flower" on Wikipedia to find its scientific name.
Action: wikipedia: rose flower
PAUSE

Observation: According to Wikipedia, the scientific name of a rose flower is Rosa.
Answer: The scientific name of a rose flower is Rosa.
```

### Example 2: Calculation
**Input**:
```
What is 30% of 200?
```

**Output**:
```
Thought: I need to calculate 30% of 200.
Action: calculate: 0.30 * 200
PAUSE

Observation: The result of the calculation is 60.0.
Answer: 30% of 200 is 60.
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Ollama**: For providing the language model.
- **LangChain**: For simplifying prompt management and action execution.
- **ReAct Framework**: For inspiring the reasoning and acting approach.

