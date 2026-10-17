import datetime


def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def word_count(text):
    return len(text.split())


def ugly_function(x, y, z):
    return x + y + z
