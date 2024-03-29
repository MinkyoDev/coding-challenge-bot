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


def check_repository_exists(username, repository):
    """
    주어진 사용자명과 레포지토리명으로 GitHub에서 해당 레포지토리의 존재 여부를 확인한다.

    Parameters:
    username (str): GitHub 사용자명
    repository (str): GitHub 레포지토리명

    Returns:
    bool: 레포지토리의 존재 여부
    """
    url = f"https://api.github.com/repos/{username}/{repository}"
    response = requests.get(url, headers={"User-Agent": "Python"})
    
    if response.status_code == 200:
        return True
    else:
        return False
    
def fetch_all_commits(username, repository):
    commits = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{username}/{repository}/commits?page={page}&per_page=100"
        response = requests.get(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        page_commits = response.json()
        if page_commits:
            commits.extend(page_commits)
            page += 1
        else:
            state_print(response)
            break
    return commits

def fetch_commits_after(username, repository, since):
    commits = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{username}/{repository}/commits?since={since}&page={page}&per_page=100"
        response = requests.get(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        page_commits = response.json()
        if page_commits:
            commits.extend(page_commits)
            page += 1
        else:
            break
    return commits

def state_print(response):
    print("\n비율 제한 상태:")
    print("시간당 최대 요청 수:", response.headers['X-Ratelimit-Limit'])
    print("현재 비율 제한 창에 남아 있는 요청 수:", response.headers['X-Ratelimit-Remaining'])
    print("현재 비율 제한 창에서 요청한 수:", response.headers['X-Ratelimit-Used'])
    reset_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(response.headers['X-Ratelimit-Reset'])))
    print("비율 제한이 리셋되는 시간:", reset_time)


if __name__ == "__main__":
    owner = "MinkyoDev"
    repo = "Programers"
    
    commits = fetch_all_commits(owner, repo)

# since = "2024-02-21T13:00:00Z"

# commits = fetch_commits_after(owner, repo, since)

# for commit in commits:
#     print("커밋 메시지:", commit['commit']['message'])
#     print("작성자:", commit['commit']['author']['name'])
#     print("날짜:", commit['commit']['author']['date'])
#     print("="*50)