from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    template = 'index.html'
    return render(request, template, {})

def about(request: HttpRequest) -> HttpResponse:
    content = {
        "f_name": "Иван",
        "s_name": "Петрович",
        "l_name": "Иванов",
        "email": "vasya@mail.ru",
        "phone": "8-923-600-01-02",
    }
    template = 'about.html'
    return render(request, template, content)




def item(request: HttpRequest, item_id: int) -> HttpResponse:

    _items = [
        {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
        {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
        {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
        {"id": 7, "name": "Картофель фри" ,"quantity":0},
        {"id": 8, "name": "Кепка" ,"quantity":124},
    ]

    for i in _items:
        if item_id == i['id']:
            return HttpResponse(f"""
                <h3>{i['name']}</h3>
                <p>quantity: {i['quantity']}</p>
            """)

    item_links = ""    
    for i in _items:
        item_links += f'<li><a href=\'{i["id"]}\'> {i["name"]} </a></li>'
        
    return HttpResponse(f"""
            <h1>Товар не найден</h1>
            Доступные товары:
            <ol>
                {item_links}
            </ol>
        """, status=404)




