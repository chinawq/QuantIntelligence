import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q

from strategy_mgr.models import Strategy
from data_mgr.models import HistData

from . import models

def run_backtesting(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'stg_list':[],'data_list':[]}

    if request.method == 'POST':
        try:
            print(request.POST)
            task_strategy_list = []
            task_dataset_list = []

            for i in request.POST.getlist('selected_stg'):
                task_strategy_list.append(i.split("(")[0])
            for j in request.POST.getlist('selected_dataset'):
                task_dataset_list.append(j.split("(")[0])

            new_task = models.BacktestingTask()
            new_task.task_name = request.POST['task_name']
            new_task.task_owner = user_name
            new_task.task_strategy_list = json.dumps(task_strategy_list)
            new_task.task_dataset_list = json.dumps(task_dataset_list)
            if 'standalone_checkbox' in request.POST:
                if 'combined_checkbox' in request.POST:
                    # task policy =2: both modes
                    new_task.task_policy = 2
                else:
                    # task policy = 0: standalone mode
                    new_task.task_policy = 0
            else:
                # task policy =1: combined mode
                new_task.task_policy = 1
            # False represents the task is not finished
            new_task.task_status = False
            new_task.save()

        except:
            print("new task add failed")

    try:
        data_set = HistData.objects.filter(Q(data_owner=user_name) | Q(data_owner='public'))
        context['data_list'] = data_set
        stg_set = Strategy.objects.filter(stg_owner=user_name)
        context['stg_list'] = stg_set
        
    except:
        print('data set get failed')

    return render(request, 'run_backtesting.html',context)

def backtesting_task_list(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user_name = request.session['user_name']
    context = {'task_list':[]}

    try:
        task_set = models.BacktestingTask.objects.filter(task_owner=user_name)
        context['task_list'] = task_set
        
    except:
        print('task list get failed')

    return render(request, 'backtesting_task_list.html', context)