# Agent Framework Demos

A Python-based project demonstrating the capabilities of Microsoft's Agent Framework for building AI agents with OpenAI integration. This repository contains progressive examples showing different agent patterns and features.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Examples](#examples)
- [Usage](#usage)
- [Contributing](#contributing)

## 🎯 Overview

This repository provides hands-on examples of building AI agents using the Microsoft Agent Framework. Each example demonstrates a specific pattern or capability, from basic agent creation to advanced multi-agent orchestration.

## ✨ Features

- **Simple Agent Creation**: Basic agent setup with instructions
- **Function Tools**: Agents that can call external functions
- **Structured Output**: Extract structured data using Pydantic models
- **Multi-Agent Systems**: Use agents as tools for other agents
- **Environment-based Configuration**: Secure API key management

## 📁 Project Structure

```
agent-framework-demos/
├── 1_simple_agent.py                    # Basic agent example
├── 2_simple_agent_functions.py          # Agent with function tools
├── 3_simple_agent_structured_output.py  # Structured data extraction
├── 4_agent_as_a_function_tool.py        # Multi-agent composition
├── utility.py                           # Shared OpenAI client utility
├── requirements.txt                     # Python dependencies
├── .env                                 # Environment variables (not in git)
└── .gitignore                          # Git ignore rules
```

## 🚀 Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager
- OpenAI API key (or compatible API)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sundasfkhan/agent-framework-demos.git
   cd agent-framework-demos
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   
   Create a `.env` file in the root directory with the following variables:
   ```env
   API_KEY=your_api_key_here
   BASE_URL=your_base_url_here
   MODEL_ID=your_model_id_here
   ```

   **Note:** The `.env` file is ignored by git to protect sensitive information.

## 📚 Examples

### 1️⃣ Simple Agent (`1_simple_agent.py`)

The most basic example demonstrating how to create an agent with simple instructions.

**What it demonstrates:**
- Creating an agent with specific instructions
- Running a simple query
- Getting text responses

**Example:**
```python
agent = client.create_agent(
    instructions="You are good for creating travel plans.",
    name="TravelAgent"
)
result = await agent.run("Make 2 days travel plan for sugar mountain, NC.")
```

**Run:**
```bash
python 1_simple_agent.py
```

### 2️⃣ Agent with Functions (`2_simple_agent_functions.py`)

Shows how to extend agent capabilities with custom functions using the `@ai_function` decorator.

**What it demonstrates:**
- Defining AI functions with type hints
- Providing tools to agents
- Function calling by the agent

**Key Features:**
- Uses `@ai_function` decorator
- Type-annotated parameters with descriptions
- Agent automatically decides when to call the function

**Example:**
```python
@ai_function
def get_weather(location: Annotated[str, "The city and state, e.g. San Francisco, CA"]) -> str:
    """Get the current weather for a given location."""
    return f"The weather in {location} is cloudy with a high of 15°C."

agent = client.create_agent(
    name="WeatherAgent",
    instructions="You are a helpful weather assistant.",
    tools=get_weather,
)
```

**Run:**
```bash
python 2_simple_agent_functions.py
```

### 3️⃣ Structured Output (`3_simple_agent_structured_output.py`)

Demonstrates extracting structured data from natural language using Pydantic models.

**What it demonstrates:**
- Using Pydantic models for data validation
- Extracting structured information from text
- Type-safe data handling

**Key Features:**
- Define data schema with Pydantic `BaseModel`
- Use `response_format` parameter
- Get validated, structured data instead of text

**Example:**
```python
class PersonInfo(BaseModel):
    """Information about a person."""
    name: str | None = None
    age: int | None = None
    occupation: str | None = None

result = await agent.run(
    "Please provide information about John Smith, who is a 35-year-old software engineer.",
    response_format=PersonInfo
)
```

**Run:**
```bash
python 3_simple_agent_structured_output.py
```

### 4️⃣ Agent as a Tool (`4_agent_as_a_function_tool.py`)

Advanced example showing multi-agent composition where one agent uses another agent as a tool.

**What it demonstrates:**
- Creating specialized agents
- Using `as_tool()` to convert an agent into a tool
- Agent orchestration and delegation
- Multi-agent collaboration

**Key Features:**
- Weather agent with function tools
- Urdu-speaking agent that delegates to the weather agent
- Demonstrates agent composition patterns

**Example:**
```python
weather_agent = client.create_agent(
    name="WeatherAgent",
    instructions="You are a helpful weather assistant.",
    tools=get_weather,
)

urdu_agent = client.create_agent(
    instructions="You are a helpful assistant who responds in Urdu.",
    tools=weather_agent.as_tool()
)
```

**Run:**
```bash
python 4_agent_as_a_function_tool.py
```

## 🔧 Usage

### Running Examples

Each example is a standalone script that can be run directly:

```bash
python 1_simple_agent.py
python 2_simple_agent_functions.py
python 3_simple_agent_structured_output.py
python 4_agent_as_a_function_tool.py
```

### Using the Utility Module

The `utility.py` module provides a shared OpenAI client factory:

```python
from utility import get_openai_client

client = get_openai_client()
agent = client.create_agent(
    instructions="Your instructions here",
    name="AgentName"
)
```

The client is automatically configured with credentials from environment variables.

## 🔐 Security

- **Never commit your `.env` file** - it contains sensitive API keys
- The `.gitignore` file is configured to exclude `.env` files
- Store production credentials in secure environment variable systems
- Rotate API keys regularly

## 📦 Dependencies

Key dependencies include:
- `agent-framework` - Microsoft Agent Framework
- `agent-framework-core` - Core framework components
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation and settings management
- `anthropic` - Anthropic API support
- Various Azure and AI service integrations

See `requirements.txt` for the complete list.

## 🎓 Learning Path

Follow the examples in order for the best learning experience:

1. **Start with `1_simple_agent.py`** - Understand basic agent creation
2. **Move to `2_simple_agent_functions.py`** - Learn about function tools
3. **Explore `3_simple_agent_structured_output.py`** - Master data extraction
4. **Finish with `4_agent_as_a_function_tool.py`** - Build multi-agent systems

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available for educational purposes.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🔗 Repository

- **Branch**: main
- **Remote**: https://github.com/sundasfkhan/agent-framework-demos.git

---

**Happy Agent Building! 🚀**

