import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message.startswith('!random'):
        parts = p_message.split(' ')
        if len(parts) == 2:
            range_values = parts[1].split('-')
            if len(range_values) == 2:
                try:
                    start = int(range_values[0])
                    end = int(range_values[1])
                    if start <= end:
                        return f':boom: {random.randint(start,end)} :boom:'
                    else:
                        return 'Starting number must be less than Ending number!'
                except ValueError:
                    return "Please provide numbers!"
            else:
                return 'Use !random X-Y to specify a range!'

    if p_message == '!roll':
        return ':game_die: ' + str(random.randint(1, 6)) + ' :game_die:'

    if p_message == '!coinflip':
        return ':coin: ' + random.choice(['Heads', 'Tails']) + ' :coin:'

    if p_message == '!help':
        return generate_help_message()

    return 'Invalid command!'


def generate_help_message() -> str:
    commands = [
        '`!kick: Kicks a user you mention                                 `',
        '`!ban: Bans a user you mention                                   `',
        '`!mute: Mutes a user you mention                                 `',
        '`!unmute: Unmutes a user you mention                             `',
        '`!random X-Y: Generates a random number within selected numbers  `',
        '`!roll: Rolls a die of 1-6                                       `',
        '`!coinflip: Flips a coin                                         `',
    ]

    return '\n'.join(commands)
