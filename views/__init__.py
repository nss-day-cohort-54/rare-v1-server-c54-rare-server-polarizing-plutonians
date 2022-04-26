"""imports functions to be easily imported in other modules
    """
from .post_requests import get_all_posts
from .post_requests import get_single_post
from .post_requests import create_post
from .post_requests import edit_post
from .post_requests import delete_post
from .post_requests import get_posts_by_title
from .post_requests import get_posts_by_user_id
#from views.category_requests import get_all_categories
from .tag_requests import get_all_tags, create_new_tag
from .user_requests import get_all_users, get_single_user, login_user, create_user
from .subscription_requests import get_all_subscriptions_by_user, create_subscription, delete_subscription
from .category_requests import get_all_categories, create_new_category

from .comment_requests import get_comments_for_post, create_comment, delete_comment

