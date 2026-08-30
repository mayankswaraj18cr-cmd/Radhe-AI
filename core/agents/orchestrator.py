class Orchestrator:
    def __init__(self):
        self.agent_registry = {
            "research": "research_agent",
            "writing": "writing_agent",
            "code": "code_agent",
        }
