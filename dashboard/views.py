from django.shortcuts import render
from django.shortcuts import redirect

from . import models
from strategy_mgr.models import Strategy
# Create your views here.

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    user_name = request.session['user_name']
    context = {'stg_num':0}
    try:
        stg_set = Strategy.objects.filter(stg_owner=user_name)
        context['stg_num'] = stg_set.count()
    except:
        print('stg set get failed')
    # print(stg_set)
    return render(request, 'index.html', context)

def base(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'base.html')

