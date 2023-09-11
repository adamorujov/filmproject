from django.urls import path
from film.api import views


urlpatterns = [
    path('films/', views.FilmListAPIView.as_view(), name="films"),
    path('film/<int:pk>/', views.FilmRetrieveAPIView.as_view(), name="film"),
    path('film-create/', views.FilmCreateAPIView.as_view(), name="film-create"),
    path('film-update/<int:pk>/', views.FilmUpdateAPIView.as_view(), name="film-update"),
    path('film-delete/<int:pk>/', views.FilmDestroyAPIView.as_view(), name="film-delete"),
    path('film-retrieve-update-delete/<int:pk>/', views.FilmRetrieveUpdateDestroyAPIView.as_view(), name="film-retrieve-update-delete"),

    path('actors/', views.ActorListAPIView.as_view(), name="actors"),
    path('actor/<int:pk>/', views.ActorRetrieveAPIView.as_view(), name="actor"),
    path('actor-create/', views.ActorCreateAPIView.as_view(), name="actor-create"),
    path('actor-update/<int:pk>/', views.ActorUpdateAPIView.as_view(), name="actor-update"),
    path('actor-delete/<int:pk>/', views.ActorDestroyAPIView.as_view(), name="actor-delete"),
]