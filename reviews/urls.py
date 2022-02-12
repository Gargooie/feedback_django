from django.urls import path, include

from . import views


urlpatterns=[
    path("", views.ReviewView.as_view()),
    path("profiles/", include("profiles.urls")),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.DetailedReviewView.as_view(), name="detailed-review")

]