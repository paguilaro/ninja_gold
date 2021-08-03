from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("Ninja Gold Prueba")


def index(request):
    context= {
        'imagenes': [
            'https://staticg.sportskeeda.com/editor/2021/05/26f5c-16202539456912-800.jpg',
            'https://kaijugaming.com/wp-content/uploads/2021/07/Genshin-Impact-announces-massive-update-with-new-city-Inazuma-and.jpg',
            'https://static3.srcdn.com/wordpress/wp-content/uploads/2021/05/Genshin-Impact-Housing.jpg',
            'https://preview.redd.it/jrdnf43bc5s51.png?width=1920&format=png&auto=webp&s=5fb70afec523e4318b67af6eab047a10fe1280ca',
        ]
    } 
    return render(request, 'index.html', context) 

