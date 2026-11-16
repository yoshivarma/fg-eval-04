from src.api.users import getUserProfile


def weekly_report(user_ids):
    rows = []
    for uid in user_ids:
        profile = getUserProfile(uid)
        rows.append(f"user {profile['id']}: active")
    return "\n".join(rows)


def monthly_report(user_ids):
    rows = []
    for uid in user_ids:
        profile = getUserProfile(uid)
        rows.append(f"user {profile['id']}: billed")
    return "\n".join(rows)
