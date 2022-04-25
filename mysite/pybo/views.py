import sqlite3

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone

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

def detail(request, question_id):
    """
    질문 상세보기 기능 구현
    pybo 내용 출력
    :param request:
    :param question_id:
    :return:
    """
    # question = Question.objects.get(id=question_id)  # 기본
    question = get_object_or_404(Question, pk=question_id)  # 오류 발생 시 상세 Debug내용이 아닌 404페이지가 뜰 수 있도록 수정
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록 기능 구현
    :param request:
    :param question_id:
    :return:
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    return redirect('pybo:detail', question_id=question.id)