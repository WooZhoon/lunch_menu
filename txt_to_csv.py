import re
import csv

def extract_restaurants_from_txt(txt_file, csv_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 정규식으로 식당 이름과 장르 추출
    restaurant_pattern = re.findall(r'<span class="TYaxT">(.*?)</span>', content)
    genre_pattern = re.findall(r'<span class="KCMnt">(.*?)</span>', content)
    
    # 데이터 정리
    data = list(zip(range(len(restaurant_pattern)), restaurant_pattern, genre_pattern))
    
    # CSV 파일 저장 (한글 깨짐 방지 utf-8-sig)
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(["index", "name", "genre"])  # 헤더 작성
        writer.writerows(data)
    
    print(f"CSV 파일이 생성되었습니다: {csv_file}")

# 실행 예시
extract_restaurants_from_txt('original_txt.txt', 'restaurants.csv')
