# Restaurant Menu Management System ( Final mini project of the teacher Pourreza )

A simple command-line Python application for managing a restaurant menu.  
All data is stored in a CSV file (`restaurant_menu.txt`).

## Features

- Add new dishes
- View all dishes in a formatted table
- Search dishes by name or category
- Update existing dish information
- Delete dishes
- Case-insensitive dish name checking (prevents duplicates)
- Persistent storage using CSV file
- Automatic file & header creation

## Technologies

- Python 3.x
- Built-in modules only: `os`, `csv`, `sys`

## Project Structure
restaurant-menu-management/
├── main.py               # Main program file
├── restaurant_menu.txt   # Data file (auto-created on first run)
└── README.md

## Installation & Usage

1. Make sure you have **Python 3** installed
2. Download or clone the repository
3. Navigate to the project folder
4. Run the program:

python main.py
# or
python3 main.py

Main Menu :
========================================
  RESTAURANT MENU MANAGEMENT SYSTEM  
========================================
1. Add new dish
2. Show all dishes
3. Search dish
4. Update dish
5. Delete dish
0. Exit

Enter your choice (0-5):


<img width="368" height="242" alt="image" src="https://github.com/user-attachments/assets/7b73fea8-8fe5-4b15-95b8-a4adf999869e" />


Important Notes

Prices must be positive integers (in Rials)
Dish names are not case-sensitive
The file restaurant_menu.txt is created automatically if it doesn't exist
When updating, leave a field empty to keep the current value

Example of restaurant_menu.txt content :

Dish Name,Description,Price,Category
Ghormeh Sabzi,Traditional Persian herb stew with meat,185000,Stew
Kebab Koobideh,Fresh minced meat kebab,220000,Kebab.

Lightweight menu management system suitable for small restaurants or learning purposes.

Just select all the text above (including the ```markdown:disable-run
Good luck with your project! 🚀
