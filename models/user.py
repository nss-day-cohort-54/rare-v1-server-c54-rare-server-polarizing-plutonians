class User():
    def __init__(self, id, first_name, last_name, email, bio, username, password, profile_image_url, created_on, active):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password
        self.profileImageUrl = profile_image_url
        self.createdOn = created_on
        self.active = active
        self.posts = []
