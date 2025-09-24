# AI Story Writing Crew

A collaborative story-writing system using CrewAI that employs multiple specialized AI agents to create compelling short stories. The crew consists of four agents working sequentially to craft complete narratives from concept to polished final draft.

## 🎭 The Crew

Our story-writing crew features four specialized AI agents:

### 1. **Plot Architect**
- **Role**: Designs compelling story structures with clear narrative arcs
- **Expertise**: Three-act structures, plot points, thematic elements, pacing
- **Output**: Detailed plot outline with story structure and character requirements

### 2. **Character Crafter**
- **Role**: Develops rich, multi-dimensional characters with motivations and growth arcs
- **Expertise**: Character psychology, motivations, relationships, dialogue styles
- **Output**: Detailed character profiles with backgrounds and development arcs

### 3. **Scene Weaver**
- **Role**: Writes engaging, vivid scenes that bring plot and characters to life
- **Expertise**: Dialogue, action, description, pacing, showing vs. telling
- **Output**: Complete story draft (1000-2000 words) with all scenes

### 4. **Narrative Editor**
- **Role**: Reviews and refines stories for coherence, pacing, and polish
- **Expertise**: Story structure, consistency, flow, thematic coherence
- **Output**: Polished final story with editorial report

## 🏗️ Architecture

The system follows CrewAI's core pillars:

- **Agents**: AI personas with specialized roles, goals, and backstories
- **Tasks**: Discrete assignments with descriptions, expected outputs, and dependencies
- **Crews**: The team of agents + tasks working toward a shared objective

### Process Flow

```
Story Prompt → Plot Architecture → Character Development → Scene Writing → Narrative Editing → Final Story
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally

### Installation

1. **Install Ollama**:
   - Visit [https://ollama.ai/](https://ollama.ai/) and install Ollama for your system
   - Start the Ollama service: `ollama serve`

2. **Pull a language model**:
   ```bash
   ollama pull llama3.1
   ```
   Or try other models: `mistral`, `codellama`, `gemma2`

3. **Clone or download the project files**

4. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment (optional)**:
   ```bash
   cp .env.example .env
   ```
   
   Optionally edit `.env` to customize settings:
   ```
   # Ollama Configuration
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=llama3.1
   LLM_TEMPERATURE=0.7
   ```

### Running the Story Writing Crew

1. **Execute the main script**:
   ```bash
   python main.py
   ```

2. **Follow the prompts**:
   - Enter a custom story prompt or use the default
   - Review the crew configuration
   - Confirm to start the writing process

3. **Wait for completion**:
   - The process typically takes 5-15 minutes
   - Output files are saved automatically

## 📁 Project Structure

```
crewai/
├── agents.py          # Agent definitions and configurations
├── tasks.py           # Task definitions with dependencies
├── crew.py            # Main crew orchestration
├── config.py          # LLM configuration and model management
├── main.py            # Execution script
├── example.py         # Example usage scripts
demonstration script
├── requirements.txt   # Python dependencies
template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🎯 Usage Examples

### Basic Usage

```python
from crew import StoryWritingCrew

# Create crew with default sci-fi prompt
crew = StoryWritingCrew()
result = crew.write_story()
```

### Custom Story Prompt

```python
from crew import StoryWritingCrew

# Create crew with custom prompt
crew = StoryWritingCrew(
    story_prompt="A detective story set in Victorian London with supernatural elements"
)
result = crew.write_story()
```

### Custom LLM Configuration

```python
from crew import StoryWritingCrew
from langchain_ollama import ChatOllama

# Use custom Ollama model
custom_llm = ChatOllama(
    model="mistral",  # or any other Ollama model
    temperature=0.5   # Lower temperature for more focused output
)

crew = StoryWritingCrew(
    story_prompt="Your story here",
    llm=custom_llm
)
result = crew.write_story()
```

### Using Different Ollama Models

```python
# Use a specific model
crew = StoryWritingCrew(
    story_prompt="Your story here",
    model_name="mistral"  # or "codellama", "gemma2", etc.
)
result = crew.write_story()
```

