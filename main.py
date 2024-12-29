import discord


with open("Tokens.txt", "r") as file:
    tokens = file.read().splitlines()


client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f" ==>  {client.user}  <== ")

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and message.author != client.user:
        message = """

      Your custom message here

"""
        await message.reply(message, mention_author=True)

for token in tokens:
    try:
        client.run(token)
    except discord.errors.LoginFailure:
        print(f"Login failed for token: {token}")
