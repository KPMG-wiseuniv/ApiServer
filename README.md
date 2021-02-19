# API Server for Fitting Room

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
