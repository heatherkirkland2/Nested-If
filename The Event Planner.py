#Objective: To practice the use of shorthand if statements.

#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, 
# but it has errors. Identify and fix them.

#Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)



#Task 2: Venue Selection

#Based on the corrected code from Task 1, further enhance your code to recommend additional things 
# like "audio system" or "projector" based on the number of attendees.


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

additional = "audio system" if attendees > 50 else "projector"
print(f"Recommended: {additional}")

#Task 3: Catering Choices

#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, 
# otherwise recommend "Gourmet Meals Caterers".


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

additional = "audio system" if attendees > 50 else "projector"
print(f"Recommended: {additional}")

vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(f"Recommended Caterer: {caterer}")
