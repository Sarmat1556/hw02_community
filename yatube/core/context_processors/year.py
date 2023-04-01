import datetime
def year(request):
    """Добавляет переменную с текущим годом."""
    year = datetime.datetime.today().strftime('%Y')
    return {
        'year':int(year)
    }