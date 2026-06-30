from user import User
from post import Post

user_one = User("Mike Black", "mike.black@example.com", "totalsecretpwd", "DevOps Engineer")
user_one.get_user_info()

user_two = User(name="Anna Green", email="anna.green@example.com", password="secret", current_job_title="DevSecOps Engineer")
user_two.get_user_info()

post_one = Post("I am very busy today", user_one.name)
post_one.get_post_info()