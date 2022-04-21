import sqlite3
import json

from models import Comment

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
        # where post_id = the post_id passed as an argument
        
        # empty list for comments to return
        comments = []
        
        # iterate over row in data
            # make into a Comment() object
            # append to comments.
            
    return json.dumps(comments)

def add_comment(new_comment):
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
        # insert into comments
        # data from new comment
        # ? functionality to add new_comment["authorId"] new_comment["postId"] new_comment["content"]

        # db_cursor.lastrowid to get the id of the added comment
        # add id to new_comments


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
        # delete from comments
        # where comments.id = comment_id ? interpolated using ? functionality
    
    # doesn't need to return anything
    return ""