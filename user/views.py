from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from flask import jsonify
import hashlib
from .models import UserModel
from django.http import JsonResponse


def sign_up(request):
    if request.method == 'POST':
        # email = request.POST.get('email', None)
        # password = request.POST.get('password', None)
        data = json.loads(request.body)
        # data = json.loads(request.data)
        email = data["email"]
        password = data["password"]
        password_hash = hashlib.sha256(
            password.encode('utf-8')).hexdigest()
        
        if '@' not in email:
            return JsonResponse({'response': '이메일 형식 에러'})
        elif len(password) < 9:
            return JsonResponse({'response': '비밀번호 길이 에러'})
        
        user = UserModel()
        user.email = email
        user.password = password_hash
        user.save()

        return JsonResponse({'response': '회원가입 완료'})
