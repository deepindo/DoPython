"""
Django settings for DoSites project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path
import time

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#^sp!k4c7g^xy-%or23j#=q++4p)ucfgz=p43!c1g=s&agzg6q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # simpleui样式的后台页面
    'simpleui',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 门户网站的app模块
    'home',      # 首页
    'about',     # 简介
    'contact',   # 欢迎咨询
    'news',      # 新闻动态
    'products',  # 产品中心
    'service',   # 服务支持
    'science',   # 科研基地

    # CRM系统的app模块
    'institution',   # 机构管理
    'customer',      # 客户管理
    'speaker',       # 讲者管理
    'jurisdiction',  # 辖区管理
    'supplier',      # 供应商管理
    'meeting',       # 会议管理
    'approve',       # 审批中心
    'system',        # 系统管理
    'forms',         # 报表中心

    # 其他插件
    'DjangoUeditor',  # 富文本编辑器
    'widget_tweaks',  # 添加模型表单定制化渲染
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DoSites.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 对于用了templates的，这个一定要设置，不然会报错TemplateDoesNotExist
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DoSites.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dy_sites_dev',
        'HOST': 'localhost',
        'POST': '3306',
        'USER': 'root',
        'PASSWORD': 'Imaioscoder123.'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 如果克隆报错提示找不到静态目录，请先在settings.py指定静态目录， clone成功后，注释掉，因为以上面STATICFILES_DIRS冲突，导致css不起效，影响显示

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 对图片的路径进行存储
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_DEFAULT_THEME = 'Green.css'
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_HOME_ACTION = True
SIMPLEUI_ANALYSIS = False
SIMPLEUI_LOGIN_PARTICLES = True
SIMPLEUI_ICON = {
    '公司简介': 'fas fa-building',
    '荣誉资质': 'fas fa-trophy',
    '新闻动态': 'fas fa-newspaper',
    '人才招聘': 'fas fa-place-of-worship',
    '招聘信息': 'fab fa-ubuntu',
    '简历信息': 'fas fa-file',
    '联系我们': 'fas fa-network-wired',
    '产品中心': 'fab fa-product-hunt',
    '产品列表': 'fas fa-list-ol',
    '服务支持': 'fab fa-servicestack',
    '文件资料': 'far fa-folder-open',
}
SIMPLEUI_CONFIG = {
    'system_keep': True,
    # 'menu_display': ['Simpleui', '测试', '权限认证', '动态菜单测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'name': 'TDesign',
        'icon': 'fas fa-code',
        'url': 'https://tdesign.tencent.com/vue/components/getting-started'
    }, {
        'name': 'Simpleui',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui'
    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
        # 自2021.02.01+ 支持多级菜单，models 为子菜单名
        'name': '多级菜单测试',
        'icon': 'fa fa-file',
        # 二级菜单
        'models': [{
            'name': 'Baidu',
            'icon': 'far fa-surprise',
            # 第三级菜单 ，
            'models': [
                {
                    'name': '爱奇艺',
                    'url': 'https://www.iqiyi.com/dianshiju/'
                    # 第四级就不支持了，element只支持了3级
                }, {
                    'name': '百度问答',
                    'icon': 'far fa-surprise',
                    'url': 'https://zhidao.baidu.com/'
                }
            ]
        }, {
            'name': '内网穿透',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-github'
        }]
    }, {
        'name': '动态菜单测试',
        'icon': 'fa fa-desktop',
        'models': [{
            'name': time.time(),
            'url': 'http://baidu.com',
            'icon': 'far fa-surprise'
        }]
    }]
}