import streamlit as st
import pandas as pd
from datetime import datetime
from EXCEL import PP1,pp2
import matplotlib.pyplot as plt

# Load Excel file
@st.cache(allow_output_mutation=True)
def load_data():
    try:
        df = pd.read_excel('athlete_data.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Id', 'Name', 'Age', 'Gender', 'Weight', 'Height', 'Sport', 'Reason', 'Date', 'Time', 'Count'])
    return df

# Display the CRUD interface
st.title('Athlete Clinic Management System')
menu = st.sidebar.selectbox('Menu', ['Create Record', 'Read Records', 'Update Record', 'Delete Record', 'Manage Medical Appointment','Track Health and Recovery Progress'])

if menu == 'Create Record':
    st.subheader('Add New Record')
    athlete_id = st.text_input('ID')
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=150)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    weight = st.number_input('Weight (kg)', min_value=0.0)
    height = st.number_input('Height (cm)', min_value=0.0)
    sport = st.text_input('Sport')
    reason = st.selectbox('Reason', ['Injury', 'Illness', 'Emergency'])
    date = st.date_input('Date', datetime.now())
    time = st.time_input('Time')
    count = 0

    if st.button('Add'):
        new_record = pd.DataFrame({'Id': [athlete_id], 'Name': [name], 'Age': [age], 'Gender': [gender], 'Weight': [weight],
                        'Height': [height], 'Sport': [sport], 'Reason': [reason], 'Date': [date], 'Time': [time], 'Count':[count]})
        df = pd.read_excel('athlete_data.xlsx')
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel('athlete_data.xlsx', index=False)
        # Add ID to 'Athlete ID' column in progress.xlsx
        PP1.add_id(athlete_id)
        
        st.success('Record added successfully.')

elif menu == 'Read Records':
    df = pd.read_excel('athlete_data.xlsx')
    st.subheader('View Records')
    if df.empty:
        st.write('No records found.')
    else:
        st.write(df)

if menu == 'Update Record':
    st.subheader('Update Record')
    record_to_update = st.number_input('Enter the ID of the record to update', min_value=0)
    df = pd.read_excel('athlete_data.xlsx')
    record_index = df[df['Id'] == record_to_update].index
    if len(record_index) == 1:
        record = df.loc[record_index[0]]
        st.write(record)

        name = st.text_input('Name', record['Name'])
        age = st.number_input('Age', value=record['Age'], min_value=0, max_value=150)
        gender = st.selectbox('Gender', ['Male', 'Female', 'Other'], index=['Male', 'Female', 'Other'].index(record['Gender']))
        weight = st.number_input('Weight (kg)', value=float(record['Weight']), min_value=0.0, max_value=350.0, step=0.1)
        height = st.number_input('Height (cm)', value=float(record['Height']), min_value=0.0, max_value=350.0, step=0.1)
        sport = st.text_input('Sport', record['Sport'])
        reason = st.selectbox('Reason', ['Injury', 'Illness', 'Emergency'], index=['Injury', 'Illness', 'Emergency'].index(record['Reason']))
        d = record['Date']
        t = record['Time']
        c = record['Count']

        if st.button('Update'):
            df.loc[record_index[0]] = {'Id': record_to_update, 'Name': name, 'Age': age, 'Gender': gender, 'Weight': weight,
                                       'Height': height, 'Sport': sport, 'Reason': reason,'Date':d ,'Time':t, 'Count':c}
            df.to_excel('athlete_data.xlsx', index=False)
            st.success('Record updated successfully.')
    elif len(record_index) > 1:
        st.warning('Multiple records found for the ID. Please check the ID.')
    else:
        st.warning('Record not found.')

elif menu == 'Delete Record':
    st.subheader('Delete Record')
    record_to_delete = st.number_input('Enter the ID of the record to delete', min_value=0)
    df = pd.read_excel('athlete_data.xlsx')
    if st.button('Delete'):
        df = df[df['Id'] != record_to_delete]
        df.to_excel('athlete_data.xlsx', index=False)
        st.success('Record deleted successfully.')
        
elif menu == 'Manage Medical Appointment':
    st.subheader('Manage Medical Appointment')
    id_number = st.number_input('Enter the Athlete ID:', min_value=100)
    progress_value = st.text_input('Enter progress value:')
    if st.button('Search'):
        st.write("hi")
        pp2.pa(id_number, progress_value)
        
elif menu == 'Track Health and Recovery Progress':
    df_athlete = pd.read_excel('athlete_data.xlsx')
    df_progress = pd.read_excel('progress.xlsx')

    # Streamlit app
    st.title('Athlete Data Analysis')

    # Ask user for Athlete ID
    id_number = st.text_input('Enter the Athlete ID:')

    # Search for the Athlete ID in the athlete data
    if st.button('Search'):
        if int(id_number) in df_athlete['Id'].values:
            # Get the count for the athlete
            count = df_athlete.loc[df_athlete['Id'] == int(id_number), 'Count'].values[0]
            st.write(f"Count for Athlete ID {id_number}: {count}")
            
            if count >= 3:
                st.subheader('Data Visualization')
                st.write('The data is being tracked.')
                
                # Create a line chart
                df_progress_id = df_progress[df_progress['ID'] == int(id_number)]
                st.write(df_progress_id)  # Debugging: Check the data for the selected Athlete ID
                fig, ax = plt.subplots()
                x_labels = [f'Progress{i}' for i in range(1, count + 1)]
                y_values = [df_progress_id[f'Progress{i}'].values[0] for i in range(1, count + 1)]
                ax.plot(x_labels, y_values, label='Progress', marker='o')
                ax.set_xlabel('Progress')
                ax.set_ylabel('Value')
                ax.set_yticks(range(1, 6))
                ax.legend()
                st.pyplot(fig)
            else:
                st.subheader('Data Status')
                st.write('The data is still being tracked.')
        else:
            st.error(f"Athlete ID {id_number} not found in athlete_data.xlsx")
