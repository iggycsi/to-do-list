from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})

def about(request):
	context = {'first_name' : 'Igor', 'last_name': 'Tasev'}
	return render(request, 'about.html', context)