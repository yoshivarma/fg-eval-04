from src.api.users import fetchUser


def start_session(user_id):
    return fetchUser(user_id)


def refresh_session(user_id):
    current = fetchUser(user_id)
    return current
