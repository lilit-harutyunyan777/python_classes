from django.shortcuts import HttpResponse
import datetime
import time


def hello(requests):
    return HttpResponse("<h1>Hello Django World</h1>")


def null(requests):
    return HttpResponse("<h1>Lilit</h1>")


def my_font(requests):
    num = random.randint(1, 5)
    shrift = f"<h{num}> Name: Lilit Surname: Harutyunyan<h{num}>"
    return HttpResponse(shrift)


def greeting(requests):
    return HttpResponse("<h3>Hello Python World</h3>")


def introduction(requests):
    return HttpResponse("<h1>It's my first work, which includes some interesting Django project ideas</h1>")


def current_datetime(requests):
    current_date = datetime.date.today()
    current_time = datetime.datetime.today().time()
    return HttpResponse(f"<h1>date: {current_date}, time: {current_time}</h1>")


def my_dictionary(requests):
    my_dict = {}
    my_nums = range(1, 16)
    for i in my_nums:
        my_dict[i] = i * 2
    return HttpResponse(my_dict)

