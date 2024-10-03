from one.api import ONE

# Initialize ONE instance
one = ONE(base_url='https://alyx.internationalbrainlab.org')

# Define a list of Mouse IDs to repopulate sessions for
mouse_ids = ['SWC_NM_082']  # Replace with actual mouse IDs
start_date = '2024-06-26'  # Replace with your desired date to filter
end_date = '2024-10-02'  # Replace with your desired date to filter

# Placeholder for sessions data
sessions = []

# Loop through each mouse and get sessions
for mouse_id in mouse_ids:
    # Query the sessions for this mouse using ONE API
    eids = one.search(subject=mouse_id, date_range=[start_date, end_date], dataset='trials')

    for eid in eids:
        # Get detailed session info
        details = one.get_details(eid)
        session_info = {
            'Mouse_ID': mouse_id,
            'Date': details['start_time'][:10],  # Extract date from start_time
            'EID': eid,
            'Hemisphere': 'both',
            'P_Opto': 0.5,
            'Stimulation_Params': 'zapit',
            'Pulse_Params': 'motor_bilateral_mask',
            'Laser_V': 2,
            'Opsin': 'VGAT-ChR2',
            'Brain_Region': 'motor_bilateral',
            'Genetic_Line': 'VGAT-Cre',
            'Trials_Range': 'ALL'
        }
        # Add more metadata if needed (like optogenetic manipulations)
        sessions.append(session_info)

print(sessions, sep='\n')

# # Now 'sessions' contains the repopulated data

# for j in range(0,len(sessions)):
#     print(sessions[j])
#     input("Press Enter to continue...")