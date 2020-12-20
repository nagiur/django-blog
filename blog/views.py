from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/list.html'


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/list_detail.html', {'post': post})


def post_list(request):
    object_list = Post.publish.all()
    # paginator = Paginator(object_list,1) # 3 posts in each page
    paginator = Paginator(object_list)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html', {'page': page, 'posts': posts})
