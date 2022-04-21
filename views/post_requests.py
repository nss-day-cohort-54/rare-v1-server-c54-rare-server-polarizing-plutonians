import sqlite3
import json
from datetime import datetime
from models.post import Post


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
              id,
              user_id,
              category_id,
              title,
              publication_date,
              image_url,
              content,
              approved
            FROM Posts
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

            # Store Category Class and User Class with
            # relevant rows of keys

            # append class variables to posts
            # and make into dictionaries

            posts.append(post.__dict__)
    return json.dumps(posts)

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
