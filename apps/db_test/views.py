from django.http import HttpResponse

# Create your views here.
from apps.db_test import models


def test(request):
    if request.method == 'GET':
        # user_dict = {"username": request.GET.get('username', default=''), "age": request.GET.get('age', default='保密')}
        # models.UserInfo.objects.create(**{"username": request.GET.get('username', default=''), "age": request.GET.get('age', default='保密')})
        pass

    return HttpResponse('', content_type="image/png")
