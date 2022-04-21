# import sqlite3, json, and the category model




# def a get_all_categories function
#function will get all categories alphabetically

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





