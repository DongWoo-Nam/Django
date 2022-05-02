# Django
파이썬 Django  연습

2022.04.20 시작
점프 투 장고


##### 2022.04.22
 - 모델의 데이터를 조회하는 방법
   - Question.objects.filter(id=1)
     - QuerySet을 반환해주며 1개 이상의 데이터를 반환한다.
     - 조건에 맞지 않은 명령을 하면 비어있는 QuerySet을 반환해준다.
 
   - Question.objects.get(id=1)
     - 1개의 데이터만 조회하고 싶다면 get을 쓰는게 좋다.
     - 조건에 맞지 않은 명령을 입력하면 오류메세지를 반환한다.
 
   - 제목의 일부를 이용하여 데이터 조회하는 방법
     - Question.objects.filter(subject__contain='장고')
     
 - 연결된 데이터 조회 하기(질문 - 답변)
   - 답변에서 질문을 찾을때는 연결된 항목이 있기에 그 항목으로 찾으면 된다. 예) a.question
   - 반대로 질문에서 연결된 답변을 찾을때에는 여러개의 답변이 있을 수 있기에 set를 이용해 찾을 수 있다. 예) q.answer_set.all()/q.연결모델명_set.all()
   
##### 2022.04.25
urls.py에서 맵핑하고, views.py에서 함수를 생성하고, .html파일을 생성하여 화면에 띄울 준비를 하는 순서
 - 질문을 확인할 때 url 별칭으로 맵핑하여 조회할 수 있도록 기능 구현
 - 질문에 답변을 등록 할 수 있는 기능 구현
 - 어떠한 답변이 등록되어있는지 확인 할 수 있는 기능 구현

##### 2022.04.27
css를 이용한 웹 화면 꾸미기 시작
 - settings.py에 static에 관련한 경로 추가하고
 - style.css파일을 만들어서 스타일 추가

문제 해결 필요
 - 질문 목록 에러 나는 문제 해결 필요(아래의 에러 메세지)
 - Reverse for 'detail' with arguments '('',)' not found. 1 pattern(s) tried: ['pybo/(?P<question_id>[0-9]+)/$']

##### 2022.04.29

|부트스트랩|클래스 설명|
|-------|---------|
|card, card-body, card-text|부트스트랩 Card 컴포넌트|
|badge|	부트스트랩 Badge 컴포넌트|
|form-control, form-label|	부트스트랩 Form 컴포넌트|
|border-bottom|	아래방향 테두리 선|
|my-3|	상하 마진값 3|
|py-2|	상하 패딩값 2|
|p-2|	상하좌우 패딩값 2|
|d-flex justify-content-end|	컴포넌트의 우측 정렬|
|bg-light|	연회색 배경|
|text-dark|	검은색 글씨|
|text-start|	좌측 정렬|
|btn btn-primary|	부트스트랩 버튼 컴포넌트|

##### 2022.05.02
 - 표준 html을 상속 받아서 사용할 때 기존의 스크립트를 주석처리하고 실행을 하면 아래와 같은 에러가 뜸
 - 우선은 기존의 앞 뒤 스크립트는 모두 삭제 함
 - Invalid block tag on line 37: 'endblock'. Did you forget to register or load this tag?
 - Invalid block tag on line 44: 'endblock'. Did you forget to register or load this tag?
 - 추후 확인 필요
