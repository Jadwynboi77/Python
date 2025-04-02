print("Welcome!")

# Name----------------------------------------------------------------------------------------------------------------

NameF = input("Please enter your first name: ")
NameF = NameF.lower()

# age and confirmation -----------------------------------------------------------------------------------------------

AgeConfirm = False 
print('age MUST be inbetween 12 and 17')
Age = int(input("Please enter your age: "))
if Age >= 12 and Age <= 17: 
    AgeConfirm == True
elif Age < 12:
    print("Sorry, you are too young.")
    quit
elif Age > 17:
    print("Sorry, you are too old.")
    quit

#Creating the list----------------------------------------------------------------------------------------------------
meal_list = ["strandard","Vegetarian","Dairy-free","No meal"]
Activity_list = ["Music jam Session","science experiments","Sports leadership training"]
Other_list = [2,3,4,"easy","moderate","challenging","$5 fee","$10 fee","$12 fee"]

#Creating the Varibables----------------------------------------------------------------------------------------------

list_cutO = 0 #------------- the amount of hours ---------------------------------------------------------------------
list_cutT = 0 #------------- the difficulty of the activity-----------------------------------------------------------
list_cutTH = 0 #------------- the cost of the fee---------------------------------------------------------------------
fee = 5
mealfee = 7

#Printing the activity list-------------------------------------------------------------------------------------------
def activity_lists():
    print('Please choose an activity')
    print(f"1. {Activity_list[0]} ({Other_list[0]} hours, {Other_list[3]}, {Other_list[6]})")
    print(f"2. {Activity_list[1]} ({Other_list[1]} hours, {Other_list[4]}, {Other_list[7]})")
    print(f"3. {Activity_list[2]} ({Other_list[2]} hours, {Other_list[5]}, {Other_list[8]})")
   

#Printing the meal list-----------------------------------------------------------------------------------------------
def meal_Lists():
    print("Meal options:")
    print(f'1. {meal_list[0]}.')
    print(f'2. {meal_list[1]}.')
    print(f'3. {meal_list[2]}.')
    print(f'4. {meal_list[3]}.')
    

#Printing all of the list----------------------------------------------------------------------------------------------
if AgeConfirm == True:
    activity_lists()
    ask1 = input("Enter the number of your chosen activity: ")
    meal_Lists()
    ask2 = int(input("Enter the number of your meal choice: ")) #asking user what meal they want----------------------

#Calculating the results----------------------------------------------------------------------------------------------


if ask1 == '1': #if user selects music--------------------------------------------------------------------------------
    list_count = 0
    list_cutO = list_count 
    list_cutT = list_cutO + 3 #-------------3 for the layout of the List "Other"--------------------------------------
    list_cutTH = list_cutT + 3
elif ask1 == '2': #if user selects Science----------------------------------------------------------------------------
    list_count = 1
    list_cutO = list_count
    list_cutT = list_cutO + 3 
    list_cutTH = list_cutT + 3
    fee = fee + 5
elif ask1 == '3': #if user selects sports------------------------------------------------------------------------------
    list_count = 2
    list_cutO = list_count
    list_cutT = list_cutO + 3
    list_cutTH = list_cutT + 3
    fee = fee + 7


if ask2 == 4: #if user selects no meal----------------------------------------------------------------------------------
    mealfee = 0

overall_fee = fee + mealfee

#Printing the results---------------------------------------------------------------------------------------------------
if AgeConfirm == True:
    print(f'{NameF}, age {Age}, has chosen {Activity_list[list_count]}, alongside a meal option of: {meal_list[ask2 - 1]}')
    print("the following activity will include:")
    print(f"{Other_list[list_cutO]} hours of practice, It's {Other_list[list_cutT]} and a {Other_list[list_cutTH]}")
    print(f"overall, the total cost comes to ${overall_fee}.")

#Asking for attendence--------------------------------------------------------------------------------------------------
if AgeConfirm == True:
    attend = input("Are you going to be attending?(Yes or no): ")
    if attend == "yes":
        print(f"{NameF} has comfirmed for {Activity_list[list_count]}, see you there!")
    elif attend == "no":
        print(f"{NameF} has not comfirmed for {Activity_list[list_count]}.")