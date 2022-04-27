from django.urls import path
from . import views

app_name = 'pybo'  # 네임스페이스 이름 지정 / 서로 다른 앱에서 같은 별칭을 사용할 경우 식별하기 위하여 네임스페이스를 사용한다.

urlpatterns = [
    path('', views.index, name='index'),  # ''으로 설정한 이유는 현재 폴더가 pybo/이기 때문에
    # 예를들어 path('question/create/', views.index) 가 추가된다면 pybo/question/create/가 되는 것이다.
    path('<int:question_id>/', views.detail, name='detail'),  # 질문 살세 보기 기능 구현
    # name='index', name ='detail' 은 URL별칭으로 하드코딩을 피하기 위한 추가 사항
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),  # 답변 등록을 위한 url맵핑
]