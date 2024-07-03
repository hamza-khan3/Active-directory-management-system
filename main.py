from ad_operations import (
    connect_to_ad, create_user, read_user, update_user, delete_user, create_group,
    add_user_to_group, remove_user_from_group, list_users, authenticate_user, 
    list_groups, read_group, update_group
)

def main():
    conn = connect_to_ad()

    if create_user(hamza, 'hkhan', 'JAdeel', 'Doe', 'password123'):
        print('User created successfully.')
    else:
        print('Failed to create user.')

    user = read_user(conn, 'jdoe')
    if user:
        print(f'User found: {user}')
    else:
        print('User not found.')

    if update_user(conn, 'jdoe', 'givenName', 'Johnny'):
        print('User updated successfully.')
    else:
        print('Failed to update user.')

    user = read_user(conn, 'jdoe')
    if user:
        print(f'User found: {user}')
    else:
        print('User not found.')

    if delete_user(conn, 'jdoe'):
        print('User deleted successfully.')
    else:
        print('Failed to delete user.')

    user = read_user(conn, 'jdoe')
    if user:
        print(f'User found: {user}')
    else:
        print('User not found.')

    if create_group(conn, 'Developers'):
        print('Group created successfully.')
    else:
        print('Failed to create group.')

    if add_user_to_group(conn, 'jdoe', 'Developers'):
        print('User added to group successfully.')
    else:
        print('Failed to add user to group.')

    if remove_user_from_group(conn, 'jdoe', 'Developers'):
        print('User removed from group successfully.')
    else:
        print('Failed to remove user from group.')

    users = list_users(conn)
    if users:
        print('Users list:')
        for user in users:
            print(user)

    if authenticate_user('jdoe', 'password123'):
        print('User authenticated successfully.')
    else:
        print('Failed to authenticate user.')

    groups = list_groups(conn)
    if groups:
        print('Groups list:')
        for group in groups:
            print(group)

    group = read_group(conn, 'Developers')
    if group:
        print(f'Group found: {group}')
    else:
        print('Group not found.')

    if update_group(conn, 'Developers', 'description', 'Development Team'):
        print('Group updated successfully.')
    else:
        print('Failed to update group.')

    conn.unbind()

if __name__ == '__main__':
    main()
