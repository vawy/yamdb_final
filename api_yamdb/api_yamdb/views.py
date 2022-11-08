from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Это главная страница')
