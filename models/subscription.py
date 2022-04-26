class Subscription():
    def __init__(self, id, follower_id, author_id, created_id, posts = []):
        self.id = id
        self.followerId = follower_id
        self.authorId = author_id
        self.createdId = created_id
        self.posts = posts