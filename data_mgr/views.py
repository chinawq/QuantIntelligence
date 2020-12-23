from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q

import pandas as pd

from QuantIntelligence.settings import MEDIA_ROOT

from . import models


# Create your views here.

def data_list(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'data_list':[]}

    if request.method == 'POST':
        if(request.POST['action']=='delete'):
            post_stg_name = request.POST['data_name']
            models.HistData.objects.filter(Q(name=post_stg_name) & Q(data_owner=user_name)).delete()
            # print('delete successful')
                
    try:
        data_set = models.HistData.objects.filter(Q(data_owner=user_name) | Q(data_owner='public'))
        context['data_list'] = data_set
        
    except:
        print('data set get failed')

    return render(request, 'data_list.html', context)

def import_hist_data(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']

    if request.method == 'POST':
        # try:
        print(request.POST)
        new_data = models.HistData()
        new_data.name = request.POST['data_name']
        new_data.code = request.POST['data_code']
        new_data.data_owner = user_name
        new_data.data_type = request.POST['data_type']
        new_data.data_frequency = request.POST['data_freq']
        new_data.data_file_path = request.FILES.get('data_file')
        new_data.save()
        data_path = MEDIA_ROOT+'/'+str(new_data.data_file_path)
        dt = pd.read_csv(data_path)
        new_data.start_date = dt['Date Time'][0]
        new_data.end_date = dt['Date Time'][dt.shape[0]-1]
        new_data.save()
        return HttpResponse('succeed')
        # except:
        #     return HttpResponse('data name conflict')
