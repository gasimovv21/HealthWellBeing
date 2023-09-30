from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import send_message



@api_view(['POST'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/send_message/',
            'method': 'POST',
            'body': None,
            'description':  [
                'Sennding message => POST',
            ]
        },
    ]
    return Response(routes)


@api_view(['POST'])
def post_message(request):
    if request.method == 'POST':
        return send_message(request)