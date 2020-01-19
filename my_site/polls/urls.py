from polls import views


app_name = 'polls'

from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='details'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name= 'vote')
]