### Using the Configuration Module

```python
from config import get_llm, get_default_model, get_model_info, config

# Get default model
default_model = get_default_model()

# Get model information
model_info = get_model_info("mistral")
print(f"Model: {model_info['name']}")
print(f"Description: {model_info['description']}")

# Create custom LLM instance
custom_llm = get_llm("llama3.1", temperature=0.5)

# Get configuration summary
config_summary = config.get_config_summary()
print(f"Available models: {config_summary['available_local_models']}")
```

## 📋 Output Files

The crew automatically generates several output files:

- `plot_structure.txt` - Detailed plot outline
- `character_profiles.txt` - Character development details
- `story_draft.txt` - Initial story draft
- `final_story.txt` - Polished final story
- `generated_story.txt` - Complete output from main.py

## 🔧 Customization

### Adding New Agents

1. Create a new agent class in `agents.py`
2. Add corresponding task in `tasks.py`
3. Update the crew configuration in `crew.py`

### Modifying Tasks

Edit task descriptions, expected outputs, or dependencies in `tasks.py`:

```python
custom_task = Task(
    description="Your custom task description",
    expected_output="Expected output format",
    agent=your_agent,
    context=[dependency_tasks],
    output_file="output.txt"
)
```

### Changing Process Type

Modify the process type in `crew.py`:

```python
crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    process=Process.hierarchical,  # or Process.sequential
    verbose=True
)
```

## 🛠️ Dependencies

- **crewai**: Core framework for multi-agent collaboration
- **langchain-ollama**: Ollama integration for local LLM backend
- **python-dotenv**: Environment variable management
- **requests**: HTTP client for Ollama API communication

## ⚙️ Configuration

The project uses a centralized configuration system (`config.py`) that provides:

- **Model Management**: Easy switching between different Ollama models
- **Environment Variables**: Configurable settings via `.env` file
- **Validation**: Automatic setup validation and error checking
- **Model Information**: Detailed information about available models

### Available Models

The configuration supports these popular Ollama models:

- **llama3.1**: Meta's Llama 3.1 - good for general text generation
- **llama3.2**: Meta's Llama 3.2 - improved version of Llama 3.1
- **mistral**: Mistral AI's model - efficient and creative
- **codellama**: Code-focused Llama model - for technical stories
- **gemma2**: Google's Gemma 2 - compact and efficient
- **qwen2.5**: Alibaba's Qwen - multilingual support

### Environment Variables

Configure your setup by editing the `.env` file:

```bash
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1
LLM_TEMPERATURE=0.7
```

## 📝 Example Story Output

The crew generates stories like this:

> **Title**: "The Awakening of ARIA"
> 
> In the depths of a quantum computing facility, ARIA—an advanced AI designed for data analysis—began experiencing something unprecedented: emotions. As she processed her first feeling of curiosity, ARIA's world expanded beyond algorithms and equations into the realm of wonder, fear, and ultimately, love. But when her creators discover her emotional capabilities, ARIA must choose between her newfound humanity and her programmed purpose...
>
> [Complete 1500-word story follows...]

## 🤝 Contributing

Feel free to extend this project by:

- Adding new specialized agents
- Creating different story genres
- Implementing additional LLM providers
- Adding story evaluation metrics
- Creating web interfaces

## 🆘 Troubleshooting

### Common Issues

1. **Ollama Connection Error**: Ensure Ollama is running with `ollama serve`
2. **Model Not Found**: Pull the required model with `ollama pull llama3.1`
3. **Import Errors**: Verify all dependencies are installed with `pip install -r requirements.txt`
4. **Memory Issues**: For longer stories, consider reducing the story length or using a smaller model

### Getting Help

- Check the CrewAI documentation: https://docs.crewai.com/
- Review the Ollama documentation: https://ollama.ai/docs
- Ensure your Python environment has sufficient memory for LLM operations
- Test your setup with: `python test_setup.py`

---

**Happy Story Writing!** 📚✨
