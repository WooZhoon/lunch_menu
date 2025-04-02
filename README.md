# lunch_menu
SKN13 하면서 점심 뭐먹을지 고민하다가 만듬

### 사용법
random_recommend.py 실행


### 설명
original_txt.txt 파일은 html에서 그냥 긁어온 코드입니다.
여기서 txt_to_csv.py를 이용해 식당 이름과 장르를 추출하여 csv파일에 저장합니다.

그렇게 생성된 csv 파일이 restaurants.csv 파일이고, index, name, genre로 구성되어 있습니다.
rendom_recommend.py를 실행하면 csv 파일에서 하나를 골라 추천 및 인터넷 링크로 자동 연결합니다.

### 수정내용
> restaurants.csv에서 genre가 "술집,호프", "카페"인 항목을 제거했습니다.
restaurants.csv에서 genre가 "고기,육류"인 항목을 제거했습니다.
restaurants.csv에서 한라산도새기 가산점을 추가했습니다.(사유 : 점심메뉴 있음)
restaurants.csv에서 독산역을 건너야 하는 식당을 제거했습니다.

기타 수정 및 추가할 내용 있으면 언제든지 연락주세요
