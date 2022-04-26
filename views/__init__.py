from .post_requests import get_all_posts
#from views.category_requests import get_all_categories

from .tag_requests import get_all_tags, create_new_tag
from .user_requests import get_all_users, get_single_user, login_user, create_user

from .subscription_requests import get_all_subscriptions_by_user, create_subscription, delete_subscription
from .category_requests import get_all_categories, create_new_category

