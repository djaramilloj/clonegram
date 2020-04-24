# Django
from django.http import HttpResponse
import json 
# Utilities 
from datetime import datetime


# founctions that responds to a Http request Django calls them views
def hello_world(rquest):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hours')
    return HttpResponse('Oh, hi! current server time is {now}'.format(
        now=str(now))
    )


def sort_integers(request):
    # Return json response of sorted list of numbers
    response_url = request.GET['numbers']
    sorted_numbers = sorted([int(x) for x in response_url.split(',')])
    data = {
        'status': 'ok',
        'numbers' : sorted_numbers,
        'message' : 'integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
        )


def say_hi(request, name, age):
    # return a greeting based on age

    if age < 12:
        message = 'sorry {}, you are not allowed to be here'.format(name)
    else:
        message = 'Hello {}, welcome to clonegram'.format(name)

    return HttpResponse(message)