from dotenv import load_dotenv
import os

# 현재 파일 기준으로 절대경로 계산
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../env/.env"))
load_dotenv(base_dir)

# 환경 변수 사용
print(os.getenv("MY_VARIABLE"))  # .env에 정의된 환경 변수 값 출력