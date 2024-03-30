import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import time, re, json

from utils.const import CLIENT_ID, CLIENT_SECRET
from schemas.commit_schema import CommitSchema


def check_repository_exists(username: str, repository: str):
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
    
def fetch_commits(username: str, repository: str, since: str=None) -> list[CommitSchema]:
    base_url = f"https://api.github.com/repos/{username}/{repository}"
    commits = []
    page = 1
    
    while True:
        if since:
            url = base_url + f"/commits?since={since}&page={page}&per_page=100"
        else:
            url = base_url + f"/commits?page={page}&per_page=100"
        response = requests.get(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))

        if response.status_code != 200:
                print(f"Failed to fetch commits: {response.status_code}")
                return None
            
        page_commits = response.json()
        if page_commits:
            commits.extend(page_commits)
            page += 1
        else:
            break
    return postprocessing(commits)

def postprocessing(commits):
    datas = []
    for commit in commits:
        level, title = extract_level_and_title(commit['commit']['message'])
        if is_coding_test_solved(level, title):
            tmp_data = {
                "author": commit['commit']['author']['name'],
                "level": level,
                "title": title,
                "url": commit['html_url'],
                "message": commit['commit']['message'],
                "commit_date": convert_utc_to_seoul(commit['commit']['author']['date'])
            }
            datas.append(CommitSchema(**tmp_data))
    return sorted(datas, key=lambda x: x.commit_date, reverse=True)
    
def convert_utc_to_seoul(utc_str):
    utc_datetime = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")

    seoul_datetime = utc_datetime + timedelta(hours=9)
    seoul_iso_format_str = seoul_datetime.strftime("%Y-%m-%dT%H:%M:%S") + "T"
    
    return seoul_datetime

def extract_level_and_title(text):
    level_pattern = "\[(.*?)\]"
    title_pattern = "Title:\s(.*?),"

    level_match = re.search(level_pattern, text)
    title_match = re.search(title_pattern, text)

    if level_match and title_match:
        level_content = level_match.group(1)
        title = title_match.group(1)
        return level_content, title
    elif level_match and not title_match:
        level_content = level_match.group(1)
        return level_content, None
    elif not level_match and title_match:
        title = title_match.group(1)
        return None, title
    else:
        return None, None
    
def is_coding_test_solved(level, title):
    if level is None and title is None:
        return False
    return True

def state_print(response: requests):
    print("\n비율 제한 상태:")
    print("시간당 최대 요청 수:", response.headers['X-Ratelimit-Limit'])
    print("현재 비율 제한 창에 남아 있는 요청 수:", response.headers['X-Ratelimit-Remaining'])
    print("현재 비율 제한 창에서 요청한 수:", response.headers['X-Ratelimit-Used'])
    reset_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(response.headers['X-Ratelimit-Reset'])))
    print("비율 제한이 리셋되는 시간:", reset_time)


if __name__ == "__main__":
    owner = "MinkyoDev"
    repo = "Programers"
    
    # since = "2024-03-27T13:00:00Z"
    commits = fetch_commits(owner, repo)

    for commit in commits:
        print("======================")
        pretty_printed_json = json.dumps(commit, indent=4, sort_keys=True, ensure_ascii=False)
        # print(pretty_printed_json)
        print("커밋 메시지:", commit['commit']['message'])
        print("작성자:", commit['commit']['author']['name'])
        print("날짜:", commit['commit']['author']['date'])
        print("url:", commit['html_url'])
