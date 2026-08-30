from core.memory.session_memory import SessionMemory


def test_session_memory_tracks_context():
    memory = SessionMemory()
    memory.add("hello", "Hi there")
    assert memory.history[-1]["prompt"] == "hello"
    assert memory.history[-1]["response"] == "Hi there"
