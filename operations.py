from ldap3 import Server, Connection, ALL, MODIFY_REPLACE, SUBTREE
from config import AD_SERVER, AD_USER, AD_PASSWORD, BASE_DN

def connect_to_ad():
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(server, user=AD_USER, password=AD_PASSWORD, auto_bind=True)
    return conn

def create_user(conn, username, first_name, last_name, password):
    dn = f'cn={username},ou=Users,{BASE_DN}'
    attributes = {
        'givenName': first_name,
        'sn': last_name,
        'cn': username,
        'userPassword': password,
        'objectClass': ['top', 'person', 'organizationalPerson', 'user']
    }
    conn.add(dn, attributes=attributes)
    return conn.result['description'] == 'success'

def read_user(conn, username):
    dn = f'cn={username},ou=Users,{BASE_DN}'
    conn.search(dn, '(objectclass=person)', SUBTREE, attributes=['cn', 'givenName', 'sn', 'memberOf'])
    return conn.entries if conn.entries else None

def update_user(conn, username, attribute, value):
    dn = f'cn={username},ou=Users,{BASE_DN}'
    conn.modify(dn, {attribute: [(MODIFY_REPLACE, [value])]})
    return conn.result['description'] == 'success'

def delete_user(conn, username):
    dn = f'cn={username},ou=Users,{BASE_DN}'
    conn.delete(dn)
    return conn.result['description'] == 'success'

def create_group(conn, group_name):
    dn = f'cn={group_name},ou=Groups,{BASE_DN}'
    attributes = {
        'cn': group_name,
        'objectClass': ['top', 'group']
    }
    conn.add(dn, attributes=attributes)
    return conn.result['description'] == 'success'

def add_user_to_group(conn, username, group_name):
    user_dn = f'cn={username},ou=Users,{BASE_DN}'
    group_dn = f'cn={group_name},ou=Groups,{BASE_DN}'
    conn.modify(group_dn, {'member': [(MODIFY_REPLACE, [user_dn])]})
    return conn.result['description'] == 'success'

def remove_user_from_group(conn, username, group_name):
    user_dn = f'cn={username},ou=Users,{BASE_DN}'
    group_dn = f'cn={group_name},ou=Groups,{BASE_DN}'
    conn.modify(group_dn, {'member': [(MODIFY_REPLACE, [])]})
    return conn.result['description'] == 'success'

def list_users(conn):
    conn.search(BASE_DN, '(objectclass=user)', SUBTREE, attributes=['cn', 'givenName', 'sn'])
    return conn.entries

def authenticate_user(username, password):
    user_dn = f'cn={username},ou=Users,{BASE_DN}'
    server = Server(AD_SERVER, get_info=ALL)
    try:
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        return True
    except:
        return False

def list_groups(conn):
    conn.search(BASE_DN, '(objectclass=group)', SUBTREE, attributes=['cn'])
    return conn.entries

def read_group(conn, group_name):
    dn = f'cn={group_name},ou=Groups,{BASE_DN}'
    conn.search(dn, '(objectclass=group)', SUBTREE, attributes=['cn', 'member'])
    return conn.entries if conn.entries else None

def update_group(conn, group_name, attribute, value):
    dn = f'cn={group_name},ou=Groups,{BASE_DN}'
    conn.modify(dn, {attribute: [(MODIFY_REPLACE, [value])]})
    return conn.result['description'] == 'success'
