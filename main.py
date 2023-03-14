import pyrogram

# Initialize the client
app = pyrogram.Client("my_account")

# Start the client
app.start()

# Define a function to handle the /start command
@app.on_message(pyrogram.Filters.command("start"))
def start(client, message):
    message.reply("Welcome to the Guess Bot game!\n\nI'm thinking of a number between 1 and 10. Can you guess it?")

# Define a function to handle the user's guess
@app.on_message()
def guess(client, message):
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Get the user's guess
    user_guess = int(message.text)
    
    # Check if the user's guess is correct
    if user_guess == secret_number:
        message.reply("You guessed it! The number was {}".format(secret_number))
    else:
        message.reply("Sorry, that's not it. The number was {}".format(secret_number))

# Run the client
app.run()
