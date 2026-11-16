from src.api.users import fetchUser


def render_home(user_id):
    user = fetchUser(user_id)
    return f"home for {user['id']}"
