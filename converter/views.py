from django.shortcuts import render
from num2words import num2words
from django.http import JsonResponse

# Create your views here.



def home(request):
    words  = num2words(4200.50)
    words = words.replace("-"," ")
    return render(request, 'numbertowords.html',{'words':words})


def get_words(request):
    number = request.GET.get('number')
    words  = num2words(number, lang='en_IN')
    words = words.replace("-"," ")
    data = {
        'words' : words,
        'valid' : True
    }
    return JsonResponse(data)