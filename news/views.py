from django.shortcuts import render
from django.core.paginator import Paginator
"""
安装：pip install pyquery, 但是仍然会出现版本问题，
找不到对应的某些模块，得改源码，那怕是从网上下载兼容python3.0以上的版本
"""
from pyquery import PyQuery as pq
from news.models import News


def newsList(request, news_name):
    sub_menu = news_name
    if news_name == 'company':
        news_name = '企业要闻'
    elif news_name == 'industry':
        news_name = '行业新闻'
    else:
        news_name = '通知公告'

    # 从数据库中取出数据
    news_list = News.objects.filter(news_type=news_name).order_by('-publish_date')
    # 对每条数据进行<p>的文本抽取
    for news_item in news_list:
        html = pq(news_item.news_description)  # 利用pq解析html内容
        news_item.mytxt = pq(html)('p').text()  # 截取html的文字

    # 分页处理
    p = Paginator(news_list, 4)
    # 获取当前页数
    page = int(request.GET.get('page', 1))
    # 根据当前页码，返回数据
    news_list = p.page(page)

    context = {
        'active_menu': 'news',
        'sub_menu': sub_menu,
        'news_list': news_list,
        'news_name': news_name
    }

    return render(request, 'news/newsList.html', context)


def newsDetail(request, id):
    news_item = News.objects.get(id=id)
    news_item.news_view += 1
    news_item.save()
    context = {
        'active_menu': 'news',
        'news_item': news_item,
    }

    return render(request, 'news/newsDetail.html', context)
