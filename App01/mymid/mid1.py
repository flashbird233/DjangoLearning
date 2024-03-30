"""
自定义中间件
"""
from django.utils.deprecation import MiddlewareMixin


class Mid1(MiddlewareMixin):

    def process_request(self, request):
        print("Mid1 process_request")
        return None

    def process_response(self, request, response):
        print("Mid1 process_response")
        return response
