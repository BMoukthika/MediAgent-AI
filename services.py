import asyncio

from agents import Runner

from agents_setup import (
    medical_agent,
    evidence_agent,
    report_agent
)

from models import MedicineInfo


# ------------------------------------
# Medical Knowledge Agent
# ------------------------------------

async def medical_information(question: str):

    result = await Runner.run(
        medical_agent,
        question
    )

    return result.final_output


# ------------------------------------
# Evidence Agent
# ------------------------------------

async def verify_information(question: str):

    result = await Runner.run(
        evidence_agent,
        question
    )

    return result.final_output


# ------------------------------------
# Report Agent
# ------------------------------------

async def generate_report(
    medical: MedicineInfo,
    evidence: str
):

    input_message = f"""
Medicine Name:
{medical.medicine_name}

Indications:
{", ".join(medical.indications)}

Mechanism of Action:
{medical.mechanism_of_action}

Common Side Effects:
{", ".join(medical.common_side_effects)}

Contraindications:
{", ".join(medical.contraindications)}

Supporting Evidence:
{evidence}

Please generate a professional report for a Medical Representative.
"""

    result = await Runner.run(
        report_agent,
        input_message
    )

    return result.final_output


# ------------------------------------
# Main Orchestrator
# ------------------------------------

async def run_mediagent(question: str):

    if not question.strip():
        return "❌ Please enter a medicine-related question."

    try:

        print("Getting medical information...")

        medical, evidence = await asyncio.gather(
            medical_information(question),
            verify_information(question)
        )

        print("Generating report...")

        report = await generate_report(
            medical,
            evidence
        )

        print("Done!")

        return report

    except Exception as e:

        return f"""
❌ Something went wrong.

Error:

{str(e)}
"""