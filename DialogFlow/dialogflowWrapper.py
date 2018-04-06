from flask_assistant import Assistant


class DialogFlowWrapper:
    # Create assistant
    Assistant = Assistant(route='/assistant')
