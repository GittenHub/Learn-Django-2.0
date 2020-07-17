from django.shortcuts import render_to_response,get_object_or_404  #不使用render，改使用render_to_response

def home(request):
    context = {}
    return render_to_response('home.html',context)