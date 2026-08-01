#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import players
from .forms import reviewform
from django.forms.models import model_to_dict
# Create your views here.
def func1(requests):
	player_details = players.objects.all() 
	return render(requests,"csk_home_page.html",{ "all_players": player_details })
def func2(requests):
	if requests.method == 'POST':
		form = reviewform(requests.POST)
		if form.is_valid():
			players.objects.create(**form.cleaned_data)
			return redirect("/")
	form = reviewform()
	return render (requests,"feedback.html", { "form" : form })
def func3(request,pid):
	item = get_object_or_404(players,pk = pid)
	if request.method == 'POST':
		form = reviewform(request.POST)
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.age = form.cleaned_data['age']
			item.save()
			return redirect ('show_url')
	data = model_to_dict(item)
	form = reviewform(initial = data)
	return render (request, "feedback.html", { "form":form })
def func4(request,pid):
	item = get_object_or_404(players,pk = pid)
	item.delete()
	return redirect ('show_url')
