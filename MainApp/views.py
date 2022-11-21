from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Index page")

def about(request: HttpRequest) -> HttpResponse:
    _about = {
        "f_name": "Иван",
        "s_name": "Петрович",
        "l_name": "Иванов",
        "email": "vasya@mail.ru",
        "phone": "8-923-600-01-02",
    }

    return HttpResponse(f"""
    <!DOCTYPE html>
    <head>
        <title>About</title>
    </head>
        <body>
            <h1>О авторе</h1>
            <table>
                <tr><td>Имя:</td><td>{_about['f_name']}</td></tr>
                <tr><td>Фамилия:</td><td>{_about['s_name']}</td></tr>
                <tr><td>Отчество:</td><td>{_about['l_name']}</td></tr>
                <tr><td>Почта:</td><td>{_about['email']}</td></tr>
                <tr><td>Телефон:</td><td>{_about['phone']}</td></tr>
            </table>
        </body>
    </html>
    """)


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
            <ul>
                {item_links}
            </ul>
        """)




