from django.urls import path

from .views import SignInView, CurrentUserView, CreateUserView


urlpatterns = [
    path('users/sign_in/', SignInView.as_view()),
    path('users/current_user/', CurrentUserView.as_view()),
    path('users/create/', CreateUserView.as_view()),
]
