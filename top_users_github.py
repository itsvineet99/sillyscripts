import requests
import time

def get_top_github_users_by_followers(top_n=[10, 70], token=None):
    url = "https://api.github.com/search/users"
    params = {
        "q": "followers:>0",
        "sort": "followers",
        "order": "desc",
        "per_page": top_n
    }
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    data = response.json()
    return data.get("items", [])

def get_user_details(user_url, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    response = requests.get(user_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Optionally add your personal GitHub token here for higher rate limits
    token = None  # e.g., "your_github_personal_access_token"
    
    print("Fetching top 50 GitHub users sorted by followers...")
    users = get_top_github_users_by_followers(50, token)
    
    print("\nTop GitHub users:")
    for i, user in enumerate(users, start=1):
        # Get detailed info (to fetch the follower count)
        details = get_user_details(user['url'], token)
        followers = details.get("followers", "N/A")
        print(f"{i}. {user['login']} - {user['html_url']} - Followers: {followers}")
        # Sleep a little to be kind with rate limits
        time.sleep(0.1)
