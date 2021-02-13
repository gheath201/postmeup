from django.shortcuts import render
from postsMain.models import post

def post(request, pk):
	post_obj = post.objects.get(pk=pk)
	context = {
	'post':post_obj
	}

	return render(request, "postsMain.html", context)
