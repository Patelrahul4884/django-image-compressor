from django.urls import path
from . import views

app_name='size_reducer'
urlpatterns = [
    path('',views.MainView.as_view(),name='all'),
    path('<int:pk>/delete',views.ImageDelete,name='delete')
]
