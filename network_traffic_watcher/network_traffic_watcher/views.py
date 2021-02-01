
from django.shortcuts import render
 
def chart(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'chart.html', context)
