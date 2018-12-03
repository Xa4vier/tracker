from database.insert import insert_group, insert_usergroup, insert_admin
from database.get import select_groups_admin_id, select_groups_admin_id_group_id, select_usergroup_by_user_group_id

def create_group(userId, name):
    groupId = insert_group(name)
    insert_usergroup(userId, groupId)
    insert_admin(userId, groupId)
    return 'succes'

# get all the groups a user is admin of
def get_all_groups_with_admin_id(userId):
    message = ''
    try :
        message = select_groups_admin_id(int(userId))
    except ValueError :
        message = 'ID just be a INT'
    return message

# get a specific group if a user is admin
def get_all_groups_admin_with_group_id(userId, groupId):
    message = ''
    try :
        message = select_groups_admin_id_group_id(int(userId), int(groupId))
    except ValueError :
        message = 'ID just be a INT'
    return message

# Lets a admin add a member to a group he owns
def add_user_to_group(adminId, userId, groupId):
    message = ''
    try :
        if check_if_user_in_group(userId, groupId) ==  False:
            if check_if_admin_of_group(adminId, groupId):
                insert_usergroup(userId, groupId)
                message = 'succes'
            else: 
                message = "Not admin of group"
        else :
            message = "User alreay in group"
    except ValueError :
        message = "ID needs to be INT"
    return message
        
def check_if_admin_of_group(adminId, groupId):
    message = False
    if len(select_groups_admin_id_group_id(adminId, groupId)) > 0:
        message = True
    return message

def check_if_user_in_group(userId, groupId):
    message = False
    if len(select_usergroup_by_user_group_id(userId, groupId)) > 0:
        message = True
    return message