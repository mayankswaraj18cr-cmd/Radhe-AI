from core.agents.orchestrator import Orchestrator


def test_orchestrator_has_agent_registry():
    orchestrator = Orchestrator()
    assert isinstance(orchestrator.agent_registry, dict)
