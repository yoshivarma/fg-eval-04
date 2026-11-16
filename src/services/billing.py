from src.api.users import fetchUserPreferences


def billing_theme(user_id):
    prefs = fetchUserPreferences(user_id)
    return prefs["theme"]
