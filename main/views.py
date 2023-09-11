from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Reza Apriono',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)