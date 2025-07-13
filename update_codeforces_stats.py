import requests

handle = "MD_Rakibul_hassan"

def fetch_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    return requests.get(url).json()

def fetch_user_rating(handle):
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    return requests.get(url).json()

def fetch_user_status(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}"
    return requests.get(url).json()

user_info = fetch_user_info(handle)
user_ratings = fetch_user_rating(handle)
user_status = fetch_user_status(handle)

if user_info["status"] != "OK" or user_ratings["status"] != "OK" or user_status["status"] != "OK":
    print("Error fetching Codeforces data")
    exit(1)

info = user_info["result"][0]
current_rating = info.get("rating", "Unrated")
max_rating = info.get("maxRating", "Unrated")
contribution = info.get("contribution", 0)
num_contests = len(user_ratings["result"])

accepted_count = 0
wrong_answer_count = 0
for sub in user_status["result"]:
    verdict = sub.get("verdict", "")
    if verdict == "OK":
        accepted_count += 1
    elif verdict == "WRONG_ANSWER":
        wrong_answer_count += 1

md_content = f"""
## 🏅 Codeforces Stats for [{handle}](https://codeforces.com/profile/{handle})

| Current Rating | Max Rating | Contests | Accepted | Wrong Answers | Contribution |
|---------------|------------|----------|----------|---------------|--------------|
| {current_rating} | {max_rating} | {num_contests} | {accepted_count} | {wrong_answer_count} | {contribution} |
"""

with open("CODEFORCES_STATS.md", "w") as f:
    f.write(md_content)
