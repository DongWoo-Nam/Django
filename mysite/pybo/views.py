import sqlite3
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForms, AnswerForm  # 질문을 등록하기 위한 장고의 폼

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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    """pybo 질문 등록"""
    if request.method == 'POST':
        form = QuestionForms(request.POST)  # POST방식의 경우 입력 값으로 request.POST로 화면에서 전달받은 값을 이용하여 폼의 값이 채워지도록 함
        if form.is_valid():  # POST요청을 받은 form이 유효한지 확인
            question = form.save(commit=False)  # commit=False는 임시저장을 위미
            # 임시저장을 하는 이유는 폼에는 날짜 필드가 없기 때문에 오류가 발생하기 때문에
            # 임시저장을 하고 question객체를 반환 받아 date 값을 설정한 후 실제 저장한다.
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:  # GET방식의 경우 입력 값 없이 객체 생성
        form = QuestionForms()
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)