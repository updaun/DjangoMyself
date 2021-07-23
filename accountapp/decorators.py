from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == requset.user:
            return func(requset, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated