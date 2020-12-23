"""QuantIntelligence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

import login.views as login_view
import dashboard.views as dashbd_view
import backtesting_mgr.views as btmgr_view
import data_mgr.views as datamgr_view
import strategy_mgr.views as stgmgr_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',dashbd_view.base),
    path('index/', dashbd_view.index),
    path('strategy_list/',stgmgr_view.stg_list),
    path('upload_strategy/',stgmgr_view.upload_strategy),
    path('remote_stg_server/',stgmgr_view.remote_stg_server),
    path('add_stg_server/',stgmgr_view.add_stg_server),
    path('run_backtesting/',btmgr_view.run_backtesting),
    path('backtesting_task_list/',btmgr_view.backtesting_task_list),
    path('data_list/',datamgr_view.data_list),
    path('import_hist_data/',datamgr_view.import_hist_data),
    path('login/', login_view.login),
    path('register/', login_view.register),
    path('logout/', login_view.logout),
    
]
