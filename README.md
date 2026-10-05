# 🩺 MediAgent AI

A multi-agent Medical Information Assistant built using OpenAI Agents SDK.

## Overview

MediAgent AI helps medical representatives quickly understand medicine-related information by orchestrating multiple AI agents.

The system uses specialized agents for:

- Medical information extraction
- Evidence verification
- Professional report generation

## Architecture

User Question

↓

Medical Knowledge Agent

↓

Evidence Agent (Web Search)

↓

Report Agent

↓

Professional Medical Representative Report


## Tech Stack

- Python
- OpenAI Agents SDK
- GPT Models
- AsyncIO
- Structured Outputs (Pydantic)
- Gradio
- Render


## Features

✅ Multi-agent orchestration

✅ Async execution

✅ Structured outputs

✅ Web search integration

✅ Error handling

✅ Gradio interface


## Run Locally

Clone repository:
git clone <repository-url>


Install dependencies:
pip install -r requirements.txt


Create `.env`
Add:


OPENAI_API_KEY=your_key


Run:
python app.py



## Future Improvements

- RAG using medical documents
- MCP integrations
- Knowledge base search