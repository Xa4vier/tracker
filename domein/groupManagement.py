from database.insert import insert_group, insert_usergroup, insert_admin

def create_group(userId, name):
    groupId = insert_group(name)
    insert_usergroup(userId, groupId)
    insert_admin(userId, groupId)
    return 'succes'

# get all the groups a user is admin of
def get_all_groups_admin(userId):
    return select_groups_of_user_as_admin(userId)