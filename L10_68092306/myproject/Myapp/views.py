from django.shortcuts import render
from Myapp.models import Person

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        if name and age:
            Person.objects.create(name=name, age=age)

    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})