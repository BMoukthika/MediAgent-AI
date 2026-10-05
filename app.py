import asyncio

import gradio as gr

from services import run_mediagent

import os


# -----------------------------
# Wrapper for Gradio
# -----------------------------

def mediagent_app(question):

    return asyncio.run(
        run_mediagent(question)
    )


# -----------------------------
# Gradio UI
# -----------------------------

with gr.Blocks(title="MediAgent AI") as demo:

    gr.Markdown(
        """
# 🩺 MediAgent AI

### Multi-Agent Medical Information Assistant

Ask a medicine-related question and receive:

- Medicine overview
- Indications
- Common side effects
- Contraindications
- Supporting evidence
- Professional summary
"""
    )

    question = gr.Textbox(
        label="Medicine Question",
        placeholder="Example: What are the common side effects of Adalimumab?",
        lines=4
    )

    with gr.Row():

        submit = gr.Button(
            "Generate Report",
            variant="primary"
        )

        clear = gr.Button("Clear")

    output = gr.Markdown(
        label="Generated Report"
    )

    submit.click(
        fn=mediagent_app,
        inputs=question,
        outputs=output
    )

    clear.click(
        fn=lambda: ("", ""),
        outputs=[
            question,
            output
        ]
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )