from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # return HttpResponse("用户列表")

    # 1.优先根目录下寻找templates, (不配置则无效)
    # 2.app/templates/寻找xx.html(按照app注册顺序寻找)
    return render(request, "user_list.html")


def user_add(request):
    # return HttpResponse("添加用户")
    return render(request, "user_add.html")


def tpl(request):
    name = "jzy"
    roles = ["管理员", "保安", "经理"]
    user_info = {"name": "超人", "salary": 100000, "role": "CTO"}
    data_list = [{"name": "01", "salary": 100000, "role": "CTO"},
                 {"name": "02", "salary": 100000, "role": "CTO"},
                 {"name": "03", "salary": 100000, "role": "CTO"}]

    return render(request, "tpl.html", {"n1": name,
                                        "n2": roles,
                                        "n3": user_info,
                                        "n4": data_list})


def news(request):
    # 1.定义一些新闻 或 去数据库 网络请求去联通新闻
    # 向地址：http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/03/news
    # 第三方模块：request
    import requests
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/03/news",
                       headers={'user-agent': 'Mozilla/5.0'})
    data_list = res.json()

    return render(request, "news.html", {"news_list": data_list})
