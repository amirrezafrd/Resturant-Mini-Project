# Restaurant Menu Management System
# Uses restaurant_menu.txt file in CSV format

import os
import csv
import sys

FILE_NAME = "restaurant_menu.txt"
DELIMITER = ","

def initialize_file():
    """Create the file with header if it doesn't exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Dish Name", "Description", "Price", "Category"])

def read_all_dishes():
    """Read and return all dishes as list of dictionaries"""
    dishes = []
    if not os.path.exists(FILE_NAME):
        return dishes
        
    with open(FILE_NAME, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dishes.append(row)
    return dishes

def dish_exists(dish_name):
    """Check if a dish with given name already exists (case insensitive)"""
    dishes = read_all_dishes()
    for dish in dishes:
        if dish["Dish Name"].strip().lower() == dish_name.strip().lower():
            return True
    return False

def add_dish():
    """Add a new dish to the menu"""
    print("\n--- Add New Dish ---")
    
    name = input("Enter dish name: ").strip()
    if not name:
        print("Dish name is required!")
        return
        
    if dish_exists(name):
        print("Error: A dish with this name already exists!")
        return
        
    description = input("Enter description (optional): ").strip()
    price_input = input("Enter price (integer in Rials): ").strip()
    category = input("Enter category (optional): ").strip()
    
    try:
        price = int(price_input)
        if price <= 0:
            print("Price must be a positive number!")
            return
    except ValueError:
        print("Price must be a valid integer!")
        return
    
    new_row = [name, description, str(price), category]
    
    with open(FILE_NAME, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
        
    print(f"Dish '{name}' added successfully!")

def show_all_dishes():
    """Display all dishes in a nice format"""
    dishes = read_all_dishes()
    
    if not dishes:
        print("\nNo dishes found in the menu.")
        return
        
    print("\n--- All Dishes ---")
    print("-" * 70)
    print(f"{'Name':<25} {'Price':>10} {'Category':<20} Description")
    print("-" * 70)
    
    for dish in dishes:
        desc = dish["Description"][:40] + "..." if len(dish["Description"]) > 40 else dish["Description"]
        print(f"{dish['Dish Name']:<25} {dish['Price']:>10} {dish['Category']:<20} {desc}")
    print("-" * 70)

def search_dish():
    """Search dishes by name or category"""
    print("\n--- Search Dish ---")
    print("1. Search by name")
    print("2. Search by category")
    choice = input("Choose (1/2): ").strip()
    
    query = input("Enter search term: ").strip().lower()
    if not query:
        print("Search term cannot be empty!")
        return
    
    dishes = read_all_dishes()
    results = []
    
    for dish in dishes:
        if choice == "1":
            if query in dish["Dish Name"].lower():
                results.append(dish)
        elif choice == "2":
            if query in dish["Category"].lower():
                results.append(dish)
        else:
            print("Invalid choice!")
            return
    
    if not results:
        print("No matching dishes found.")
        return
        
    print(f"\nFound {len(results)} matching dish(es):")
    print("-" * 70)
    for dish in results:
        print(f"{dish['Dish Name']} | {dish['Price']} Rials | {dish['Category']}")
        if dish["Description"]:
            print(f"   → {dish['Description']}")
        print("-" * 70)

def update_dish():
    """Update an existing dish"""
    print("\n--- Update Dish ---")
    name = input("Enter dish name to update: ").strip()
    
    if not dish_exists(name):
        print("Dish not found!")
        return
    
    dishes = read_all_dishes()
    updated_dishes = []
    found = False
    
    print("Leave field empty to keep current value")
    
    for dish in dishes:
        if dish["Dish Name"].strip().lower() == name.strip().lower():
            found = True
            print(f"\nCurrent: {dish['Dish Name']} | {dish['Price']} | {dish['Category']}")
            
            new_name = input("New name (or Enter to keep): ").strip()
            new_desc = input("New description (or Enter): ").strip()
            new_price_input = input("New price (or Enter): ").strip()
            new_category = input("New category (or Enter): ").strip()
            
            dish["Dish Name"] = new_name if new_name else dish["Dish Name"]
            dish["Description"] = new_desc if new_desc else dish["Description"]
            dish["Category"] = new_category if new_category else dish["Category"]
            
            if new_price_input:
                try:
                    price = int(new_price_input)
                    if price > 0:
                        dish["Price"] = str(price)
                    else:
                        print("Invalid price - keeping old value")
                except ValueError:
                    print("Invalid price - keeping old value")
                    
        updated_dishes.append(dish)
    
    if not found:
        print("Dish not found!")
        return
    
    # Write back all dishes
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Dish Name", "Description", "Price", "Category"])
        writer.writeheader()
        writer.writerows(updated_dishes)
        
    print("Dish updated successfully!")

def delete_dish():
    """Delete a dish by name"""
    print("\n--- Delete Dish ---")
    name = input("Enter dish name to delete: ").strip()
    
    if not dish_exists(name):
        print("Dish not found!")
        return
    
    dishes = read_all_dishes()
    updated_dishes = [d for d in dishes if d["Dish Name"].strip().lower() != name.strip().lower()]
    
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Dish Name", "Description", "Price", "Category"])
        writer.writeheader()
        writer.writerows(updated_dishes)
        
    print(f"Dish '{name}' deleted successfully!")

def main():
    initialize_file()
    
    while True:
        print("\n" + "="*40)
        print("  RESTAURANT MENU MANAGEMENT SYSTEM  ")
        print("="*40)
        print("1. Add new dish")
        print("2. Show all dishes")
        print("3. Search dish")
        print("4. Update dish")
        print("5. Delete dish")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-5): ").strip()
        
        if choice == "1":
            add_dish()
        elif choice == "2":
            show_all_dishes()
        elif choice == "3":
            search_dish()
        elif choice == "4":
            update_dish()
        elif choice == "5":
            delete_dish()
        elif choice == "0":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()