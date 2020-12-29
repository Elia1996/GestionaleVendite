import datetime

def Hour():
    return datetime.datetime.now().strftime("%H:%M")

def Data():
    return datetime.datetime.now().strftime("%d/%m/%Y")

