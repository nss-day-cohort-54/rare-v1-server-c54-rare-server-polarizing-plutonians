# define a function to get all tags

    # write sql block to select names/labels for all tags

        # use ORDER BY to order them alphabetically
        # eaxmple ORDER BY label ASC;


# define a new function, create_new_tag which accepts one parameter, "new_tag"

    # docstring

    # connect to the database

    # set db_cursor equal to conn.cursor() 

    # write sql block which inserts into the "Tags" table, (label) 
# VALUES 
    # add one binding ? for the incoming value, 
        # (new_tag)['label']

        # return json.dumps(new_tag) 