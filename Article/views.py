from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "article/index.html", context=context)


@login_required
def search_article(request):
    "Search for article using title"
    query = request.GET.get("query")

    if query:

        articles = Article.objects.filter(title__icontains=query)
        context = {"articles": articles}
        return render(request, "article/search.html", context=context)
    else:
        return render(request, "article/search.html")


def create_article(request):
    "Create new article object"
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article = Article(title=title, content=content)
        article.save()
        return render(
            request, "article/create_article.html", context={"article": article}
        )
    else:
        return render(request, "article/create_article.html")


def delete_article(request):
    "Delete article using ID"
    if request.method == "POST":
        article_id = request.POST.get("article_id")
        article = Article.objects.get(id=article_id)
        article.delete()
        return render(
            request, "article/delete_article.html", context={"article": article}
        )
    else:
        return render(request, "article/delete_article.html")


def edit_article(request):
    "Update article using ID"
    if request.method == "POST":
        article_id = request.POST.get("article_id")
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return render(
            request, "article/edit_article.html", context={"article": article}
        )
    else:
        return render(request, "article/edit_article.html")


def updateArticle(request, article_id):
    "Update article using ID"
    try:
        article = Article.objects.get(id=article_id)
        context = {"article": article}
        return render(request, "article/updateArticle.html", context=context)
    except Article.DoesNotExist as e:
        return render(request, "article/ERROR_404.html", context={"error": e})


def profile(request):
    return render(request, "article/profile.html")


def ERROR_404(request):
    return render(request, "article/ERROR_404.html")
