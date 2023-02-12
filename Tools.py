import random
import os
import webbrowser

# Define the Folder Maker tool
def folder_maker_tool():
    num_folders = int(input("How many folders do you want to create? "))
    folder_name = input("Enter the name of the folder: ")
    folder_location = input("Enter the file location to create the folder(s): ")
    for i in range(num_folders):
        os.mkdir(os.path.join(folder_location, f"{folder_name}_{i+1}"))
        print(f"Created folder {folder_name}_{i+1} at {folder_location}.")

# Define the Discord Promotion tool
def discord_promotion_tool():
    discord_link = "https://discord.gg/B73FFJpTnV"
    webbrowser.open(discord_link)

# Define the Random Name Picker tool
def random_name_picker_tool():
    names = input("Enter a comma-separated list of names: ").split(",")
    print(f"The randomly selected name is: {random.choice(names)}")

# Define the Random Quote Generator tool
def random_quote_generator_tool():
    quotes = ["The best way to predict the future is to invent it.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "It does not matter how slowly you go as long as you do not stop.", "You miss 100% of the shots you don't take.", "Believe you can and you're halfway there."]
    print(f"Random quote: {random.choice(quotes)}")

# Define the Chat Bot tool
def chat_bot_tool():
    responses = ["Hello!", "How are you?", "I'm sorry, I don't understand.", "Goodbye!"]
    for i in range(3):
        message = input("You: ")
        response = random.choice(responses)
        print(f"Bot: {response}")

# Define the main function to run the script
def main():
    # Define the list of tools
    tools = ["Folder Maker", "Discord Promotion", "Random Name Picker", "Random Quote Generator", "Chat Bot"]

    while True:
        # Print the list of tools
        print("\033[92mRandom Tools:\033[0m")
        for i, tool in enumerate(tools):
            print(f"{i+1}. {tool}")
        print("\033[92mOpen:\033[0m")

        # Prompt the user to select a tool
        tool_choice = int(input("Enter the number of the tool you want to use: "))

        # Execute the selected tool
        if tool_choice == 1:
            folder_maker_tool()
        elif tool_choice == 2:
            discord_promotion_tool()
        elif tool_choice == 3:
            random_name_picker_tool()
        elif tool_choice == 4:
            random_quote_generator_tool()
        elif tool_choice == 5:
            chat_bot_tool()
        else:
            print("Sorry, that tool is not available.")

        # Ask if the user wants to repeat the process
        repeat_choice = input("Do you want to do something again? (y/n): ")
        if repeat_choice.lower() != "y":
            break

if __name__ == "__main__":
    main()
