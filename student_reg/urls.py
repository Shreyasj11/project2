from django.contrib import admin
from django.urls import path , re_path
from student_reg import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    re_path(r'^$',views.home,name='home'),
    re_path(r'^reg',views.reg,name='reg'),
    re_path(r'^report',views.report,name='report')

]