import sqlite3

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')  # 질문 목록 생성하기
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)  # 'pybo/question_list.html' 이것을 템플릿이라 부른다.
    # render는 context에 있는 데이터를 html코드로 변환해준다.
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")