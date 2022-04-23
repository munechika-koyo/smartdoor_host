from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from keymanagement.models import Key

import json


@ensure_csrf_cookie
def authenticate(request):
    """
    Response the result of key authentication if idm request is recieved.
    """
    # For get csrf token
    if request.method == "GET":
        return JsonResponse({}, status=200)

    # For idm authentication process
    try:
        # parse requested json body
        data = json.loads(request.body)

        # check if data has idm key
        if "idm" not in data:
            return JsonResponse({"message": "has no idm key"}, status=400)

        # search for key in Key models
        querysets = Key.objects.all()
        queryset = querysets.filter(idm__iexact=data["idm"])
        if queryset:
            return JsonResponse(
                {
                    "auth": "valid",
                    "name": queryset[0].name,
                    "allow_423": queryset[0].allow_423,
                    "allow_475": queryset[0].allow_475,
                },
                status=200,
            )
        else:
            return JsonResponse({"auth": "invalid"}, status=200)
    except Exception:
        return JsonResponse({"message": "ERROR"}, status=500)
