import os
import pytesseract
from PIL import Image
from django.shortcuts import render
from django.conf import settings

def ocr_view(request):
    result_text = ""
    digit_numbers = []

    # Media/temp 폴더의 이미지 경로
    temp_folder = os.path.join(settings.MEDIA_ROOT, 'temp')
    image_files = [f for f in os.listdir(temp_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if image_files:
        image_path = os.path.join(temp_folder, image_files[0])  # 첫 번째 이미지 처리
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        config = '-l kor+eng --oem 3 --psm 6'
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

        try:
            img = Image.open(image_path)
            raw_text = pytesseract.image_to_string(img, config=config)

            # 13자리 숫자 추출
            digit_numbers = extract_13_digit_numbers(raw_text)

            result_text = f"OCR Result:\n{raw_text}\n\nExtracted 13-digit numbers:\n{digit_numbers}"
        except Exception as e:
            result_text = f"Error processing image: {str(e)}"
    else:
        result_text = "No images found in Media/temp folder."

    return render(request, 'tesseractOCR/ocr_result.html', {'result_text': result_text, 'digit_numbers': digit_numbers})

def extract_13_digit_numbers(text):
    import re
    pattern = r'\b\d{13}\b'
    return re.findall(pattern, text)