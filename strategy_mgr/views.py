from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q

import random

from . import models

def stg_list(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'stg_list':[]}

    if request.method == 'POST':
        if(request.POST['action']=='delete'):
            post_stg_name = request.POST['stg_name']
            models.Strategy.objects.filter(Q(stg_name=post_stg_name) & Q(stg_owner=user_name)).delete()
            # print('delete successful')
                
    try:
        stg_set = models.Strategy.objects.filter(stg_owner=user_name)
        context['stg_list'] = stg_set
        
    except:
        print('stg set get failed')

    return render(request, 'strategy_list.html', context)

def upload_strategy(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'stg_list':[]}

    if request.method == 'POST':
        try:
            print(request.POST)
            new_stg = models.Strategy()
            new_stg.stg_name = request.POST['stg_name']
            new_stg.stg_owner = user_name
            new_stg.stg_description = request.POST['stg_description']
            new_stg.stg_file_path = request.FILES.get('stg_file')
            new_stg.save()
            return HttpResponse('succeed')
        except:
            return HttpResponse('strategy name conflict')


    try:
        stg_set = models.Strategy.objects.filter(stg_owner=user_name)
        context['stg_list'] = stg_set
    except:
        print('stg set get failed')

    return render(request, 'strategy_list.html', context)

def remote_stg_server(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'stg_server_list':[]}

    if request.method == 'POST':
        if(request.POST['action']=='delete'):
            post_stg_server_name = request.POST['stg_server_name']
            models.StrategyServer.objects.filter(Q(stg_server_name=post_stg_server_name) & Q(stg_server_owner=user_name)).delete()
            # print('delete successful')
                
    try:
        stg_server_set = models.StrategyServer.objects.filter(stg_server_owner=user_name)
        status = []
        for _ in range(len(stg_server_set)):
            status.append(random.randint(0,3))
        context['stg_server_list'] = dict(zip(stg_server_set,status))
        print(context['stg_server_list'])
        
    except:
        print('stg_server set get failed')

    return render(request, 'remote_stg_server.html', context)

def add_stg_server(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'stg_server_list':[]}

    if request.method == 'POST':
        try:
            print(request.POST)
            new_stg_server = models.StrategyServer()
            new_stg_server.stg_server_name = request.POST['stg_server_name']
            new_stg_server.stg_server_owner = user_name
            new_stg_server.stg_server_ip_addr = request.POST['stg_server_ip_addr']
            new_stg_server.stg_server_ip_port = request.POST['stg_server_ip_port']
            new_stg_server.save()
            return HttpResponse('succeed')
        except:
            return HttpResponse('strategy name or IP address conflict')


    try:
        stg_server_set = models.Strategy.objects.filter(stg_server_owner=user_name)
        context['stg_server_list'] = stg_server_set
    except:
        print('stg_server set get failed')

    return render(request, 'strategy_list.html', context)