from django.shortcuts import render, redirect

# Create your views here.
def func1(requests):
	return render(requests,'rcb_home_page.html')
