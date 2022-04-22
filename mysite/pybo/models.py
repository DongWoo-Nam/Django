from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 글자수 제한을 둘 때
    content = models.TextField()  # 글자 수 제한을 두지 않을때
    create_date = models.DateField()  # 날짜 시간 관련 속성

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question class와 연결하기 위해 Foreignkey사용
    # on_delete=models.CASCADE -> 답변에 연결된 질문이 삭제되면 답변도 함께 샂데하라는 의미
    content = models.TextField()
    create_date = models.DateField()