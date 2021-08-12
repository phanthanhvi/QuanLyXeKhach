from django.http import HttpResponse


def index(request):
    return HttpResponse("QUẢN LÝ XE KHÁCH")