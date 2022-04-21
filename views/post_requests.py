import sqlite3
import json
from datetime import datetime
from models.post import Post
from models.category import Category
from models.user import User


def get_all_posts():
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Join tables Users and Categories
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
                c.label category_label
                u.first_name 
            FROM Posts p
            JOIN Categories c
                ON c.id = p.category_id
            JOIN Users u
                ON u.id = p.user_id
        """,)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post = Post(
                row['id'],
                row['user_id'],
                row['category_id'],
                row['title'],
                row['publication_date'],
                row['image_url'],
                row['content'],
                row['approved']
            )

            category = Category(
                row['id'],
                row['label']
            )

            user = User(
                row['id'],
                row['first_name'],
                row['last_name'],
                row['email'],
                row['bio'],
                row['username'],
                row['password'],
                row['profile_image_url'],
                row['created_on'],
                row['active']
            )

            post.category = category.__dict__

            post.user = user.__dict__

            # TAG CODE
            # db_cursor.execute("""
            # SELECT
            #     t.id,
            #     t.name
            # FROM Entry e
            # JOIN Entrytags et
            #     ON e.id = et.entry_id
            # JOIN Tags t
            #     ON t.id = et.tag_id
            # WHERE e.id = ?
            # """, (entry.id, )
            # )

            # tag_list = db_cursor.fetchall()

            # for et_row in tag_list:
            #     tag = Tag(
            #         et_row['id'],
            #         et_row['name']
            #     )

            #     entry.tags.append(tag.__dict__)

            # Store Category Class and User Class with
            # relevant rows of keys

            # append class variables to posts
            # and make into dictionaries

            posts.append(post.__dict__)
    return json.dumps(posts)

# function to get posts by single user


# def get_posts_by_user_id(user_id):
#     """
#     get list of posts by a single user

#     Args:
#         user_id (int): user id of the author

#     Returns:
#         list: list of the posts by the specified user
#     """
#     with sqlite3.connect('./db.sqlite3') as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()
#         # sql query
#         # select desired columns
#         # from posts
#         # where posts.user_id = ? # interpolate user_id argument

#         # declare empty list for posts
#         posts = []

#         # get dataset from db_cursor

#         # iterate over dataset
#         # for each one make into a Post() object
#         # append post.__dict__ to posts

#     return json.dumps(posts)

# define function to get a single post, this will
# take need a parameter to take a post UID later

    # connect to database and store in var, set to use rows for db,
    # user cursor method on conn

    # execute query looking for id in tuple

    # fetch one post on db_cursor and store in var

    # Use relevant models and store in vars

    # change classes into dictionaries and attach to post
    # i.e. post.author = author.__dict__

    # return post.__dict__ and parse into JSON


# Define delete post function that will take id as arg

    # connect to db and store in conn, use cursor method on conn
    # and store in db_cursor

    # execute method to query db, looking for id in tuple

    # Define function to create entry, taking a param that will
    # take new_entry as an arg

    # connect to db, store in conn, use cursor method on conn and store
    # db_cursor

    # use execute method on db_cursor to query db, this will INSERT INTO
    # taking ? as values, observing all relevant keys on Post Class;
    # except id

    # store lastrowid in id var
    # pack new id into id var

    # iterate tags in the relevant key in the arg

    # use execute method on db_cursor to query db, using INSERT INTO
    # for all keys except id, VALUES will be ?
    # observing new id and tag in tuple

    # parse new_entry into json


# define function to update post

    # connect to db and store in conn
    # use rows
    # use cursor method on conn and store in db_cursor

    # use execute method on db_cursor to query db
    # use UPDATE and SET, use relevant keys and values set to ?
    # WHERE id = ?
    # observing all relevant keys in new_entry
    # with id last in tuple

    # use rowcount on db_cursor and store in var

    # if rows_affected is 0, return False, else return True
