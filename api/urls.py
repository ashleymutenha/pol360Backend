from django.urls import path
from . import views

urlpatterns =[

    path('add/',views.postData),
    path('checkData/',views.checkPostedData),
    path('addBroker',views.addBroker),
    path('getBrokers', views.getBrokers),
    path('deleteBroker', views.deleteBroker),
    path('setasdefault',views.setAsDefault),
    path('editBroker',views.editBroker)
]