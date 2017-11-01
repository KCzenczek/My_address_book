from datetime import datetime


def get_date(request):
    ctx = {
        'datetime': datetime.now(),
    }
    return ctx
