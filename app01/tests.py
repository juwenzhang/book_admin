from django.test import TestCase
import os
# Create your tests here.
# 开始实现准备我们的测试环境
if __name__=="__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_admin.settings')
    import django
    django.setup()

    # 下面的就是我们的测试代码