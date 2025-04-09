from django.db import models

# 기존 모델
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    time = models.CharField(max_length=30)

# # 리뷰 모델
# class Review(models.Model):
#     restaurant = models.ForeignKey(
#         Restaurant, 
#         on_delete=models.CASCADE,  # 식당이 지워질 때, 리뷰도 같이 지워짐
#         related_name='reviews'     # 다른 코드에서 사용될 이름이 "reviews"인 것이다.
#         )
#     content = models.TextField()  # 리뷰 내용
#     rating = models.FloatField()  # 평점
#     created_at = models.DateTimeField(auto_now_add=True)  # 리뷰 작성 시간

#     def __str__(self):
#         return f"{self.restaurant.name}의 리뷰"