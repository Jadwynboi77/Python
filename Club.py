print("Welcome!")

# Name---------------------------------------------------------------------------------------------------------------
NameF = "" # name >>F<< means Name_>>First<<-------------------------------------------------------------------------
while NameF == "":
    NameF = input("Please enter your first name: ")
NameF = NameF.lower()

# age and confirmation -----------------------------------------------------------------------------------------------

print('age MUST be inbetween 12 and 17')
try:
    Age = int(input("Please enter your age: "))
    if Age < 12:
        print("Sorry, you are too young.")
        exit()
    elif Age > 17:
        print("Sorry, you are too old.")
        exit()
# if there is an exception, print this out
except ValueError:
  print("That's not a valid number!")
  
#Creating the list---------------------------------------------------------------------------------------------------
meal_list = ["strandard","Vegetarian","Dairy-free","No meal"]
Activity_list = ["Music jam Session","science experiments","Sports leadership training"]
Other_list = ["bypass",2,3,4,"easy","moderate","challenging","$5 fee","$10 fee","$12 fee"]
fee_list = [5,10,12]
#the bypass allows this list to start at 1, instead of starting at 0-------------------------------------------------

#Creating the Varibables---------------------------------------------------------------------------------------------
mealfee = 7

#Printing the activity list------------------------------------------------------------------------------------------
def activity_lists():
    print('Please choose an activity')
    print(f"1. {Activity_list[0]} ({Other_list[0]} hours, {Other_list[3]}, {Other_list[6]})")
    print(f"2. {Activity_list[1]} ({Other_list[1]} hours, {Other_list[4]}, {Other_list[7]})")
    print(f"3. {Activity_list[2]} ({Other_list[2]} hours, {Other_list[5]}, {Other_list[8]})")
   

#Printing the meal list----------------------------------------------------------------------------------------------
def meal_Lists():
    print("Meal options:")
    print(f'1. {meal_list[0]}.')
    print(f'2. {meal_list[1]}.')
    print(f'3. {meal_list[2]}.')
    print(f'4. {meal_list[3]}.')

#activity list loop--------------------------------------------------------------------------------------------------
activity_lists() #---- options for activites ---------------------------------------------------------------------
ask1 = "" #starting a while loop----------------------------------------------------------------------------------
while ask1 == "":
    ask1 = int(input("Enter the number of your chosen activity: "))
    if ask1 == 0:
        ask1 = ""
        print("please choose option 1, 2, or 3")
    elif ask1 >= 4:
        ask1 = ""
        print("please choose option 1, 2, or 3")

#meal list loop--------------------------------------------------------------------------------------------------
meal_Lists() #---- options for Meals -----------------------------------------------------------------------------
ask2 = ""
while ask2 == "":
    ask2 = int(input("Enter the number of your meal choice: ")) #asking user what meal they want----------------------
    if ask2 == 0:
        ask2 = ""
        print("please choose option 1, 2, 3 or 4")
    elif ask2 >= 5:
        ask2 = ""
        print("please choose option 1, 2, 3 or 4")

#Calculating the results----------------------------------------------------------------------------------------------

if ask2 == 4: #if user selects no meal----------------------------------------------------------------------------------
    mealfee = 0 #this here is to make sure that incase they dont select a meal, it wont create an error-----------------

overall_fee = fee_list[ask1 - 1] + mealfee #adds all the addition fees together for the overall cost-----------------------------------

#Printing the results---------------------------------------------------------------------------------------------------
print(f'{NameF}, age {Age}, has chosen {Activity_list[ask1 - 1]}, alongside a meal option of: {meal_list[ask2 - 1]}')
if ask2 == 4:
    print("there will not be a meal cost since you have not chosen one.")
else: print("Your meal will add an additional $7,")
print("the following activity will include:")
print(f"{Other_list[ask1]} hours of practice, It's {Other_list[ask1 + 3]} and a {Other_list[ask1 + 6]}")
print(f"overall, the total cost comes to ${overall_fee}.")

#Asking for attendence--------------------------------------------------------------------------------------------------

attend = input("Are you going to be attending?(Yes or no): ")
if attend == "yes":
    print(f"{NameF} has comfirmed for {Activity_list[ask1]}, see you there!")
elif attend == "no":
    print(f"{NameF} has not comfirmed for {Activity_list[ask1]}.")
    exit()