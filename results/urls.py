from django.urls import path

from results.views import ResultView, SalesKPIView, PaymentKPIView, PartyKPIView

urlpatterns = [
    path('', ResultView.as_view()),
    path('sales/', SalesKPIView.as_view()),
    path('payment/', PaymentKPIView.as_view()),
    path('party/', PartyKPIView.as_view()),
]