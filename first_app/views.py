from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={
        'value' : ['a','b','c','d'],
        'Add':21,
        'slash':' “I’m Jai” ',
        'Cap':'cap',
        'Cut' :'Tanvir Mahmud Neon',
        'Birthday':datetime.datetime.now(),
        'Sort': [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
                ],
        'lines' :[
            {
                'one'
            },
            {
                'two'
            },
            {
                'three'
            },

        ],
        'Lower':'MY NAME IS TANVIR',
        'List':'Naveen',
        'Word':"Tanvir Mahmud"
    }
    return render (request,'home.html',d)