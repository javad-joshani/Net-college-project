
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",include('product.urls')),
    path("",include('account.urls')),
    path('admin/', admin.site.urls),
    path("",include("django.contrib.auth.urls")),
    path('comment/', include('comment.urls')),
    path('cart/',include('cart.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)