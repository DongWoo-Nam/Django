from django import forms
from pybo.models import Question, Answer

class QuestionForms(forms.ModelForm):  # 모델 폼을 상속 받은 것이다.
    class Meta:  # 장고 모델 폼은 내부 클래스로 반드시 Meta 클래스를 가져야 한다.
        model = Question
        fields = ['subject', 'content']
        # 수작업으로 폼 작성을 위한 widget항목 제거
        # widgets = {  # Meta를 사용하여 부트스트랩을 적용하지 못했을 때 Meta클래스 내부의 widgets를 사용
        #     'subject' : forms.TextInput(attrs={'class':'form-control'}),
        #     'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }
        labels = {  # 한글로 변경하고 싶을때는 Meta의 labels를 사용
            'subject' : '제목',
            'content' : '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }