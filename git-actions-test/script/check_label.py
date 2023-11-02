import requests
import os

# GitHub Personal Access Token
token = os.environ.get('GH_TOKEN')

# PR 번호
pr_number = os.environ.get('PR_NUMBER')

# GitHub API 엔드포인트
url = f"https://api.github.com/repos/{os.environ.get('GITHUB_REPOSITORY')}/issues/{pr_number}/labels"

# GitHub API 호출
response = requests.get(url, headers={'Authorization': f'token {token}'})

if response.status_code == 200:
    labels = response.json()
    if labels:
        print("At least one label is attached to this Pull Request.")
    else:
        print("No labels are attached to this Pull Request.")
        exit(1)
else:
    print("Failed to fetch labels from the GitHub API.")
    exit(1)
