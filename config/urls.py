"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls    import path, include

from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg       import openapi


schema_url_patterns = [
    path('restaurants', include('restaurants.urls')),
    path('results', include('results.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Bear-Robotics-API",
        default_version='1.0.0',
        description="Bear-Robotics 과제 swagger",
        terms_of_service="https://github.com/wanted-pre-onboarding-2nd-BE-Team-D/002_Bear_Robotics_Korea",
    ),
    public=True,
    permission_classes=(AllowAny, ),
    patterns=schema_url_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('restaurants', include('restaurants.urls')),
    path('results', include('results.urls')),

    # swagger url
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]
