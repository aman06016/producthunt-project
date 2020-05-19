"""bookkritic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import selfhelp.views
import genre.views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('',genre.views.home,name='home'),
    path('home/',genre.views.home,name='home'),
    path('book_detail/<int:onebook_id>/',selfhelp.views.bookdetail,name='bookdetail'),
    path('genre/<int:book_id>/',selfhelp.views.booklist,name='selfhelp'),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
