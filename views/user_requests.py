import sqlite3
import json
from datetime import datetime
from models.post import Post

from models.user import User

def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True
                        and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (first_name, last_name, username, email, password, bio, created_on, active) values (?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })


def get_all_users():
    """
    get all users in database
    """
    # set up sqlite3 connection to database
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # db_cursor.execute sqlite3 SELECT query
            # select
                # list out the user column headers
                # need first and last name, username, and email for issue #40
            # from users s
        # no filtering needed
        db_cursor.execute("""
            SELECT
                u.id,
                u.username,
                u.first_name,
                u.last_name,
                u.email,
                u.bio
            FROM users u
            ORDER BY u.username ASC
        """)

        dataset = db_cursor.fetchall()

        # initialize empty list for users
        users = []

        # iterate over dataset from execute query
        for row in dataset:
            # append the data as a User object to the new list
            user = User(row["id"],row["first_name"], row["last_name"],
                        row["email"], row["bio"], row["username"], "", "", "", "")
            users.append(user.__dict__)

    # return new list
    return json.dumps(users)


def get_single_user(user_id):
    """
    get single user in database
    """
    # set up sqlite3 connection to database
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # db_cursor.execute sqlite3 SELECT query
            # select
                # list out the user column headers
                # need first and last name, username, and email for issue #40
            # from users s
        # filter for user id
        db_cursor.execute("""
            SELECT
                u.id,
                u.username,
                u.first_name,
                u.last_name,
                u.email,
                u.bio,
                u.profile_image_url,
                u.created_on,
                u.active
            FROM users u
            WHERE u.id = ?
        """, ( user_id, ))

        data = db_cursor.fetchall()[0]

        rows = data.keys()

        user = User(data['id'], data['first_name'], data['last_name'],data['email'],
                    data['bio'], data['username'], '', data['profile_image_url'], data['created_on'], data['active'])
        
        # get all posts by the user
        db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved
            FROM posts p
            WHERE p.user_id = ?
        """, (user_id, ))

        postdata = db_cursor.fetchall()
        
        posts = []
        
        for row in postdata:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'],
                        row['image_url'], row['content'], row['approved'])
            posts.append(post.__dict__)

        user.posts = posts

    return json.dumps(user.__dict__)
        