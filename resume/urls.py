from django.urls import path
from resume.views import Home

urlpatterns = [

	path('', Home.as_view(), name="home")

]