# MCP Test Application

A simple test application that demonstrates the integration of an LLM-powered agent with MCP (Model Context Protocol). This application sends prompts to an LLM and streams the resulting output.
The default configuration is setup to run [IBM Cloud MCP Server](https://github.com/IBM-Cloud/ibmcloud-mcp-server)

## Features

- Integration with OpenAI's GPT-4 model
- Streaming response handling
- MCP agent implementation for structured interactions
- Configuration-based setup

## Prerequisites

- Python 3.13 or higher
- [Ollama](https://ollama.com) installed locally with granite3.3 and/or other models downloaded
- OpenAI API key (set in .env or OPENAI_API_KEY env var) if non-local LLM providers are being used.
- [IBM Cloud MCP Server](https://github.com/IBM-Cloud/ibmcloud-mcp-server) must be installed locally
- MCP server configuration (See example mcp.json) must be updated with the full path to ibmcloud mcp server

## Installation

1. Clone the repository:

```bash
git clone git@github.com:ccmitchellusa/mcp-test.git
cd mcp-test
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
uv sync --reinstall
```

## Configuration

1. Create a `.env` file in the project root with your OpenAI API key:

```bash
OPENAI_API_KEY=your-api-key-here
```

2. Ensure your `mcp.json` is properly configured with your MCP server settings.

## Usage

Run the assistant:

```bash
uv run ibmcloud-assist.py
```

The application will:

1. Connect to the IBMCloud MCP server using the provided configuration
2. Initialize an LLM connection to local Ollama qwen3 model
3. Send a prompt completion requesting resource groups.
4. Output response from the LLM.

## Project Structure

- `ibmcloud-assistant.py` - Assistant application example
- `mcp.json` - MCP server configuration
- `pyproject.toml` - Project dependencies and metadata

## Dependencies

- langchain-ollama >= 0.3.22
- mcp-use >= 1.3.0

## License

MIT License

