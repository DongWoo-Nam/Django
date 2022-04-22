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
   - 