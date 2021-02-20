# API Server for Fitting Room

## Fitting Room by 슬기로운 대학생활
안녕하십니까, 
저희는 COVID-19 이후 ‘인테리어 모바일 커머스 시장’이 급속도로 성장하고 있는 가운데, AI 기술을 활용한 인테리어 상품 추천 플랫폼 ‘Fitting Room’을 선보이고자 하는 ‘슬기로운 대학생활’ 팀입니다. 

## Summary
COVID-19가 전 세계적인 영향을 미치며, 자유로운 외부 활동이 거의 불가능해지는 현상이 지구 전체에 발생하였습니다. 이로 인해 집 안에서 활동해야 하는 시간이 늘어나면서 외부 활동과 관련된 소비액이 자연스레 ‘집안 활동’과 관련된 항목으로 옮겨가는 현상이 발생하였습니다. 

국내외 가구 브랜드에서는 AR, VR 등 다양한 기술을 접목한 홈 스타일링 서비스를 선보이고 있지만, 여전히 공간 전반을 아우르는 홈 스타일링 서비스를 제공받기 위해서는 매장을 방문해야 한다는 치명적인 단점이 존재하는 상황입니다.

이에 저희 팀은 모바일 홈 스타일링 솔루션 ‘Fitting Room’을 제공하고자 합니다. 

서비스에 관한 자세한 내용은 "APP Repositories"의 Readme에 정리하였으며, 다음의 URL을 통해 확인해주시면 감사하겠습니다.

## About Service (URL)
https://github.com/KPMG-wiseuniv/App/blob/main/README.md


## 1. Server 환경
1) Framework-Django
2) Language-Python
3) Connecting AI model-Pytorch
4) API-RESTful API using djangoframework
5) Data-SQLLite3

## 2. Server 환경 구축
1) 가상환경 설치: python -m venv myvenv
2) 가상환경 활성화(Windows): source myvenv/Scripts/activate
3) 가상환경 활성화(Linux): conda activate myvenv
4) django 설치: pip install django
5) django project 생성: django-admin startproject project이름
6) djangorestframework 설치: pip install djangorestframework
7) 최종 migrate: python manage.py migrate
8) 서버 실행: python manage.py runserver

## 3. API Explanation
1)가구 데이터 가져오기 API(GET)
+ 최종 결과로 보여줄 가구 상품 데이터를 어플리케이션으로 가져오기 위한 API<br>
+ URLPattern: /send_imgdata/<br>
+ Android RetrofitAPI<br>
  + @GET("send_imgdata/")<br>
    Call<ArrayList<Imgdata>> get_imgdata();<br>
+ Response Format
  + imgname: CharField(String)
  + bigcategory: CharField(String)
  + middlecategory: CharField(String)
  + furniturename: CharField(String)
  + style: CharField(String)
  + selectfd: CharField(String)
  + price: IntegerField(int)
  + color: IntegerField(int)
  + detail: IntegerField(int)
  + image: IntegerField(int)<br><br>
    

2)사진 전송 API(POST)
+ 사용자가 업로드한 방 사진을 서버에서 받기 위한 API<br>
+ URLPattern: /train_img/<br>
+ Android RetrofitAPI<br>
  + @Multipart<br>
    @POST("train_img/")<br>
    Call<Void> send_img(@Part MultipartBody.Part image,<br>
                        @Part("imgname") String imgname,<br>
                        @Part("Furniture") String Furniture,<br>
                        @Part("FD") String FD);<br>
+ Request Format
  + image: FileField(Image)<br><br>
  

3)인공지능 학습 결과 가져오기 API(GET)
+ 업로드한 방 사진을 인공지능 학습을 통해 얻은 결과값을 어플리케이션으로 가져오기 위한 API<br>
+ URLPattern: /send_train_result/<br>
+ Android RetrofitAPI<br>
  + @GET("send_train_result/")<br>
    Call<result> get_result();<br>
+ Response Format
  + interior: IntegerField(int)
  + color: IntegerField(int)
  + FD: IntegerField(int)<br><br>

## 4. AI Model Load & Inference
1) pip install torch
2) pip install torchvision
3) pip install numpy
4) pip install pillow
5) model.load_state_dict(model이름.pth)
