from django.shortcuts import render
import os
#from functions import *


def index(request):
	return render(request,'index.html')
	
def diff_path(request):
	print "pol"
	if request.method=="GET":
		path = request.GET.get("address")
		print path
#		all_names = split_into_names(path)
#		print all_names
		return render(request,'diff_path.html')
	else:
		return render(request,'index.html')
		
def same_path(request):
	if request.method == "GET":
		return render(request,'same_path.html')
	else:
		return render(request,'index.html')
		
