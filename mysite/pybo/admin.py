from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# admin.site.register(Question)  # admin 페이지에 모델 관리 할 수 있도록 추가
admin.site.register(Question, QuestionAdmin)  # admin 페이지에 데이터 검색 기능 추가