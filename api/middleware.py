class ApiMiddleware:
    def __init__(self):
        self.enabled = True

    def process(self, request):
        return request
