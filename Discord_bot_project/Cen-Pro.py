import discord
import os
from dotenv import load_dotenv
import w_list


load_dotenv()

client = discord.Client()
Token = os.getenv('TOKEN')

words = w_list.b_words


async def kick(ctx, member: discord.member, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} Kicked...')

@client.event
async def on_ready():
    print('Bot logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    for s in words:
        if(member.name == s):
            kick(member)

@client.event
async def on_message(message): 
    
    #ignore messages made by itself
    if message.author == client.user: 
        return

    #triggers when a string contains a word in b_words
    if any(string in message.content.lower() for string in words): 
        await message.delete()
        await message.channel.send("Message Deleted!")
        



#Driver Function
def main():
    client.run(Token)

if __name__ == "__main__":
    main()