import sqlite3
import json

from models import Comment, User

def get_comments_for_post(post_id):
    """
    get comments for a single post

    Args:
        post_id (int): id for the post to get comments for
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # sql query
        db_cursor.execute("""
            SELECT
                c.id,
                c.post_id,
                c.author_id,
                c.content,
                u.username
            FROM comments c
            JOIN users u
                ON c.author_id = u.id
            WHERE c.post_id = ?
        """, (post_id, ))
        # where post_id = the post_id passed as an argument

        # empty list for comments to return
        comments = []

        dataset = db_cursor.fetchall()
        # iterate over row in data
        for row in dataset:
            # make into a Comment() object
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            # append to comments.
            user = User(row['author_id'], "", "", "", "", row['username'], "", "", "", "")

            comment.user = user.__dict__

            comments.append(comment.__dict__)

    return json.dumps(comments)

def create_comment(new_comment):
    """
    adds new comment to the comments table

    Args:
        new_comment (dict): object of new comment to be added

    Returns:
        dict: new comment with the new id added
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # sql query
        db_cursor.execute("""
            INSERT INTO Comments
                (post_id, author_id, content)
            VALUES
                (?, ?, ?)
        """, (new_comment["postId"], new_comment["authorId"], new_comment["content"]))
        # insert into comments
        # data from new comment
        # ? functionality to add new_comment["authorId"] 
        # new_comment["postId"] new_comment["content"]

        # db_cursor.lastrowid to get the id of the added comment
        id = db_cursor.lastrowid
        # add id to new_comments
        new_comment["id"] = id

    return json.dumps(new_comment)

def delete_comment(comment_id):
    """
    deletes comment with given comment id

    Args:
        comment_id (int): id of comment to delete

    Returns:
        none: nothing to return
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # sql query
        db_cursor.execute("""
            DELETE FROM Comments
            WHERE id = ?
        """, (comment_id, ))
        # delete from comments
        # where comments.id = comment_id ? interpolated using ? functionality

    # doesn't need to return anything
