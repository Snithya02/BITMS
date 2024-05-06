import pandas as pd
def pa(id_number, progress_value):
    # Read the progress Excel file
    df_progress = pd.read_excel('progress.xlsx')

    # Read the athlete data Excel file
    df_athlete = pd.read_excel('athlete_data.xlsx')

    # Check if the ID is present in the athlete data
    if id_number in df_athlete['Id'].values:
        # Get the index of the athlete record
        record_index = df_athlete[df_athlete['Id'] == id_number].index[0]
        
        # Increment the count for the athlete
        count = df_athlete.loc[record_index, 'Count'] + 1
        df_athlete.loc[record_index, 'Count'] = count
        
        progress_value = float(progress_value)
        # Update the progress value in the progress DataFrame
        df_progress.loc[df_progress['ID'] == id_number, f'Progress{count}'] = progress_value
    else:
        print(f"Athlete ID {id_number} not found in athlete_data.xlsx")

    # Save the updated progress DataFrame back to the Excel file
    df_progress.to_excel('progress.xlsx', index=False)
    df_athlete.to_excel('athlete_data.xlsx', index=False)