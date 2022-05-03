from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from restaurants import views

urlpatterns = [
    path('subsidary', views.SubsidaryList.as_view()),
    path('subsidary/<int:id>', views.SubsidaryDetail.as_view()),
    path('', views.RestaurantAPI.as_view()),
    path('subsidary/menu', views.MenuListView.as_view()),
    path('subsidary/menu/<int:id>/', views.MenuDetailView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)