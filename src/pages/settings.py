from src.api.users import fetchUserPreferences


def render_settings(user_id):
    return fetchUserPreferences(user_id)
