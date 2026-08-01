from django.urls import path
from . import views
urlpatterns = [
	path('',views.func1,name = 'show_url'),
	path('feedback',views.func2),
	path('update/<int:pid>',views.func3),
	path('delete/<int:pid>',views.func4)
]