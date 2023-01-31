from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .froms import PostForm,EditForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model =  Post
    template_name = 'home.htm'
    ordering = ['-post_date']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.htm'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name  = "add_post.htm"
    # fields = '__all__'  
    
    # fields  = ('title','body')
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.htm"
    # fields = ['title','title_tag','body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.htm"
    
    success_url = reverse_lazy('home')
    