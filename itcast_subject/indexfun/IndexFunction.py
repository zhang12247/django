from itcast_subject import models
from django.core.exceptions import ObjectDoesNotExist


def login(username, password):
    try:
        print(models.nami_user.objects.filter(username=username))
    except ObjectDoesNotExist:
        return False
