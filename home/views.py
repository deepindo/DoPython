from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import cache_page
from django.db.models import Q

from news.models import News
from products.models import Product


@cache_page(60 * 15)  # 单位：秒数，这里指缓存 15 分钟
def home(request):
    # 新闻展报
    news_list = News.objects.all().filter(~Q(news_type='通知公告')).order_by('-publish_date')
    post_list = set()
    post_num = 0
    for s in news_list:
        if s.news_photo:
            post_list.add(s)
            post_num += 1
        if post_num == 3:  # 只截取最近的3个展报
            break

    # 新闻列表
    if len(news_list) > 7:
        news_list = news_list[0:7]

    # 通知公告
    notice_list = News.objects.all().filter(Q(news_type='通知公告')).order_by('-publish_date')
    if len(notice_list) > 4:
        notice_list = notice_list[0:4]

    # 产品中心
    product_list = Product.objects.all().order_by('-product_views')
    if len(product_list) > 4:
        product_list = product_list[0:4]

    # 返回结果
    context = {
        'active_menu': 'home',
        'post_list': post_list,
        'news_list': news_list,
        'notice_list': notice_list,
        'product_list': product_list,
    }
    return render(request, 'home/home.html', context)
