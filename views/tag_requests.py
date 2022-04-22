import sqlite3
import json
from models import Tag

def get_all_tags():
    """_summary_

    Returns:
        _type_: _description_
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tags t
        ORDER BY label ASC
        """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return json.dumps(tags)


# define a new function, create_new_tag which accepts one parameter, "new_tag"
def create_new_tag(new_tag):
    """_summary_

    Args:
        new_tag (_type_): _description_
    """
    # docstring

    # connect to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
    # set db_cursor equal to conn.cursor() 

    # write sql block which inserts into the "Tags" table, (label)
        db_cursor.execute("""
    INSERT INTO Tags
        ( label )
    VALUES
        ( ? );
    """, (new_tag['label'], ))
# VALUES 
    # add one binding ? for the incoming value, 
        # (new_tag)['label']
        id = db_cursor.lastrowid
        # return json.dumps(new_tag)
    return json.dumps(new_tag)