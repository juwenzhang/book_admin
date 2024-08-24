from django.db import models

# Create your models here.
# 开始实现我们的数据库表的创建

# 书表
class Book(models.Model):
    # 书的标题
    book_title = models.CharField(max_length=100)
    # 书的价格
    book_price = models.DecimalField(max_digits=5, decimal_places=2)
    # 书的出版时间
    book_publish_date = models.DateField(auto_now_add=True)

    # 书和出版社的关系，一对多的关系
    book_publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)
    # 书的作者:多对多关系
    book_author = models.ManyToManyField(to="Author")


# 出版社信息
class Publisher(models.Model):
    # 出版社名称
    publisher_name = models.CharField(max_length=100)
    # 出版社地址
    publisher_address = models.CharField(max_length=100)
    # 出版社邮箱
    publisher_email = models.EmailField(max_length=100)


# 作者信息
class Author(models.Model):
    # 作者名称
    author_name = models.CharField(max_length=100)
    # 作者年纪
    author_age = models.IntegerField()

    # 作者和作者详情市一对一的关系
    author_detail = models.OneToOneField(to="Author_detailInfo", on_delete=models.CASCADE)


# 作者详情表
class Author_detailInfo(models.Model):
    # 作者地址
    author_address = models.CharField(max_length=100)
    # 作者联系邮箱
    author_email = models.EmailField(max_length=100)
    # 作者联系电话
    author_phone = models.BigIntegerField()


"""
我们在实现添加数据的时候，首先的是先实现添加出版社的信息，然后再实现添加书的数据信息

然后我们的咋数中的玩意的，跨表用的字段名(关系字段)是会自动添加id的

这个数据库中的我们需要使用的表的关系就是:
1.书表和作者是多对多的关系
2.书表和出版社一对多的关系
3.作者和作者详情之间是一对一关系

如果还想扩展我们还是可以直接实现的是我们的作者和出版社之间 也是可以建立关系的
"""