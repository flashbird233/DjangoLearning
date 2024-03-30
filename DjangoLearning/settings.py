"""
Django settings for DjangoLearning project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# 用于配置整个网站的环境和功能，核心配置必须有项目路径，密钥配置，域名访问权限，app列表，中间件，资源文件，模板配置，数据库的连接方式

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目路径
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥配置
# 主要用于重要的数据加密处理，提高项目的安全性，避免遭到攻击者的恶意破坏，密钥主要用于用户密码， CSRF机制，会话Session等数据加密
SECRET_KEY = 'django-insecure-k$4x^a16o@#bh@qv6u47grqutp$r(x!m44#2#^6yn+%wbhm+e@'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发时使用True，正式发布时使用False
DEBUG = False

# 允许访问的域名，在Debug为True时，不能为空，需填入域名
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # 管理后台
    'django.contrib.auth',  # 认证系统
    'django.contrib.contenttypes',  # 内容类型，所有的Model元数据
    'django.contrib.sessions',  # 会话功能，用于标识当前访问网站的用户身份，记录相关用户信息
    'django.contrib.messages',  # 消息提示功能
    'django.contrib.staticfiles',  # 查找静态资源路径
    "App01.apps.App01Config"
]

# 中间件, 是一个用来处理请求和响应的框架，是一个轻量级的、底层的系统级别的插件系统，用于全局范围内改变Django的输入或输出
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # 安全中间件，用于处理请求和响应的安全问题
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话中间件，用于处理会话相关的功能
    'django.middleware.common.CommonMiddleware',  # 通用中间件，用于处理请求和响应的通用问题，规范化请求内容
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF中间件，用于处理CSRF相关的功能，开启CSRF功能
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 认证中间件，用于处理认证相关的功能，开启用户认证功能
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件，用于处理消息相关的功能，开启消息提示功能
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # XFrameOptions中间件，防止恶意程序单击劫持
    # 自定义中间件（主要的是process_request和process_response方法），在自己定义中间件时，必须继承MiddlewareMixin
    # process_request(self, request)：在请求到达视图(views)之前调用
    # process_view(self, request, callback, callback_args, callback_kwargs)：在请求到达视图之前调用，但是会在process_request之后调用
    # process_template_response(self, request, response)：在视图函数返回响应之后，模板渲染之前调用
    # 该方法对视图函数返回值有要求，必须是一个含有render方法的对象，才会执行此方法
    # process_response(self, request, response)：在视图函数返回响应之后调用，请求执行完成，返回页面前会执行
    'App01.mymid.mid1.Mid1',
]

# 指定了当前项目的根URL配置文件，是路由系统的入口
ROOT_URLCONF = 'DjangoLearning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 模板引擎
        'DIRS': [BASE_DIR / 'templates',
                 BASE_DIR / 'App01/templates']
        ,  # 模板文件路径
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

# 项目部署时，Django的内置服务器使用的WSGI应用程序对象的完整Python路径
WSGI_APPLICATION = 'DjangoLearning.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# local database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ryegrassdb',
#         'USER': 'root',
#         'PASSWORD': 'qwe123zxc',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# server database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ryegrassdb',
        'USER': 'jnhhpcgdav',
        'PASSWORD': 'TP30ryegrass',
        'HOST': 'ryegrass-server.mysql.database.azure.com',
        'PORT': '3306',
        # 'OPTIONS': {
        #     'ssl': {
        #         'ca': BASE_DIR / 'DigiCertGlobalRootCA.crt.pem'
        #     }
        # }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# 设置一个支持拔插的密码验证器，且可以一次性配置多个，Django会通过这些内置组件来避免用户设置的密码等级不足的问题
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# 设置静态资源文件集合
STATICFILES_DIRS = [
    BASE_DIR / "App01/static"
]

# 设置静态资源文件路径，项目发布时，需要将静态资源文件收集到STATIC_ROOT路径下(collectstatic)
STATIC_ROOT = BASE_DIR / "static"

# 设置媒体路由
MEDIA_URL = 'media/'
# 设置媒体目录的完整路径
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
