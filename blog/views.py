from django.shortcuts import render
from django.http import render, get_object_or_404

# Create your views here.
from .models import BlogPost



def blog_post_detail_page(request, id):
    obj = get_object_or_404(BlogPost, id=id)
    #obj = BlogPost.objects.get(id=str(id))
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, "", {})