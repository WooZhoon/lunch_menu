import csv
import random
import webbrowser

def recommend_random_restaurant(csv_file):
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 스킵
        restaurants = list(reader)
    
    if not restaurants:
        print("식당 데이터가 없습니다.")
        return
    
    random_choice = random.choice(restaurants)
    print(f"오늘의 추천 식당: {random_choice[1]} ({random_choice[2]})")
    webbrowser.open(f"https://map.naver.com/v5/search/{random_choice[1]}")

# 실행 예시
recommend_random_restaurant('restaurants.csv')
