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
            posts.append(post.__dict__)
    return json.dumps(posts)
