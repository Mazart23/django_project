from django.http import JsonResponse

def get_routes(request):
    routes = [
        'GET api/',
        'GET api/activity',
        'GET api/activity/:id'
    ]
    return JsonResponse(routes, safe=False)