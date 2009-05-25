from make.utils.http import render

def index(request):
    return render('home/index')
