# Import the module
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
user = (input("Enter your username:"))
profile = instaloader.Profile.from_username(bot.context, user)

print("Below are the details of entered usernames: ")
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Following: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)