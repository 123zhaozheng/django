from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns=[
    path('',views.index,{'name':'赵正通'}),
    # path('<year>/<int:month>/<slug:day>',views.myvariable,{'riqi':'今天的日期是：'},name='mydate')
    path('<int:year>/<int:month>/<int:day>/', views.myvariable, {'riqi': '今天的日期是：'}, name='mydate'),
    path('test',views.test,name='test'),
    path('turnTo',RedirectView.as_view(url='/'),name='turnTo'),
    path('download',views.download,name='download'),
    path('upload',views.upload,name='upload'),
    path('create',views.create,name='create'),
    path('cookie',views.cookie,name='cookie'),
    path('getHeader',views.getHeader,name='getHeader'),
    path('turnTo2',views.turnTo.as_view(),name='turnTo2'),
    path('nihao',views.nihao.as_view(),name='nihao'),
]