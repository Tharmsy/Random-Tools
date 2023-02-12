import random
import os
import webbrowser

tools = ["Folder Maker", "Discord Promotion", "Random Name Picker", "Code Formatter"]

print("Random Tools:")
for i, tool in enumerate(tools):
    print(f"{i+1}. {tool}")

tool_choice = int(input("Enter the number of the tool you want to use: "))

if tool_choice == 1:
    num_folders = int(input("How many folders do you want to create? "))
    folder_name = input("Enter the name of the folder: ")
    folder_location = input("Enter the file location to create the folder(s): ")
    for i in range(num_folders):
        os.mkdir(os.path.join(folder_location, f"{folder_name}_{i+1}"))
        print(f"Created folder {folder_name}_{i+1} at {folder_location}")

elif tool_choice == 2:
    discord_link = "https://discord.gg/your_server_code"
    webbrowser.open(discord_link)

else:
    print("Sorry, that tool is not available.")
