from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Categorie, Comment, Post
from .forms import CommentForm, EditForm, PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.
# def home(request):
#     return render(request,'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu']= cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True


        context['cat_menu']= cat_menu
        context['total_likes'] = total_likes 
        context['liked'] = liked
        return context

class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Post added successfully!"

    # fields = '__all__'

class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Post edited successfully!"
    
class DeletePostView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Post deleted successfully!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeletePostView, self).delete(request, *args, **kwargs)

class AddCategoryView(SuccessMessageMixin, CreateView):
    model = Categorie
    template_name = 'add_category.html'
    
    fields = '__all__'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Category added successfully!"

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '),'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Categorie.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user) 
        liked = True
    
    # return HttpResponseRedirect(reverse('articleDetail', args=[str(pk)]))
    return redirect('articleDetail', post.pk)   

class AddCommentView(SuccessMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy('articleDetail', kwargs={'pk': self.kwargs['pk']})

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Comment added successfully!"

class DeleteCommentView(SuccessMessageMixin, DeleteView):
    model = Comment
    template_name = 'article.html'
    success_url = reverse_lazy('home')
    success_message = "Comment deleted successfully!"

    # def delete(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     messages.success(self.request, self.success_message % obj.__dict__)
    #     return super(DeleteCommentView, self).delete(request, *args, **kwargs)      


# def LikeView(request, pk):
#     post = Post.objects.get(id=pk)
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('articleDetail', args=[str(pk)]))