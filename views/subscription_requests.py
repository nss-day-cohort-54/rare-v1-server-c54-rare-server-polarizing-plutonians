import sqlite3
import json

from models import Subscription
from views import get_posts_by_user_id

def get_all_subscriptions_by_user(user_id):
    """
    gets the subscription relationships 
    where the user id is the subber NOT the author
 
    Args:
        userId (int)): user_id of the person subscribed
    """
    # set up sqlite3 connection to database
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # db_cursor.execute sqlite3 SELECT query
            # select 
                # follower_id
                # author_id
                # created_on -- is this needed for anything?
            # from subscriptions s
            # where s.follower_id = ?
            # ? tuple functionality interpolating user_id
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_on
            FROM Subscriptions s
            WHERE s.follower_id = ?
        """, (user_id, ))
        
        dataset = db_cursor.fetchall()
        # initialize empty list for subscriptions
        subscriptions = []
        # iterate over dataset from execute query
        for row in dataset:
            subscription = Subscription(row['id'], row['follower_id'],
                                        row['author_id'], row['created_on'])
            
            #subscription.posts = get_posts_by_user_id(row['author_id'])
            subscription.posts = json.loads(get_posts_by_user_id(row['author_id']))
            
            # append the data as a Subscription object to the new list
            subscriptions.append(subscription.__dict__)
            
    # return new list
    return json.dumps(subscriptions)


def create_subscription(new_subscription):
    """
    adds new subscription to the subscription table

    Args:
        new_subscription (dict): should have the following keys
            - follower id
            - author id
            - created on date

    Returns:
        dict: new_subscription object with the proper id in the database
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # insert into sql statement
            # subscription table
            # values follower_id, author_id, and created_on
            # interpolated using ? functionality
        db_cursor.execute("""
            INSERT INTO subscriptions
                (follower_id, author_id, created_on)
            VALUES
                (?, ?, ?)
        """, (new_subscription['followerId'],
              new_subscription['authorId'],
              new_subscription['createdOn']))
            
        # get id of new table row
        id = db_cursor.lastrowid
        # add id to the new_subscription object
        new_subscription['id'] = id
    # return the new_subscription object with the id as added
    return json.dumps(new_subscription)

def delete_subscription(subscription_id):
    """
    removes a subscription entry from the subscription table

    Args:
        subscription_id (int): id of the subscription to delete

    Returns:
        None
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # delete from sql statement
            # subscriptions
            # where s.id = subscription_id # interpolate using ? functionality
        db_cursor.execute("""
            DELETE FROM Subscriptions
            WHERE id = ?    
        """, (subscription_id, ))
    
    # doesn't need to return anything
