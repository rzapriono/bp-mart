from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
      'app_name' : 'bp-mart',
      'name': 'Reza Apriono',
      'class': 'PBP D',
   }
    return render(request, "main.html", context)