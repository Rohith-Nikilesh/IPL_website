from django.shortcuts import render

# Create your views here.
def func(requests):
	return render(requests,"home_page.html")