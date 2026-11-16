"""User API helpers."""


def fetchUser(user_id):
    """DEPRECATED: use getUserProfile. Kept for backwards compatibility."""
    return {"id": user_id}


def getUserProfile(user_id):
    return {"id": user_id, "profile": {}}


def fetchUserPreferences(user_id):
    """Not deprecated. Returns display preferences."""
    return {"id": user_id, "theme": "light"}
