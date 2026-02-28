import requests


def fetch_users_with_requests_get(user_ids: list[int]):
    results = []
    for uid in user_ids:
        # Использование обычного метода get
        response = requests.get(f"https://api.example.com/v1/users/{uid}")
        results.append(response.json())
    return results


def fetch_users_with_session(user_ids: list[int]):
    results = []
    # Использование сессии
    with requests.Session() as session:
        for uid in user_ids:
            response = session.get(f"https://api.example.com/v1/users/{uid}")
            results.append(response.json())
    return results

