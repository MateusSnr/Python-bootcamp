class User:
    def _init_(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user being created...")

    def follow(self, user):
        user.followers += 1


user_1 = User("001", "Mateus")
# user_1.id = "001"
# user_1.name = "Mateus"

user_2 = User("002", "Mateus snr")
# user_2.id = "002"
# user_2.name = "Mateus snr"

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)