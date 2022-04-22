from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # ''으로 설정한 이유는 현재 폴더가 pybo/이기 때문에
    # 예를들어 path('question/create/', views.index) 가 추가된다면 pybo/question/create/가 되는 것이다.
]