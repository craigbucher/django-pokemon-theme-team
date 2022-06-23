from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random
import requests as HTTP_Client

# Create your views here.
def index(request):
    rand = random.randint(1, 100)
    poke = request.GET.get('poke') or rand
    
    endpoint = f'https://pokeapi.co/api/v2/pokemon/{poke}/'
    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()
    pokeType = responseJSON['types'][0]['type']['url']
    type_name = responseJSON['types'][0]['type']['name']
    print(type_name)
    url1 = responseJSON['sprites']['front_default']

    urls = []
    test = type_name

    for i in range(2,8):
        newrand = random.randint(1, 50)
        API_response2 = HTTP_Client.get(pokeType)
        responseJSON2 = API_response2.json()
        type_url = responseJSON2['pokemon'][newrand]['pokemon']['url']
        API_response3 = HTTP_Client.get(type_url)
        responseJSON3 = API_response3.json()
        poke_url = responseJSON3['sprites']['front_default']
        urls.append(poke_url)
        
    response = render(request, 'pages/index.html', {'type_name': type_name, 'preview_url': url1, 'preview2_url': urls[0], 'preview3_url': urls[1], 'preview4_url': urls[2], 'preview5_url': urls[3], 'preview6_url': urls[4], })
    return response

# from Francisco
# picture ={
#     "pic":responseJSON['sprites']['front_default']
# }