from django.shortcuts import render

# Create your views here.
def index(request):
    mensaje=''
    context={
        'mensaje':mensaje,
    }
    return render(request, 'base.html',context)
