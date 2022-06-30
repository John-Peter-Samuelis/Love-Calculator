username    = input("Enter your name: ")
crush_name  = input("Enter your crush's name: ") 

combined_names = username + crush_name
combined_names = combined_names.lower()


total_count_true    = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e") 
total_count_love    = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + username.count("e")

love_percentage         = str(total_count_true) + str(total_count_love)    
converted_love_percentage = int(love_percentage)

if converted_love_percentage < 10 or converted_love_percentage > 90:
    print (f"Your score is {love_percentage}, you go together like coke and mentos.")
elif converted_love_percentage >= 40 and converted_love_percentage <= 50:
    print (f"Your score is {love_percentage}, you are alright")
else:
    print(f"You are {love_percentage}% compatible")
