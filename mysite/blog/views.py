from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
def home(request):

    queryset=Post.objects.all()
    data={
        "queryset":queryset
    }
    return render(request,'blog/home.html',{})