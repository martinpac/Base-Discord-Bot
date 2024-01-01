import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


async def process_admin_commands(message, user_message):
    if user_message.startswith('!kick'):
        try:
            member_to_kick = message.mentions[0]
            await member_to_kick.kick(reason="Kicked by command")
            return 'User has been kicked!'

        except IndexError:
            return 'Please mention the user you want to kick'

        except discord.Forbidden:
            return 'I do not have the necessary permissions to kick this user!'

    elif user_message.startswith('!ban'):
        try:
            member_to_ban = message.mentions[0]
            await member_to_ban.ban(reason="Banned by command")
            return 'User has been banned!'

        except IndexError:
            return 'Please mention the user you want to ban'

        except discord.Forbidden:
            return 'I do not have the necessary permissions to ban this user!'

    elif user_message.startswith('!mute'):
        try:
            member_to_mute = message.mentions[0]
            await member_to_mute.add_roles(message.guild.get_role(YOUR_ROLE_ID_GOES_HERE), reason="Muted by command")
            return 'User has been muted!'

        except IndexError:
            return 'Please mention the user you want to mute'

        except discord.Forbidden:
            return 'I do not have the necessary permissions to mute this user!'

    elif user_message.startswith('!unmute'):
        try:
            member_to_unmute = message.mentions[0]
            await member_to_unmute.remove_roles(message.guild.get_role(YOUR_ROLE_ID_GOES_HERE), reason="Unmuted by command")
            return 'User has been unmuted!'

        except IndexError:
            return 'Please mention the user you want to unmute'

        except discord.Forbidden:
            return 'I do not have the necessary permissions to unmute this user!'

    return None  # No admin command matched


def run_discord_bot():
    TOKEN = 'YOUR TOKEN GOES HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said "{user_message}" ({channel})')

        if (user_message.startswith('!kick') or user_message.startswith('!ban') or user_message.startswith('!mute')
              or user_message.startswith('!unmute')):
            admin_command_result = await process_admin_commands(message, user_message)
            if admin_command_result:
                await message.channel.send(admin_command_result)

        elif user_message.startswith('!'):
            response = responses.get_response(user_message)
            await message.channel.send(response)

        else:
            pass

    client.run(TOKEN)
