import os
import shutil

def move_file(source_path, destination_folder):
    try:
        # 파일 이름 추출
        file_name = os.path.basename(source_path)

        # 이동할 경로 생성
        destination_path = os.path.join(destination_folder, file_name)

        # 파일 이동
        shutil.move(source_path, destination_path)
        print(f"File moved to: {destination_path}")
    except FileNotFoundError:
        print("Source file or destination folder does not exist.")
    except PermissionError:
        print("Permission denied. Check your access rights.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 테스트
if __name__ == "__main__":
    source_file = "source_folder/example.txt"  # 이동할 파일 경로
    destination_dir = "destination_folder"    # 이동할 대상 폴더

    move_file(source_file, destination_dir)