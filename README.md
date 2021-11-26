# Instagram-Clone

An attempt to clone IG
Project consisted of 3 applications. 
The user app used AbstractUser class to define the User model, it also made use of a Custom Manager.
Email was used for authenticating users primarily, however users had a choice to use their usernames instead.
Class based Views were used, mainly View class was inherited, however TemplateView and DetailView were also scarcely inherited.
ModelAdmin and UserAdmin were used for better representation of all the models in the admin interface.
The authentication app handled user registration, logging-in, logging-out, and restoration of forgotten passwords. 
login required decorator was used, passwords were hashed with argon2 hashing. 
The core app dictated user feed page, profile page, profile edit page, profile search functionality,
posting and deleting of pictures, liking and disliking of posts, commenting, deletion of comments, follower/following list,
and following/unfollowing functionalities.
https://user-images.githubusercontent.com/68525687/143653084-f7023ecb-9ade-42fa-9a6c-0c64d4032d6e.png
