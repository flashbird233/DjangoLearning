"""
URL configuration for DjangoLearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

import App01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', App01.views.hello_world),
    path('blog/<int:blog_id>', App01.views.blog),  # 定义一个带参数的URL
    path('', App01.views.hello_world),  # 默认访问路径
    # 设置媒体文件的路由地址
    re_path(r'media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}, name="media")
]
