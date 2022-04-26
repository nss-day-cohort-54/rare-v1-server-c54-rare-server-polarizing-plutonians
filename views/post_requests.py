import sqlite3
import json
from models.post import Post
from models.category import Category
from models.user import User
from models.tag import Tag


def get_all_posts():
    # CODE COMPLETE
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
                p.approved,
                c.id category_id,
                c.label category_label,
                u.first_name,
                u.last_name,
                u.email,
                u.bio,
                u.username,
                u.password,
                u.profile_image_url,
                u.created_on,
                u.active
            FROM Posts p
            JOIN Categories c
                ON c.id = p.category_id
            JOIN Users u
                ON u.id = p.user_id
            ORDER BY p.publication_date DESC

        """)

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
                row['category_id'],
                row['category_label']
            )

            user = User(
                row['user_id'],
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
            db_cursor.execute("""
            SELECT
                t.id,
                t.name
            FROM Posts p
            JOIN PostTags pt
                ON p.id = pt.post_id
            JOIN Tags t
                ON t.id = pt.tag_id
            WHERE e.id = ?
            """, (post.id, )
            )

            tag_list = db_cursor.fetchall()

            for pt_row in tag_list:
                tag = Tag(
                    pt_row['id'],
                    pt_row['name']
                )

                post.tags.append(tag.__dict__)

            # Store Category Class and User Class with
            # relevant rows of keys

            # append class variables to posts
            # and make into dictionaries

            posts.append(post.__dict__)
    return json.dumps(posts)


def get_posts_by_user_id(id):
    # CODE COMPLETE
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            c.label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.user_id = ?
        """, (id,))
        posts = []
#       iterate over dataset

        dataset = db_cursor.fetchall()
        for row in dataset:
            #         # for each one make into a Post() object
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
                row['category_id'],
                row['label']
            )

            # add category to
            post.category = category.__dict__

            db_cursor.execute("""
                SELECT
                t.id,
                t.label,
                pt.tag_id,
                pt.post_id
                FROM PostTags pt
                JOIN Tags t 
                    ON t.id = pt.tag_id
                WHERE pt.post_id = ?
            """, (post.id, ))

            tags = []

            tag_dataset = db_cursor.fetchall()

            for tag_row in tag_dataset:
                tag = Tag(
                    tag_row['tag_id'],
                    tag_row['label']
                )

                tags.append(tag.__dict__)

            post.tags = tags

#         # append post.__dict__ to posts
            posts.append(post.__dict__)

#     return json.dumps(posts)
    return json.dumps(posts)


def get_posts_by_title(title_string):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active,
            c.label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.title = ?
        """, (f"%{title_string}%", ))

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

            user = User(
                row['user_id'],
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

            category = Category(
                row['category_id'],
                row['label']
            )

            post.user = user.__dict__
            post.category = category.__dict__
            posts.append(post.__dict__)
    return json.dumps(posts)


def get_single_post(id):
    # connect to database and store in var, set to use rows for db,
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        # user cursor method on conn
        db_cursor = conn.cursor()

        # execute query looking for id in tuple
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active,
            c.label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """, (id, ))

        # fetch one post on db_cursor and store in var
        data = db_cursor.fetchone()

        # Use relevant models and store in vars
        post = Post(
            data['id'],
            data['user_id'],
            data['category_id'],
            data['title'],
            data['publication_date'],
            data['image_url'],
            data['content'],
            data['approved']
        )

        user = User(
            data['user_id'],
            data['first_name'],
            data['last_name'],
            data['email'],
            data['bio'],
            data['username'],
            data['password'],
            data['profile_image_url'],
            data['created_on'],
            data['active']
        )

        category = Category(
            data['category_id'],
            data['label']
        )

        # change classes into dictionaries and attach to post
        # i.e. post.author = author.__dict__
        post.user = user.__dict__
        post.category = category.__dict__

    # return post.__dict__ and parse into JSON
    return json.dumps(post.__dict__)


def edit_post(id, edited_post):

    # connect to db and store in conn
    with sqlite3.connect("./db.sqlite3") as conn:

        # use cursor method on conn and store in db_cursor
        db_cursor = conn.cursor()

        # use execute method on db_cursor to query db
        # use UPDATE and SET, use relevant keys and values set to ?
        # WHERE id = ?
        # observing all relevant keys in new_entry
        # with id last in tuple
        db_cursor.execute("""
        UPDATE Posts
            SET
                user_id = ?,
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (
            edited_post['userId'],
            edited_post['categoryId'],
            edited_post['title'],
            edited_post['publicationDate'],
            edited_post['imageUrl'],
            edited_post['content'],
            edited_post['approved'],
            id)
        )

        # use rowcount on db_cursor and store in var
        rows_affected = db_cursor.rowcount

    # if rows_affected is 0, return False, else return True
    if rows_affected == 0:
        # Forces 404 header response by main module
        return False
    else:
        # Forces 204 header response by main module
        return True


def get_posts_by_filter(url_dict):
    """
    filters posts by given key column

    Args:
        key (str): the column to be filtered on
        value (str): the search term to check for

    Returns:
        list: list of dicts of posts
    """
    # connect to db conn stuff
    # sqlstmt = ""
    # if "category" in url_dict:
    # python stuff ..
    # db_cursor.execute(sqlstmt)
    # sgl query
    # mostly copies from get all posts to get posts
    # with category, user, title, tag embedded
    # select *whatever columns we need*
    # from posts
    # join categories
    # join users
    # where ?[%key%] LIKE ?[%value%]
    # OR categories.label LIKE ?[%value%]
    # options for user
    # OR users.first_name LIKE
    # OR users.last_name LIKE
    # OR users.username LIKE

    # sql query searching tags
    # select columns
    # from posttags
    # join posts
    # join tags

    # Where tags.label like ?

    return ""


def create_post(new_post):

    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            (
            user_id,
            category_id,
            title,
            publication_date,
            image_url,
            content,
            approved
            )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ? );
        """, (
            new_post['userId'],
            new_post['categoryId'],
            new_post['title'],
            new_post['publicationDate'],
            new_post['imageUrl'],
            new_post['content'],
            new_post['approved'])
        )

        id = db_cursor.lastrowid
        new_post['id'] = id

        for tag in new_post['tags']:

            db_cursor.execute("""
            INSERT INTO PostTags
                (
                post_id,
                tag_id
                )
            VALUES
                (?,?);
                """, (new_post['id'], tag)
            )

    return json.dumps(new_post)


def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, )
        )

# def get_posts_by_*(value):
#     conn stuff, sqlite3.Row, cursor,

#     execute("""
#         relevant data
#         relevant data from other table
#         FROM table
#         JOIN table
#             ON the point the right ids match
#         WHERE relevant key's value is LIKE ?
#         """, (f"%{value}%")

#     posts = []
#     dataset = db_cursor.fetchall()

#     for row in dataset
#         class stored in Variable

#         class stored in variable

#         post.other_class = other_class.__dict__

#         posts.append(post.__dict__)

#     return json.dumps(posts)
