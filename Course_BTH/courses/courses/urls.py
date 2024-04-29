from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version='v1',
        description="APIs for CourseApp",
        contact=openapi.Contact(email="btrinh2505@gmail.com"),
        license=openapi.License(name="LT Bảo Trinh @2024"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('courseapp.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',schema_view.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui'),
    re_path(r'^redoc/$',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
