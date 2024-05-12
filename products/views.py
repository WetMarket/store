from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

# Добавил категории для сайта
categories_db = [{'title': "Женское", 'url_name': 'women'},
                 {'title': "Мужское", 'url_name': 'men'},
                 {'title': "Детское", 'url_name': 'kids'},
]

data_db = [

    {'id': 1, 'title': 'Синяя куртка The North Face',
     'content': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель. ',
     'is_published': True},

    {'id': 2, 'title': 'Черный рюкзак Nike Heritage',
     'content': 'Плотная ткань. Легкий материал.',
     'is_published': True},

    {'id': 3, 'title': 'Черные туфли Dr. Martens 1461',
     'content': 'Гладкий кожаный верх. Натуральный материал.',
     'is_published': True},
]

def index(request):
    data = {
        'title': 'Подборка товаров',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'products/index.html', context=data)

def about(request):
    return render(request, 'products/about.html',
                  {'title': 'О сайте', 'menu': menu})
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
def addpage(request):
    return HttpResponse("Добавление статьи")
def contact(request):
    return HttpResponse("Обратная связь")
def login(request):
    return HttpResponse("Авторизация")
def show_categories(request, cat_slug):
    for category in categories_db:
        if category['url_name'] == cat_slug:
            return HttpResponse(f"Категория {category['title']}")

#Из первой лабораторной
def archive(request, year):
    if year > 2024:
        return redirect('index', permanent=True)
    return HttpResponse(f"<h1>Коллекции по годам</h1><p><h2>Год: {year}</h2></p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
