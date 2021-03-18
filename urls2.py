from django.contrib import admin
from django.urls import include,path   
from . import views2

urlpatterns=[
    path('',views2.main),
    path('page5',views2.history),
    path('mainhtml2.html',views2.main),
    path('create_account.html',views2.account),
    path('cost',views2.cost),
    path('cost1',views2.cost1),
    path('transaction',views2.transaction),
    path('transaction_done_now_main_page',views2.main),
    path('about',views2.about),
    path('details',views2.details),
    path('food_booked',views2.food_booked_pay),
    


]
