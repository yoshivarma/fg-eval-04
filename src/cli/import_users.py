from src.api.users import fetchUser, fetchUserPreferences


def import_one(user_id):
    record = fetchUser(user_id)
    prefs = fetchUserPreferences(user_id)
    return record, prefs
