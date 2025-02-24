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
        #use keyword self, because 
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
    def rate_delivery(self, numberOfStars = None):
        if 

#Main method will be executed as soon as the progrm runs
def main():
    #Create a new delivery object **Instantiating a new object here
    #=calling the constructor for the dunn delivery class
    delivery = DunnDelivery()

    #Show the menu
    delivery.show_menu("Coffee Drinks")

    #Sample order at 9:30am (peak morning hour)
    order = ["Latte", "Bagel"]

    #Display the receipt for the order
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True);

#Add the line of code to automatically call the main method
if __name__ == "__main__":
    main()
