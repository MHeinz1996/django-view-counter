from django.shortcuts import render
from django.http import HttpResponse
import random

# Initialize a users dictionary to keep track of session
users = {}

def index(request):
    print(users)

    # get user id from our cookies
    user_id = request.COOKIES.get('user_id')

    user = users.get(user_id)

    # if there is no user yet, generate a random user_id and set the count to 1
    if not user:
        unique = False
        while unique == False:
            # While loop ensures that the generated user_id is not already being used 
            user_id = str(random.randint(10000000, 99999999))
            if user_id not in users:
                unique = True

        users[user_id] = {
            'count': 1
        }
    else:
        # if the user has an open session, increment their view counter
        users[user_id]['count'] += 1

    response = render(request, 'view_counter_app/index.html', users[user_id])
    
    # set cookie to the user_id
    response.set_cookie('user_id', user_id)
    return response