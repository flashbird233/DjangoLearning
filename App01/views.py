from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 从数据库中获取数据，然后将数据传递给模板，模板加数据即为网页
# 用于编写web应用视图，接收数据，处理数据，与model（模型），Template（模板）交互，返回应答
def hello_world(request):
    print("页面请求处理中")
    return render(request, "app01page.html")


def blog(request, blog_id):
    return HttpResponse("博客ID：%s" % blog_id)
