from django.urls import path


from .views import DrawView, RouterBusView

urlpatterns = [
    path('draw', DrawView.as_view(), name='draw'),
    path('', RouterBusView.as_view(), name='router'),
]