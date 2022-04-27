import sqlite3
import json

from models import Post
from models import tag
from models import PostTag

def get_all_post_tags():
    """
    get all post tags
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id            
        FROM PostTags pt
        """)

        dataset = db_cursor.fetchall()

        post_tags = []

        # Iterate list of data returned from database
        for row in dataset:

            # Create an post instance from the current row
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(post_tags)

def get_all_post_tags_for_post(post_id):
    """
    get post tag relationships for specific post
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id            
        FROM PostTags pt
        WHERE pt.post_id = ?
        """, ( post_id, ))

        dataset = db_cursor.fetchall()

        post_tags = []

        # Iterate list of data returned from database
        for row in dataset:

            # Create an post instance from the current row
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])

            post_tags.append(post_tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(post_tags)

def create_post_tag(post_id, tag_id):
    """
    add new post tag relationship
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            INSERT INTO PostTags
                (post_id, tag_id)
            VALUES
                (?, ?)
            """, ( post_id, tag_id ))

def delete_post_tag(id = "", post_id = ""):
    """
    delete post tag relationship
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        if id:
            db_cursor.execute("""
                DELETE FROM PostTags
                WHERE id = ?
                """, ( id, ))
        elif post_id:
            db_cursor.execute("""
                DELETE FROM PostTags
                WHERE post_id = ?
                """, ( post_id, ))

def update_tags_for_post(new_post):
    """
    update existig tags for post
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # get all post_tags for this post_id
        post_tags = get_all_post_tags_for_post(new_post["id"])
        post_tags = json.loads(post_tags)
        # # need to
        # - remove post_tags that are no longer correct
        # '''
        #     iterate over new_post.tags
        #         each step iterate over post_tags to compare
        #         add ones that don't exist?
        # '''
        for tag_id in new_post["tags"]:
            found = False
            for post_tag in post_tags:
                if post_tag["tagId"] == tag_id:
                    found = True
            if found:
                pass
            else:
                create_post_tag(new_post["id"], tag_id)

        # - add post_tags that are new
        # '''
        #     iterate over post_tags
        #         each step iterate over new_post.tags to compare
        #         delete ones that don't exist?
        # '''
        for post_tag in post_tags:
            found = False
            for tag_id in new_post["tags"]:
                if post_tag["tagId"] == tag_id:
                    found = True
            if found:
                pass
            else:
                delete_post_tag(post_tag["id"])
        # - do nothing if post_tag relationship already exists
