from src.api.users import getUserProfile


def render_dashboard(user_id):
    profile = getUserProfile(user_id)
    return f"dashboard for {profile['id']}"
