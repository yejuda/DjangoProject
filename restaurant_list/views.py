from django.shortcuts import render
# from .models import Restaurant
# from django.db.models import Avg
from .services.google_maps import restaurant_data_reviews


# welcome 뷰
def welcome(request):
    return render(request, 'welcome/welcome.html')

def restaurant_list(request):
    query = request.GET.get("query", "구리역 근처 맛집")
    restaurant_data = restaurant_data_reviews(query)
    return render(request, "restaurant_list/restaurant_list.html", {"restaurants": restaurant_data})



# # 식당 목록 뷰 - 각 식당의 평균 평점도 함께 계산
# def restaurant_list(request):
#     restaurants = Restaurant.objects.annotate(  # annotate: 쿼리셋에 새로운 필드를 추가하는 메서드
#         avg_rating=Avg('reviews__rating')  # reviews: Review 모델과의 관계를 나타냄 (Restaurant 모델의 related_name의 별칭 "reviews") 
#     )                                      # rating: Review 모델의 rating 필드
#     return render(request, 'restaurant_list/restaurant_list.html', {'restaurants':restaurants})