from models import Note
from django.contrib.auth.models import User
from random import randrange
from sys import stdout
from django.utils.timezone import now
from django.utils.encoding import smart_unicode


def gen_random_string_en(dicts_array, size):
    string = ""
    dicts_size = len(dicts_array)

    while size > len(string):
        string += dicts_array[randrange(dicts_size)] + " "

    return string


def gen_random_string_zh(dicts_array, size):
    string = ""
    dicts_size = len(dicts_array)

    while size > len(string):
        string += smart_unicode(dicts_array[randrange(dicts_size)])
        if 0 == (len(string) % randrange(2, 5)):
            string += " "

    return string


def gen(count, dicts, get_string_function):
    user = User.objects.all()[0]
    date_now = now()
    total = count

    while 0 < count:
        stdout.write("%d\r" % (total - count))
        stdout.flush()
        count -= 1
        note = Note()
        note.user = user
        note.pub_date = date_now
        note.title = get_string_function(dicts, randrange(20, 100))
        note.body = get_string_function(dicts, randrange(500, 1000))
        note.save()


def gen_en(count):
    f = open("dict.txt", "r")
    dicts = [line.strip() for line in f]
    f.close()

    gen(count, dicts, gen_random_string_en)


def gen_zh(count):
    f = open("zh_dict.txt", "r")
    dicts = [line.strip() for line in f]
    f.close()

    gen(count, dicts, gen_random_string_zh)
