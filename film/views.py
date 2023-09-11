from django.shortcuts import render, redirect
from film.models import FilmModel, ActorModel, CommentModel
from film.models import LikeModel, Category
from django.views.generic import View

def isprime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

class IndexView(View):
    def get(self, request, *args, **kwargs):
        films = FilmModel.objects.order_by("-id")
        categories = Category.objects.all()

        search = request.GET.get("search")

        if search:
            films = FilmModel.objects.filter(
                name__contains = search
            )

        context = {
            "films": films,
            "isprime": isprime(28),
            "categories": categories,
        }
    
        return render(request, 'index.html', context)

class CategoryFilmsView(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=id)
        categories = Category.objects.all()

        context = {
            "category": category,
            "categories": categories,
        }

        return render(request, 'categoryfilms.html', context)

class DetailView(View):
    def get(self, request, id, *args, **kwargs):
        film = FilmModel.objects.get(id=id)
        film_comments = CommentModel.objects.filter(
            film = film,
            parent = None
        )
        categories = Category.objects.all()

        context = {
            "film": film,
            "film_comments": film_comments,
            "categories": categories,
        }
        if request.user.is_authenticated:
            user_comments = CommentModel.objects.filter(
                user = request.user,
            )
            context["user_comments"] = user_comments
        return render(request, 'detail.html', context)
    def post(self, request, id, *args, **kwargs):
        choice = request.POST.get("choice")

        if choice == "comment":
            comment = request.POST.get("comment")
            film_id = request.POST.get("film_id")

            film = FilmModel.objects.get(id=film_id)

            CommentModel.objects.create(
                user = request.user,
                film = film,
                comment = comment
            )
        elif choice == "like":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)

            if not LikeModel.objects.filter(user=request.user, film=film).exists():
                LikeModel.objects.create(
                    user = request.user,
                    film = film
                )
            else:
                like = LikeModel.objects.get(user=request.user, film=film)
                like.delete()
        elif choice == "reply":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            reply = request.POST.get("reply")

            CommentModel.objects.create(
                user = request.user,
                film = film,
                comment = reply,
                parent = comment,
            )
        return redirect("detail", id=id)


def deleteComment(request, id):
    comment = CommentModel.objects.get(id = id)
    comment.delete()
    return redirect("detail", id = comment.film.id)


    