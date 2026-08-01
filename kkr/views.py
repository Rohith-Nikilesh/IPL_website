from django.shortcuts import render,redirect

# Create your views here.
def func1(requests):
	return render(requests,'kkr_home_page.html')