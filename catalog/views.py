from django.shortcuts import render

def some_title(request):
    return render(request, 'catalog/some_title.html')
