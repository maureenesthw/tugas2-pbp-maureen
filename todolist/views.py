from django.shortcuts import render

# Create your views here.
def show_todolist(request):
    context = {
        'name' : 'Maureen Esther Wijaya',
        'npm' : '2106705335'
    }
    return render(request, "todolist.html", context)