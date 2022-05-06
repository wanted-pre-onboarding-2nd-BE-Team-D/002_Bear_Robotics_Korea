from django.urls import path

from results.views import ResultView

urlpatterns = [
    path('/', ResultView.as_view()),
]