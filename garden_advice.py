# Hardcoded values for the season and plant type
season = input("plase enter 'summer' or 'winter': ")
plant_type = input("Please enter 'flower' or 'vegetable': ")

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
'''
This block of code determines what season the user has chosen and adds the string to the "advice" varible.
'''
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
elif season == 'autumn':
    advice += 'This a great growing type for fruits and vegetables make sure they recive the nutrients they need\n'
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
'''
This block of code determines what type of plant the user has chosen and adds the string to the "advice" varible.
'''
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
