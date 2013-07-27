from models import Note
from django.contrib.auth.models import User
from random import randrange
from datetime import datetime


def gen_random_string(dicts_array, size):
    string = ""
    dicts_size = len(dicts_array)

    while size > len(string):
        string += dicts_array[randrange(dicts_size)] + " "

    return string


def gen(count):
    f = open("dict.txt", "r")
    dicts = [line.strip() for line in f]
    f.close()
    user = User.objects.all()[0]

    while 0 < count:
        print(count)
        count -= 1
        note = Note()
        note.user = user
        note.pub_date = datetime.now()
        note.title = gen_random_string(dicts, 100)
        note.body = gen_random_string(dicts, 1000)
        note.save()
