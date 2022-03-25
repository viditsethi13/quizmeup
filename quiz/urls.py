from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name="index"),
	path('home',views.home,name="home"),
	path('login',views.login,name="login"),
	path('registration',views.registration,name="registration"),
	path('logout',views.logout,name="logout"),
	path('quizzing',views.quizzing,name="quizzing"),
	path('exam',views.exam,name="exam"),
	path('message',views.message,name="message"),
	path('contact',views.contact,name="contact"),
	path('about',views.about,name="about")
]