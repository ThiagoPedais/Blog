from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When

# Create your views here.
class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(pubished_post=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comment__published_comment=True, then=1)
                )
            )
        )

        return qs


class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(title_post__icontains=termo) | 
            Q(author_post__first_name__iexact=termo) | 
            Q(content_post__icontains=termo) | 
            Q(exerpt_post__icontains=termo) | 
            Q(category_post__name_cat__iexact=termo)              
        )

        return qs


class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)
        if not category:
            return qs
        
        qs = qs.filter(category_post__name_cat__iexact=category)

        return qs



class PostDetails(UpdateView):
    pass