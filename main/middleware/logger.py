class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        print(f"Запрос: {request.method} {request.path} от {user}")
        return self.get_response(request)