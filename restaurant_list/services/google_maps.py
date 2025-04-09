import os
import requests

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY 환경 변수가 설정되지 않았습니다.")

def restaurant_data_reviews(query):
    """
    식당 정보와 리뷰를 가져오는 함수
    Args:
        query(str): 검색어 (예: 구리역 근처 맛집)
    Returns:
        dict: 식당 이름, 유형(음식점/카페 등 카테고리), 주소, 전화번호, 현재 영업 여부, 주간 운영 시간, 세부 시간대, 평점, 리뷰 수, 최근 리뷰 5개
    """

    # 장소 검색
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_params = {
        "query": query,
        "key": GOOGLE_API_KEY,
        "language": "ko",
    }
    search_response = requests.get(search_url, params=search_params).json()

    if not search_response.get("results"):
        return {"error": "식당을 찾을 수 없습니다."}
    

    # 여러 식당의 정보를 담을 리스트
    restaurants = []

    # 각 식당에 대한 상세 정보 요청
    for place in search_response["results"][:3]:   # 식당 3곳만

        place_id = place["place_id"]

        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
                "place_id": place_id,
                "fields": "name,types,formatted_address,formatted_phone_number,opening_hours,rating,user_ratings_total,reviews",
                "key": GOOGLE_API_KEY,                                                                                                                                                                                                         
                "language": "ko"  # 한국어로 반환
            }
        details_response = requests.get(details_url, params=details_params).json()

        if details_response.get("result"):
            result = details_response["result"]
            opening_hours = result.get("opening_hours", {})
            restaurant_data = {
                "name": result.get("name"),
                "types": result.get("types", []),
                "address": result.get("formatted_address"),
                "phone_number": result.get("formatted_phone_number"),
                "open_now": opening_hours.get("open_now", False),
                "weekday_text": opening_hours.get("weekday_text", []),
                "current_opening_hours": opening_hours,  # 세부 시간대 전체
                "rating": result.get("rating"),
                "review_count": result.get("user_ratings_total"),
                "reviews": result.get("reviews", [])[:5]  # 최근 리뷰 5개
            }
            restaurants.append(restaurant_data)

    return restaurants if restaurants else [{"error": "상세 정보를 가져올 수 없습니다."}]
    
# 테스트
if __name__ == '__main__':
    data = restaurant_data_reviews("구리역 근처 맛집")
    for restaurant in data:
        print(restaurant)
    