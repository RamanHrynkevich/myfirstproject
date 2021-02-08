from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_name = request.GET['username']
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	s_user_text = user_text.split()
	len_user_text = len(s_user_text)
	return render(request, 'reverse.html',{'username':user_name,'usertext':user_text, 'reversedtext':reversed_text, 'lenusertext':len_user_text})
