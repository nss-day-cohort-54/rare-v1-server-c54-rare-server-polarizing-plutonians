class Comment():

    def __init__(self, id, post_id, author_id, content):
        self.id = id
        self.postId = post_id
        self.authorId = author_id
        self.content = content
        self.user = None

