from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'fleet': reverse('fleet', request=request, format=format),
        'vehicle': reverse('vehicle', request=request, format=format)
    })
