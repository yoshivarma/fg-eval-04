from src.api.users import fetchUser, fetchUserPreferences


def render_profile(user_id):
    user = fetchUser(user_id)
    prefs = fetchUserPreferences(user_id)
    return user, prefs
