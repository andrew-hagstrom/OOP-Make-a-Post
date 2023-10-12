class User:

    posts = []
    user_id = 0

    def __init__(self, user_name):
        User.user_id += 1
        self._user_name = user_name
        self._id = User.user_id
        self._posts = []
        # User.user_id[self._id] = self
    
    # def __repr__(self):
    #     return f"{self.get_make}"
 

    @property
    def get_user_name(self):
        if type(user_name) == str: 
            return self._user_name

    @get_user_name.setter
    def set_user_name(self, new_user_name):
        self._user_name=new_user_name

    @property
    def get_posts(self):
        return self._posts
    
    # @get_posts.setter
    # def set_post(self, new_post):
    #     print(input('Post your comment here: '))
    #     current_posts = get_posts()
    #     print(current_posts)
    #     # self._posts.append(new_post)

    @staticmethod
    def make_a_post():
        post = input('Post your comment here: ')
        # print(post)
        User.posts.append(post)
        return post

user_1 = User("andrew.hagstrom")
user_2 = User("josh.kim")
user_2.make_a_post()
user_1.make_a_post()
print(User.posts)


