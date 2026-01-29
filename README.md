# Montana License Plate County Lookup

## Overview
This program allows users to look up Montana county information based on license plate prefix numbers. It demonstrates file I/O, data structure selection, and user interaction principles.

## Features
- ✅ Load county data from CSV file into memory
- ✅ Look up county information by license plate prefix
- ✅ Multiple queries without restarting the program
- ✅ Configurable output (county name, seat city, or both)
- ✅ User-friendly interface with clear instructions
- ✅ Error handling for invalid inputs
- ✅ Clean exit with "exit"

## Usage

### Basic Usage
```bash
python montana_plate_lookup.py
```

### Example Session
```
Montana License Plate County Lookup System
============================================================

✓ Successfully loaded 56 counties from MontanaCounties.csv

What information would you like to display?
  1. Both county name and seat city (default)
  2. County name only
  3. Seat city only

Enter your choice (1-3) or press Enter for default: 1

============================================================
Montana License Plate County Lookup
============================================================

Instructions:
  • Enter a license plate prefix number (1-56) to look up county info
  • Type 'quit', 'exit', or 'q' to exit the program
  • Type 'change' to modify display preferences
============================================================

Enter license plate prefix number: 1

============================================================
License Plate Prefix: 1
------------------------------------------------------------
County:      Butte-Silver Bow
County Seat: Butte
============================================================

Enter license plate prefix number: 5

============================================================
License Plate Prefix: 5
------------------------------------------------------------
County:      Lewis & Clark
County Seat: Helena
============================================================

Enter license plate prefix number: quit

Thank you for using the Montana License Plate Lookup!
Safe travels! 🚗
```

## Design Decisions

### 1. Data Structure Choice: Dictionary (Hash Map)

**For prefix-based lookup (current implementation):**
```python
county_dict = {
    1: ("Butte-Silver Bow", "Butte"),
    5: ("Lewis & Clark", "Helena"),
    12: ("Hill", "Havre"),
    ...
}
```

**Why a dictionary?**
- **O(1) lookup time** - Constant time complexity, regardless of dataset size
- **Direct access** - No need to iterate through data
- **Memory efficient** - Small overhead for 56 counties
- **Perfect for key-value lookups** - Prefix is a unique identifier

**Alternative: If lookup was by county name:**
```python
county_name_dict = {
    "Butte-Silver Bow": (1, "Butte"),
    "Lewis & Clark": (5, "Helena"),
    "Hill": (12, "Havre"),
    ...
}
```
Still O(1), just with a different key!

**Rejected alternatives:**
- **List of tuples** - O(n) lookup time, must search sequentially
- **List of lists** - Same problem, O(n) complexity
- **Sorted list + binary search** - O(log n), but unnecessary complexity
- **Database** - Overkill for 56 records

### 2. File Reading Strategy

The program reads the entire CSV file into memory at startup:

**Advantages:**
- Fast lookups after initial load (no disk I/O during queries)
- Simple implementation
- Suitable for small datasets (56 counties)
- Data validated once at load time

**Trade-offs:**
- Entire file in memory (minimal impact for this size)
- Changes to CSV require program restart
- For very large datasets (millions of records), might need different approach

### 3. User Experience Features

**Multiple queries:** 
- Infinite loop until user types 'quit'
- No need to restart program

**Flexible exit:**
- Multiple exit keywords: 'quit', 'exit', 'q'
- Case-insensitive

**Configurable display:**
- Choose what information to see
- Can change preference without restarting
- Type 'change' during queries

**Error handling:**
- Invalid prefix numbers (not in range)
- Non-numeric input
- Missing CSV file
- Malformed CSV data

## How It Addresses the Challenge Requirements

### ✅ Read file and store in memory
- `load_county_data()` function reads CSV using Python's csv module
- Stores data in dictionary for instant access

### ✅ User provides county number, get county name and seat
- `lookup_county()` accepts user input
- `display_result()` shows the information

### ✅ Allow multiple queries
- While loop continues until user explicitly quits
- No need to restart program

### ✅ Exit on specific input
- 'quit', 'exit', or 'q' terminates the program cleanly

### ✅ Extra Challenge: Configurable output
- User chooses at startup what to display
- Can change preference during runtime with 'change' command
- Options: both, county only, or seat only

## Code Structure

```
montana_plate_lookup.py
│
├── load_county_data()      # File I/O and data loading
├── get_display_preference() # User preference configuration
├── display_result()         # Formatted output display
├── lookup_county()          # Main query loop
└── main()                   # Program entry point
```

## Learning Points

1. **File I/O**: Reading CSV files with Python's csv module
2. **Data Structures**: Choosing the right structure for O(1) lookup
3. **User Interaction**: Building an interactive command-line interface
4. **Error Handling**: Graceful handling of invalid inputs
5. **Code Organization**: Breaking functionality into logical functions
6. **Extensibility**: Easy to modify for future requirements

## Preparing for the Next Challenge

This program provides a solid foundation for future enhancements:
- ✅ Data is loaded into memory (efficient for modifications)
- ✅ Dictionary structure makes it easy to add new lookup methods
- ✅ Modular design allows adding new features without major rewrites
- ✅ Error handling framework in place for validation

## Files Required

- `montana_plate_lookup.py` - Main program file
- `MontanaCounties.csv` - County data file (must be in same directory)

## CSV File Format

```csv
County,County Seat,License Plate Prefix
Butte-Silver Bow,Butte,1
Lewis & Clark,Helena,5
...
```

## Testing the Program

Test cases to verify functionality:
1. Valid prefix (1, 5, 12) - should display correct county info
2. Invalid prefix (99, 0, -1) - should show error message
3. Non-numeric input ("abc", "!@#") - should show error message
4. Empty input (just Enter) - should show error message
5. Exit commands (quit, exit, q) - should exit cleanly
6. Display preferences - verify all three modes work
7. Change command - verify can switch display modes

## Python Version

This program is compatible with Python 3.6+

## Author Notes

This solution prioritizes:
- **Clarity**: Easy to understand code with comments
- **Efficiency**: O(1) lookup using dictionary
- **User Experience**: Clear prompts and error messages
- **Extensibility**: Easy to add new features
- **Best Practices**: Proper error handling, documentation, modular design
