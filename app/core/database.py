user_role_db = {'professor': 'professor', 'student': 'student'}  # Example users

# Role dependency
def get_current_user_role(username: str):
    return user_role_db.get(username, 'student')
