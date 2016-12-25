from django.shortcuts import render
import os
from functions import *

def index(request):
	return render(request,'index.html')
	
def diff_path(request):
	if request.method=="GET":
		
		take_path = request.GET.get("take_path")
		
		# make valid path
		path = ""
		if take_path == "diff_path":
			path1 = request.GET.get("address")
			path = os.path.dirname(os.path.abspath(__file__))
			path = path + path1
		else:
			path = os.path.dirname(os.path.abspath(__file__))
			path = path + "/../../search"	
		
		# send path and fetch all files
		all_files = split_into_names(path)
		# not fetch movies from that files
		all_movies = bring_movies(all_files)
#		print all_movies
		return render(request,'diff_path.html',{'movies':all_movies})
	else:
		return render(request,'index.html')
