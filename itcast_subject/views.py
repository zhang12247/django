from django.shortcuts import render
from itcast_subject.models import nami_user
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.template import loader
from itcast_subject import models
import json
from itcast_subject import toolsfun
import uuid


# Create your views here.
def index(request):
    if (request.method == 'POST'):
        # 判断是否是提交登录表单
        if (request.POST["submit"] == "登录"):
            #登录处理方法
            user_name = request.POST["Username"]
            password = request.POST["Password"]
            try:
                print(models.nami_user.objects.filter(username=user_name))
                # print(usermodel['ase_password'])
                return JsonResponse({'username': '用户名已注册'})
            except ObjectDoesNotExist:
                return HttpResponse({'username': '可以正常注册'})
            print('user_name:' + user_name + ',password:' + password)
        if (request.POST["submit"] == "重置密码"):
            #重置密码处理方法
            return 0
        if (request.POST["submit"] == "注册"):
            #注册处理方法
            return 0
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # user_name = request.POST['user_name']
            # e_mail = request.POST['e_mail']
            # # print(request.POST['password'])
            # # print(models.nami_user.get(uid='1ad7300c-6933-11e6-ab4e-005056c0'))
            # password = toolsfun.DESUtil().encrypt(request.POST['password'])
            # add_model = models.nami_user(uid=uuid.uuid1(), username=user_name, firstname=first_name, lastname=last_name,
            #                              email=e_mail, login=0,
            #                              ase_password=password,
            #                              admin=0)
            # add_model.save()
    return render(request, 'index.html')

    # subject_list = Subject.objects.all()
    # content = {'subject': subject_list}
    # return render(request,'index.html',content)
    # user_name = request.GET['user_name']
    # password = request.GET['password']
    # print("username=:" + user_name + "password=:" + password)
    # return HttpResponse("username=:" + user_name + "password=:" + password)


def check_name(request):
    username = request.POST['user_name']
    try:
        models.nami_user.objects.get(username=username)
        return JsonResponse({'username': '用户名已注册'})
    except ObjectDoesNotExist:
        return HttpResponse({'username': '可以正常注册'})

#
# def work_index(request):
#     # username = request.GET('user_name')
#     # password = request.GET('password')
#     # print("username=:" + username + "password=:" + password)
#     # return render(request,'work_index.html')
#     return render(request, 'Test_index/work_index.html')
#
#
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'Test_index/change_password.html', {'form': form})
#
#
# def about_pages(request, page):
#     path = "Test_index/%s.html" % page
#     template = loader.get_template(path)
#     return HttpResponse(template.render(None, request))
