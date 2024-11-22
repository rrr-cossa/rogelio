import csv

def read_csv(filename):
    accidents_dictionary = {}
    with open(filename, mode='r', newline = "") as file:
        reader = csv.reader("accidents.csv")
        next(reader)
        for row in reader:
            Year = row[0]
            Fatalities = row[1]
            Injuries = row[2]
            Crashes = row[3]
            Fatal_Crashes = row[4]
            Distraction_Affected_Fatal_Crashes = row[5]
            Fatal_Crashes_involving_Cell_Phone_Use = row[6]
            Fatal_Crashes_involving_Excessive_Speed = row[7]
            Fatal_Crashes_while_Driving_under_the_Influence= row[8]
            Fatal_Crashes_involving_Fatigue_or_Illness = row[9]
            accidents_dictionary[Year]= [Fatalities, Injuries, Crashes, Fatal_Crashes, Distraction_Affected_Fatal_Crashes, Fatal_Crashes_involving_Cell_Phone_Use, Fatal_Crashes_involving_Excessive_Speed, Fatal_Crashes_while_Driving_under_the_Influence, Fatal_Crashes_involving_Fatigue_or_Illness]
    return accidents_dictionary

def display_columns(columns):
    print("\nAvailable Columns:")
    for index, column in enumerate(columns, 1):
        print(f"{index}. {column}")
    print()
    
def main():
    filename = 'accidents.csv'
    accidents_dictionary = read_csv(filename)
    
    if not accidents_dictionary:
        print("No data found in the CSV file.")
        return
    year = input("Enter a year to search for: ").strip()
    if year not in accidents_dictionary:
        print(f"No data found for the year {year}.")
        return
    
    columns = list(accidents_dictionary[year].keys())
    
    display_columns(columns)
    
    column_choice = input(f"Enter a column number (1-{len(columns)}): ").strip()
    try:
        column_choice = int(column_choice)
        if column_choice < 1 or column_choice > len(columns):
            raise ValueError("Invalid choice.")
        
        column_name = columns[column_choice - 1]
        print(f"Data for the year {year}, column '{column_name}': {accidents_dictionary[year][column_name]}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()