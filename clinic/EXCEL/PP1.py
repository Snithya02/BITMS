import pandas as pd

# Read the Excel file


# Ask user for ID number
# id_number = int(input("Enter ID number: "))
def add_id(id_number):
    df = pd.read_excel('progress.xlsx')
    # Append a new row with the ID numbers
    new_row = {'ID': id_number}
    df = df._append(new_row, ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel('progress.xlsx', index=False)
