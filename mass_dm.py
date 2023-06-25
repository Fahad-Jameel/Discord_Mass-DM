import discord
import os

# Get the token and usernames from the files
token_file = os.path.join(os.getcwd(), "token.txt")
usernames_file = os.path.join(os.getcwd(), "usernames.txt")
message_file = os.path.join(os.getcwd(), "message.txt")

# Create a Discord client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Load the token, usernames, and message
with open(token_file, "r") as f:
    token = f.read()

with open(usernames_file, "r") as f:
    usernames = f.readlines()

with open(message_file, "r") as f:
    message = f.read()

# Create a list of used tokens
used_tokens = []

@client.event
async def on_ready():
    print("Bot is ready.")

    # Send a DM with the message to each user
    for username in usernames:
        username = username.strip()  # Remove newline characters
        user = discord.utils.get(client.users, name=username)
        if user is not None:
            await user.send(message)

        # Save the used token
        used_tokens.append(token)

    # Save the used tokens to a file
    with open("used_tokens.txt", "w") as f:
        for used_token in used_tokens:
            f.write(used_token + "\n")

    # Close the client
    await client.close()

# Run the client
client.run(token)
