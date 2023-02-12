import random
import os
import webbrowser
import json
import requests

def folder_maker_tool():
    num_folders = int(input("How many folders do you want to create? "))
    folder_name = input("Enter the name of the folder: ")
    folder_location = input("Enter the file location to create the folder(s): ")
    for i in range(num_folders):
        os.mkdir(os.path.join(folder_location, f"{folder_name}_{i+1}"))
        print(f"Created folder {folder_name}_{i+1} at {folder_location}.")

def discord_promotion_tool():
    discord_link = "https://discord.gg/B73FFJpTnV"
    webbrowser.open(discord_link)

def random_name_picker_tool():
    names = input("Enter a comma-separated list of names: ").split(",")
    print(f"The randomly selected name is: {random.choice(names)}")

def random_quote_generator_tool():
    quotes = ["The best way to predict the future is to invent it.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "It does not matter how slowly you go as long as you do not stop.", "You miss 100% of the shots you don't take.", "Believe you can and you're halfway there."]
    print(f"Random quote: {random.choice(quotes)}")

def accounts_tool():
    num_alts = int(input("How many Minecraft alts do you want to generate? "))
    output_file = input("Enter the output file name: ")

    alts = []
    for i in range(num_alts):

        email = f"{i}_{random.randint(0, 10000)}@example.com"
        password = f"password_{random.randint(0, 10000)}"


        alt = f"{email}:{password}"
        alts.append(alt)

    for alt in alts:
        email, password = alt.split(":")
        response = requests.post(
            "https://authserver.mojang.com/authenticate",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "agent": {
                    "name": "Minecraft",
                    "version": 1
                },
                "username": email,
                "password": password,
                "requestUser": True
            })
        )

        if response.status_code == 200:
            print(f"Alt '{alt}' is valid!")
        else:
            print(f"Alt '{alt}' is invalid.")

    if output_file:
        with open(output_file, "w") as file:
            file.write("\n".join(alts))
    print(f"Saved {len(alts)} Minecraft alts to {output_file}.")

def main():
    tools = ["Folder Maker", "Discord Promotion", "Random Name Picker", "Random Quote Generator", "Accounts"]

    while True:
        print("\033[92mRandom Tools:\033[0m")
        for i, tool in enumerate(tools):
            print(f"{i+1}. {tool}")
        print("\033[92mOpen:\033[0m")

        tool_choice = int(input("Enter the number of the tool you want to use: "))

        if tool_choice == 1:
            folder_maker_tool()
        elif tool_choice == 2:
            discord_promotion_tool()
        elif tool_choice == 3:
            random_name_picker_tool()
        elif tool_choice == 4:
            random_quote_generator_tool()
        elif tool_choice == 5:
            accounts_tool()
        else:
            print("Sorry, that tool is not available.")

        repeat_choice = input("Do you want to do something again? (y/n): ")
        if repeat_choice.lower() != "y":
            break

if __name__ == "__main__":
    main()
