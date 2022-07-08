from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


def handler404(request, exception):
    return render(request, "errorHandlers/404.html")


def handler500(request, *args, **argv):
    return render(request, 'errorHandlers/500.html', status=500)


def questionary_success_created(request):
    return render(request, "questionary/questionary_success_create.html")


def questionary_list(request):
    user = request.user

    if user.is_anonymous or not user.is_staff or not user.is_authenticated:
        raise Http404

    return render(request, 'questionary/questionary-list.html')


def questionary_creating(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        raise Http404

    return render(request, "questionary/questionary-creating.html")
