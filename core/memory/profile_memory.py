class ProfileMemory:
    def __init__(self):
        self.profile = {}

    def update(self, **kwargs):
        self.profile.update(kwargs)
        return self.profile
