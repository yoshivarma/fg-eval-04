from src.api.users import fetchUser


def sync_user(user_id):
    user = fetchUser(user_id)
    return {"synced": user["id"]}
