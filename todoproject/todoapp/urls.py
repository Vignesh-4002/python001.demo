from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('detail',views.,name='detail'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Detaildetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Updateupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Deletedeleteview.as_view(),name='cbvdelete')
]
