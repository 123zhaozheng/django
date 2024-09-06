from pydoc import resolve

from django.http import FileResponse, Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect


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
    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES.get('file',None)
        print(file)
        with open('D:\logs\course03\demo.2023-12-07.0.log','wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse('上传成功')
    # return render(request,'upload.html')
    pass
