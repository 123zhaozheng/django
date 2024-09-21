from pydoc import resolve

from django.http import FileResponse, Http404, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import os

from django.views.generic import RedirectView, TemplateView
from sympy import content
from zmq.decorators import context


# Create your views here.
def index(request,name):
    # value = 'This is test!'
    # print(name)
    name = '赵正通'
    age = '18'

    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES.get('file', None)
        print(file.chunks())
        with open('D:\logs\course03\demo.2023-12-07.0.log', 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse('上传成功')

    print(reverse('index:mydate',args=[2019,12,12]))
    # print(type(redirect(reverse('index:mydate',args=[2019,12,12]))))
    # return redirect(reverse('index:mydate',args=[2019,12,12]))
    return render(request, "index.html",locals())
    # print(redirect('/2019/12/12/'))
    # return HttpResponse('This is test!')

def myvariable(request,year,month,day,riqi):
    # args = [2019,12,12]
    # print(reverse('index:mydate',args=args))
    # result = resolve(reverse('index:mydate',args=args))
    # print('kwargs:',result.kwargs)
    # print(year,month,day)
    # # return render(request,'index.html'
    # args = [2019, 12, 12]
    # url = reverse('index:mydate', args=args)
    # print('Generated URL:', url)
    # result = resolve(url)
    # print('Resolved View:', result.view_name)
    # print('kwargs:', result.kwargs)
    # print(year, month, day)
    return HttpResponse(riqi + str(year)+'/'+str(month)+'/'+str(day)+'你好')
def test(request):
    return HttpResponse('This is test!')


def download(request):
    # response = HttpResponse(file)
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="1.txt"'
    # return response
    try:
        file = open('D:\logs\course03\demo.2023-12-07.0.log', 'rb')
        print(type(file))
        r = FileResponse(file,as_attachment=False,filename='nihao.txt')
        return r
    except Exception as e:
        raise Http404('download false')

def upload(request):
    # if request.method == 'POST':
    #     print(request.FILES)
    #     file = request.FILES.get('file',None)
    #     print(file)
    #     with open('D:\logs\course03\demo.2023-12-07.0.log','wb') as f:
    #         for chunk in file.chunks():
    #             f.write(chunk)
    #     return HttpResponse('上传成功')
    # # return render(request,'upload.html')
    # pass
    if request.method == 'POST':
        myFile = request.FILES.get('myFile', None)
        if not myFile:
            return HttpResponse('no files for upload!')
        xiangmu = os.path.dirname(os.path.abspath(__file__))
        print(xiangmu)
        with open(os.path.join(xiangmu, myFile.name), 'wb+') as destination:
            for chunk in myFile.chunks():
                destination.write(chunk)
        return HttpResponse('upload success!')
    return HttpResponse('请用post上传文件')
        # destination = open('D:\\course03\demo.2023-12-07.0.log','wb+')


def create(request):
    r = HttpResponse('创建cookie')
    r.set_signed_cookie('name','zhangsan',salt='zhangsan',max_age=10)
    return r

def cookie(request):
    cookieExist = request.COOKIES.get('name','')
    if cookieExist:
        return HttpResponse('cookie存在')
    else:
        raise Http404('cookie不存在')

def getHeader(request):
    header = request.META.get('HTTP_SIGN','')
    if header:
        return JsonResponse({'header':header})
    else:
        raise Http404('header不存在')

def index1(request):
    return render(request,'index.html')


class turnTo(RedirectView):    # 设置属性
    permanent =False
    url = None
    pattern_name = 'index:turnTo'
    query_string = True

    # 重写get_redirect_url
    def get_redirect_url(self, *args, **kwargs):
        print('This is get_redirect_url')
        return super().get_redirect_url(*args, **kwargs)

    # 重写get
    def get(self, request, *args, **kwargs):
        print(request.META.get('HTTP_USER_AGENT'))
        return super().get(request, *args, **kwargs)

class nihao(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = None
    extra_context = {'title':'Get!!'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['name'] = 'zhangsan'
        context['value'] = 'nihao'
        return context
    def post(self,request,*args,**kwargs):
        self.extra_context = {'title':'nihao'}
        content = self.get_context_data(**kwargs)
        return self.render_to_response(content)


