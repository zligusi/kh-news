from django.shortcuts import render

def home(request):
    data = {
        'title':'Home',
        'values':['some','Hello','123'],
        'oleg':{
            'car': 'BMW',
            'age': 23 ,
            'hobby' : 'football',
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request , 'main/about.html', {'title':'About'})
