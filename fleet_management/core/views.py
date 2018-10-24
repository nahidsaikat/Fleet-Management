from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'fleet': reverse('fleet', request=request, format=format),
        'vehicle': reverse('vehicle', request=request, format=format)
    })

@login_required(login_url='/login/')
def dashboard(request, **kwargs):
    return render(request, 'layout.html', {})
