from django.contrib import admin
from django.http.request import HttpRequest
from film.models import FilmModel, ActorModel, CommentModel, LikeModel, Category


@admin.action(description="Mark selected stories as published")
def change_rating(FilmAdmin, request, queryset=FilmModel.objects.all()):
    queryset.update(rating=0)


class CommentAdmin(admin.TabularInline):
    model = CommentModel
    extra = 3

@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "pub_date")
    list_display_links = ("name", "rating")
    list_editable = ("pub_date",)
    list_filter = ("pub_date",)
    search_fields = ("name",)
    fieldsets = [
        (
            "BASIC OPTIONS",
            {
                "fields": ["name", "rating", "pub_date"],
            },
        ),
        (
            "ADVANCED OPTIONS",
            {
                "fields": ["poster", "video", "views_count", "about"],
            },
        ),
    ]
    actions = [change_rating]
    inlines = [CommentAdmin]



# admin.site.register(FilmModel, FilmAdmin)
admin.admin.register(ActorModel)


admin.site.register(LikeModel)
admin.site.register(Category)

admin.sites.AdminSite.site_title = "Film Administrasiyası"
admin.sites.AdminSite.site_header = "Film Administrasiyası"