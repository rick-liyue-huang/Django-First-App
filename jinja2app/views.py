from django.shortcuts import render

# Create your views here.

def test(request):

  data = {'name': 'rick', 'age': 122}
  return render(request, 'test.html', data)