# spartamarket_DRF
# 프로젝트 소개
마켓 백엔드 기능을 구현(by. DRF)
# 개발기간
# 개발환경
Python : Django DRF
DB : SQlite
# ERD
![image](https://github.com/user-attachments/assets/a911c441-c2ae-493c-9eb7-08ff54a3fd0c)
![image](https://github.com/user-attachments/assets/dd391e1e-80a2-478a-b12a-20f98ccb3a20)
![image](https://github.com/user-attachments/assets/d08f75f1-3dbe-44b5-a63b-c624c7b9c8bd)


# 설치 및 실행방법
- pip install -r requirements.txt
- .env 확인
- python manage.py migrate
- python manage.py runserver
# RESTful API 명세서
# Permission 이슈
- class내에 permission_classes를 설정할때, GET과 POST 함수를 분리해서 permission을 주지 못하는 이슈
- https://zhelddustmq.tistory.com/129
# 기능 상세

