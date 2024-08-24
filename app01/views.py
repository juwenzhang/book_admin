from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from app01 import models

# Create your views here.
# 开始书写我们的基本的页面设计
def home(request):
    return render(request, "home.html")

# 开始我们的图书的视图函数==========================================
# 开始我们的图书的展示的视图函数、
def book_list(request):
    # 开始实现我们的获取图书的所有的数据,然后实现的就是在前端页面中实现基本的渲染
    book_queryset = models.Book.objects.all()
    return render(request, "book_list.html", locals())


# 开始实现我们的添加我们书籍的操作界面
def book_add(request):
    # 开始实现我们的添加书籍的操作

    # 开始实现我们的获取我们的数据库中含有那些作者信息和出版社信息
    publisher_datas = models.Publisher.objects.all()
    author_datas = models.Author.objects.all()

    # 开始实现获取前端的数据
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        book_price = request.POST.get("book_price")
        book_publish_date = request.POST.get("book_publish_date")
        book_publisher_id = request.POST.get("book_publisher")
        book_author_list = request.POST.getlist("book_author")

        # 开始实现操作数据库来实现添加数据
        book_obj = models.Book.objects.create(book_title=book_title,
                                              book_price=book_price,
                                              book_publish_date=book_publish_date,
                                              book_publisher_id=book_publisher_id
        )
        # 开始实现的是操作我们的书籍和作者之间的关系
        book_obj.book_author.add(*book_author_list)

        # 然后实现的是我们的重定向到我们的列表的展示中去
        return redirect("book_list")
    return render(request, "book_add.html", locals())


# 开始书写我们的编辑的视图函数
def book_edit(request, edit_id):
    publisher_datas = models.Publisher.objects.all()
    author_datas = models.Author.objects.all()
    # 实现获取我们的删除的书的id值
    # 通过我们的传递的这个id值来实现获取需要修改的对象
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        book_price = request.POST.get("book_price")
        book_publish_date = request.POST.get("book_publish_date")
        book_publisher_id = request.POST.get("book_publisher")
        book_author_list = request.POST.getlist("book_author")
        publisher_instance = get_object_or_404(models.Publisher, pk=book_publisher_id)
        # 开始实现更新书籍的数据,就是实现的是使用我们的update来实现的我们的更新的
        models.Book.objects.filter(pk=edit_id).update(book_title=book_title,
                                                      book_price=book_price,
                                                      book_publish_date=book_publish_date,
                                                      # book_publisher_id=book_publisher_id,
        )
        edit_obj.book_publisher = publisher_instance
        # 开始实现修改第三张表，由于我们的这里实现的是我们的更新的操作，所以说就是使用的我们的set方法
        edit_obj.book_author.set(book_author_list)
        # 然后实现的就是我们的返回最后的那个页面的呈现的效果
        return redirect("book_list")
    return render(request, "book_edit.html", locals())


# 开始我们的书籍的删除的视图函数
def book_delete(request, delete_id):
    # 开始实现获取我们的数据库中的信息来实现我们的删除数据的界面
    models.Book.objects.filter(pk=delete_id).delete()
    # 需要实现基本的一些那个删除的提示框的还是可以使用的哈，这个也是一个思路
    # 直接实现我们的重定向到书籍列表的位置来实现展示
    return redirect("book_list")


# 开始我们的出版社的视图函数==============================================
# 开始实现我们的出版社列表展示
def book_publisherList(request):
    # 开始实现获取我们的所有的出版社的数据
    publisher_datas = models.Publisher.objects.all()
    return render(request, "book_publisherList.html", locals())

# 出版社添加的视图函数
def publisher_add(request):
    # 开始实现我们的获取数据
    if request.method == "POST":
        # 先实现我们的获取数据
        publisher_name = request.POST.get("publisher_name")
        publisher_address = request.POST.get("publisher_address")
        publisher_email = request.POST.get("publisher_email")

        # 然后实现我们的向数据库中添加数据
        publisher_obj = models.Publisher.objects.create(
            publisher_name=publisher_name,
            publisher_address=publisher_address,
            publisher_email=publisher_email
        )
        # 然后实现的就是重定向最开始的页面
        return redirect("book_publisherList")
    return render(request, "book_publisherAdd.html", locals())

# 出版社编辑函数
def book_publisherList_edit(request, edit_id):
    # 开始实现我们的获取需要实现修改的出版社信息
    publisher_data = models.Publisher.objects.filter(pk=edit_id).first()
    if request.method == "POST":
        # 开始实现我们的获取数据
        publisher_name = request.POST.get("publisher_name")
        publisher_address = request.POST.get("publisher_address")
        publisher_email = request.POST.get("publisher_email")
        publisher_instance = get_object_or_404(models.Publisher, pk=edit_id)

        # 开始我们的更新数据
        models.Publisher.objects.filter(pk=edit_id).update(
            publisher_name=publisher_name,
            publisher_address=publisher_address,
            publisher_email=publisher_email
        )
        models.Publisher.objects.filter(pk=edit_id).first().id = publisher_instance

        return redirect("book_publisherList")
    return render(request, "book_publisherList_edit.html", locals())

# 出版社删除函数
def book_publisherList_delete(request, delete_id):
    models.Publisher.objects.filter(pk=delete_id).delete()
    return redirect("book_publisherList_delete")


# 开始我们的作者的视图函数
def authorList(request):
    # 开始获取我们的视图数据
    authorDatas = models.Author.objects.all()
    return render(request, 'book_authorList.html', locals())

# 开始我们的作者的编辑视图
def authorEdit(request, edit_id):
    return render(request, "author_edit.html", locals())

def authorDelete(request, delete_id):
    # 直接实现我们的删除
    models.Author.objects.filter(pk=delete_id).delete()
    return redirect("author_list")

def authorAdd(request):
    # 开始实现我们的的获取数据
    if request.method == "POST":
        # 开始实现我们的获取前端传入的数据
        author_name = request.POST.get("author_name")
        author_age = request.POST.get("author_age")
        author_address = request.POST.get("author_address")
        author_email = request.POST.get("author_email")
        author_phone = int(request.POST.get("author_phone"))
        # 我们必须先实现的是先操作我们的作者详情，然后才可以实现我们的添加作者的数据
        # 开始实现我们的额添加作者的详情的信息
        author_detail_obj = models.Author_detailInfo.objects.create(
            author_phone=author_phone,
            author_address=author_address,
            author_email=author_email
        )
        # 开始我们的创建我们的作者的信息，并且加入我们的数据库
        models.Author.objects.create(
            author_name=author_name,
            author_age=author_age,
            # 通过我们的作者详情来实现我们的添加一对一的作者详情信息
            author_detail=author_detail_obj,
        )
        return redirect("book_authorList")
    return render(request, 'authorAdd.html', locals())

