#!/usr/bin/env python3
"""
Montana License Plate County Lookup Program

This program allows users to look up Montana county information based on
the license plate prefix number. Users can specify what information to 
display (county name, seat city, or both) and make multiple queries.

Data Structure Choice:
- Dictionary with prefix as key: O(1) lookup time - optimal for this use case
- If lookup was by county name instead, we'd use a different dictionary with 
  county name as the key (still O(1))
"""

import csv
import sys


def load_county_data(filename):
    """
    Load county data from CSV file into a dictionary.
    
    Args:
        filename: Path to the CSV file containing county data
        
    Returns:
        Dictionary mapping prefix number (int) to tuple of (county_name, seat_city)
        
    Data Structure: Dictionary chosen for O(1) lookup performance.
    Key is the license plate prefix (integer), value is a tuple of (county, seat).
    """
    county_dict = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # skip header
            next(reader)

            for row in reader:
                county = row[0]
                seat = row[1]
                prefix = int(row[2])
                county_dict[prefix] = (county, seat)
        print(f"Successfully loaded!")
        return county_dict
        
    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        print("Please ensure the MontanaCounties.csv file is in the same directory.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: CSV file is missing expected column: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid data in CSV file: {e}")
        sys.exit(1)

def ask_display_preference():
    """
    Ask user what information they want to see in query results.
    
    Returns:
        String indicating display preference: 'both', 'county', or 'seat'
    """
    print("What information would you like to display?")
    print("  1. Both county name and seat city (default)")
    print("  2. County name only")
    print("  3. Seat city only")
    
    while True:
        choice = input("\nEnter your choice (1-3) or press Enter for default: ").strip()
        
        if choice == '' or choice == '1':
            return 'both'
        elif choice == '2':
            return 'county'
        elif choice == '3':
            return 'seat'
        else:
            print("Invalid choice. Please enter 1, 2, 3, or press Enter.")

def display_result(prefix, county_data, display_preference):
    """
    Display the lookup result based on user's display preference.

    Args:
        prefix: License plate prefix number
        county_data: Tuple of (county_name, seat_city)
        display_preference: What to display ('both', 'county', or 'seat')
    """
    county_name, seat_city = county_data

    print(f"\n{'=' * 60}")
    print(f"License Plate Prefix: {prefix}")
    print('-' * 60)

    if display_preference == 'both':
        print(f"County:      {county_name}")
        print(f"County Seat: {seat_city}")
    elif display_preference == 'county':
        print(f"County: {county_name}")
    elif display_preference == 'seat':
        print(f"County Seat: {seat_city}")

    print('=' * 60)

def lookup_county(county_dict, display_preference):
    """
    Main lookup loop - allows user to query multiple license plate prefixes.
    
    Args:
        county_dict: Dictionary mapping prefix to (county, seat) tuples
        display_preference: User's display preference
    """
    print("\n" + "="*60)
    print("Montana License Plate County Lookup")
    print("="*60)
    print("\nInstructions:")
    print("  • Enter a license plate prefix number (1-56) to look up county info")
    print("  • Type 'exit' to quit the program")
    print("  • Type 'change' to modify display preferences")
    print("="*60)
    
    while True:
        user_input = input("\nEnter license plate prefix number: ").strip().lower()
        
        # Check for exit commands
        if user_input== 'exit':
            print("\n See ya!")
            break
        
        # Check for display preference change
        if user_input == 'change':
            display_preference = ask_display_preference()
            print(f"\nDisplay preference updated!")
            continue
        
        # Try to parse as integer
        try:
            prefix = int(user_input)
            
            # Look up the prefix in our dictionary
            if prefix in county_dict:
                display_result(prefix, county_dict[prefix], display_preference)
            else:
                print(f"\nPrefix {prefix} not found in database.")
                print(f"   Valid prefixes are 1-56.")
                print(f"   Please check the license plate number and try again.")
                
        except ValueError:
            print(f"\nInvalid input: '{user_input}' is not a valid number.")
            print("   Please enter a numeric prefix or 'exit' to quit.")

def main():
    """Main program entry point."""
    # Path to the CSV file
    csv_filename = 'MontanaCounties.csv'
    
    print("\n" + "="*60)
    print("Montana License Plate County Lookup System")
    print("="*60)
    print()
    
    # Load county data from CSV file
    county_dict = load_county_data(csv_filename)
    
    # Get user's display preference
    display_pref = ask_display_preference()
    
    # Run the lookup loop
    lookup_county(county_dict, display_pref)


if __name__ == "__main__":
    main()
