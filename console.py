from base import bot


user_input = 'start'
while user_input:
    user_input = input('>>> ')
    print(bot.response(user_input))
