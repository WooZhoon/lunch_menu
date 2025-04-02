# lunch_menu
SKN13 하면서 점심 뭐먹을지 고민하다가 만듬

### *사용법
random_recommend.py 실행


### *설명
original_txt.txt 파일은 html에서 그냥 긁어온 코드입니다.
여기서 txt_to_csv.py를 이용해 식당 이름과 장르를 추출하여 csv파일에 저장합니다.

그렇게 생성된 csv 파일이 restaurants.csv 파일이고, index, name, genre로 구성되어 있습니다.
rendom_recommend.py를 실행하면 csv 파일에서 하나를 골라 추천 및 인터넷 링크로 자동 연결합니다.
