from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants import views

urlpatterns = [
    path('/subsidary', views.SubsidaryList.as_view()),
    path('/subsidary/<int:id>', views.SubsidaryDetail.as_view()),

    path('/', views.RestaurantListCR.as_view()),
    path('/<int:id>', views.RestaurantListUD.as_view()),

    path('/subsidary/menu', views.MenuCreateListView.as_view(), name='MenuCreateList'),
    path('/subsidary/menu/<int:id>', views.MenuDetailView.as_view(), name='MenuDetail')
]

# urlpatterns = format_suffix_patterns(urlpatterns)