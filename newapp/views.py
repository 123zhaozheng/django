
from django.shortcuts import render
from django.views.generic import ListView
from .models import PersonInfo

# Create your views here.


class newapp(ListView):
    template_name = 'index2.html'
    extra_context = {'title' : '人员信息表'}

    queryset = PersonInfo.objects.all()
    #设置每页展示一条数据
    paginate_by = 1


