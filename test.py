import requests
from requests.auth import HTTPBasicAuth
import time
from pathlib import Path
import os, dotenv


env_path = Path('.') / '.env'
if env_path.exists():
    dotenv.load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# GitHub 저장소 정보 설정
owner = "MinkyoDev"  # 저장소 소유자명
repo = "Programers"  # 저장소명

for i in range(1):
    # GitHub API를 사용하여 커밋 기록 가져오기 2024-03-20T13:00:00+00:00
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?since=2024-03-22T13:00:00+00:00"
    response = requests.get(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    commits = response.json()

    # 커밋 정보 출력
    for commit in commits:
        print("커밋 메시지:", commit['commit']['message'])
        print("작성자:", commit['commit']['author']['name'])
        print("날짜:", commit['commit']['author']['date'])
        print("="*50)
        
    print("횟수:",i)
    print("개수:",len(commits))
    
    
    print("\n비율 제한 상태:")
    print("시간당 최대 요청 수:", response.headers['X-Ratelimit-Limit'])
    print("현재 비율 제한 창에 남아 있는 요청 수:", response.headers['X-Ratelimit-Remaining'])
    print("현재 비율 제한 창에서 요청한 수:", response.headers['X-Ratelimit-Used'])
    reset_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(response.headers['X-Ratelimit-Reset'])))
    print("비율 제한이 리셋되는 시간:", reset_time)