from django.urls import path, re_path, include
from app01 import views

# 开始书写我们的路由匹配的玩意
urlpatterns = [
    # 开始实现我们的图书项目的类容
    # 开始我们的图书显示
    path('book/list/', views.book_list, name='book_list'),

    # 开始实现我们的在页面上面实现添加书籍
    path("book/add/", views.book_add, name='book_add'),

    # 出版社的展示的功能的实现
    path("book/publisher_list/", views.book_publisherList, name='book_publisherList'),

    path("book/publisher_add/", views.publisher_add, name='publisher_add'),

    # 开始添加我们的作者的列表展示
    path("book/author_list/", views.authorList, name='book_authorList'),

    # 作者的添加列表
    path("book/author_add/", views.authorAdd, name='book_authorAdd'),

    # 开始实现我们的编辑页面的实现
    re_path("book/edit/(?P<edit_id>\d+)/", views.book_edit, name='book_edit'),

    # 开始实现我们的书籍的删除功能的路由的设置
    re_path("book/delete(?P<delete_id>\d+)/", views.book_delete, name='book_delete'),

    # 开始实现我们的出版社的页面的实现——删除和添加的功能
    re_path("book/publisher_list/(?P<edit_id>\d+)/", views.book_publisherList_edit,
            name='book_publisherList_edit'),

    re_path("book/publisher_list/(?P<delete_id>\d+)/", views.book_publisherList_delete,
            name='book_publisherList_delete'),

    # 作者的删除和编辑的界面的实现——编辑和删除的功能的实现
    re_path("book/author_list/edit/(?P<edit_id>\d+)/", views.authorEdit, name='author_edit'),
    re_path("book/author_list/delete/(?P<delete_id>\d+)/", views.authorDelete, name='author_delete'),

    re_path('^$', views.home, name='home'),
]