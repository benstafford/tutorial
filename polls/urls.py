from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),

]