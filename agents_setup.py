from dotenv import load_dotenv

from agents import (
    Agent,
    WebSearchTool
)

from agents.model_settings import ModelSettings

from prompts import (
    MEDICAL_AGENT_PROMPT,
    EVIDENCE_AGENT_PROMPT,
    REPORT_AGENT_PROMPT
)

from models import MedicineInfo


# Load environment variables
load_dotenv(override=True)


# Model
MODEL_NAME = "gpt-5.4-mini"


# Web Search Tool
settings = ModelSettings(
    tool_choice="required"
)

tools = [WebSearchTool()]


# -------------------------
# Medical Knowledge Agent
# -------------------------

medical_agent = Agent(
    name="Medical Knowledge Agent",
    instructions=MEDICAL_AGENT_PROMPT,
    model=MODEL_NAME,
    output_type=MedicineInfo,
)


# -------------------------
# Evidence Agent
# -------------------------

evidence_agent = Agent(
    name="Evidence Agent",
    instructions=EVIDENCE_AGENT_PROMPT,
    tools=tools,
    model=MODEL_NAME,
    model_settings=settings,
)


# -------------------------
# Report Agent
# -------------------------

report_agent = Agent(
    name="Report Agent",
    instructions=REPORT_AGENT_PROMPT,
    model=MODEL_NAME,
)