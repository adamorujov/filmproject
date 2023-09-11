from django.urls import path
from film import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('detail/<int:id>/', views.DetailView.as_view(), name="detail"),
    path('delete/<int:id>/', views.deleteComment, name="delete_comment"),
    path('category/<int:id>', views.CategoryFilmsView.as_view(), name="categoryfilms"),
]