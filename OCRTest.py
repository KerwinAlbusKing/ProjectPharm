import pytesseract
import numpy as np
from PIL import Image
from MoveFile import move_file
import SQLiteCRUD

import re

def extract_13_digit_numbers(text):
    # 정규 표현식으로 13자리 숫자 추출
    pattern = r'\b\d{13}\b'  # 13자리 숫자
    matches = re.findall(pattern, text)
    return matches

#SQLiteCRUD.create_table()
#SQLiteCRUD.add_medicine(8809416470306, '올리브영촉촉', 10, 17500, 'A-30', '2025-01-31')

# Tesseract 실행 파일 경로 지정 (Windows 사용자의 경우)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Tesseract 설정 옵션, 베스트
config=('-l kor+eng --oem 3 --psm 1')
# -l kor+eng : 언어 설정, 한국어와 영어를 동시에 처리하도록 설정.
# --oem : OCR 엔진의 작동 모드를 설정
    # 0 : Legacy Tesseract-Only 엔진 사용.
    # 1 : LSTM 기반의 Neural Network 엔진 사용.
    # 2 : Legacy + LSTM 혼합 엔진 사용.
    # 3 : 기본 설정, LSTM 기반 Neural Network 엔진 사용 (최신 기술).
# --psm : 페이지 레이아웃 분석 모드를 설정
    # 0 : 기본값 (Automatic) – 페이지 전체 분석.
    # 1 : 한 줄의 단일 텍스트로 처리.
    # 3 : 하나의 단어로 처리.
    # 6 : 한 블록(단락)으로 구성된 텍스트를 처리하는 모드.
    # 7 : 한 줄의 단일 텍스트(이미지를 그대로 처리).

# OCR 처리할 이미지 파일 경로
image_path = 'C:/Users/KerwinKing/Documents/GitHub/ProjectPham/Images/Temp/OCRTestImage.jpg'
img = np.array(Image.open(image_path))

# OCR 실행 (문자열로 결과 반환)
raw_text = pytesseract.image_to_string(img, config=config)

# 공백 기준으로 배열 저장
#text = raw_text.split()

goodsList = extract_13_digit_numbers(raw_text)

# 텍스트 출력
print(raw_text)
print(goodsList)
for i in goodsList:
    SQLiteCRUD.view_medicine_by_code_or_name(i)

#move_file('C:/Users/KerwinKing/Documents/GitHub/ProjectPham/Images/Temp/OCRTestImage.jpg', 'C:/Users/KerwinKing/Documents/GitHub/ProjectPham/Images/Old')