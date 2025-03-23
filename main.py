# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls
class DunnDelivery:
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        #Menu attribute = menu of items you can order to be delivered:
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Horchata", "Chai", "Espresso shot"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        #Prices are encapsulated within the class:
        #initialize it right now, assign in values
        #using a dictionary, there is a single key and single value
        self.prices = {
            "Monster" : 3.99, 
            "Rockstar": 3.99, 
            "Latte": 4.99,
            "Cappuccino": 4.99,
            "Horchata": 3.99,
            "Chai": 4.99,
            "Espresso shot": 2.99,
            "Bagel": 2.99,
            "Muffin": 2.99,
            "Scone": 2.99,
            "Falafel Wrap": 8.99,
            "Hummus & Pita": 7.99,
            "Chicken Wrap": 8.99
        }

        #Add a dictionary of the delivery locations and number minutes to deliver to that location
        #use keyword self, because delivery_locations is an attribute of the class
        #key-value pairs, key is location, value is number of minutes to that location
        self.delivery_locations = {
            #number of minutes to deliver:
            "Library": 10, 
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    #Show the menu of items available for delivery
    # Create a new method using def
    #category is set to none by default
    def show_menu(self, category = None):   
        #if there is a category value chosen, print items in category:
        if category: 
            print(f"\n=== {category} ===")     
            #Loop through items in category on the menu, display them to the user:
            #use for loop, predefined number of items
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            #show the entire menu if they haven't specified a category
            for category in self.menu:
                #show the category name:
                print(f"\n=== {category} ===")
                #nest a second for loop, to go through each item within the category
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
    #Method to calculate the total cost of the order:
    #set false as default

    def calculate_total(self, items, has_student_id=False):
        #Calculate the total 
        total = sum(self.prices[item] for item in items)
            
        #calculate the student discount based on the student id  
        #if has_student_id = True and total is more than 10
        if has_student_id and total > 10:
            total *= 0.9

        #this method returns the total cost of the order to the code that called the method
        return total;  
    
    #Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour):
        #Calculate the base time for the delivery (get base time from the dictionary)
        base_time = self.delivery_locations[location]

        #Calculate the delivery time based on the time of day (adjust for busy time of day)
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        
        #if they aren't ordering during a busy time, return the base_time with no adjustment
        return base_time

    #Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id = False):
        #display the order information
        print("\n === Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")

        #Loop through the list of menu items they ordered:
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        #Call the methods to get the total cost and the delivery time
        total = self.calculate_total(items, has_student_id);

        #new variable:
        delivery_time = self.estimate_delivery(location, current_hour)

        #Display the subtotal
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")

        #Calculate the total with the discount if the customer has a student id:
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student discount applied!")

        #Display the total after discount and the estimated delivery time:
        print(f"Total after discount: ${total:.2f}") 
        print(f"Estimated delivery time: {delivery_time} minutes")   

    #Part 2:Individual exercise: Create a rate_delivery method that lets customers rate 
    # their delivery (1-5 stars)
    def rate_delivery(self, location, items, numberOfStars = None):
        #make sure the location and items are not empty:
        if location and items:
            if numberOfStars is None:
                #ask the customer to rate their delivery experience
                try:
                    numberOfStars = int(input("Please rate your delivery experience (1-5 stars): "))
                except ValueError:
                    print("Please enter a valid number of stars (1-5)")
                    return   

            # numberOfStars = input(int()) (would need to actually ask the customer, but using example data for this)
            #TODONE ^^above add error handling for invalid (non numerical/integer) input

        if numberOfStars >= 1 and numberOfStars <= 5:
            print(f"Rating: {numberOfStars} stars")
        else: 
            print("Please enter a valid number of stars (1-5) ")
            return
        
        #priority_delivery = False by default:
    def add_priority_delivery(self, location, items, current_hour, priority_delivery=False):
        #add $2 to the total cost
        #subtract 3 minutes from the delivery time
        #delivery time can't be less than zero, so the initial estimate_delivery needs to be greater than 3

        #1. Get regular delivery time: 
        regular_time = self.estimate_delivery (location, current_hour)
        regular_total = self.calculate_total(items)

        if priority_delivery:
            #If > 3 minutes, can decrease delivery time, otherwise can't
            if regular_time > 3:
                priority_time = (regular_time - 3)
            else: 
                priority_time = regular_time

            #2. Add $2.00 to the total cost
            priority_total = regular_total + 2.00
            print(f"Priority delivery added! + $2.00")
            print(f"You delivery time is reduced from {regular_time} to {priority_time} minutes")   

            return priority_total, priority_time

        return regular_total, regular_time   

#Main method will be executed as soon as the program runs
def main():
    #Create a new delivery object **Instantiating a new object here
    #=calling the constructor for the dunn delivery class
    delivery = DunnDelivery()

    #Show the menu
    delivery.show_menu("Coffee Drinks")

    #Sample order at 9:30am (peak morning hour)
    order = ["Latte", "Bagel"]
    location = 'ITEC Computer Lab'
    current_hour = 9
    has_student_id = True

    #Display the receipt for the order
    delivery.print_order(location, order, current_hour, has_student_id);

    #Ask if customer wants priority delivery
    # Add priority delivery of the order (cost $2, but reduces delivery time by 3 minutes)
    #user app for real would ask for input
    #priority_choice = input("Would you like priority delivery for $2.00? (y/n): ").lower() == 'y'
    priority_choice = True #to test, use True instead of constantly putting in y/n

    if priority_choice:
        #TODO this was Dr. Mary's code but it doesn't produce the results I expect and I don't understand why
        #the new_total, new_time is used. The updated delivery time AND the estimated delivery time are the same

        #Start up priority delivery, add $2 and reduce delivery time
        new_total, new_time = delivery.add_priority_delivery(location, order, current_hour)
        print(f"Updated total: ${new_total:.2f}")
        print(f"Updated delivery time: {new_time} minutes")

    #Ask for a rating from the customer: 
    delivery.rate_delivery(location, order, 5)

#Add the line of code to automatically call the main method
if __name__ == "__main__":
    main()
