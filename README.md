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
Images:

1.)login
<img width="1440" alt="login" src="https://user-images.githubusercontent.com/68525687/143656050-1764e49a-0bb7-4487-9e09-3fa79f85a1bf.png">
2.) signup 
<img width="1440" alt="signup" src="https://user-images.githubusercontent.com/68525687/143656062-39ad9ee2-4762-4bf6-8b81-6e2a36b01dd6.png">
3.)Forget password
<img width="1440" alt="forgot pass" src="https://user-images.githubusercontent.com/68525687/143656075-96936876-0201-4d52-bb54-5923e38ba230.png">
4.) Email sent
<img width="1440" alt="sent" src="https://user-images.githubusercontent.com/68525687/143656093-f6601887-9a69-45da-a67b-4b97b9a8f81d.png">
5.) Change View
<img width="1440" alt="restore" src="https://user-images.githubusercontent.com/68525687/143656108-b52d1b59-dce7-427b-bba3-34b4755258c2.png">
6.)Success Message
<img width="1440" alt="success" src="https://user-images.githubusercontent.com/68525687/143656122-10f3172c-0efc-49b0-a937-a066f001d667.png">
7.) Reattempt to restore using same link
<img width="1440" alt="reattempt" src="https://user-images.githubusercontent.com/68525687/143656154-de75d9cd-6925-4a11-b2a4-24f2ddaa3582.png">
8.)Home Feed Page
<img width="1440" alt="home page" src="https://user-images.githubusercontent.com/68525687/143656180-d378fe5c-c4cd-498b-ae46-3b592b405dfe.png">
9.) Detail Post View
<img width="1440" alt="detailpage" src="https://user-images.githubusercontent.com/68525687/143656196-44b66273-34f1-4af6-b25a-1c8df0684f09.png">
10.) Profile Page
<img width="1440" alt="profilepage" src="https://user-images.githubusercontent.com/68525687/143656249-cfe662bf-e6df-4b5f-97de-90aace516918.png">
11.) Create Post 
<img width="1440" alt="createmodal" src="https://user-images.githubusercontent.com/68525687/143656261-8fc1db3b-74e2-4cd9-a463-fc036470b4bb.png">
12.)Following List
<img width="1440" alt="following list" src="https://user-images.githubusercontent.com/68525687/143656276-29c74163-7146-47ee-8829-4517f2498fc5.png">
13.) Change Password
<img width="1440" alt="change password" src="https://user-images.githubusercontent.com/68525687/143656296-7fa24d3b-5afb-4759-89c8-e70261902f29.png">
14.) Follow and Unfollow
<img width="625" alt="follow" src="https://user-images.githubusercontent.com/68525687/143656488-6fcf833e-4394-482f-8f77-4eead98d263c.png"><br>
<img width="639" alt="unfollow" src="https://user-images.githubusercontent.com/68525687/143656492-e992fb58-761a-4ca2-a5ef-78068be707d1.png">
15.)search User
<img width="1440" alt="search users" src="https://user-images.githubusercontent.com/68525687/143656345-7be6f8ad-e6da-4ee5-9879-76c9a52fe0f9.png">
16.) Edit Profile
<img width="1440" alt="edit profile" src="https://user-images.githubusercontent.com/68525687/143656352-1c2b15f6-3984-47f6-bcd7-e039b5242ede.png">











