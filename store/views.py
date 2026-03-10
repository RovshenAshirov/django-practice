from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def product_list(request):
    # Open this endpoint on Browser

    # return HttpResponse("OK")
    return Response("OK")


@api_view()
def product_detail(request, pk):
    return Response(pk)
