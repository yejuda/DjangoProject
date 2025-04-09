from django.core.management.base import BaseCommand, CommandParser
import csv
from restaurant_list.models import Restaurant, Review

class Command(BaseCommand):
    help = "CSV 파일에서 리뷰 데이터를 가져옵니다."

    def add_arguments(self, parser):
        parser.add_argument('reviews.csv', type=str, help='C:/Users/iyj05/restaurant_review/reviews.csv')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['reviews.csv']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # 식당이 없으면 생성하기
                restaurant, created = Restaurant.objects.get_or_create(
                    name = row['restaurant_name']
                )

                # 리뷰 생성
                Review.objects.create(
                    restaurant=restaurant,
                    content=row['content'],
                    rating=float(row['rating'])
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f'리뷰가 추가되었습니다: {restaurant.name}'
                    )
                )