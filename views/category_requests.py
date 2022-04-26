# import sqlite3, json, and the category model

import sqlite3
import json
from models import Category


# def a get_all_categories function
# function will get all categories alphabetically
def get_all_categories():

    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                c.id,
                c.label
            FROM Categories c
            ORDER BY label ASC
            """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return json.dumps(categories)

#  create a connection to sqlite database
#  Write an SQL query to get category info and order it alphabetically
#  create an empty list to hold each category instance
# convert data into python
# iterate through the list and create a category instance from the current row
# add dictionary representation of category to the list using append
# convert data to json


# def a DELETE category function

# connect to database
# write sql query to delete a single category instance


# def a EDIT or UPDATE category function

# connect to database
# write sql query to update/edit a single category instance
# check if rows are affected to force the appropriate fetch response(204/404)


# define a function create_category
# takes one parameter (new_category)

    # connect to the database

    # set db_cursor equal to conn.cursor()

    # write sql query which inserts into the "Categories" table, (label)
# VALUES
    # add one binding ? for the incoming value,
    # (new_category)['label']

    # set the id equal to the last row id
    # (id = db_cursor.lastrowid)

    # add that id property to the new category dictionary
    # new_category['id'] = id

    # return json.dumps(new_category)
    
# define a new function, create_new_tag which accepts one parameter, "new_tag"
def create_new_category(new_category):
    
    # connect to the database
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
    # set db_cursor equal to conn.cursor() 

    # write sql block which inserts into the "Category" table, (label)
        db_cursor.execute("""
    INSERT INTO Categories
        ( label )
    VALUES
        ( ? );
    """, (new_category['label'], ))
# VALUES 
    # add one binding ? for the incoming value, 
        # (new_category)['label']
        id = db_cursor.lastrowid
        new_category["id"] = id
        # return json.dumps(new_category)
    return json.dumps(new_category)
