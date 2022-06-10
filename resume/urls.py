from django.urls import path
from resume.views import Home, Home_Page, Power_Building

urlpatterns = [

	path('', Home_Page.as_view(), name="home"),
	path('home_page', Home.as_view(), name="home_page"),
	path('power_building/', Power_Building.as_view(), name="power_building")

]