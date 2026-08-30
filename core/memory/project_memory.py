class ProjectMemory:
    def __init__(self):
        self.projects = {}

    def save(self, project_id, payload):
        self.projects[project_id] = payload
        return self.projects[project_id]
