from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

# Create your views here.
# @login_required
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)