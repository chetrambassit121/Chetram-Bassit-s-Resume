from django.urls import path
from resume.views import Home, Home_Page

urlpatterns = [

	path('', Home_Page.as_view(), name="home"),
	path('home_page', Home.as_view(), name="home_page")

]