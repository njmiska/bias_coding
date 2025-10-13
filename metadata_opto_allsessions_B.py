
def find_sessions_by_advanced_criteria(sessions, **criteria):
    eids = []
    trials_ranges = []
    MouseIDs = []
    stim_params = []

    for session in sessions:
        match = True
        for key, value in criteria.items():
            if callable(value):
                # If value is a function (like lambda), call it with the session's value for this key
                if not value(session.get(key)):
                    match = False
                    break
            else:
                # Regular value comparison
                if session.get(key) != value:
                    match = False
                    break
        if match:
            eids.append(session.get('EID'))
            trials_ranges.append(session.get('Trials_Range'))
            stim_params.append(session.get('Stimulation_Params'))
            MouseIDs.append(session.get('Mouse_ID'))

    return eids, trials_ranges, MouseIDs, stim_params


#Laser stimulation params:
#'QPRE' = Quiescent period to reward/error (standard stimulation)
#'SORE' = Stimulus onset to reward/error
#'QP' = Quiescent period only
#'ITI' = Intertrial interval only

### to do: SWC_NM_076 (snr but didn't work?), SWC_NM_063 finish sessions (PL)


# ########### STN inhibition
### ALL
eids = [
        'ce6be632-7986-4e05-b2c3-231d459d4dc4','cab9a767-05b4-4033-b074-225db0d37221'] #26 3/2, 2/2

trials_ranges = [
                 list(range(90,470)), list(range(90,528))] #26 3/2, 2/2


sessions = [
    ### STN Mice
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-21', 'EID': 'f4d793a5-9ee6-429c-974a-498250566be0'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-17', 'EID': '77268c3c-7879-4a7a-b83c-97e17293613a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-16', 'EID': '7f869985-4779-4e07-9e89-4f31267dd5e8'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-15', 'EID': '4f54fbea-064c-4a5b-942f-684fd5c28692'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-14', 'EID': '1dcab41c-9ec6-4a1c-bd4c-67721db91df6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90, 571))}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-13', 'EID': '84734bec-d898-4f50-b659-b4a7b7686fe8'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-10', 'EID': '3ca6c201-91f2-4ba9-8b8a-012446bdf7d2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90, 932))}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-09', 'EID': 'd2f085c3-0a84-48c6-88fa-e6b25bd89938', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90, 897))}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-08', 'EID': '81e58c8f-bfbd-4c54-b7ee-56d1d37767cc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90, 709))}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-07', 'EID': 'b64467f6-0fb9-4d77-8c97-eacb3a15dffe', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90, 586))}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-06', 'EID': '521827e5-e064-4df7-af21-391e7689102e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-03', 'EID': '1d5e592c-580d-440a-bc9a-5d3f5011f7c1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-03', 'EID': '4ab45924-65a7-4178-8723-ab457c6ee242'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-02', 'EID': 'b754992d-ac3a-477f-a4d9-421e10f34681'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-02-01', 'EID': '607afbbc-5fd9-4dae-aaa5-3edd187604f3'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-31', 'EID': '7b3632dc-5166-4b7e-ad12-d6ff203af76d'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-30', 'EID': '6f79d062-9d04-4467-b3ef-c6afd1b961cb'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-27', 'EID': '47093eb5-2516-4e6f-a66e-92275c52659b', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(182, 470))}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-26', 'EID': '765a6f2a-958e-4520-a30a-f8bacd9bd7b6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-25', 'EID': 'db759891-2760-48fa-98d8-00f53dccb8d1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-24', 'EID': '7504026d-a0f8-433d-bd4f-f1d35e1cc4e2'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-23', 'EID': 'e8933f87-c00d-4e84-811b-38459b8b36ca'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-20', 'EID': 'f62bbff2-a1c6-4646-9306-454f1c5b07a9'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-19', 'EID': 'bca63bed-244c-4cb6-b173-26661d02e901'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-18', 'EID': 'c82ceab1-ad8f-42aa-bb2d-c9594315d2cd', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,409))}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-17', 'EID': '08eec5ef-1874-490e-b0c3-4cc887a69250'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-16', 'EID': '63d56035-3929-49ee-8dcb-fef8c0e83934'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-16', 'EID': '4c4d5c12-14e2-458f-9336-bab7eecb17e3'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-13', 'EID': 'ee75986f-a2a0-470a-8e70-c23b76273f2a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-13', 'EID': '72c797b8-6320-4f2b-8f13-ff7be1629339'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-12', 'EID': 'cb8f7026-175b-4386-97ae-46858a721197'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-11', 'EID': '75615687-3cca-4728-841f-10874bfe78be'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-10', 'EID': '2f95753b-06cf-4860-b3a7-82b4d7a9fd45'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2023-01-09', 'EID': '6c00228c-fea0-49b2-8d3a-70c4f11cae00'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-22', 'EID': '279d6a88-fbcb-42ab-b46e-fa12a26d6618'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-22', 'EID': '3d2d70f9-3486-400e-a9d8-6aed17b6193a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-21', 'EID': '9c4b3fd9-f937-4f2b-9b7b-39be7bc2a7f8'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-20', 'EID': '3bec32f7-9c81-41be-bd39-dd5f9056fee5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-19', 'EID': 'd371049d-bebc-4488-ad8e-3f364d409fc9'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-16', 'EID': '1ddfaa39-f15b-4eda-9c70-c6d4f874fdb6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-15', 'EID': '2b8f4563-477b-4311-ad27-52de0ef20143'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-14', 'EID': '0cba0d73-ba8d-4121-af42-1ed14cf8e8ec'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-13', 'EID': 'ac6a5e09-3458-44bd-aadc-5578a2131902'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-12-12', 'EID': '05f72e19-86ba-4d31-958f-f04ea11d8b5d'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-11-04', 'EID': 'f95acc24-9774-46a0-bd35-316faa897b38'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-11-03', 'EID': '139e23d5-9b2a-4cf8-8a20-a9560ac4a90f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-11-02', 'EID': '0e7a2b3c-a2cb-404c-a7b2-94f56c860f14'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-11-01', 'EID': '86ff4554-35e7-4db2-849e-04bc20e21e18'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-31', 'EID': '422ed754-3a5b-490f-8611-538a635e55b5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-28', 'EID': '9d66c090-bc2b-4921-965f-3de0588a2ebb'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-27', 'EID': 'c91ac666-66cf-4c96-af73-3dc9d819f658'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-26', 'EID': 'd59bfb65-b7f6-4b37-96ee-d8c1cb362062'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-25', 'EID': 'd5d1d764-db1b-4aa6-95ea-72527d65aeef'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-24', 'EID': 'ddc57b5a-4a22-4baf-be2d-271f12456732'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-21', 'EID': '4a7e1b50-2972-415a-bdd3-8b3f9ccb9fe1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-20', 'EID': '5eea4ab5-68ac-4f1a-ae63-3e9e594cccc3'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-19', 'EID': '43e5ebf5-b9cc-4316-bdd3-7091313e1fe4'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-18', 'EID': '765938f4-8490-4ba0-8097-2ee53f8d066b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-14', 'EID': 'c7a00820-37c4-46e6-b448-17c8e4b20e7b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-13', 'EID': '3c30536f-6b35-414b-9bc0-ba8fef446251'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-12', 'EID': '29e12c0e-d541-42f9-ae24-9a14e3e0e8c1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-11', 'EID': 'a61bdde4-4013-4064-9806-4789514e0a97'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-10', 'EID': 'cd10362a-b4ee-41d7-a7c2-bf4e0e9d6f9a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-07', 'EID': '14a7d701-d28a-4cdf-8df6-f2c16c4cc182'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-06', 'EID': '7dd9149a-f8c9-4e32-b0e3-1bb47cddd91c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-05', 'EID': '3ae862b1-8d89-4e1b-bc20-cf648974677e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-04', 'EID': '61486305-8b8e-4986-b48b-e6e6ecba7667'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-10-03', 'EID': 'bc48ea66-d3a7-46b7-8687-214ae724efe5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-30', 'EID': '3f14b131-c799-438f-a816-e7413da20a0f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-29', 'EID': 'e849c842-b557-4bed-9184-f9d7f22984c0'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-28', 'EID': '87c6de39-6b53-492d-9ad3-ee8bf8906b75'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-27', 'EID': 'b3b7bf9c-d49e-4fc0-9cc3-0bc3674e7e22'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-26', 'EID': 'd7a057db-3690-428e-b41a-c59193baef80'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-23', 'EID': 'ae55e517-a6df-4907-b328-78af93712efc'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-22', 'EID': '0789e433-16e1-4637-a951-8fd50f61df1a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-21', 'EID': 'e858b4a6-a359-4e7d-be09-b44a44fcef1c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-20', 'EID': 'd52eba3c-741d-4c2c-9b3a-6bf51fa6d0b9'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-16', 'EID': 'e27eaec4-34f7-44d7-89f5-a06324d889e6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-15', 'EID': '92784f33-af8e-4b27-8461-092ec8cb6a5e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-14', 'EID': 'b9b39324-2666-44f2-bd68-545af04af62b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-13', 'EID': 'dbf4e8bf-9053-44f9-abd5-f2595e6a1e49'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-12', 'EID': 'c1d77420-6893-4bc7-bdef-88654d384d9c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-09', 'EID': 'e921ead3-ec94-4f02-b752-b57da6616323'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-08', 'EID': 'dc3c685f-da4e-4029-b475-5d10631459ff'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-07', 'EID': 'b659a685-e314-4449-ad05-f80715e0d0a4'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-06', 'EID': '7a6147c7-2247-4a2c-89d5-113dace7466b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-05', 'EID': 'ac4f703e-fd34-422b-9f19-cdf9aefba364'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-05', 'EID': '6f411ed6-f6db-4ad3-90b4-e2f901d15243'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-02', 'EID': 'be3bce52-d7ac-4b87-a857-44cf76ab5166'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-09-01', 'EID': '29a6da34-99dc-4d1b-b2a2-2dc68104eb1e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-08-31', 'EID': 'd9d86c21-ae30-44bc-8b3e-fd4fd9dc2987'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-08-30', 'EID': '6e86d984-ecc9-4f54-8234-9b09e9cf950b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-08-26', 'EID': 'beac81d9-4842-432a-a7c7-99f83303d23a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-08-25', 'EID': 'ccf2e91d-7e93-458b-b0c2-01c24a987c51'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_024', 'Date': '2022-08-24', 'EID': '823e5d65-26aa-4a5e-bc06-632fcfb96104'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-12-09', 'EID': '827fb7d6-4680-42b6-a7cd-c95b393a8502'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-12-08', 'EID': 'f453dd8b-8edc-4885-af0b-e9b92a3b8703'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-12-07', 'EID': '513b8846-b3f5-4fb9-892f-db3bcd520054'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-12-06', 'EID': '0f162f4a-ef0c-4cd6-87d2-584879e7a104'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-12-01', 'EID': 'c5304b1e-aa11-440e-9df0-7807680f4928'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-29', 'EID': '2e20099b-4eb1-400d-b217-bf0a30cd4caf'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-08', 'EID': '4ac3caaf-1b27-4c89-9020-560b7f6f6df4', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(137, 746))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-07', 'EID': '3dd68334-84cc-402d-a053-45bd352c14fc', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(325,623))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-04', 'EID': 'b4fa0296-28ef-4e31-af9e-514e2537bb9c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-04', 'EID': 'bb590645-fd17-4025-84e5-e65d3ef948ea'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-03', 'EID': '9606af89-12f6-4a57-8cd9-24f733beae8a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(162,791))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-02', 'EID': '45b7a288-8bf7-411c-b1ba-178b58fc7f6f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(97,816))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-11-01', 'EID': 'c0892faa-519e-430f-9b40-992b09fd618a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-31', 'EID': 'b6f80439-98e6-41cf-a7e8-7216b1d93feb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(100,461))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-31', 'EID': 'c4f246b4-454c-4d42-9e4a-daf2c92b7787'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-28', 'EID': 'e8db73ec-eff4-4704-a81b-ecbd00c5daf0'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-28', 'EID': '67688ca2-a5a3-4cea-8131-8da5b920dcff', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(150,618))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-27', 'EID': '002e60e1-e646-4f69-b6e3-d3b00f082797', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(102,939))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-26', 'EID': '0068b011-c60f-491f-a29c-245877cd1bc1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(146,790))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-25', 'EID': '117c2948-f460-48fd-85cd-1df01ae1c18b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-25', 'EID': 'abf38955-b5d4-4319-921a-f0658188ad57', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(188,236)) + list(range(413,597))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-24', 'EID': '87484eda-da05-4470-8a7e-4bde707e423d'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-21', 'EID': '80a2e5c9-285f-49b9-abef-57a5bc594f35', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(131,251)) + list(range(372,497))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-20', 'EID': '7bd7cbf6-e3ab-4222-ade8-458a5afb30f9', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(191,555))}, 
    {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-19', 'EID': '3ce813d3-75f1-4558-83ea-c125f71f6bba', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(269,333))}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-18', 'EID': '56cd3543-000a-49d7-a58d-b172f1d5db44'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-10', 'EID': 'a9e98830-1312-4b79-a06e-fa2d10c18c56'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-07', 'EID': 'd8555ea2-ddac-4a96-b189-8c37318d05b6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-06', 'EID': 'c7d7ad18-8796-4d83-a9ee-7388dbbf702c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-05', 'EID': '8cea02f0-2eaf-4abc-9da7-2275d2039754'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-04', 'EID': '095dae74-bddb-4dd5-adbb-5f5a29500b2e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-10-03', 'EID': 'a0c3f892-28f8-41c1-a0d8-f9f65be376a4'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-30', 'EID': '20e0086b-33d0-4c0d-92c4-cbe652e54cfe'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-29', 'EID': '385da0db-5736-477a-b72a-781560ee2c8a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-28', 'EID': 'e10d792a-3265-4b1b-b485-db4e83b53337'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-27', 'EID': '028decff-03d6-4aea-9379-1f8292d19a7c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-26', 'EID': '30a509eb-d1fb-48a4-8358-3f7642b163c7'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-23', 'EID': 'a41da95a-d3a8-4612-9c4c-2b2e8b3791ac'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-22', 'EID': '618f59bb-5ea5-40ec-bc96-38d30ac74791'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-21', 'EID': '1c0d9306-d402-4758-b0e8-0b45f1aed5c9'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-20', 'EID': 'a21cfcf3-9d5d-40fe-9353-1870d3c65493'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-16', 'EID': '8f12fe49-38e7-4b77-84cf-e801bc33452e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-15', 'EID': 'f2efe2f8-f13c-47d2-a230-1a7271524e69'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-14', 'EID': 'a88672bd-2605-4011-8a7a-a9e849bbc58c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-13', 'EID': '63e84042-a3bd-4488-ab3f-e61bce11eabe'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-12', 'EID': '22f1fb50-bb4b-4d92-b5bc-e5e2184b615b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-09', 'EID': 'f333c44c-01f4-4f3a-bf60-1aa4da41770d'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-08', 'EID': '23a8c347-05ba-49cb-b9fd-96d4a9bbf139'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-07', 'EID': 'a0c52cbc-de5c-47ae-ac76-b5e7cadd01d5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-06', 'EID': '03382bba-1dec-44e8-86fa-ae800edc971f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-05', 'EID': 'bb0da113-38d2-4977-8328-27665e076199'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-02', 'EID': 'c1e24aa1-22f6-46ee-b73b-faf30c8b836c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-09-01', 'EID': 'f842f68a-ac0d-4fe4-b30a-df9c21cec816'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-08-31', 'EID': '8d98814c-4d88-4737-b942-8a47dbeedcd2'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-08-30', 'EID': 'f63c15be-d41e-4d2b-acd3-79831424b665'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-08-26', 'EID': '28ff2214-aa13-4973-97dc-4a9bf8b64abd'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-08-25', 'EID': 'a742f62f-7c03-4646-8f42-6219ad84834b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_025', 'Date': '2022-08-24', 'EID': '536da8f6-c487-445f-9bee-5350ed7bcb14'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-21', 'EID': 'cdaf8a0d-ba9a-4963-b347-47aa3520244f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-16', 'EID': 'ac52a1ce-3b6c-4421-bc12-3d898d7d6527'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-15', 'EID': '091f5721-72f4-4f73-a4ed-037d86040778'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-14', 'EID': 'b6de331a-495a-42b3-b029-ee743a99ac10'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-13', 'EID': '7791c224-b38d-4a1f-a133-beb043ee1301'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-10', 'EID': '455f55c1-81ef-4541-8894-cf6c713a3a82', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,400))}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-08', 'EID': 'eacd7f97-f676-4d95-af31-e61b3182cfcf'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-07', 'EID': 'd7dd0a50-b099-4320-855c-066bc6dd6d36'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-06', 'EID': '7aa67b01-67b8-44a2-bf23-2e58152fb8d3', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,281))}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-03', 'EID': 'ce6be632-7986-4e05-b2c3-231d459d4dc4', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,470))}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-02', 'EID': 'cab9a767-05b4-4033-b074-225db0d37221', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,528))}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-02-01', 'EID': '784af2de-8082-4117-8149-aa967558b4a3'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-31', 'EID': '121545ee-2cd7-461c-beb6-c8c1742572fb'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-30', 'EID': '198dfd8b-7c2d-47d4-9df0-afd1b384a0e7'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-27', 'EID': 'f4d0076a-d9ef-4952-92ec-0ec92936fda1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-26', 'EID': '583bf8b4-c500-494e-be90-6548bf26173a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-25', 'EID': '3475b385-19af-4be2-a667-4cd9a4ba7527'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-24', 'EID': '5654a819-d54a-4ef0-ac2d-247624ab4f50', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,256))}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-23', 'EID': '6b4a1004-9508-4ef4-b7a7-7cd10a676948', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(173,308))}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-20', 'EID': '91857de2-766f-43e2-a3cc-ace233485ebd', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,450))}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-18', 'EID': 'baf2b96e-c587-49cf-acf7-c2ffb1c332a6', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,400))}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-17', 'EID': '76862a7b-f07e-47e3-b8ea-dc4588109cef'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-17', 'EID': '45d56882-0a12-4e6f-9ad8-568d1755bc39'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-16', 'EID': '5419ebc2-4aa0-446a-966e-23097c17e7e1'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-16', 'EID': '79468bd8-6fa2-48e4-8151-88951b33a8e0', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': list(range(90,300))}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-13', 'EID': '51c69567-21a4-4353-8bec-b543093f5e0b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-12', 'EID': '67a7b96c-c3d1-440f-9023-0ad50dfae94b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-11', 'EID': '64bbe8d1-704f-4266-88a5-db9aa7fc9ef8'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-10', 'EID': '5f785316-fddf-4c8e-b301-edc76782600b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2023-01-09', 'EID': 'f18559d5-cc43-4643-aa1b-e6c829b33840'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-22', 'EID': '1af16900-dcc0-4e58-a417-25d4af6fbefa'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-21', 'EID': 'b8ab9388-6fe5-4fc8-a689-ddde0762b871'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-20', 'EID': 'fad4ec16-0fb7-486b-bfef-d935cb8491e6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-19', 'EID': 'db9b8dc4-5034-4d71-96a0-f5685cfbb10e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-19', 'EID': '1ea4539e-e86d-4cf8-a04b-ea8c069eb879'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-16', 'EID': 'ee1d7262-ad5b-4e41-94de-09f01f0e3682'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-15', 'EID': '68f1b11c-ce0f-4dfd-b005-bc9488585e31'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-12-12', 'EID': '26089e9f-4a88-4624-98e0-f09be1d6d872'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-11-04', 'EID': 'de6fc1d7-cf84-4f45-a5db-e4fb41728b6f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-11-03', 'EID': 'f9dffcda-3ed2-4778-a911-61dd19008bb0'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-11-02', 'EID': 'de613cfa-c625-4310-b16f-c883b1bfc179'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-11-01', 'EID': 'c603b131-7ad3-459f-907d-9f3e9e186d0a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-31', 'EID': '0b125b5a-196a-4dea-a311-6d6fa2a40894'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-28', 'EID': '86b8d8d4-b90e-4206-9650-00fd428bc69a'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-27', 'EID': 'f609e74a-da8e-40ce-ab20-cd5d3f15d88c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-26', 'EID': '3fdbc495-456a-45ee-8f16-00e33baf20f5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-25', 'EID': 'dc032def-588f-4133-a603-d906af27ffb4'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-24', 'EID': 'ed0dcb08-a4fa-4ad8-8f8c-fb7f69142d45'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-21', 'EID': '976a6547-01d8-4c63-aa70-d8340729a7f0'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-20', 'EID': 'b2765d67-6749-4c37-9561-ba4bd65323d7'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-19', 'EID': '855c50f7-6614-4520-9ef6-fc0c617363e2'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-18', 'EID': '7814ca5e-9a97-4791-8a89-21b51bd4b51e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-14', 'EID': '8c6421f2-8842-4378-9f79-93f54f85b3bb'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-13', 'EID': '52ae6d0c-412b-413b-8252-2edef2d4f586'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-12', 'EID': '3c91ecc7-c16e-44b3-8442-8e357f0ca763'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-11', 'EID': 'a4676635-a462-4f4b-a820-88fea14b6402'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-10', 'EID': '8ba44bf6-a64a-4fca-97f5-c05d36029d44'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-07', 'EID': '3fe7de08-6adc-4df9-93d0-d9328946308d'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-06', 'EID': 'ad5fe583-89f7-4eae-a9c1-86e1f17ffeb2'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-05', 'EID': 'ef079dda-7c62-4698-8270-df287b3d6e66'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-04', 'EID': 'e3758551-60ec-4a90-8644-311f0b89f59e'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-10-03', 'EID': 'aa0d94ce-1a10-4155-9966-d2618b9ed081'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-30', 'EID': '7cf808ca-29f8-49b0-993c-4c8389528083'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-29', 'EID': 'd5983c5e-d2b1-4685-8aaa-ca6b917850fb'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-28', 'EID': 'daeea042-47cd-4ed7-aed2-cb85e4a25186'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-27', 'EID': '3d4ba06b-2b1c-426b-a17e-d95603075347'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-26', 'EID': '766f82de-6d3a-4b6b-852d-181d0c9759d5'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-23', 'EID': 'e79267ae-080c-4a05-8b7a-087eb4179263'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-22', 'EID': '5b3fa3d4-94be-4297-bcb1-75e9df5fe311'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-21', 'EID': '2da353f8-a00e-4ce6-b97a-a05ffa59d641'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-20', 'EID': 'd17a05e7-8404-42ee-bcad-635cf5c06d04'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-16', 'EID': '910572d8-894f-450c-937b-ab177cf4e508'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-15', 'EID': '480e406b-7348-466f-9519-2702d649fd6c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-14', 'EID': 'c5faf6be-5666-4f66-849e-1a9f595e7c0f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-13', 'EID': '51b01890-1335-4ea2-bfd4-c755d74a40ea'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-12', 'EID': 'c9a1fc4e-2612-4626-bf29-ff860b716c30'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-09', 'EID': '3002f8c0-9184-4281-be26-989c1b3f6bb6'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-09', 'EID': '840166ad-ce17-4878-9f12-1ecc626bd563'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-08', 'EID': 'a74d99c3-6207-48e8-81d1-226ccb164b8b'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-07', 'EID': 'cf1b2b5c-3330-4dac-9437-eb881c4a32ca'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-06', 'EID': 'a711e3f8-e3e3-4f34-aa7f-5eff5b8123e4'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-05', 'EID': '68515963-1ec3-4e47-b09c-688c96a7c36f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-02', 'EID': '9e47ccee-42a3-4d1f-b704-346daa8ada22'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-09-01', 'EID': 'b9aa8bef-a686-4199-a345-d7a8791fe38f'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-08-31', 'EID': 'ead1344e-052b-4334-afc4-bdd9a7c0b89c'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-08-30', 'EID': '38be95d7-27d9-4d9b-a08d-107bb77999aa'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-08-26', 'EID': '051be36a-d166-48c3-905f-92b027b12b95'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-08-25', 'EID': '6ddca86f-4eb7-4952-9786-621bae8eb648'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_026', 'Date': '2022-08-24', 'EID': '76009463-205d-47a5-bb9a-87b367e8cd70'), 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'STN', 'Genetic_Line': 'GLUA1-Cre', 'Trials_Range': 'ALL'},

    # --- SWC_AY_002 ---
    # SNr hit perfectly. 
    {'Mouse_ID': 'SWC_AY_002', 'Date': '300924', 'EID': '34b90b7e-290d-49fc-9456-90d35a1f56f5', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(80,9999))},
    {'Mouse_ID': 'SWC_AY_002', 'Date': '011024', 'EID': '8d9026cb-1226-4105-943a-812f9ab69472', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(452,9999))},    
    {'Mouse_ID': 'SWC_AY_002', 'Date': '021024', 'EID': '8375351a-72f7-4fc5-a5e4-cf0d2334e91b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(258,385))},    
    #{'Mouse_ID': 'SWC_AY_002', 'Date': '211024', 'EID': 'f0c954d9-9ed4-4974-9365-f35e6e3077b9', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    missing
    {'Mouse_ID': 'SWC_AY_002', 'Date': '231024', 'EID': 'bd1a6bd3-6640-4a8f-ba06-70a0278d0d61', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '241024', 'EID': 'bfe791d1-ee1f-48b1-bc39-1c0bbdc45dd6', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    #no effect w/ QP?
    {'Mouse_ID': 'SWC_AY_002', 'Date': '251024', 'EID': 'c39cedcc-0a24-4f63-90ce-288599e4be83', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '281024', 'EID': '8a05ac7c-8c20-4202-bfb8-57b177f0a679', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    #no effect w/ QP?
    {'Mouse_ID': 'SWC_AY_002', 'Date': '291024', 'EID': 'd973471b-8d22-40dc-bc75-2f4862c383c7', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    {'Mouse_ID': 'SWC_AY_002', 'Date': '301024', 'EID': '57147880-f688-4f66-8353-0b013422ea1b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    {'Mouse_ID': 'SWC_AY_002', 'Date': '311024', 'EID': 'a79a53fd-269f-4770-b40b-7d844ae71109', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    {'Mouse_ID': 'SWC_AY_002', 'Date': '011124', 'EID': 'a4ed3214-b74a-4588-9ac0-ed7726b6c7d9', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '041124', 'EID': 'a517af74-3e00-43b2-8756-b2167f9bc7b9', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    #no effect w/ QP?
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '051124', 'EID': '30edc331-6d60-410f-b20a-7866b9fab921', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    #no effect w/ QP?
    {'Mouse_ID': 'SWC_AY_002', 'Date': '061124', 'EID': '9cf1bccd-7c76-4aff-9990-f6ce8527fe87', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    {'Mouse_ID': 'SWC_AY_002', 'Date': '071124', 'EID': 'b40b2a90-e7c5-46fd-a7dc-b48e767e5f0d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},   #laser leakage 
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '081124', 'EID': 'a6823cac-f720-4c58-9b3a-3a1e62fef301', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    missing trials data
    # {'Mouse_ID': 'SWC_AY_002', 'Date': '111124', 'EID': '3eee2dd2-61f9-4565-8967-d65dea3dd801', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    missing trials data
    {'Mouse_ID': 'SWC_AY_002', 'Date': '121124', 'EID': '7f6bbddd-12b4-4e5a-8e91-3b89288ef6e9', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},    
    # ----- END -----

    # --- SWC_AY_003 ---
    # Perfect expression in ZI. However, cannulas were inserted at a slight angle. Some cortical damage. 
    {'Mouse_ID': 'SWC_AY_003', 'Date': '141024', 'EID': 'c83f4abc-789a-47ed-af18-ead78af22072', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(260,348))},    
    {'Mouse_ID': 'SWC_AY_003', 'Date': '141024', 'EID': 'c83f4abc-789a-47ed-af18-ead78af22072', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(348,9999))},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '151024', 'EID': '65cb8473-ec4a-4796-86bf-ee1613e109a3', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '161024', 'EID': '318e2dad-b9d6-4502-a336-5c5a3c438e1c', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '171024', 'EID': '3b3c0021-d459-4949-a2a9-6780df2550f4', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '181024', 'EID': '4d7de64d-97f5-4824-95b9-3bb692dff21b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '211024', 'EID': '8b00b851-a2b0-434e-b444-0cbe10c9f1ef', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    #{'Mouse_ID': 'SWC_AY_003', 'Date': '221024', 'EID': '8b00b851-a2b0-434e-b444-0cbe10c9f1ef', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # missing
    {'Mouse_ID': 'SWC_AY_003', 'Date': '231024', 'EID': 'e72a72da-2a5b-4966-8dd7-ce967ea9202f', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '241024', 'EID': '61a373e7-069a-4e09-8bc7-228e58e0fc7c', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '251024', 'EID': 'ab93d122-3be9-4662-b7d2-62035df15c8c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '281024', 'EID': '9039562a-644c-41cd-af41-c5f1eace8917', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '291024', 'EID': 'd58eca6e-f25a-4268-9766-a69a93c72b90', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '301024', 'EID': '4fd3f898-17d7-44ad-9886-5ecaec026f35', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(73,9999))},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '311024', 'EID': '1e6d7bb6-5cc5-4852-94b1-244c19d2de2a', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '011124', 'EID': '403f0790-ba57-4150-929b-aa9651c55f4f', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # need to double check if this is SORE or QPRE
    {'Mouse_ID': 'SWC_AY_003', 'Date': '041124', 'EID': '426c82b6-6442-492c-bc8d-2ee3c4c45eb9', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '051124', 'EID': '5904d256-5560-4733-8fc2-d3a23c277b00', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '061124', 'EID': '8f67afc8-55cd-40e9-9998-6585939610e9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '071124', 'EID': '03caca70-1ce1-45fe-a646-d31f6011d8f6', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '081124', 'EID': '0cc70315-ca62-4480-83f4-30b681d19649', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '111124', 'EID': '304b1f0e-fd1f-4fa0-b8fa-2eeba794a1fe', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_003', 'Date': '121124', 'EID': '635fb737-8f4f-40aa-a7d2-d70f0aa8b36e', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # ----- END -----

    # --- SWC_AY_008 ---
    # Only shows expression in L hemisphere
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '181224', 'EID': '766be52a-1606-4a72-9333-f0e6def25ab1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(279,9999))},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '191224', 'EID': '74819782-0ca6-4fd3-bb57-b49499dd1ecc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '201224', 'EID': '9cc96397-cd1f-41af-a85e-b52ef13500dd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(350,9999))},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '301224', 'EID': 'dc341d20-af5c-4a10-a06c-5b0f865736f3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(312,9999))},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '311224', 'EID': '0f03c02c-5512-4407-a4ef-59be3fc95945', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '010125', 'EID': 'e8ae71e7-bc32-40c7-8082-c3d9759ca4b5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '020125', 'EID': 'f85350f6-648d-4004-b3e5-1f9046e8a153', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '030125', 'EID': 'c96eba55-7ea5-4c27-93a3-5636caced632', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(42,9999))},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '060125', 'EID': '0d447372-2493-4ad1-a681-7b4dbad56ab2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '070125', 'EID': '9b1e0b9a-fc0d-49e0-9ff4-5aff2ddf48bd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # period 18.12.24 - 07.01.24: need to check which sessions are DWZ vs AY (loose fibre connection)
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '080125', 'EID': '07424119-022a-43a9-8b10-5a1597f8387e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '220125', 'EID': 'b65398ff-a779-4fd3-b931-7864a0ed75fc', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '230125', 'EID': 'a4f0b258-976a-4378-b6a0-a70104aedf70', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '240125', 'EID': '43b070a5-d3e3-4e25-b238-b1e4df4c19be', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '270125', 'EID': '6293e872-be13-4ea7-8444-9a79e23e1601', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '280125', 'EID': 'b6b21e0b-d241-49dd-aa7b-9495cd6e1791', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '290125', 'EID': 'efdeed93-0c9a-4c19-9f59-a945c4075045', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #no QP effect?
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '300125', 'EID': '546c8243-f6cd-4df7-8038-3d9c999602de', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '310125', 'EID': '6b4eefef-85e8-4f4c-a092-aba01cb7d0fc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '030225', 'EID': 'd00e96f2-393b-48c0-97f6-1c8abf5668a8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '040225', 'EID': '79615d17-546f-4c03-9c47-c3ece13bc994', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # trials not found?
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '050225', 'EID': 'b1686b3a-00ce-4fe8-8d8c-fe9cb18d5cf0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '060225', 'EID': '234e2264-3960-41ed-830c-fd61c9017e5a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '070225', 'EID': '16104299-599a-470e-aea7-899d5a3f8a3c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '100225', 'EID': '4b3e5d53-63d3-417a-8e4f-27b31d51a38c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '110225', 'EID': '8386007f-5d0c-465f-aaee-be54c8b89bc9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '120225', 'EID': 'a0c59fe2-c050-4270-b685-66febf301b73', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '130225', 'EID': '7db2bf93-3f6c-42f4-9de4-c3e10dfb7643', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '140225', 'EID': '7d4f02b6-8b06-4b0f-aa65-d770f7c5e690', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '170225', 'EID': '9c490636-b444-4863-b9be-e15d56a8f65d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '180225', 'EID': '7a554974-a824-4993-9f36-2b42dd6cbacc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #no QP effect?
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '190225', 'EID': 'a44ba81e-ddc3-4cd2-a03b-24f05c3f25df', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '200225', 'EID': '20b6d00e-98fb-40d5-81b4-2215b8b9be36', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '210225', 'EID': 'd6f84cd9-2803-435f-b18c-054426645483', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '240225', 'EID': '11fbe3e2-55d6-4294-aebd-51ff11efa4e8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '250225', 'EID': 'd9308a5d-ea7d-46c0-9234-3295b0ed6cfe', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_008', 'Date': '260225', 'EID': 'e22cfba5-5b2f-4c2e-bf37-c11666a4705f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_008', 'Date': '270225', 'EID': '59d1c570-576d-429b-aa3d-729b1ef71dfa', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # ----- END -----


    # --- SWC_AY_006 ---
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '220125', 'EID': 'a95342b6-34e0-4986-81c9-3da3b2d3d552', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '230125', 'EID': '5af8e109-6e6a-4584-ab63-8a9982bd0abf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '240125', 'EID': 'ac98071b-58d3-47df-8738-d59e99dc6fb0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '270125', 'EID': 'b2c60075-433c-407d-98c1-5c107985c43d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '280125', 'EID': 'cccf0a2f-9921-4c17-bb78-dd210cec5619', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '290125', 'EID': 'd996950a-a35d-4ae9-9594-f077e6be3853', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '300125', 'EID': 'e36935ea-dcfe-4fd6-95ba-405aa211e751', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # changed from 0.1V -> 0.5V at trial 625
    {'Mouse_ID': 'SWC_AY_006', 'Date': '310125', 'EID': 'e3416b27-419c-46ae-a7d0-6eaf8ca12747', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '030225', 'EID': '063e79f0-8a34-4acc-98b8-8df644d24580', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #trials not found
    {'Mouse_ID': 'SWC_AY_006', 'Date': '040225', 'EID': 'b7804bc4-cd95-4b7a-bc89-507b0d1fb290', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '050225', 'EID': '5061926d-b7ce-40b1-9f87-2b195e18ea1c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '060225', 'EID': '0e976843-e0da-4d81-bf4e-392d89495991', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '070225', 'EID': '68c88d54-3a66-41ff-9991-6ae6cd5efb8c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '100225', 'EID': 'da607c74-41f2-4874-b479-10e56ea9b7d8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '110225', 'EID': '7266bfe3-ee65-45c7-b5b4-9d8a1c4778ae', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '120225', 'EID': 'dc566ee0-a204-49e0-87e1-39385caf6c17', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '130225', 'EID': '6aa8136d-5f7d-4480-bf32-4e8573fac438', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '140225', 'EID': '44804a50-2798-4487-9fd9-3bf486f8dc8d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '170225', 'EID': 'f701d4e8-22a6-4437-857b-f81c3d9d6928', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '180225', 'EID': '025647c7-47f6-4ff4-94a9-d8448a44ceb2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '190225', 'EID': 'd4c811e7-aaa4-40bd-b34f-cac0e9c6a6a6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '200225', 'EID': '800cafdd-b649-47f6-b5c5-e9ab48f20e7e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '210225', 'EID': 'a3a56690-f20b-4301-be9c-c872c92c3e10', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '240225', 'EID': '351e4866-8246-47c9-9e2c-4c3b155020d3', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '250225', 'EID': 'a6532b11-ec0b-4950-8a2c-d42988c94f3b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '260225', 'EID': '419e624e-2b0d-47ba-8dfc-1fe2eaecaa1c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '270225', 'EID': '14aa23a1-43dc-4163-bd0d-b8af34660e68', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '280225', 'EID': '7fa53427-0011-4204-b2b6-a150f25c4fb1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '030325', 'EID': 'fbf72af1-c777-403b-ad14-97bc220db751', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '040325', 'EID': 'a8fb5aa3-bf06-40a2-b1ea-5773aa07e374', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '050325', 'EID': '3499d182-132e-4c03-a853-c6e5d1dc12cf', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '060325', 'EID': 'adb6ab8c-c9a5-4e7c-99ee-9c456f4d1b04', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_006', 'Date': '070325', 'EID': 'b8b0c1f2-c012-42a1-8482-1744496df656', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '110325', 'EID': '17ad0ba8-1ae0-4c5b-984d-b6ad13725d8b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '120325', 'EID': 'fbf17127-bcd2-4699-897a-80d917093d31', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #no effect w/ laser
    {'Mouse_ID': 'SWC_AY_006', 'Date': '130325', 'EID': '19becee2-8876-4577-9237-f6604749df19', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '140325', 'EID': 'ecb6537f-1ac6-4d21-813d-ecb1242031bc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-28', 'EID': '7f41e39f-06df-44e9-8442-bb34a1a29618', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-27', 'EID': 'f4cfd177-f9c0-4238-8664-40b091020f30', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-26', 'EID': '9fd4dd09-814c-4b75-9c03-2b3822d2bb3f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-25', 'EID': 'c471fbeb-21e4-4d01-86e1-5a67327089ea', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-24', 'EID': 'c2dc7668-2cbb-4ef7-85cd-a64cc887ee3d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-21', 'EID': 'c8bac6f7-e6c0-4a71-b132-6fb0e3eae567', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-20', 'EID': 'dc98a028-8aa6-4185-a0b4-1c802251c7f1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-19', 'EID': '3ca0b4da-c765-408a-964a-e7ee1ca71247', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-18', 'EID': '1afd03ce-0247-4689-857d-a6fe454e993f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #no effect
    {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-17', 'EID': '9db5ac4e-8746-492e-be70-ed884d1469d7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    ### likely no expression in R hemisphere
    
    # --- SWC_AY_012 ---
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '070225', 'EID': '486a6256-4d4f-42f1-af66-4d3362471145', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(185,9999))},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '100225', 'EID': '7e822546-8829-45a2-ba04-4fa0cf2d2121', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(158,9999))},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '210225', 'EID': '162a3579-7fb6-4e13-8b6f-a0645040dc9a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(165,9999))},  # OR P_Opto = 0.1 ?
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '240225', 'EID': '01e81b6f-0a4e-4aa5-ae1e-329e4c5e000e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '250225', 'EID': '35624143-0761-46e7-8711-56ba6559a5cd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #strong effect
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '260225', 'EID': 'c548b258-fc24-4d8c-96d2-b3239f70e388', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  #strong effect
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '270225', 'EID': 'a8519c6f-a1cc-4208-a2ab-4e633ebf7bf9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '280225', 'EID': '3d886842-529b-42cd-9147-e3eaddbf9077', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '030325', 'EID': '6dec6739-2ea7-4a12-aa96-dff93b41d917', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '040325', 'EID': '71b141f7-c4ca-4e17-b77f-5c273a94ff53', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '050325', 'EID': 'd6382c68-013f-4714-b784-8a72a1f207f2', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '060325', 'EID': '29413835-6aa1-488d-be91-463a95685e1f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '070325', 'EID': '2c09f398-caab-4f0d-9ab9-aae0a18081c1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '110325', 'EID': 'f3485eae-dc02-4e30-ae26-7e0289e9ee5a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '120325', 'EID': '8b407f19-062e-44d1-b9d1-17104a053530', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '130325', 'EID': '012cda53-9aa2-4c51-87a4-ff338702af4a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-27', 'EID': 'f9bbafb0-fb1d-46c6-b297-5414d87d3ce1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-26', 'EID': '35877ee1-1863-4d03-aac0-db38de8219a6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-25', 'EID': '0e204e84-da8a-452e-968f-74d8edf29c3f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-24', 'EID': '81841b7b-522c-47b1-8294-86ed2ef748b6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-21', 'EID': 'e8eb78e4-1b44-4766-a2ff-a6a73ada6716', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-20', 'EID': 'fda6133d-5c38-4a0d-a6ec-11ca2ffd4cce', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-19', 'EID': '70502208-2081-4a38-a22b-b130a3cd4cac', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-18', 'EID': '0ebb203e-cdbd-480c-a780-0a0178b1688f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-17', 'EID': '854d8ed5-1f11-478b-980f-eb2e865ddb6d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-14', 'EID': 'd57c3edc-7c9d-4a66-a5e5-0c1a1dafad41', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},


    # --- SWC_AY_005 ---
    {'Mouse_ID': 'SWC_AY_005', 'Date': '250225', 'EID': '2f51c379-8492-4e64-ae9d-911295484359', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(218,9999))},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '260225', 'EID': 'b66d2eab-af9a-4e84-8ac5-11a60b45fb21', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '270225', 'EID': 'fe38edab-9d0c-48de-b111-e7ab8e1af155', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '280225', 'EID': 'f82f43d6-4db2-4149-ae89-d5f7ecd5f639', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '030325', 'EID': '7f0ea307-985e-42c7-b778-06833a08b3f4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '040325', 'EID': '63c659cf-5ffc-474c-bb71-eb297bb2ce55', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '050325', 'EID': 'c056bc5c-27db-468b-926a-93988f10fdee', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '060325', 'EID': '20bf2ae3-1266-4a2b-b77b-c4c250ba12c3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '070325', 'EID': '52e68598-9e20-4c05-a5b7-eeb530e4cc0a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '100325', 'EID': '13c0169c-bba0-439b-9756-6b9faaa5b304', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_005', 'Date': '110325', 'EID': '061bbb33-b7fb-4a89-9890-d65e111bb84b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # ----- END -----

    # --- SWC_AY_010 ---
    # {'Mouse_ID': 'SWC_AY_010', 'Date': '040325', 'EID': '75bad027-f598-4805-bf0f-504aaab3b485', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(185,9999))},  #questionable
    # {'Mouse_ID': 'SWC_AY_010', 'Date': '050325', 'EID': '7774e0a2-9c1f-4766-b210-0885a77b37de', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(45,9999))},  #questionable
    {'Mouse_ID': 'SWC_AY_010', 'Date': '060325', 'EID': 'c41af6f6-d08e-497b-a3a1-e737cb3bff64', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_010', 'Date': '070325', 'EID': '56de52a0-6ceb-4455-b438-deddbbec7ea6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    {'Mouse_ID': 'SWC_AY_010', 'Date': '100325', 'EID': 'd6d45589-00cd-47f6-a2a9-4cd6f76e21b4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_010', 'Date': '110325', 'EID': '1f032167-c752-4fae-8e63-6c23aaaa2194', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},   # NEED TO DOUBLE CHECK LEFT/RIGHT HEM.
    {'Mouse_ID': 'SWC_AY_010', 'Date': '120325', 'EID': 'b7827ee6-6c04-4816-8fe7-453839ec1018', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},   
    {'Mouse_ID': 'SWC_AY_010', 'Date': '130325', 'EID': '7498d9ac-9c3b-40af-bb24-bfa498175ff2', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},   
    {'Mouse_ID': 'SWC_AY_010', 'Date': '140325', 'EID': 'cb6050c5-c248-4de3-b8b1-c470aeef0dbf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-17', 'EID': 'd8650bb0-8467-40ac-90c1-34f4e3da1119', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-16', 'EID': 'ca029e73-5f7e-451a-bbc2-95a8929f7da8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-15', 'EID': '7d0d37b1-133d-4405-ae50-3cb310b81293', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-14', 'EID': '418424ad-0fb9-465c-8beb-d483d67e894e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-11', 'EID': '8ae8551f-9699-46ce-af42-96f9c2759dc0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-10', 'EID': 'c0b63340-b86b-493b-b937-76be83387b27', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-09', 'EID': '1b667a08-f88e-4c61-a133-6dd19cce0fb8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-08', 'EID': '82c2809a-276c-4c02-8486-c659aa2d422f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-07', 'EID': '2d817c19-0f65-4b0c-abcc-ce0f8a417b8f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-04', 'EID': '85311343-d370-4a86-8dd4-08d899a418f0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-04-03', 'EID': '6cf8bd50-6d0d-4268-be6a-04c9c6686244', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-27', 'EID': 'f9bbafb0-fb1d-46c6-b297-5414d87d3ce1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-26', 'EID': '35877ee1-1863-4d03-aac0-db38de8219a6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-25', 'EID': '0e204e84-da8a-452e-968f-74d8edf29c3f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-24', 'EID': '81841b7b-522c-47b1-8294-86ed2ef748b6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-21', 'EID': 'e8eb78e4-1b44-4766-a2ff-a6a73ada6716', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-20', 'EID': 'fda6133d-5c38-4a0d-a6ec-11ca2ffd4cce', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-19', 'EID': '70502208-2081-4a38-a22b-b130a3cd4cac', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-18', 'EID': '0ebb203e-cdbd-480c-a780-0a0178b1688f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_012', 'Date': '2025-03-17', 'EID': '854d8ed5-1f11-478b-980f-eb2e865ddb6d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},   



    # {'Mouse_ID': 'SWC_NM_072', 'Date': '110324', 'EID': '4a74f159-ef87-4c1e-a05b-d5c03712473e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(21,9999))}, ### No ZAPIT log data for this session?
    # {'Mouse_ID': 'SWC_NM_072', 'Date': '120324', 'EID': 'e66329e4-21ac-4762-aa14-28443d7dc4ad', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(49,9999))},
    ### issue with datetime?
    # {'Mouse_ID': 'SWC_NM_072', 'Date': '120324', 'EID': '9ab0912d-d8b5-43c5-bc7e-56f5ca82cb66', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(30,9999))}, ### ZAPIT log data potentially corrupt for this session???
    {'Mouse_ID': 'SWC_NM_072', 'Date': '130324', 'EID': '94adaf4a-f52d-4bb0-ae4c-54f235379e3d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '140324', 'EID': '8d9c0607-7550-4bca-af9b-c26fa1162729', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '150324', 'EID': '6ac7cec5-9c87-46da-8dc8-6619cca21d9b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    ### lots of sessions for 18/3 - check and see if all folders in right place
    {'Mouse_ID': 'SWC_NM_072', 'Date': '190324', 'EID': 'cf88dc0a-9ae1-49a6-a86e-4cda25810c6d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(3,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '200324', 'EID': 'fc9d905c-d474-40d0-ae3a-bc4b062a1881', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '210324', 'EID': 'eab4dda8-d7b5-4122-9137-369311730ddb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '220324', 'EID': 'ac72bdf7-0a3b-43ec-a110-a173eade8855', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(6,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '250324', 'EID': 'e27df933-fddd-4446-b621-6b3c6fee652d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '270324', 'EID': '363fd96f-fb16-4bac-97e4-56d10f9d6872', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(24,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '280324', 'EID': 'bfeae9f2-be48-4b06-bcfd-9ed48da0b493', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '290324', 'EID': '21ee8737-3bea-4f7c-9f66-24813fe75e77', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '030424', 'EID': '38c2e901-9dc7-4370-9ebc-f3605f270464', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '040424', 'EID': '92e8d75d-9b7e-4af6-9a68-22316b8ac9a2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '050424', 'EID': '8dd76537-f9fa-4c0c-ad88-1b8af650d28a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '080424', 'EID': 'e654a5b9-c611-4736-a38f-aa7b8f1d0f01', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '090424', 'EID': 'c67e4a9c-13d5-4645-ab39-dca4b6f2944c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '100424', 'EID': '5e41e3c4-d4e1-4053-9bee-057a32d53550', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '110424', 'EID': '66cb06fe-9185-47c1-8119-496f9be12376', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '120424', 'EID': '04943eaf-800b-4f36-b51a-c387015fbbe1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(3,9999))},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '150424', 'EID': '63ff2bf7-a6f0-43d8-a0c4-98c48a5683a3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '160424', 'EID': '8f226d68-e09f-4d66-b57f-35baf4e5a7b8', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '170424', 'EID': 'd35cc45b-1106-4390-be48-46933d639f7b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    # {'Mouse_ID': 'SWC_NM_072', 'Date': '180424', 'EID': '5e41e3c4-d4e1-4053-9bee-057a32d53550', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #Poor performance. Also, need to remove last ~half of trials
    {'Mouse_ID': 'SWC_NM_072', 'Date': '180424', 'EID': '4029b439-bdc0-429e-9d58-477b01d46e92', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '190424', 'EID': '5e41e3c4-d4e1-4053-9bee-057a32d53550', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '220424', 'EID': '89005d0e-0d72-4ca2-834a-681169215f64', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '230424', 'EID': '488f1f35-9e92-4996-85a4-cc587994bd02', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '240424', 'EID': 'd5927e83-1534-485c-9ac1-3e79c33b4895', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '250424', 'EID': '85c88d02-7d97-40cc-9739-4873b5a00cab', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '260424', 'EID': '9bb56e87-e822-44f7-8427-c667137f6f84', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '290424', 'EID': 'c7cb2e70-58eb-4937-aedd-1a0db8c5dddb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '300424', 'EID': 'c455c333-a0d7-4079-9313-651e5e190ba0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '010524', 'EID': '11cb372b-1ab6-438a-ba02-b467e5c0f9f9', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '020524', 'EID': '85e51b98-b263-4138-b4ea-2b641c889508', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '030524', 'EID': 'e4e7afa9-47dd-4e3c-9053-d8601ead8eb1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '070524', 'EID': 'cd14cece-cef0-4fc7-aafa-1664898cf145', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '080524', 'EID': 'bfa34f53-058a-4516-8f96-a8fcb04ade1d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '090524', 'EID': 'd5638791-f527-49e6-9776-78e9cb733900', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '100524', 'EID': '29a297f8-7818-4e46-b89a-57a90a22c826', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '280524', 'EID': '3ec0e0ac-a2ce-4d26-87ab-b89f741f0ee0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '290524', 'EID': 'ee1d1d58-45e8-48ec-a135-aea27fc9a9d8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '300524', 'EID': 'e71f9e0f-d334-49b2-840e-fb1e5081b56a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '310524', 'EID': 'a75a0f51-65c8-48d7-9e47-0a207c49656f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '030624', 'EID': '73dd127a-c233-4848-a789-e0768a0c6a3e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'RSP-quadrangle', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'RSP', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_072', 'Date': '040624', 'EID': '3eb7903b-54a8-4d35-b4fc-8992cde9d62b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, # freezing
    {'Mouse_ID': 'SWC_NM_072', 'Date': '050624', 'EID': '7f7e966c-56c3-4fa7-b430-b324fa707af3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '060624', 'EID': '88f4fbf9-9dc1-4031-a641-15911721c440', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '070624', 'EID': '4e04f6cc-5ace-4993-9a64-4a418672d6da', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '100624', 'EID': 'cb64de66-f749-4664-b9d3-d26489e271e1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '110624', 'EID': 'b40f3329-6a02-4df7-9570-3d6fee26cb93', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '120624', 'EID': 'b505a85c-9612-4f75-b64f-33722f94b7c7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '130624', 'EID': '963cc308-96f3-4be9-9ace-f78fd41cf92c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #first day of masking stimulus
    {'Mouse_ID': 'SWC_NM_072', 'Date': '140624', 'EID': '78a0ee20-c1ea-43a2-b561-f4a6ae99223f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '170624', 'EID': '5f5fa4ab-0dd5-4df6-ba64-f707f82df638', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '180624', 'EID': '579b9718-8255-4b90-af09-1f5b4dc9cf61', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '190624', 'EID': 'd20bfba3-383b-462a-bc2c-135806d9a486', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '200624', 'EID': '0c910b13-2b55-4a7b-aa95-8b39f60557fb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '210624', 'EID': '970c4bcd-5a46-4d4b-bc4e-b2e93075501b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '240624', 'EID': 'e8448c2f-d2e3-48e2-bed0-407815bba120', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '250624', 'EID': '69845bb7-2a57-41d7-98ab-61b8c5b14b99', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_072', 'Date': '260624', 'EID': '22591fc2-4871-4a41-9ff7-1065475cf66f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_071', 'Date': '050324', 'EID': '4024d778-f840-4060-b5ee-d32a9c471ec5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '060324', 'EID': '58751cd1-2b46-4220-a067-0ee5673bc40d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '070324', 'EID': '0a293882-b29f-44f0-9799-8b3a78e282ab', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(15,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '110324', 'EID': 'bd6bbfe0-0390-4d1a-b132-127e82e98e09', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '120324', 'EID': '31a9d3e2-7a58-4228-b814-74c8e2d404d0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(23,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '130324', 'EID': '3a8ab779-363e-4681-b855-f897fa4e6d18', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(17,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '140324', 'EID': 'c118dbfb-39ec-4ef8-9ed1-959748b4192e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '150324', 'EID': '95794d97-dd6d-411e-92a2-e4d4839b1165', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(8,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '180324', 'EID': '617babd9-e386-487a-87dc-6469326785cc', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(12,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '190324', 'EID': '12c6443d-b514-4395-aa1a-8faf2bd4ffa7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '200324', 'EID': 'f10a88fa-467c-462d-8be1-cf062d6b9a4f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '210324', 'EID': 'b8f6a17f-5965-4ee3-98ac-60be1504ba04', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '220324', 'EID': 'c7301a1f-5bd0-4606-8b7d-f6580672e562', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '250324', 'EID': '539e8157-7f97-4487-95d6-5486db2f6b4c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(16,9999))},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '270324', 'EID': '5a41494f-25b9-48d4-8159-527141bd4742', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(16,9999))}, ### ZAPIT log data missing for this session?
    {'Mouse_ID': 'SWC_NM_071', 'Date': '280324', 'EID': 'ecbc6cfb-a420-4025-bc8c-9059b8505999', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '290324', 'EID': '14f386c3-6765-4642-bdcd-e6d8884a5787', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '030424', 'EID': 'e48e9a69-a954-4fe4-9c23-a2a8fb7a066c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '040424', 'EID': '926a8b06-d9d6-4076-bafa-05f3405698b8', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_071', 'Date': '040424', 'EID': 'f3477c74-b1e0-47ef-9acb-bc72322096a6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(15,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '050424', 'EID': '7b3a7b4b-70ec-4689-a53a-6d2f884e6d74', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '080424', 'EID': '6ce0f240-8ade-4af5-afc2-6de6e0028bbd', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '090424', 'EID': 'a941a864-1cd2-41b7-8f60-e3df645c1a45', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(3,9999))},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '100424', 'EID': '7708935a-44f5-4f9d-be8d-0dcf7fff77da', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '110424', 'EID': 'e5e0474b-9370-4a9c-86d0-6bac9cfff05c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))}, #unclear why not loading?
    {'Mouse_ID': 'SWC_NM_071', 'Date': '120424', 'EID': 'cc662a35-4cbc-420c-a017-4995986bc5a4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '150424', 'EID': 'b5124dca-6fb6-4666-a759-2ecd0bd9218d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '160424', 'EID': '7b64d2f9-8e26-4a27-b50e-8ba9cd7e5184', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '170424', 'EID': 'a2c8be14-0001-441a-adb9-9e8ad5047a91', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '180424', 'EID': '93aee973-a843-46ad-ad45-8eee317d1a72', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #unclear why not loading?
    {'Mouse_ID': 'SWC_NM_071', 'Date': '190424', 'EID': '5041a0a8-84ed-497f-87ad-6ae6349b8306', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '220424', 'EID': '63d7ecf2-ee20-4af4-ad60-917022c48a07', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '230424', 'EID': 'ed5004dc-7489-462d-80c3-857f3977fdeb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '240424', 'EID': '0fd9bc09-0ced-4196-86fd-9d71bbcdad90', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '250424', 'EID': 'abb6dde2-47c4-4cf3-8e20-75a8229985ca', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '260424', 'EID': '98c3c1e3-be3d-42da-a977-20a98be9b0f1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '290424', 'EID': 'a8264463-6867-44ca-b195-ba36c71f5b06', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '300424', 'EID': '10c4b9db-8cc8-4bce-988c-c5a6391fd2f1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '010524', 'EID': '5181e5a7-ab4d-4fc2-978a-151ada7ac5af', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '020524', 'EID': 'd877c1d3-61a2-4eca-9daf-cf30600e6115', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '030524', 'EID': '3e2f49c3-1590-4874-adc6-c68c518e7baf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '070524', 'EID': '86e24147-7d3c-42e8-ad62-b82497e6e9bc', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '080524', 'EID': 'a911eeda-f400-4030-b3c6-73207d779fe8', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '090524', 'EID': 'd0bff1e3-acbd-480f-820d-01a2b802855d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '280524', 'EID': '513d567e-cbe7-4889-beee-8dce75693c46', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, # freezing
    {'Mouse_ID': 'SWC_NM_071', 'Date': '290524', 'EID': 'f1a212b9-e6c0-4dc2-bd9c-5c27c3b42c18', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '300524', 'EID': '06a244bd-9e57-49e2-8fda-cdbc888c4243', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '310524', 'EID': 'f429d2cf-a5d8-4c3e-8807-176128601d53', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #not loading?
    {'Mouse_ID': 'SWC_NM_071', 'Date': '030624', 'EID': '1c4fd7f7-6b72-4273-96f9-c0d255193170', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'RSP-quadrangle', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'RSP', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '040624', 'EID': '396137b0-f2b9-4a87-bcec-66b5e19450eb', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #not loading?
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '050624', 'EID': 'ad7d566c-a9f7-4d1b-8c92-126bd3142c79', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #not loading?
    {'Mouse_ID': 'SWC_NM_071', 'Date': '060624', 'EID': 'aa3edfa1-5a55-4079-96ea-80ef8f5bcb95', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '070624', 'EID': '18294d0f-4d0e-442a-a099-26d10d5ec493', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '100624', 'EID': '98e221dc-e3bf-4970-832c-7685214a2bf2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '110624', 'EID': '2a009253-f4b1-492d-8f31-23aba0d32b9f ', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '120624', 'EID': '2499872a-0fc5-47bd-928b-f59edcb299d6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '130624', 'EID': 'a8ec46f3-0c2b-4c3f-91d8-17828c5aaf59', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '140624', 'EID': 'a10cdb6b-f044-4040-9e0d-51a7dfaa1e86', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '170624', 'EID': '053bf690-e0a1-4743-af69-747999975b78', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '180624', 'EID': 'a21a94cb-9731-470b-ab32-0e780a2118a3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '190624', 'EID': '4cfc10dc-cd1d-46a9-b726-05bf5d14a942', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, # freezing
    {'Mouse_ID': 'SWC_NM_071', 'Date': '200624', 'EID': '873134ba-4723-4895-b9ed-a23a72a1c2ec', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '210624', 'EID': '892c68f1-0eb6-4ddb-9b39-47be3f9a937a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_071', 'Date': '240624', 'EID': 'd85133a7-e449-43a3-9529-8f176742bef0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '250624', 'EID': '28eada18-4860-48a3-b238-774ca2b9a5ea', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '260624', 'EID': 'c13b4708-6f17-4c0f-ae1f-9ad27ed70a47', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'none', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-16', 'EID': '72ad6aba-78cd-461e-9400-a14f4052807e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-15', 'EID': 'e605fa1b-14c9-45be-9d46-2c8b9f92d2ea', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-14', 'EID': 'ca58a8db-8817-4cd0-acb8-1712191949a7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-13', 'EID': '89ead274-0247-49b0-95b5-f6aa77b9431c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-09', 'EID': '66e34ece-416d-471a-a3af-878f06fdae22', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-08', 'EID': 'f88fc8aa-b95b-4b28-94e7-4da50689a1cf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-07', 'EID': '8cf213e9-f60b-4b81-b268-bc95fb61cdfe', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-06', 'EID': 'f3818e1f-51c4-477e-bbea-783f77f84843', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2_3pointweak', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'AnterolateralM2_3pointweak', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-08-01', 'EID': '6b480c09-af07-4574-b04f-9ed2b862318a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackMedial', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'FrontBackMedial', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-31', 'EID': '7ec24b48-a65e-492a-89ef-142dace45da5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'AnterolateralM2', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-30', 'EID': '3fce4e6c-1408-4fde-b95d-72a75b4e63da', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'AnterolateralM2', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-29', 'EID': '29bd566b-2163-4934-9a32-4fd45b85f7bb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackLateral', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'FrontBackLateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-05', 'EID': '3f792775-5f93-4e15-969d-9d8deb8d4b19', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-03', 'EID': 'e9f298e0-744e-4d7f-b042-7a02ff524838', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-02', 'EID': '4650da81-e01e-4db4-89a9-a74d1b9ab953', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-07-01', 'EID': '461f1dc8-4463-4705-bce3-70fb28d24275', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-06-28', 'EID': '12f2c51a-f66c-4792-a7e2-f1696fccca1f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_071', 'Date': '2024-06-27', 'EID': 'c48a16d9-3532-4812-8a79-debc28a83b01', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_057', 'Date': '280224', 'EID': '6a705a8b-a1e2-4b6c-a765-e01c39c35a94', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '290224', 'EID': '517d3788-0906-40da-af96-4ed951296b8d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '010324', 'EID': 'c7e85573-63b6-49ec-9475-cc99f44cee74', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '040324', 'EID': 'ceee000f-6d6e-4163-9425-88df522e7d91', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '050324', 'EID': '25bb7cc2-efec-4924-9e39-658d981964c9', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '060324', 'EID': '451dc3c4-cd0c-4789-8b6c-6b5e99243ffd', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(136,9999))}, #ALF object not found: trials
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '070324', 'EID': '39c0dfe8-7432-41db-b780-1b0a1ffea698', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #ALF object not found: trials

    {'Mouse_ID': 'SWC_NM_057', 'Date': '080324', 'EID': 'b8d63536-7330-40ac-883a-7bf3da6b0215', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))}, #ALF object not found: trials
    
    {'Mouse_ID': 'SWC_NM_057', 'Date': '110324', 'EID': 'a8a607ec-2e79-44ca-b38f-0b367cbf0fb5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### ZAPIT log data missing for this session?
    ### sessions were commented up until here and I'm not sure why
    {'Mouse_ID': 'SWC_NM_057', 'Date': '120324', 'EID': '97915622-0f89-4357-bff5-25886315629b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(9,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '130324', 'EID': 'a3cf97cc-13ad-4c5e-a5b7-1ae883d93de7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '140324', 'EID': 'ff977130-b37f-465c-b5c5-ba21e206b836', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(345,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '150324', 'EID': '746863ce-00c2-4009-8aa8-bba5c7e32256', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(14,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '180324', 'EID': '24f1a7d8-3de1-4767-b950-a38e18e4dd73', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(14,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '190324', 'EID': '00ffb81e-c8f7-4643-af92-e067f6b604a4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(3,9999))}, #ALF object not found: trials
    {'Mouse_ID': 'SWC_NM_057', 'Date': '200324', 'EID': '1f30356e-2cce-49a5-a1a4-c0de4fbc6fa1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '210324', 'EID': '68ce3728-3156-40e7-91f8-1a76061619f5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(6,9999))},
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '220324', 'EID': '96c6eed9-5776-4e1e-9e1e-409174c781df', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #tried raw session
    {'Mouse_ID': 'SWC_NM_057', 'Date': '270324', 'EID': '9b513427-d32c-4934-a2c3-5b20b2fb7e55', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '290324', 'EID': '21d33b44-f75f-4711-a2c7-0bdfe8eec386', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(16,9999))}, ### ZAPIT log data potentially corrupt for this session???
    {'Mouse_ID': 'SWC_NM_057', 'Date': '030424', 'EID': 'ae7f6bc7-f36a-4308-9aa4-cb82fb4bf4ef', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '040424', 'EID': '7b1774b1-bad3-4784-a4fb-7f59b77426b3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #below threshold performance
    {'Mouse_ID': 'SWC_NM_057', 'Date': '050424', 'EID': 'f009b0ca-ec49-4796-bb42-1731b9f90b07', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #below threshold performance
    {'Mouse_ID': 'SWC_NM_057', 'Date': '080424', 'EID': '914910b3-fafc-4ce3-9eeb-ef6c70d4d7dd', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '090424', 'EID': 'f5a77da9-3613-4b14-b5e7-0c537e4ecb7a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '100424', 'EID': '6138ed1d-a533-4923-94bf-411e202e2c91', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '110424', 'EID': 'd14830ce-c94d-48a6-a687-d9ca468beed4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(8,9999))},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '110424', 'EID': '959a059f-3e98-47e3-99ff-8cef99190605', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '120424', 'EID': '55bb7eea-8e4d-4788-af5d-06e1b0423afe', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '150424', 'EID': '04c46a39-bc2f-42fc-9ce2-d48adf8fc545', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '160424', 'EID': '33760c33-10f6-4670-8c4c-a35c2c274019', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '170424', 'EID': 'a01456bd-810d-44d3-afc8-e6251efa5399', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '180424', 'EID': 'e70af17a-00c3-4549-979d-c06bfb1deb21', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #unclear why not loading?
    {'Mouse_ID': 'SWC_NM_057', 'Date': '190424', 'EID': 'd99a3f2a-b9da-42f2-851d-bf6cd57e752e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '220424', 'EID': '326fc4e3-5de2-4426-a270-6ad33bc72bf4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '230424', 'EID': '860172ec-22bf-4bdf-aee7-1a9e85536e59', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '240424', 'EID': '5378cb09-a3ed-4e13-873c-e0653e97ed8a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '250424', 'EID': '3ce30db9-6acd-4d4f-b3ef-cdae72193cca', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '260424', 'EID': '6cc5b3d5-653b-45a6-b2d8-851e40172017', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #tried raw session flag
    {'Mouse_ID': 'SWC_NM_057', 'Date': '290424', 'EID': '30cca44f-fa68-41d4-ad4a-1d3b41178860', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '300424', 'EID': '63cd8105-e388-4d22-a396-f1e5f597b392', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #unclear why not loading?
    {'Mouse_ID': 'SWC_NM_057', 'Date': '010524', 'EID': '48f93196-a573-4e46-95ee-08fc9484785c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '020524', 'EID': '4fe120ac-7da6-49a1-88ae-8326f93aff5b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '030524', 'EID': '371667a3-635b-43aa-a74d-d35a164387a6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '070524', 'EID': '0a2ff699-db3f-4b39-a24e-394153403c15', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '080524', 'EID': '27ed63de-c2d4-4efd-ba0d-7d29c4e7eb3c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '090524', 'EID': '9e0fe336-8409-4187-b89f-e45b3718d125', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '100524', 'EID': '69670d64-f5e3-444a-b25d-ca77e9233480', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '280524', 'EID': 'b0229669-5d43-4558-bcb3-3f11d23430d4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '300524', 'EID': 'f2d64f81-1f89-46d9-9e84-f7aa2613bf96', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '310524', 'EID': '35bdb284-f5c5-4bb7-a1b1-0e84505fedf2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #not loading
    {'Mouse_ID': 'SWC_NM_057', 'Date': '030624', 'EID': '303904fe-4a51-4d32-a1bb-b0b4a0d97861', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'RSP-quadrangle', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'RSP', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, # freezing
    {'Mouse_ID': 'SWC_NM_057', 'Date': '040624', 'EID': '1db797cb-20c3-46e0-85f0-4726e6583b81', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '050624', 'EID': '9da10bc1-6e6d-40a9-b387-285b509e9bb6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '060624', 'EID': '6793cda3-d753-4d5b-9043-f00e7eff4cba', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '070624', 'EID': '89bdad9f-7eff-4fac-86c1-9a9154fa7fca', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '100624', 'EID': '9496c947-84de-47d5-b8b3-25f4d7dc03e2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '110624', 'EID': '75202410-a01a-4730-ae3e-f647887120ff', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '120624', 'EID': 'a3dda1d9-372b-4d58-a6b9-7f549fb01709', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '130624', 'EID': '504030da-9e68-4e26-9c68-0efad8a8bec4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_057', 'Date': '170624', 'EID': 'fbc97f6f-4be8-4fe2-8d99-caa2935045b6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '180624', 'EID': '0bbfbe3c-8db2-4f69-b82d-4c74be5fbb6c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '190624', 'EID': '2a8d18e5-42cb-4b24-bd39-bcc1f2fa16d5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '200624', 'EID': '646e3bc6-9b24-4ad2-8226-1f6d6e74fd6c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_057', 'Date': '210624', 'EID': 'f51ef757-6a15-43bb-b7cf-d6fd6561d61e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'ephys_validation', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'ephys_validation', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_058', 'Date': '280224', 'EID': '4a18049a-0092-4a2f-8391-579355874b57', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '290224', 'EID': 'dcc0706e-722e-46d5-ab1a-17bd68ffee97', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  ### ZAPIT log data incorrect for this session? take a looksie
    {'Mouse_ID': 'SWC_NM_058', 'Date': '010324', 'EID': 'd3b5372a-cad8-4523-bbf6-1ee8358b837e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '040324', 'EID': '9d4e8626-8934-4df7-b914-ab5d060e6f10', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))}, ### ZAPIT log data missing for this session?
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '050324', 'EID': 'bc3ad39f-ad91-49e5-8427-30e432dcb18d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### ZAPIT log data missing for this session?
    {'Mouse_ID': 'SWC_NM_058', 'Date': '060324', 'EID': '60bcdd38-9c33-4d96-8851-512efad238cf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '070324', 'EID': '3bc290dc-ce10-4896-90e1-3e66069d96fa', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### ZAPIT log data missing for this session?
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '110324', 'EID': '4ee94651-4238-4aa1-aca5-86bcda82b6d2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### ZAPIT log data missing for this session?
    {'Mouse_ID': 'SWC_NM_058', 'Date': '120324', 'EID': '4234bb64-5beb-4688-8b18-9b06988f9bf1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '130324', 'EID': '04f0abcc-e142-43e2-8b8d-95f822108332', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '130324', 'EID': '92f629af-9a0e-459e-825d-b07994097af9', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #not correct session number? take a look to see if data can be recovered and given correct number
    {'Mouse_ID': 'SWC_NM_058', 'Date': '140324', 'EID': '2293f315-a58f-47cb-a8b3-1a49d5b21fd1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '150324', 'EID': '842680fc-6344-4359-9507-864511682c33', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(8,9999))}, 
    {'Mouse_ID': 'SWC_NM_058', 'Date': '180324', 'EID': 'e81e1244-7986-4660-8cb0-6838e7cf69e3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))}, 
    {'Mouse_ID': 'SWC_NM_058', 'Date': '190324', 'EID': '52863e85-3496-4f29-8438-fd4f7510ca1a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(21,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '200324', 'EID': '9de7240e-fcd0-4811-840e-7a313011c93f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(5,9999))}, 
    {'Mouse_ID': 'SWC_NM_058', 'Date': '210324', 'EID': '0074fb83-203c-4ca9-b4d9-b726e40ed68c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(8,9999))}, 
    {'Mouse_ID': 'SWC_NM_058', 'Date': '220324', 'EID': '32b8c735-bbec-4af9-9eb5-8368890fbeae', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_058', 'Date': '250324', 'EID': '5e2b68cb-ea4e-46c1-9393-1c903c496a9c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #no data on server
    {'Mouse_ID': 'SWC_NM_058', 'Date': '270324', 'EID': '7e7fb5a0-5bb2-4624-a071-c54f23a3de86', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '280324', 'EID': '1be03bb9-6ce3-4508-a02f-26a302bb6d12', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '030424', 'EID': 'd406c461-d724-4d4d-8861-65f33fc6a3b5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '040424', 'EID': 'bb16ba38-34f1-452c-84a5-ca910b49b2cb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '050424', 'EID': '3c50aa42-f734-4c62-83fb-d548a443ddb2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '080424', 'EID': '5e2652b8-a3be-43e7-ba97-3097f4cef637', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '090424', 'EID': '25df56f8-5d2f-47b0-9d02-766ac936702e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '100424', 'EID': '05aea529-b4ef-4d53-a6e7-16ceb757d7d5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(8,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '110424', 'EID': '82518ed0-469f-4311-aedc-fad2c9d5ea0b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '120424', 'EID': '6a44a4b7-4041-4e74-8477-da40f28cc1bc', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(9,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '150424', 'EID': 'e0913c11-ad2e-4fb9-a2ab-70f041fc624c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(2,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '160424', 'EID': 'a0fc0a1b-6fe7-46f6-a731-4fa4cf334459', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '170424', 'EID': '54a710b5-5985-44aa-9a7e-c36976621dae', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '180424', 'EID': '8df5a96a-c4ec-4f1c-bb63-c232fb598607', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '190424', 'EID': '2fb64c24-a802-4c67-9ef8-63c0b5e94239', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '220424', 'EID': '8ad0b793-0faf-4ee6-ba4e-fd0ac99f14bf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '230424', 'EID': 'e2a4db4a-352f-49a2-80bf-3e5dc3e81fe9', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '240424', 'EID': '42097ae3-6c89-436b-b1f6-531706602faf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '250424', 'EID': 'b002842b-7101-46e6-a585-72dc08e0265f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_058', 'Date': '260424', 'EID': '5633930b-0d8d-439d-9329-baf9b93423e2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #tried raw session

    {'Mouse_ID': 'SWC_NM_081', 'Date': '070624', 'EID': '2fb4c72b-093b-4cd1-92d0-08b5b2377646', 'Hemisphere': 'none', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'none', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '100624', 'EID': '588da2cc-15a1-4bb9-8898-0e373e1cd92a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '110624', 'EID': '7dfd1974-1618-496c-9b0e-ba89f9f3f160', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #first session with masking
    {'Mouse_ID': 'SWC_NM_081', 'Date': '120624', 'EID': '3d20e274-d965-429b-9198-526bb1df3ff7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '130624', 'EID': 'f59be80a-b2ef-4d3f-98fc-daf1920a6f68', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '140624', 'EID': 'fd79f350-78f1-403e-ba83-2a3233ae47a5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '170624', 'EID': '68bc47e2-12ec-4b4e-8b8a-4cbc07005b06', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '180624', 'EID': '90742c5d-dbef-4f97-9c26-cfbee9413f24', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '190624', 'EID': '16ff936f-c87b-4d1f-ad5e-96236962cdb9', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-4point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_081', 'Date': '200624', 'EID': 'c2159615-3071-4dec-a240-f04cbf1a962f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '210624', 'EID': '56c88b74-2219-47c6-80dd-43bbf5198743', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '240624', 'EID': '8833a0d2-468b-4a13-b940-a31356f39323', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '250624', 'EID': 'cc930af5-0246-4eb7-ae73-0c825fc035ed', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-24', 'EID': 'e1bcd040-be3e-4b42-ae53-5519e72c1138', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-23', 'EID': 'e44f1809-9e17-4def-9a78-b8b8988432fa', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-20', 'EID': 'a346634b-5d82-4b0d-b332-0df8d4bda767', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-19', 'EID': 'e06c7556-0586-448f-94f7-f735e9e5a72e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-18', 'EID': '5d904819-1755-43a6-9d5b-bb47aee17c95', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-17', 'EID': '8ce5314a-dadf-443d-a2d8-20e6af85e469', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(21,9999))}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-16', 'EID': '0ee2894f-29dd-4ba7-a089-292b7cbd2c03', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-13', 'EID': '1d28f538-2217-44bb-99a8-bec8bd437f49', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-12', 'EID': 'f87cebbf-d8cf-4938-9658-582d5201e932', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-11', 'EID': 'fadf5c7f-d450-45ac-8ca8-01ae773232d4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-10', 'EID': '023a1231-132a-4d37-a1df-7f06c7aefb98', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-09', 'EID': '417a81f7-222a-4dc7-95e5-189675d9d680', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-06', 'EID': '084b0e43-b736-4424-a856-c961fe9b6777', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-05', 'EID': '971510e1-87e0-4199-91a3-9105ed59fa6b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    ###
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-03', 'EID': '28f71052-e487-47db-900f-0f7d1634a3c1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-09-02', 'EID': 'c721f67a-4fed-423b-8480-4d17e59d4800', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-30', 'EID': '1af9eb1f-beb3-411d-b1cf-6e8363b9d7c7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-29', 'EID': '30dc77ad-9d38-4760-ae7b-71034f4558db', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-28', 'EID': '617d0c3f-1658-411e-84b8-1d46bfc61cea', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-27', 'EID': '19ed32db-bfc1-44ee-8743-1181d3a656d0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-23', 'EID': '55ccca2a-7b5b-419f-bd5e-fabae3efda80', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-23', 'EID': 'd1e4163e-2f90-4300-86ef-ef3bd08de130', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-22', 'EID': '4ea40850-42f6-4efd-b517-3eaa65157dd8', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-21', 'EID': 'f68a32ec-baaf-4816-b633-c3a1bf80b4e1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-20', 'EID': '9a22208a-ceeb-42e3-a97c-797b0f037efc', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-16', 'EID': 'ec790553-d67b-4b25-97ad-4040254457e8', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-15', 'EID': '2622435f-deeb-49ec-94c2-b4c57c3282bf', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-14', 'EID': 'e5f0eb8c-bfb5-416e-a070-ec13b37c60e4', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-13', 'EID': '4399db90-c883-43df-a94b-97dc5b664935', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-12', 'EID': 'b2c4bd2b-5c8e-4c18-8a4b-e8e9e49d1895', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBackMedial', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-09', 'EID': '82940d8e-ca0e-41e2-9bba-3eed7a843bf6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBack', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-08', 'EID': '636e9324-0434-4422-a584-4e7a5324ad63', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBack', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-07', 'EID': '1a4d2532-3aae-4a96-a790-9c3920a34bd1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackLateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-06', 'EID': '4569efa8-dc24-4f03-88ef-94d0f96c5f2d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackMedial', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-08-01', 'EID': '319c04c0-25b9-4550-a962-cb12561752cd', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2_3pointweak', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-31', 'EID': 'd8381daf-2ec2-4315-9191-e06a2dc79055', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackMedial', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-30', 'EID': 'f84bc6b7-d419-4c5c-afdb-cb7cf0847ef2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-29', 'EID': '1b2f1edb-2b13-4d9d-8d4b-8bf57cf4be83', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackLateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-05', 'EID': '114031ac-51af-4afc-b93f-1c845c3d5f84', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-04', 'EID': 'd0a1186d-cf12-42fb-9937-ae4036197f4a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'PL-2point', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-03', 'EID': '9087e545-269b-454a-8dce-90ea449ef7a0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontFront', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-02', 'EID': '0afb230c-1cf1-4e98-b28a-c88de5e1405d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBack', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-07-01', 'EID': 'df35f035-6e52-4c9d-b492-d5026f4ff946', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBack', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-06-28', 'EID': '17a0cc7a-248b-49da-9056-6c627ce2d587', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBack', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-06-27', 'EID': '23e9ed4a-4f7b-47a2-807e-87fcac571f63', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontFront', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-06-27', 'EID': '985a0bca-ac8c-4bf9-8277-626dfaea8626', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_081', 'Date': '2024-06-26', 'EID': '1d6aa420-c44f-4998-9c9b-2634df455056', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-10-01', 'EID': 'b9144091-420f-4a4b-b896-002d65fa07d0', 'Hemisphere': 'both', 'P_Opto': 0.7, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-30', 'EID': '18f881f8-da77-41fa-9d04-72e5d6980ab2', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-27', 'EID': 'e7c55eb5-70d2-47ed-be6c-1eb04d024dd6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-26', 'EID': '3f56b55e-33f9-404a-9de5-8cdd91028856', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-25', 'EID': '0962661c-301c-49bd-8143-3ecf226c0804', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-24', 'EID': 'b3ecffcb-cce3-4649-bb6d-6426e3442e57', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-23', 'EID': '3a7840b6-9283-4bd2-a3d1-16b377fa1d7f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-20', 'EID': 'bc3b3cb8-e526-4d30-bfcb-1e5320938009', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-19', 'EID': 'd2e1be73-5f46-4eb2-80b0-a1ca9ad19f8a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-18', 'EID': '9826572e-e0d1-4abd-ab76-a05541469b54', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-17', 'EID': '49720c45-6130-4f3b-aeb8-d0c38c13e087', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-16', 'EID': 'c88820b6-e3cd-44b2-bd98-2d0ccfb8d8ab', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-13', 'EID': '10014c6c-c903-4510-963d-c1310ce567e7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    #####
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-11', 'EID': '54b2b629-537a-4a8c-a584-93ccb71c9645', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(4,9999))}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-10', 'EID': '0750678c-c2a3-4a3f-b7b5-7a556c3baa3c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # #####
    # #####
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-05', 'EID': 'c0efd96b-8a4c-4eaf-b5d6-281f6dae4b7e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(65,9999))}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-04', 'EID': '13d909d4-9361-419e-813c-2958e52addf7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-03', 'EID': 'f6864aef-e9e9-4eca-b9cd-143f73886a4b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-09-02', 'EID': 'bd9b8aa3-e80a-4d6c-8845-f293b59b9e94', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-30', 'EID': 'ce8d7b48-22a6-4b8d-b3ca-19101174f1e1', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-29', 'EID': 'ea066425-3994-4182-98e8-e78ff08b5d5e', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-28', 'EID': 'cd1b600d-00e2-4542-a94e-1864237342ac', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-27', 'EID': 'b44d3c9a-93f4-47e4-8f4f-45870519e80d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-23', 'EID': 'fa9315db-a903-4ab2-9317-e092ef98cd83', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-22', 'EID': '6f4a4ca6-5933-439a-ac3e-a7af05ee5f8c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-21', 'EID': '3e16843e-4d15-421a-8e38-eb862aa09e0a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-20', 'EID': 'c6e05a2f-6500-4d42-a317-7a2398e3c0f0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-15', 'EID': '91038046-b631-4424-abef-00dc331511f3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-14', 'EID': '57388eb2-2bbf-4f9a-8c3d-43cf6a72fb2a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-14', 'EID': '8e146cdf-a627-4d51-8894-3c4055f90beb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-13', 'EID': '6ac687b8-a991-46f6-a571-8ba695a5c51b', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-12', 'EID': '65d7c1b5-c17c-4c15-a738-e18969a4b33d', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBackMedial', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-09', 'EID': '0e62d042-def5-42d6-870e-6f88bd9f8dbb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBack', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-08', 'EID': '490c23d3-f9ef-49b2-bdf3-fe493a1d1623', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackBack', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-07', 'EID': 'c908300c-d600-4b0b-baea-27e427a1722c', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'FrontBackLateral', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-06', 'EID': 'fdd83585-f74e-44c7-b7aa-876b2d358daa', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'AnterolateralM2_3pointweak', 'Laser_V': 1, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-08-01', 'EID': '35581c37-e576-4394-8195-24136669edaa', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-31', 'EID': 'cc161745-bc5f-437f-9e4d-aaa5f60cedb3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    #####
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-29', 'EID': '1ad8c12b-6158-49a8-9b4f-1518c5dc0433', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-05', 'EID': '7ddc484c-ad74-488b-bb17-8b1034ccefb7', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-04', 'EID': '1e02a748-1f58-42f6-8e8b-e06e335c9c23', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-03', 'EID': 'e458efaa-2569-4cc5-a59e-acbba79568dc', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-02', 'EID': '63d83965-e02f-401e-9469-03d979d077f5', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-07-01', 'EID': '9e63140c-094f-4ab0-b33e-a2682af47a8f', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    ### check session 002 eid once extracted
    # {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-06-28', 'EID': '883826c1-3a26-4d3d-8fab-eb0ef0792ecb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-06-27', 'EID': '6e5baa0d-c3d3-412b-a2c4-4f0167ed79da', 'Hemisphere': 'none', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'none', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_082', 'Date': '2024-06-26', 'EID': 'cbc8839b-9820-4f63-bf3b-b05ec6d8b939', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-10', 'EID': '59af6af8-fa5f-42fe-84a9-755e83c9314b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-09', 'EID': 'c18f821b-eb37-440e-9f89-07f0aada683d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-08', 'EID': '12965ed5-8d47-407c-96e3-4a9579ca548d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-07', 'EID': '0b1a7c9e-36ce-4370-a8df-ae6ce3d49bdd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-06', 'EID': 'e7ab04b3-cb02-4e5e-a54a-c5119e3105bb', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-03', 'EID': '4f8c6d55-921c-47a3-a029-1ee9a8e3f7cd', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-02', 'EID': '07fc3997-620a-45e0-abed-cc4c0bcd66f6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2025-01-01', 'EID': '78ed1b73-386e-4f26-8efb-857356233d00', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-31', 'EID': '081cb963-1bd3-4182-b685-9da5c308e71b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-30', 'EID': 'fb6ad2c6-3a78-4763-bb40-40f6c959964d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-20', 'EID': '0d2c18f4-5360-46b8-ac60-996bfb97f59d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-19', 'EID': '3cf380ef-4209-41da-b425-e64bd0212169', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(65,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-18', 'EID': '2eef12b7-def8-4bdd-8c4b-166e2eef059a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-17', 'EID': '4585378e-6d33-48c7-8d4b-aea6671fcb8d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-16', 'EID': 'e4c5fadc-e7d9-4e03-b772-6980109ba5f3', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-13', 'EID': '6fce2eae-965d-49d6-9b5d-60316cf5d260', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-12', 'EID': 'fccf8f8d-d8de-4fb5-8021-8c451ac26d61', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-11', 'EID': 'fc1ddebd-3365-4301-bb94-538b7f33d3c4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-10', 'EID': '296344c7-fb61-4d34-b732-6d0aa308fcd7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-09', 'EID': '3386e5b5-815b-4c24-9b13-4a8dad6ec321', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-06', 'EID': '0e26b069-d530-46c7-ba0d-9e4f3f973ff8', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-05', 'EID': '14629fee-ebcc-4ed8-9612-cc7654936e17', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-04', 'EID': '47653f0e-6858-4a74-92cd-a8ae5837f617', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-12-02', 'EID': '12ba99b8-c705-4548-85dd-facca35b0346', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-29', 'EID': 'ea769a04-61bb-464d-9e70-0bca05697ce1', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-28', 'EID': '3c27738f-65dd-492e-bf49-5dbd11c1f374', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-27', 'EID': 'bff9e217-49fa-4037-9895-0de60696d92f', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-26', 'EID': '514153aa-98c8-4559-bc12-442e93ecd5c0', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-25', 'EID': '931ad575-14cf-4aa1-89a1-768ae43db45a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-22', 'EID': '4a6b8509-cc65-4a3f-bbe2-b320b26e73bc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-21', 'EID': 'a159c54d-767c-43da-9aba-a595926d88a4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-20', 'EID': '87e1051e-a6bb-47d0-9ab2-8bec0efdecf2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-19', 'EID': 'd426b002-ff10-4861-a460-9518fc49834d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-18', 'EID': '88afa934-5374-45fc-bdda-77c45ba52cc3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-15', 'EID': 'a2c97656-fb3d-4587-9980-c0ad26a712c0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-14', 'EID': 'dc247ecb-001d-4efa-9a52-4a331f9551bc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-13', 'EID': '18ed3660-3f19-42b2-8074-a5fc1a38822e', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, #laser not on
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-12', 'EID': 'c11808b2-e37f-4e32-8557-4e5789356d90', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    ### session from 11/11?
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-08', 'EID': 'b3571586-df64-4fef-a7fc-c29e5b2c8a2b', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-07', 'EID': '388c2e40-19cc-4de5-9f63-387c427d1fa9', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-06', 'EID': 'd896a03e-2994-4676-bab7-e0bd1160fe9b', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-05', 'EID': '960f2fb8-d2de-4dc9-89a0-6d8498e5658a', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-04', 'EID': '8b746ff6-eccf-4071-a78a-f2897ee8d688', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-11-01', 'EID': '6ea09269-412e-45e0-a2cd-4ed25057e2c6', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(4,9999))}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-31', 'EID': '2e70831c-41a2-489c-b242-94e9893287cd', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-30', 'EID': '6614827e-4fa2-4911-9ef6-f6a75e135d5e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-29', 'EID': 'a04a6503-116b-48c9-a8cd-ced434b03c0d', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-28', 'EID': '15db050c-de59-4cee-94ea-c1e630a89cce', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-25', 'EID': '20d7077d-da54-4753-9dd5-12da062aa784', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    ### not sure why not extracted?
    # {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-23', 'EID': '5996464a-7c61-48c6-93f1-7d5aad4ed47e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-22', 'EID': '51a755af-aef2-42cd-9ed4-0755bfbc4ad0', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-21', 'EID': '513c4259-7023-44b3-a371-d28e5c081326', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-18', 'EID': '8d7d34e1-6613-4e37-b4e8-8d38347c5141', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-17', 'EID': 'dcf05b87-72c8-46a4-ad1b-b2dbb5909f5e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-16', 'EID': '99ec3503-d0c7-4c87-b0e3-901b240af919', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    ### not sure why not extracted?
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-14', 'EID': 'c11d4536-8b6d-4815-bdff-8053256a75b7', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-11', 'EID': '647286b0-22ef-42d5-a502-c4529ec6dafb', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-10', 'EID': 'e27b3878-2914-416f-99dd-9d4a46d58b8a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-08', 'EID': '632ce799-4023-4c4b-9fda-21825edbf287', 'Hemisphere': 'both', 'P_Opto': 0.6, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-07', 'EID': '625120a5-9cf7-40af-8b38-adad129c6891', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-04', 'EID': '0998f766-ee7c-4795-ae75-07d712ae66b3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-03', 'EID': '0df1c8ed-3d0b-4dac-ac5b-1ea2060869f0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-02', 'EID': '580100e9-94f1-4542-9183-f0b5234b29a3', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-10-01', 'EID': '93608635-6b1d-45df-a484-18ef6f17a937', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-09-30', 'EID': '66a8f4ea-f783-494d-a154-96f077a9852a', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-09-27', 'EID': '95704630-82ff-4a83-b583-e47e7b261df0', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-09-26', 'EID': '65ea4186-ca91-4082-9e72-282dc83b7fbb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_085', 'Date': '2024-09-25', 'EID': 'b16c50ac-7ee9-4a38-b775-801bf5f83495', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'none', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 

    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-10', 'EID': 'a1d88cbc-ac86-4649-afef-5ac579f8e5a5', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-09', 'EID': '492241e2-6d50-4b2e-be20-74f6c9072b93', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-08', 'EID': '3879f37d-980f-4edf-9798-ce12aa457847', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-07', 'EID': 'a65aa3be-0521-45be-b979-b8b262d37d49', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-06', 'EID': 'f48f1c90-056f-471c-be3e-98c61763ece2', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-03', 'EID': 'f99a7ba5-5afa-418e-ba4c-a8819d39a528', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-02', 'EID': 'a0f828ce-1ef6-428e-a65c-ad3010ac482e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2025-01-01', 'EID': '2fbd3b7b-db18-4e00-a118-602aa912a682', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-31', 'EID': '851a3966-a5bb-4a36-9a69-45c9ce743628', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-30', 'EID': '92521a6b-4ecc-4617-aa27-ea4edab804e4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': list(range(10,9999))}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-20', 'EID': '17e111a2-34be-4fdf-ae9c-d25f3dbf500a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-19', 'EID': 'a3f7d1da-d3ce-42eb-a2d2-e60d722b464f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    ### where's 12-18?
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-17', 'EID': 'b31fbbd9-aa6d-445d-80c4-4d56adeea1a5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-16', 'EID': 'c2ea4acb-bb23-4609-a0f9-d316875a79fb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    ### where's 12-13?
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-12', 'EID': '4630fbf2-a6b3-4443-b6da-af6a07cf0909', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-11', 'EID': '0c82a60e-0668-464c-98bc-39a7c7ff89d0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-10', 'EID': 'ca25b543-07cf-4701-a2a4-7139a5ed28c7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-09', 'EID': 'a3acb50a-97d9-4f50-b3be-e572e9ccad31', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'pMOp', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'MOp', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-06', 'EID': '1bf37f1c-a692-4109-8793-ea9a381278bd', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-05', 'EID': 'a61ec24b-6085-4f3d-9f51-4cbbce4ea8be', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-04', 'EID': 'fe425c29-1821-4511-ab25-796094608c70', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-12-02', 'EID': 'fda81aa1-f820-42cb-9fe2-dc71d20d46dc', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-29', 'EID': '9bbb497e-4a0a-4c95-b448-e34d44ee61a8', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-28', 'EID': 'fb1cc70a-75ba-4cad-82a1-ab8cc7729592', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-27', 'EID': 'ff7f00c9-4ce6-4c5a-9320-a86467066b7a', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-26', 'EID': 'fd5fee5c-9acf-4f31-87ba-8dea806d6a66', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-25', 'EID': 'c23de770-6f3c-41a8-b0c6-8c11389042c4', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-22', 'EID': 'f3fd97dd-135a-49fc-a8cd-b114efe3a238', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-21', 'EID': 'c5438bf2-631a-4021-b501-2c9adbddb238', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-20', 'EID': '0ae7e7d1-b285-42b9-be3b-daf688a80d4d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-19', 'EID': '51e6d249-847a-48a1-8379-44992997fc95', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-18', 'EID': '0f7f1e06-a597-4cbd-a409-7c2c0d40b1d6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-15', 'EID': '504a0fd0-0c1b-413e-b78a-ab3c0e8c16ef', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-14', 'EID': '226b3997-5222-47ac-a221-49a43c4a2543', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-13', 'EID': '319149f0-0aba-485e-892c-e033e5bb86f0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-12', 'EID': '6bec8bb3-fdb0-4b0c-b271-cda764daa056', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'aMOs-targeted', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'aMOs', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    ### missing session for 11/11?
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-08', 'EID': 'd080423e-4a43-4012-963d-5332b048396e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-07', 'EID': 'a3973b9f-43a3-42e0-aca8-bdc04955a4c0', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-06', 'EID': '11438296-fa41-4344-9987-69fb66fcbc5d', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-05', 'EID': '6bf5168a-657d-420e-9288-738ed5a51310', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 3, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-04', 'EID': '504ad71b-46e9-47d3-ae49-f75a4167107b', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-11-01', 'EID': '86b2fe93-2d47-4a0a-a3b1-2a4f6a6e3da9', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-31', 'EID': 'fc33d0eb-fc57-44c1-a58a-42dfb86a6e44', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-30', 'EID': 'c5649fc0-3867-4616-8068-e4f2f198ab60', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-29', 'EID': '1b91e9a4-46ea-4581-9184-f3d4532ca1b0', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-28', 'EID': 'c8ce5eb7-0773-4eaf-8ae2-e440183c831d', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-25', 'EID': 'e107d121-c253-4e12-9150-e22f4877bd94', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-24', 'EID': '55ab5631-73d8-4929-857d-38979ab5dd8d', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-23', 'EID': 'eab9579c-9830-4dbd-88df-1ef0baea22bf', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-22', 'EID': 'e7560128-50ef-4c3d-8cac-c5988e1e68c5', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-21', 'EID': 'd7aff52b-60ea-4d6e-973b-fec5c2b3b4c4', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-18', 'EID': 'ded6f278-2a54-41c3-8124-3962e8cd2683', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-17', 'EID': '1bb13c8c-aac2-439e-986d-78d3eed47f74', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-16', 'EID': '505b6370-97e9-4192-8a91-d18ce864e85e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-15', 'EID': 'ffa6015c-97c0-4479-9842-9fb8297a960e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-14', 'EID': '120ba61f-48a0-4d65-89cc-2076fbc5701e', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-11', 'EID': 'd81147d3-8198-4c71-8559-ea5aab2f358a', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-10', 'EID': '147f5dd3-f35c-409b-a503-d8914a6e78a6', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-08', 'EID': 'e03b2c10-8791-4074-8a4e-a65db5a5ea10', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-07', 'EID': '6825a34c-98bf-4643-861a-288d3545dbfb', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-04', 'EID': '02e6a896-001e-4c05-8acf-6a2d8c4198bd', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-03', 'EID': '2207c9c5-543b-46c2-bff1-0085151bbc16', 'Hemisphere': 'both', 'P_Opto': 0.5, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_086', 'Date': '2024-10-02', 'EID': 'a89b438f-80fe-42e5-8f01-5093fb79d151', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'VGAT-ChR2', 'Brain_Region': 'none', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-31', 'EID': '96d56638-8bea-494f-9baf-d7495bfb11db', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-30', 'EID': 'abb899e8-6322-4ba0-abd0-b1bdff48d3ef', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-29', 'EID': '2e9ad686-c2d9-4bf9-aef6-abf2bd1cdfbe', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-28', 'EID': 'bc1d5d38-e056-4cf7-91c5-6af3dbc44b4f', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-27', 'EID': '51f537ee-b82c-446e-971e-017179aa4341', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-24', 'EID': '947da2a5-e353-46d2-8630-fe5456251df2', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-23', 'EID': 'bae55a88-eb85-4d24-9621-6a99e2bb71e8', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-22', 'EID': 'b7fd4cba-2bd2-4e36-8bd1-13832cc91fdd', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-21', 'EID': '770472b5-e6c5-4025-ba2e-5a6747e87da7', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-20', 'EID': 'fba10776-822d-4c20-a58c-a2e7eae0ba37', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-17', 'EID': '00556f60-cb27-41f2-8352-62a4b26f9f40', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_090', 'Date': '2025-01-15', 'EID': 'e4a51dfa-b784-4ade-b60a-aecfd36df014', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-31', 'EID': '4513ca43-092c-4d70-89f9-f431b281fe8c', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-30', 'EID': 'd669ac0a-1411-4834-983c-9e5a2d6cf4a8', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-29', 'EID': '59e6bef0-f807-4afb-8b2b-bba63c034610', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-27', 'EID': '4483138b-6f1b-48f5-84e8-8cb0f09270a4', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-24', 'EID': 'fc4787ef-8e61-45d6-afee-d87ce5f1dca1', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-23', 'EID': 'b19c533d-e9ac-4dcf-bf21-8e936fe48df3', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-22', 'EID': '4bb73d63-fec9-4f4b-9d9d-c4efdb5453e4', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-21', 'EID': '94d02ee9-ab83-4dad-9d75-6c43fa0e2a31', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-20', 'EID': 'da8f2c6e-419d-40cc-9f34-bbcf87f03d85', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-17', 'EID': 'b3d8987f-013c-4838-b55d-be24a1fab8bf', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_091', 'Date': '2025-01-15', 'EID': '82ada5f7-88ce-4796-8923-72c6f373bcf3', 'Hemisphere': 'both', 'P_Opto': 0.75, 'Stimulation_Params': 'zapit', 'Pulse_Params': 'motor_bilateral_mask', 'Laser_V': 2, 'Opsin': 'ChR2', 'Brain_Region': 'motor_bilateral', 'Genetic_Line': 'VGAT-ChR2', 'Trials_Range': 'ALL'},
    
    # {'Mouse_ID': 'SWC_NM_003', 'Date': '240921', 'EID': 'a7222f4a-93aa-42f8-ab93-df0b7868bc25', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '290921', 'EID': '3e3535fb-b06f-4e57-9460-cbe071984171', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '041021', 'EID': '3f704200-a246-4276-ae7f-c47c33e29f63', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '051021', 'EID': '3cf488ae-c327-4e58-b6f6-7b7d81721628', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '061021', 'EID': 'bb3a4433-65db-4640-8690-5bbc81ef8d49', 'Hemisphere': 'both', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '280921', 'EID': '87d94eeb-3754-414a-9dba-453f84b0f5fe', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,370))},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '280921', 'EID': '87d94eeb-3754-414a-9dba-453f84b0f5fe', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(370,9999))},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '081021', 'EID': '205e8076-40b3-4432-8044-0dd890839db7', 'Hemisphere': 'both', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '111021', 'EID': '05edb069-980d-42de-b9fa-178ef0648a21', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '121021', 'EID': 'd9dab492-0243-4135-b6aa-09ddc92e2d77', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '131021', 'EID': '6f7e2e29-68d1-4c8c-a7a5-4ec0baad08eb', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '141021', 'EID': '8b0545fa-3a21-43b2-bfcb-7cfed09961cb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '151021', 'EID': '411d5f71-4f16-4ca5-ae20-a9789a4b49a6', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '211021', 'EID': '335a0eda-f61d-45d2-b1df-1aea44c5abcb', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP*', 'Pulse_Params': 'cont', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '221021', 'EID': '2b920090-8256-4a13-9923-a4b57952faa7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '270921', 'EID': 'ba7bbd72-c41a-4dbd-9992-4a51489f4289', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,388))},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '270921', 'EID': 'ba7bbd72-c41a-4dbd-9992-4a51489f4289', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(388,676))},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '261021', 'EID': 'c9f6d00a-b6ca-4d83-a1fd-6082453445ee', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_003', 'Date': '281021', 'EID': '51a67fc5-0930-43d9-8458-5ec54578b773', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    # {'Mouse_ID': 'SWC_NM_004', 'Date': '251021', 'EID': '35cd3f60-267d-42b4-8606-a3eb2d763bab', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor/no expression in R hemisphere
    # {'Mouse_ID': 'SWC_NM_004', 'Date': '091121', 'EID': '9264704f-85f4-46b9-a269-e09cdba76e02', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_004', 'Date': '221021', 'EID': '8c2163f0-41c3-4c2c-8293-b6523790bfb4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #actually bilateral, but poor/no expression in R hemi
    {'Mouse_ID': 'SWC_NM_004', 'Date': '161121', 'EID': 'f78cbd4c-4a96-4da4-b2fd-b8d140150841', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_004', 'Date': '261021', 'EID': 'e098791a-305b-4338-9f3f-562a89948603', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor BL perf; cant salvage w/ earlier trials
    {'Mouse_ID': 'SWC_NM_004', 'Date': '101121', 'EID': '23520eca-b5b1-45fb-a629-3ebf3a620c2f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #borderline BL perf; cant salvage w/ earlier trials
    {'Mouse_ID': 'SWC_NM_004', 'Date': '151121', 'EID': '88726cf3-2821-4075-8bfa-bdfcf1c6bfd8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor BL perf; cant salvage w/ earlier trials
    {'Mouse_ID': 'SWC_NM_004', 'Date': '211021', 'EID': 'c90780f1-9304-4bcf-b74b-6ec9cae581ad', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor BL perf; cant salvage w/ earlier trials; actually bilateral, but poor/no expression in R hemi
    {'Mouse_ID': 'SWC_NM_004', 'Date': '011121', 'EID': 'a8f4b965-89b6-4905-b953-3f6f7c42bbb7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_004', 'Date': '021121', 'EID': 'ae981ae0-748d-4edc-9a6f-98ea1b417c34', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor BL perf; cant salvage w/ earlier trials; bias appears intact
    {'Mouse_ID': 'SWC_NM_004', 'Date': '201021', 'EID': 'b1dd1c50-6fbe-4f9b-8267-0b48a819c78e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor BL perf; cant salvage w/ earlier trials
    {'Mouse_ID': 'SWC_NM_004', 'Date': '191021', 'EID': 'edcaf465-4d4e-4d0d-86a0-aec5733ccd13', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 6, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_004', 'Date': '181021', 'EID': 'f162137e-73b7-4b5c-bd76-e2846276d2ac', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #poor/no expression in R hemi
    {'Mouse_ID': 'SWC_NM_004', 'Date': '271021', 'EID': '034bf182-47bb-4866-8340-1e910bdc79c6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_008', 'Date': '080921', 'EID': '5a6457b5-95bb-4026-b825-c38d8adc49e4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE*', 'Pulse_Params': 'cont', 'Laser_V': 3.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '090921', 'EID': '8a09bb30-a040-41b4-bfe0-492a0cc921e7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE*', 'Pulse_Params': 'cont', 'Laser_V': 3.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '100921', 'EID': '2bbae950-9555-43d0-9891-03e47f18b286', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP*', 'Pulse_Params': 'cont', 'Laser_V': 9, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '130921', 'EID': 'ed27c5bf-7b72-40de-9167-a74eac48a4c8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE*', 'Pulse_Params': 'cont', 'Laser_V': 9, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '140921', 'EID': '124cddb8-22d2-4632-be4d-92181901a65e', 'Hemisphere': 'both', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE*', 'Pulse_Params': 'cont', 'Laser_V': 9, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '170921', 'EID': '5c78ef8b-50d5-4e34-9e05-1ac6964aa551', 'Hemisphere': 'right', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE*', 'Pulse_Params': 'cont', 'Laser_V': 9, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '240921', 'EID': '1cceaf57-cd56-410e-bddb-634ee9840c50', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,495))},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '240921', 'EID': '1cceaf57-cd56-410e-bddb-634ee9840c50', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(495,9999))},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '191021', 'EID': '67a3d9a8-5ec5-4ed6-9473-f3c16f62d087', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '221021', 'EID': '409dc01a-c5dc-40cb-8356-e19372e4f546', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,750))},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '300921', 'EID': '238a0a48-392e-4d18-836a-eb5fe0853bfe', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '011021', 'EID': '318bffb7-9bca-4145-affe-b52588a5dc1c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '071021', 'EID': '8e71c2f4-f931-4b1b-8f45-1ccb8b2460e8', 'Hemisphere': 'both', 'P_Opto': 0.3, 'Stimulation_Params': 'QP', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '290921', 'EID': '96aaa6e1-1b1d-46e9-b8a0-47de29d195a7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90,1004))},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '041021', 'EID': '448d7b48-af08-47e0-bace-3167ba4ba9cc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '051021', 'EID': 'be7b5af4-be82-4be4-903d-678c59d8d365', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '061021', 'EID': '52f21cc6-6b1c-4fdc-b26e-c04bd4a4ce99', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_008', 'Date': '111021', 'EID': '05edb069-980d-42de-b9fa-178ef0648a21', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QP', 'Pulse_Params': '50hz', 'Laser_V': 4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_010', 'Date': '030222', 'EID': '8e6c8994-6a12-4e2c-b066-958b9f84ab67', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '150222', 'EID': '330ebac8-a94e-4a0c-a50a-c571fb162b02', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '180222', 'EID': '8b4f0ea4-9185-44eb-a27e-40238563bef7', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '210222', 'EID': '2aa240a4-0d31-4271-845d-c33e951e9118', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '220222', 'EID': '0a6400bf-3f90-4be2-9b63-19d9f659cf16', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '240222', 'EID': 'c44751ce-3ef1-4fb1-9744-a8f6ac4b28ac', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '010322', 'EID': 'd75fefd9-4203-41a8-a3fc-33a1c031d90e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '020322', 'EID': 'ab4938a4-b64c-4a91-8620-d8707a2d2df6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '020222', 'EID': '11a8532c-5718-43a9-8bac-b6f6e0fb4cba', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '070222', 'EID': '7ade859f-02cb-4b8f-bb9d-957b26ece7be', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '160222', 'EID': '5e37ce85-aa69-4651-b8a0-03101faf4d33', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '170222', 'EID': 'b2da6e36-e25c-4b2a-9937-2ab30003ac48', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '230222', 'EID': 'd70115ec-4589-4dbe-8ae8-2191c9b5af94', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '250222', 'EID': '167f71eb-61c0-45fe-9531-5cb5dd33f396', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_010', 'Date': '280222', 'EID': '98ee5eaf-d3bd-4101-a4ed-b074f537798a', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1.5, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_011', 'Date': '041121', 'EID': 'd71ec5e3-f257-47e2-8690-f943d13e0c13', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '081121', 'EID': '3debc803-cabb-444a-ad4b-62b52f34dc1f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '101121', 'EID': '269798e4-4837-42f0-80a8-12feafb5325e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '121121', 'EID': 'f0780250-d261-4337-b736-303658a7848a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '171121', 'EID': '16bb91ac-5701-48c4-8098-1861660d8ccb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '181121', 'EID': '7dd4db33-7c27-4491-b0b5-3b5af9f526dd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '191121', 'EID': '997bed88-f960-4d40-9e3b-872727784e3c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '221121', 'EID': '60e0089d-d755-4e32-8a2b-f5dbd6b3a520', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '231121', 'EID': 'fddf4805-46fe-482c-ae12-b0a717f0d6a8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(96,784))},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '261121', 'EID': '28d3ceed-1edb-4ac6-b7c8-e3647ad36370', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #borderline BL performance
    {'Mouse_ID': 'SWC_NM_011', 'Date': '021121', 'EID': 'fefde89c-53d2-4ed0-b5d6-7c2f05b55767', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '051121', 'EID': '9e4b80e4-ae85-4e5e-8e1d-519eb68347be', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '091121', 'EID': '3abd3941-4f14-482b-a9af-d9ee0e4bc69d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '161121', 'EID': '847cdd72-0859-4bb4-9bba-c3b11045d7c8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '241121', 'EID': '02af576e-0aa1-4784-b631-adbc3792f4d5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,229))+list(range(349,409))+list(range(576,647))},
    {'Mouse_ID': 'SWC_NM_011', 'Date': '251121', 'EID': '7373f901-2f6e-48f4-981c-30192a9299de', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,114))+list(range(390,527))},

    {'Mouse_ID': 'SWC_NM_012', 'Date': '030222', 'EID': 'a4501dd7-8613-4cdf-99ef-ca56971557c5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '070222', 'EID': '95acdc6e-8959-4d9a-b039-9c28a9f06ee0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '080222', 'EID': 'ccf42b1c-8ed4-4265-afe6-2afb25d10d08', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '090222', 'EID': 'ef962323-9464-483f-992c-6a3de096a963', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '150222', 'EID': '15f0c551-0bc2-4423-ab09-90e03dd240c5', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '160222', 'EID': '288b4537-a539-49f3-a56c-c67c80b3704c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '180222', 'EID': '186f7c0a-81ca-488a-92c0-14d41263edbe', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '210222', 'EID': '6c01b126-12cf-4739-8aa3-120bc62e2aee', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '220222', 'EID': 'ff54300e-0061-4ab3-9bee-b56a54d71376', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '230222', 'EID': 'a418eb79-b949-4fdf-9fad-b5d8b240e638', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '240222', 'EID': '2a2efcbf-0269-477b-97f2-89f8ef04decf', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '010322', 'EID': 'd75fefd9-4203-41a8-a3fc-33a1c031d90e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #very poor performance
    {'Mouse_ID': 'SWC_NM_012', 'Date': '020222', 'EID': '1f19e366-46b0-46ea-a137-1bf58a3d83c5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '040222', 'EID': '2aed2d49-fced-4465-b3bb-58b225079748', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(80,9999))},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '100222', 'EID': '04260f14-4329-4d71-9061-092cc441e2d7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '110222', 'EID': '03bd9265-4e9e-4c96-8e57-4cc3827aa0d8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '250222', 'EID': '167f71eb-61c0-45fe-9531-5cb5dd33f396', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'pre_stim', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_012', 'Date': '280222', 'EID': '98ee5eaf-d3bd-4101-a4ed-b074f537798a', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'pre_stim', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_018', 'Date': '300322', 'EID': 'e059b876-c4ef-4a6b-aa1e-6ffc496ed9fc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_018', 'Date': '310322', 'EID': 'e418cf94-e626-4a1e-9796-e9dcb35a5ad1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #possible issue with BNC pulses
    {'Mouse_ID': 'SWC_NM_018', 'Date': '010422', 'EID': '028cca41-d6cf-4487-b0d1-817a3c2ee94f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '060422', 'EID': 'b4dd0cff-3aed-4b74-973a-0a015cc2ad11', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '070422', 'EID': '8c070089-7fb4-4bd9-b88e-c99b498f7acf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '120422', 'EID': 'dd64e7e8-eee5-4a68-9799-b776527e3137', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(100,9999))}, #poor BL perf; no effect on bias? short RT
    {'Mouse_ID': 'SWC_NM_018', 'Date': '020622', 'EID': '8b60db57-1ec4-419a-8424-c33739d54dbb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(87,620))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '030622', 'EID': 'cfde78ae-0d8f-4a06-9e7f-8fe9fe7d1813', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(78,844))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '060622', 'EID': '55b1d768-6bd1-4365-b0b5-9f320f68af41', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(108,758))}, #seems there is little/no effect in L hemisphere
    {'Mouse_ID': 'SWC_NM_018', 'Date': '070622', 'EID': '9ea88450-65e7-4c6c-a619-76cccbc163a8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '090622', 'EID': '2a2583b4-18b9-4dbe-918c-eb753d16c03e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(62,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '290322', 'EID': '9428f5fc-a6b9-4689-8200-b0a846933a1d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '030522', 'EID': '866547c2-c965-4278-aedf-0df750e29a7b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(123,302))+list(range(614,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '030522', 'EID': '866547c2-c965-4278-aedf-0df750e29a7b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(302,614))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '040522', 'EID': '6daaa3c9-67c1-497a-932a-e4c521c8cf3d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(108,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '050522', 'EID': 'd1a66312-dad9-4951-8a9c-7497c3aaf69f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPSO', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(157,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '150622', 'EID': '25863f4c-20d6-43e1-903d-088bcbfdc441', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(149,242))+list(range(364,461))+list(range(581,674))+list(range(769,798))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '150622', 'EID': '25863f4c-20d6-43e1-903d-088bcbfdc441', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(242,364))+list(range(461,581))+list(range(674,769))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '160622', 'EID': '786b0feb-31a8-4598-a51d-7f13ffb936d1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(121,283))+list(range(423,528))+list(range(660,767))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '160622', 'EID': '786b0feb-31a8-4598-a51d-7f13ffb936d1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(283,423))+list(range(528,660))+list(range(767,9999))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '170622', 'EID': 'b1f5abe0-8261-498c-a8e6-24381750da18', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(422,485))},
    {'Mouse_ID': 'SWC_NM_018', 'Date': '170622', 'EID': 'b1f5abe0-8261-498c-a8e6-24381750da18', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(371,422))+list(range(485,9999))},

    {'Mouse_ID': 'SWC_NM_016', 'Date': '080422', 'EID': 'efeef8a4-af69-44ef-9cfa-44c91ab67926', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(197,756))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '110422', 'EID': '9934246e-0e5a-4fe9-90dc-bf179c84482f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(122,9999))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '120422', 'EID': 'ca97595c-1ae9-4bf5-8703-4368abe28c9e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(119,400))}, #truncated for better performance; still borderline
    {'Mouse_ID': 'SWC_NM_016', 'Date': '140422', 'EID': '1f05c49c-1b40-418b-ab59-89232916710a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(204,545))}, #well below threshold perf
    # {'Mouse_ID': 'SWC_NM_016', 'Date': '150422', 'EID': '1d09b08b-8883-4d84-aed0-0e53e91995ea', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(159,948))}, #mouse turns right 100% of trials?
    {'Mouse_ID': 'SWC_NM_016', 'Date': '250422', 'EID': 'cc800aa2-768a-4ca3-8710-99a9fa1d2e79', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(107,575))}, #perf on STIM trials is pretty random, also, few stim trials (70)
    # {'Mouse_ID': 'SWC_NM_016', 'Date': '260422', 'EID': '17abc01b-e2e3-4815-af11-85f0700efbd4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(94,612))}, #mouse turns right 100% of trials?
    {'Mouse_ID': 'SWC_NM_016', 'Date': '280422', 'EID': '32cf6ee5-2397-4482-a1f6-bb01745a4b4b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90,700))}, #bias still there?
    {'Mouse_ID': 'SWC_NM_016', 'Date': '220422', 'EID': '9cc77c22-08f2-49cd-b37d-905397fab334', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'ITI', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90,662))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '070422', 'EID': '0ff9161b-bae8-4ff1-a080-2928fc45cc54', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,342))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '080422', 'EID': 'efeef8a4-af69-44ef-9cfa-44c91ab67926', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(85,197))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '130422', 'EID': 'cc14dbaf-300b-4df5-8fba-edb4b4b06cf8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(42,407))},
    {'Mouse_ID': 'SWC_NM_016', 'Date': '130422', 'EID': 'cc14dbaf-300b-4df5-8fba-edb4b4b06cf8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(407,9999))},
    # {'Mouse_ID': 'SWC_NM_016', 'Date': '230622', 'EID': 'dcca0a3e-791d-4cdd-91bd-effe2d811041', 'Hemisphere': 'left', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,69))+list(range(197,320))}, #few trials; performance poor
    # {'Mouse_ID': 'SWC_NM_016', 'Date': '230622', 'EID': 'dcca0a3e-791d-4cdd-91bd-effe2d811041', 'Hemisphere': 'left', 'P_Opto': 0.3, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(69,197))+list(range(320,473))}, #performance poor; unexpected QP/RT effects?

    {'Mouse_ID': 'SWC_NM_039', 'Date': '140423', 'EID': 'c2c0e631-02a0-46a0-a1c8-ae633132e438', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(100,243)) + list(range(332,365))},
    {'Mouse_ID': 'SWC_NM_039', 'Date': '140423', 'EID': 'c2c0e631-02a0-46a0-a1c8-ae633132e438', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(365,9999))},
    # more sessions for SWC_NM_039

    {'Mouse_ID': 'SWC_NM_022', 'Date': '240822', 'EID': '17cd8693-ab43-41fd-9667-b1c1b2cacc0a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,409))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '240822', 'EID': '17cd8693-ab43-41fd-9667-b1c1b2cacc0a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(409,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '250822', 'EID': '95b46097-4cc0-4574-9ed3-7d9a2fd4b5ca', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,425))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '250822', 'EID': '95b46097-4cc0-4574-9ed3-7d9a2fd4b5ca', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(425,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '260822', 'EID': 'bbb93ef8-8439-4515-96a1-776c797bb7d8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '310822', 'EID': '681a022d-7158-40de-9ffc-a780ebe3a26d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '010922', 'EID': '81d6093f-29ca-496f-82d5-82cd70b13316', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '020922', 'EID': '3c7bfbf6-bff7-4a9e-88ed-71d533e1aee8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '050922', 'EID': 'cb124905-f035-4b45-acc6-5eefd06f695b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(149,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '070922', 'EID': 'eab374d8-c1e4-4e4b-9391-5c1b42b02e5e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '090922', 'EID': '5388bcbc-b4e6-4a3d-bfff-8f38440e1368', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '120922', 'EID': '4f5d64c2-f685-49c8-bbd6-ebe7e65f4686', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(51,9999))}, #effect?
    {'Mouse_ID': 'SWC_NM_022', 'Date': '130922', 'EID': 'ea9f947a-e166-4fdf-863e-781e37c19234', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(134,9999))},
    {'Mouse_ID': 'SWC_NM_022', 'Date': '150922', 'EID': 'd87971e3-1253-49ea-9574-8d094c782e29', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0,9999))},
    # ephys sessions for SWC_NM_022 (ZI)

    {'Mouse_ID': 'SWC_NM_036', 'Date': '090323', 'EID': '74c09dd3-1037-4020-a4d9-b499fd6599be', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100,676))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '100323', 'EID': '63504410-3830-40f4-9e7b-8b15e73b476c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(3,734))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '130323', 'EID': '0a161756-e61a-4211-9f39-59987caac9b2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1,609))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '140323', 'EID': '3ffd2a46-cbc5-4a6b-965f-c3baeb4c4899', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1,674))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '150323', 'EID': 'a5c3a7bf-23af-44ba-aa17-6814a84264c7', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1,781))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '160323', 'EID': 'a34c3639-4a0c-4bb2-b369-dd72487e4e1f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(101,975))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '170323', 'EID': '4e5e7d0b-6bc4-445a-8975-d1c1a3caaa26', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,743))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '200323', 'EID': '51c8f945-560c-4d9d-8079-7eed0ac3573a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1,673))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '210323', 'EID': '37f0bd30-767f-45d2-a667-ac14a2a0787e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(16,685))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '220323', 'EID': '61c10489-929f-4bdb-bc0e-a5feaf075183', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(2,958))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '230323', 'EID': '84c5c7e8-c19b-490f-a878-7672047440da', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(3,735))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '240323', 'EID': 'bef903f8-fedb-42b7-83e7-c06446bb766b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1,794))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '270323', 'EID': '7ae2b0ea-9982-4fb8-8d02-c918f6d09a44', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(11,859))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '280323', 'EID': 'bef903f8-fedb-42b7-83e7-c06446bb766b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(5,458))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '290323', 'EID': '82e041f8-b677-48a2-84d6-b42deb4803b7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.7, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(8,709))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '300323', 'EID': 'be50456b-7477-4638-887e-a8895e34b7b2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,658))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '310323', 'EID': '19aaab85-9ee4-4959-9592-2fdcc9101264', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(6,649))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '030423', 'EID': '7f37d94b-a3f8-4ad3-af45-d5b2fce5119d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(150,900))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '040423', 'EID': 'c2c3cc18-e125-42e3-b2ac-fc6b6e1e70b8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(4,918))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '050423', 'EID': '20ed1969-96f6-4f57-9ae7-66ee094e47d7', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(5,580))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '060423', 'EID': '2845f8ed-6f0b-4b48-85a2-974b07c6a0a0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(130,664))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '070423', 'EID': 'cf3a1d93-486a-4f76-99bd-41539d29c4d3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(130,992))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '120423', 'EID': '46dd2112-a336-4221-b1f1-601e57fbd972', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,468))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '130423', 'EID': 'a079d54f-825f-4267-925b-a2ec3ba1b631', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,753))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '140423', 'EID': '2fc30f24-10ee-4f3d-bc03-a42e2a1eb51e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,914))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '170423', 'EID': '74586452-6ce3-4be5-a86c-ed0ffb6b0be9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,653))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '180423', 'EID': '1d7fedc4-04be-468f-8d4e-76c8e51d4e91', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,9999))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '190423', 'EID': '23c27379-e440-4013-9a1b-6ee05eed33b3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(5,878))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '200423', 'EID': '3e3b5e27-032c-4ee0-8db1-c61bf2b6aade', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(22,675))},
    {'Mouse_ID': 'SWC_NM_036', 'Date': '210423', 'EID': 'fa418725-acfd-4853-975d-66041008affa', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(16,844))},
    ### may even be more sessions?

    ### appears to be no expression at all for 54! Maybe mouse was not Cre+
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '031023', 'EID': 'e93d6e9b-80c2-449f-860d-4fb59567914b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,862))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '041023', 'EID': '3547f202-eaed-48e8-b20d-e209c8e61386', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(189, 757))}, #no baseline bias
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '051023', 'EID': '2cbd0ae3-69e0-4586-9de2-a68dca14f878', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 799))}, #low baseline bias
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '061023', 'EID': 'e9e44d2d-b15c-46be-8442-dd2dda5d5723', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(200,1116))},
    # # {'Mouse_ID': 'SWC_NM_054', 'Date': '091023', 'EID': 'fc7e0d7b-36ef-4a9b-a451-6e2e8b87fb33', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,654))}, #laser not on?
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '101023', 'EID': '3daacb5c-9de8-4434-a3bb-269e0adb034f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90,658))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '191023', 'EID': '2439b61f-83ca-48e0-af89-3d701fb74b76', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(119, 887))},
    # # {'Mouse_ID': 'SWC_NM_054', 'Date': '201023', 'EID': '58f72a9f-471a-4889-a986-49edf7732fc9', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(500, 851))}, #listed as 50hz, but maybe cont?
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '231023', 'EID': '8424a850-ba6e-42a4-8731-c5f2cbc38833', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(205, 663))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '311023', 'EID': 'b5195c82-0269-4c4b-87c0-c1d7eaa9f1fc', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 718))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '021123', 'EID': '5e0bc149-ad12-4aaa-a7e8-5cdf0cf2f16b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(120, 893))}, #no QPRT effect?
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '091123', 'EID': '9d1fad67-c822-4cb7-9d63-69324f79a38e', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(154, 680))}, #seems like an effect - QP lower, RT higher
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '101123', 'EID': '58c96b89-b575-4998-a883-87bb0980ebdc', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 939))}, #suspiciously no effect; no RT or QP effect either
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '151123', 'EID': 'f2f59a40-c08f-4504-b709-52cf4383072a', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(99, 544))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '171123', 'EID': '07d19e88-6d3b-493f-b005-9ce458771265', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(216, 400))}, #few trials - low baseline bias
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '201123', 'EID': '0e1daaaf-2e18-444f-a2f0-991c74c77055', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(141, 500))}, #borderline perf; late trials removed for better accuracy
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '171023', 'EID': 'c86f4ece-cb61-4f61-a32b-044cc5a7a83f', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(95, 588))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '181023', 'EID': '4e317696-79b1-40ec-90d9-5712dc799948', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(246, 611))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '201023', 'EID': '58f72a9f-471a-4889-a986-49edf7732fc9', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 500))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '241023', 'EID': '9251ad04-0d88-40c1-b9e0-3b0350caefe2', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(112, 500))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '251023', 'EID': '37208000-0476-42ef-8282-322272040e5b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 900))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '301023', 'EID': 'b8a984ea-4e15-492f-b646-e5899aa66e85', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(115, 802))},
    # # {'Mouse_ID': 'SWC_NM_054', 'Date': '031123', 'EID': '9c2df030-e9d9-4d1d-b7c3-b4b302cd8f7f', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 571))},
    # # {'Mouse_ID': 'SWC_NM_054', 'Date': '061123', 'EID': '30ba5777-9504-4653-a37f-0317c4eb5ced', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(145, 440))}, #range truncated; mouse changes strategy toward end of session
    # # {'Mouse_ID': 'SWC_NM_054', 'Date': '081123', 'EID': '1edede50-ccf9-4b75-92d9-9c0d8945e84d', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(127, 741))}, #effect opposite as expected? - QP lower, RT higher
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '131123', 'EID': '5e3e4a98-3d79-4ffa-8e16-0c44a167440b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(121, 450))}, #trials truncated for better performance
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '141123', 'EID': '128c872c-5e79-4e60-b644-b53d5854189d', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(147, 667))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '161123', 'EID': 'a5e48872-2376-4c8e-b1db-8c31f8cd069b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 656))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '211123', 'EID': 'c4a31290-90ab-42d4-83ce-341bc6c980ce', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(150, 563))},
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '231123', 'EID': '21861d63-c3be-40f4-961b-421cb5fc3913', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(120, 500))}, #borderline perf though strong effect; late trials removed for better accuracy
    # {'Mouse_ID': 'SWC_NM_054', 'Date': '011223', 'EID': 'b1582929-1117-4e44-862e-c775008ca548', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 731))}, #strong effect

    ##### 53 was labeled with RETRO virus
    ##### left hemisphere missed target
    ##### right hemisphere hit VLS, but weak local labeling; barrel cortex barrels clearly light up, interesting
    ##### however, little/no expression in M2
    {'Mouse_ID': 'SWC_NM_053', 'Date': '171023', 'EID': '0a5d156f-696c-442d-a3e5-a1ec0535edd2', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(146, 863))}, #unilateral R 50hz (no sidedness afaik)
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '181023', 'EID': '0829492a-84cd-40d9-a17d-e2ba77a28a8c', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 888))}, #unilateral L 50hz (no sidedness afaik)
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '191023', 'EID': 'a6a3ac50-c5a2-4e40-a7d1-f66c041d5f89', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 534))}, #baseline bias gone
    {'Mouse_ID': 'SWC_NM_053', 'Date': '201023', 'EID': '49ed175c-9f47-4048-9ea2-af267f7ca445', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(124, 769))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '231023', 'EID': '4cef1a10-acd0-48af-bd8b-a5c1a1d2fef6', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 598))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '241023', 'EID': '6a971abe-3287-487b-b1ee-faef050303e4', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 829))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '251023', 'EID': '1978c5fc-239e-47e4-9d97-b0c1473a7b78', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(113, 749))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '261023', 'EID': 'ea0eb232-5d95-4702-888d-b014c96419a2', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(127, 849))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '271023', 'EID': '00b8057d-117d-434a-82e3-94cf7eb5f020', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(148, 941))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '301023', 'EID': '8b2214be-2ff3-42c0-829f-f6441d02e0be', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(106, 722))}, #no baseline bias
    {'Mouse_ID': 'SWC_NM_053', 'Date': '311023', 'EID': '413bda0c-0b1c-4d2f-9bd2-fff32a2e928c', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(95, 530))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '011123', 'EID': 'e170ea22-f828-4435-99e9-36220d050c4c', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(122, 670))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '031123', 'EID': '5428d5e7-7a1f-46a3-af91-323226f28f25', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(104, 901))}, #low baseline bias
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '061123', 'EID': 'e73998dd-cff2-40d6-80ab-8f87aad0db7a', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(101, 675))}, #no baseline bias; mouse impulsive
    {'Mouse_ID': 'SWC_NM_053', 'Date': '081123', 'EID': '56b6f822-4538-43c6-9f14-7831cedcb1bc', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(105, 718))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '101123', 'EID': '0974d094-1011-4ab0-a093-f96bdf257b67', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(159, 800))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '131123', 'EID': '3693330f-2dee-4943-8713-2ee908736a06', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(124, 668))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '141123', 'EID': 'd5b2ce58-65d4-42f3-841d-59358e386090', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(106, 623))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '161123', 'EID': 'af0e43f5-d3a4-44af-9924-20eecff02744', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 756))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '171123', 'EID': 'ef77efd8-d1ba-4904-ad7b-565e1425198b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 799))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '201123', 'EID': 'c558a4bd-0960-49c4-94ec-7964168a05a7', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(265, 700))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '211123', 'EID': '96ff08d6-b9f1-4596-bc70-ee10c7502670', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(150, 450))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '221123', 'EID': '9a6f6206-5958-450f-84a0-9689d1ef34c3', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(111, 805))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '231123', 'EID': '94a30725-7b79-4eb2-8938-7838e874f367', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(108, 767))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '241123', 'EID': '5c476c28-c6f1-454b-92bf-b790c81f1eb2', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 767))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '271123', 'EID': '2630a3ef-20fb-4511-bd40-5baae2e2f33e', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(123, 887))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '141223', 'EID': '98e16563-a739-4c72-864e-bb2b4e8425fd', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 944))}, #unilateral R 0hz low baseline bias; no obvious QP effect?
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '131223', 'EID': '5a1c0170-68c3-4e64-8b46-4f4c37a47c5e', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 859))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '281123', 'EID': '3ad1c330-a34e-460b-894c-1c50d04e6d38', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 738))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '291123', 'EID': 'b4ef9d1c-4897-4b7e-9c05-40867cc1888d', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 978))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '301123', 'EID': '37af82ca-2b18-463c-b4a8-8c3ac2242c30', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 788))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '011223', 'EID': 'f264b806-07f1-40a7-9fe3-4c1eb063b9b6', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 532))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '041223', 'EID': 'b09b7f9b-4833-426c-b395-1599b2e015f9', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 400))},
    {'Mouse_ID': 'SWC_NM_053', 'Date': '051223', 'EID': '45e79f8f-d7ae-4329-921f-4470278d7723', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 758))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '061223', 'EID': '7d7193a8-bee8-4b37-90e4-9c26c17b7387', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 588))},
    # {'Mouse_ID': 'SWC_NM_053', 'Date': '071223', 'EID': 'ffa1825c-a520-4f2f-bd70-33c3d53aa8a1', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'SORE', 'Pulse_Params': 'cont_c', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 926))},
    # 3 no stim sessions as well

    #### Expression in 38 labels only very small region of dorsal VLS
    {'Mouse_ID': 'SWC_NM_038', 'Date': '070623', 'EID': '6b0b342d-5bb3-403b-85bd-22996e3d03f5', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(195, 527))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '120623', 'EID': 'aae41bc3-6965-4629-a02f-71ea8eeeac26', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(129, 618))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '150623', 'EID': 'd1b1cf5a-c68d-416a-9a92-b3a77f5145f6', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(102, 555))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '290623', 'EID': '34478c65-c8e9-4343-9e1a-492bbcdd4fa7', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 400))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '270623', 'EID': '1a5b1972-bc01-4abd-8124-0a31ea814912', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 364))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '030723', 'EID': 'f29f284d-2cf9-42ac-8a71-24c2d4a2d241', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 450))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '050723', 'EID': '4721f49b-6772-400f-b9e9-fd8c65fc2183', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 615))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '120723', 'EID': '21a01c43-d4ff-4f64-8b69-931cfd91ecb3', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 250))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '170723', 'EID': 'f328df1d-d736-455c-a09b-a55869cb8723', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 300))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '210723', 'EID': 'a5b427bf-e4ae-428d-8955-b2bfa534011b', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 597))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '240723', 'EID': '33326079-f197-4dea-a319-b3377dd2996e', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(126, 562))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '260723', 'EID': '7a898aeb-e6d0-4241-9bdd-e593720fbb3c', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(113, 457))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '280723', 'EID': '77828eaf-27bb-41bb-a111-c56f2c500233', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(214, 405))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '310723', 'EID': 'd873e6c7-4e61-46a3-9c0d-038cc5544b1e', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(91, 408))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '040823', 'EID': 'aa645856-a18c-4564-a046-0d8793404106', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(103, 539))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '090623', 'EID': '1f5bc7a5-1703-492a-8df4-f1aaa17e8935', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(110, 604))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '160623', 'EID': '6f2a676d-7524-4d5e-b965-4a744c65eab2', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(126, 501))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '140623', 'EID': 'c84b3e0d-93be-42e7-9dc4-49bc87e12005', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 405))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '280623', 'EID': '86029b2d-4855-4fb0-b2a7-1b4c0da70c6c', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 341))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '300623', 'EID': 'e0c7b3ed-bf0c-48af-922c-48e3aab76086', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 667))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '040723', 'EID': '2bd9be29-02c5-4727-929c-045c6acb2d90', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(250, 586))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '130723', 'EID': '71aa1c84-0174-4e6b-b394-0dc883391452', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 275))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '190723', 'EID': '7e6e6ea5-c138-4514-9ac1-8ab369979782', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(245, 699))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '200723', 'EID': '65fb2455-2764-4972-9a4c-cd23decbff32', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(189, 596))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '250723', 'EID': '4cdfca10-c1b2-4e57-bbe4-1bf3e325de91', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 436))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '010823', 'EID': '0cb59f03-761d-4a65-98a5-3a38d3a31def', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 637))},
    {'Mouse_ID': 'SWC_NM_038', 'Date': '030823', 'EID': '77de0838-d155-40a1-9b5d-7cd663012188', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 503))},

    {'Mouse_ID': 'SWC_NM_035', 'Date': '090323', 'EID': '5f0964f7-7018-44f9-9310-1819055c88a4', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(50, 761))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '010323', 'EID': '64a9517f-fefb-43dc-98d5-e0041e38e906', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(321, 451))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '130323', 'EID': '42413192-cad7-44bf-a759-9f761a3b973d', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(131, 1055))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '160323', 'EID': 'b1b0a076-1527-4d1e-a714-27adbfff6219', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(170, 867))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '200323', 'EID': 'b4cff50c-934f-4855-9aa3-9b04d989de59', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1, 545))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '030423', 'EID': '631af73a-23bf-4c63-b3b6-29382e3ec992', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(110, 844))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '050423', 'EID': '6d2652ab-abdc-4e34-9f82-1be1ae95393e', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 535))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '080323', 'EID': '4535379c-1216-40f8-a0fd-054cc27799f0', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 922))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '020323', 'EID': '8fc44e79-5d11-40c5-b338-87dfd1c115d3', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(538, 669))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '100323', 'EID': '252731b9-9b96-4bea-a2b2-056683506cf7', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(1, 396))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '170323', 'EID': 'b8bbf15b-115c-495a-86b4-818bbacb39fe', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(3, 795))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '210323', 'EID': 'a6fe82bf-8d76-4a07-8dfe-0da5cb168e06', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(20, 482))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '040423', 'EID': '56445d1b-8e49-4358-8cb7-4b85ba68c0a5', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 929))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '140323', 'EID': 'e56d0d56-00ac-4cba-8ea5-3429632d87d4', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(4, 728))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '300323', 'EID': '8e3bec84-9a1e-4d97-a22d-f08793b1dc6d', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 744))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '060423', 'EID': '3f4d8647-1701-4763-9630-3aee0b7b8f88', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(300, 960))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '070423', 'EID': '95f3745b-64c8-46db-924a-3cb867349804', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(170, 491))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '310323', 'EID': 'da0ccad4-33fb-45f5-be60-434789df1758', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(14, 654))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '170423', 'EID': '76af3bdb-0842-4418-b06b-1ca45c519c53', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 546))},
    {'Mouse_ID': 'SWC_NM_035', 'Date': '220323', 'EID': '1f36b80d-dfb5-4842-a7fc-8af8f10ce602', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(7, 787))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '230323', 'EID': 'e49d896c-e724-4966-98d9-6bfd9691a70f', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(18, 663))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '240323', 'EID': '9e2ebea3-450d-41da-8066-77cbbc3b46c7', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(118, 966))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '270323', 'EID': '48d99226-0974-40b6-8357-a5876f7765df', 'Hemisphere': 'right', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(3, 177))},
    {'Mouse_ID': 'SWC_NM_035', 'Date': '120423', 'EID': '192eb333-4a1b-4db2-9e0d-72f86ff0fd62', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(165, 651))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '020323', 'EID': '8fc44e79-5d11-40c5-b338-87dfd1c115d3', 'Hemisphere': 'left', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(180, 537))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '060323', 'EID': 'c2a819bb-0cdf-4f91-8646-d227f65f6c78', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(134, 788))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '030323', 'EID': 'c0e0f994-7f1f-4c71-a781-9843f034ef50', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(460, 829))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '150323', 'EID': '96468f7e-df40-4b3f-9651-cfb25d8d0b3e', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(35, 741))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '280323', 'EID': 'd9bb48d5-d886-499e-bd4a-203c5277f64f', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 672))}, 
    {'Mouse_ID': 'SWC_NM_035', 'Date': '290323', 'EID': 'a0f4b0fb-388e-4a15-a3fc-4792814f18ac', 'Hemisphere': 'both', 'P_Opto': 'unknown', 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VMS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(8, 907))},

    {'Mouse_ID': 'SWC_NM_037', 'Date': '170723', 'EID': 'aabe7656-2d2f-44ee-9e87-bd5ca4102523', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(252, 401))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '310723', 'EID': '1ce32560-314a-49c5-afac-57cc7f5cdb9b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(148, 689))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '140723', 'EID': '69d52afd-957b-4e91-8bf3-2f83c0053682', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(55, 189))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '280723', 'EID': '4cf61029-b073-4418-8207-1ec86ff80226', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(88, 985))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '260723', 'EID': 'e4786276-0cb8-45fa-97cb-182658596d3f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(59, 755))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '210723', 'EID': '97555715-ddfd-4e98-be18-c5616125cde5', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.03, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(185, 641))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '130723', 'EID': 'da48644d-6859-4838-8e2c-5435e5e83764', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(176, 308))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '250723', 'EID': '36d25914-b9d7-4660-929e-6b6abe64d7c6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.03, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(200, 824))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '270723', 'EID': '33201ab9-04fe-455b-827b-8aea51949a70', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(136, 662))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '010823', 'EID': '1f87f9fa-da91-41c9-92ae-8e1be72766dd', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(132, 551))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '180723', 'EID': '2dccb63e-d226-4851-9b3b-432c8a855e52', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.03, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(198, 523))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '020823', 'EID': 'e9bae280-d294-4310-af89-b1a98da5cc8e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(102, 249)) + list(range(500, 9999))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '020823', 'EID': 'e9bae280-d294-4310-af89-b1a98da5cc8e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(250, 499))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '030823', 'EID': '75f548d0-2069-427f-a4ee-f9a816558731', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(395, 926))},
    {'Mouse_ID': 'SWC_NM_037', 'Date': '030823', 'EID': '75f548d0-2069-427f-a4ee-f9a816558731', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(258, 395))},

    ###### 42 expression pattern is in middle of striatum and not completely ventral; restricted area; mostly missing frontal region and tail
    ###### also, shows potential cell death in middle of inj site
    ###### shows partial reduction in bias
    {'Mouse_ID': 'SWC_NM_042', 'Date': '240523', 'EID': 'a109e274-2379-409f-afd8-783ac2852565', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.6, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(81, 343))},
    {'Mouse_ID': 'SWC_NM_042', 'Date': '240523', 'EID': 'a109e274-2379-409f-afd8-783ac2852565', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.6, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(343, 9999))},
    {'Mouse_ID': 'SWC_NM_042', 'Date': '250523', 'EID': '13e4a6f2-580c-4548-861e-6617a2ae038b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.6, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(90, 308))},
    {'Mouse_ID': 'SWC_NM_042', 'Date': '250523', 'EID': '13e4a6f2-580c-4548-861e-6617a2ae038b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.6, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(308, 9999))},
    {'Mouse_ID': 'SWC_NM_042', 'Date': '310523', 'EID': 'd0d3ac54-9986-47c5-a76c-14085134afd9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(90, 758))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '300523', 'EID': '779182c1-64c8-431f-87dd-b23964232795', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(95, 700))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '260523', 'EID': 'b0734d14-c1c0-4291-94e6-96a5f7d7d86a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(111, 623))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '090623', 'EID': 'd3542e8b-c171-4e20-bbaf-d6487785e9f5', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(123, 654))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '080623', 'EID': '947bf043-ff1d-4dc7-8db3-ec05164ccfb7', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(98, 640))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '020623', 'EID': '38dd63f0-297b-44a8-b469-2c16c76461ac', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(148, 621))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '010623', 'EID': '84911885-3efa-4398-a699-4805b3ad9a93', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(120, 645))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '070623', 'EID': 'e7c61b0e-b713-480f-8acc-0f480620f895', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(158, 499))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '060623', 'EID': '63e2a4ae-80c3-4a87-8bee-64e4f604e389', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 'unknown', 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(161, 598))}, 
    {'Mouse_ID': 'SWC_NM_042', 'Date': '150623', 'EID': '3aedd7d5-b3e1-4617-99e4-3923c19105c9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(106, 9999))},
    
    ###### 43 expression pattern is in middle and posterior striatum; mostly missing frontal region
    ###### shows strong bias reduction! so maybe mediated by tail?
    {'Mouse_ID': 'SWC_NM_043', 'Date': '100823', 'EID': 'eee1e6d6-4ab7-4a17-860e-209f1cf2ca31', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(122, 696))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '140823', 'EID': 'a0343dc0-911a-4ba8-a968-105274075537', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(169, 737))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '150823', 'EID': '380311ce-5021-412d-b9d7-d2f1e048ec63', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(98, 657))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '110923', 'EID': 'ca498612-10c7-4921-b394-87259e6ca735', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(146, 815))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '080823', 'EID': '949ffb0c-a81a-49ea-a5c8-b0f50400e955', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(172, 378))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '090823', 'EID': 'a775f6d4-d83e-4ef4-ae98-8a72a79d6517', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(127, 534))}, 
    {'Mouse_ID': 'SWC_NM_043', 'Date': '080923', 'EID': '44da6b87-38ed-4544-8f93-adaff91c92de', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(80, 527))},
    {'Mouse_ID': 'SWC_NM_043', 'Date': '130923', 'EID': '62370077-f4eb-4d34-95cd-eeaf8f932602', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(55, 366))},
    {'Mouse_ID': 'SWC_NM_043', 'Date': '140923', 'EID': '336a7390-5f64-4217-a9ba-832083f1cb16', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 'unknown', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(103, 523))},

    ###### 56 labeled with transsynaptic AAV... interesting expression pattern, but difficult to interpret
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '081223', 'EID': 'f3a3d4da-ec17-4930-9082-cc570a16716d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.6, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 827))}, #no effect?
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '111223', 'EID': '3ea50895-2063-4336-8311-5a3cfa32bcf1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1.6, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 909))}, #no effect?
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '131223', 'EID': '8e20306b-a905-4806-8a59-bb0453714c63', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 458))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '131223', 'EID': '8e20306b-a905-4806-8a59-bb0453714c63', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(458, 909))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '141223', 'EID': '12afeae7-e40b-4670-87bb-f32d81dd182e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 362))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '141223', 'EID': '12afeae7-e40b-4670-87bb-f32d81dd182e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(362, 968))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '151223', 'EID': 'ce616651-aba5-4754-91f3-79d5e929ec70', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.6, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 974))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '160124', 'EID': 'e3406c05-3b36-42f4-8bc1-fe8cb62a78fe', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(73, 350))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '160124', 'EID': 'e3406c05-3b36-42f4-8bc1-fe8cb62a78fe', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(350, 743))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '170124', 'EID': '2cefd1e7-fae4-41ad-acaf-269beda3e863', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(408, 853))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '180124', 'EID': 'd79cc64d-74d2-486c-b4d6-a9ea28aa4bce', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(212, 450))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '190124', 'EID': 'c71ffa2c-6b02-4832-9ea4-23aedc25775a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(28, 400))}, #truncated for better performance early trials
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '220124', 'EID': '3eeb5340-a35f-437f-a8ff-adc9190b33fa', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(120, 730))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '230124', 'EID': '1c60efd4-1e37-4e84-bfa3-57df2d8e921e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(26, 680))}, #poor performance; very right-biased
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '230124', 'EID': '1c60efd4-1e37-4e84-bfa3-57df2d8e921e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(26, 680))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '250124', 'EID': '2abdd68c-719f-45b3-975d-219e956c0896', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(142, 760))}, #below thresh performance
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '260124', 'EID': 'ead2158a-777a-4c3b-a801-8fd8dc526e4e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'LS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(90, 550))}, #truncated for better performance
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '290124', 'EID': 'fc5768de-6a49-47ca-9060-e057c83660cf', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(86, 779))}, #no effect; performance below threshold
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '300124', 'EID': '3ddde045-3407-4300-9086-b6a6aba096fb', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.6, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(208, 779))},
    # # {'Mouse_ID': 'SWC_NM_056', 'Date': '310124', 'EID': '169a5507-5b0a-42e6-9868-64bc729642ca', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(42, 500))}, #possible fibre optic connection issue
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '010224', 'EID': '397de733-6e48-4e69-ae57-1857d42d63f3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(155, 964))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '020224', 'EID': '8b49240f-6fc2-40ab-afd6-0a3ed5d029ba', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.2, 'Opsin': 'ChR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(203, 981))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '050224', 'EID': 'bd6ac1a8-e9e0-4d4f-8e6c-ec4764c6dc38', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(103, 805))}, #below threshold perf
    # # {'Mouse_ID': 'SWC_NM_056', 'Date': '060224', 'EID': '2700b05b-8ae5-43c1-a187-4fb8033bf566', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(103, 805))}, #ALF not found
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '070224', 'EID': '79510270-8d6f-45ac-ae13-1eb0b70ee956', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(191, 864))},
    # {'Mouse_ID': 'SWC_NM_056', 'Date': '080224', 'EID': 'b318d1e2-d04a-4a10-9577-7598bfaf7c27', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(178, 600))}, #borderline
    # # {'Mouse_ID': 'SWC_NM_056', 'Date': '090224', 'EID': '73673d45-3d3e-4c6d-a1d7-069bcdc660b9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(178, 600))}, #ALF not found

    # {'Mouse_ID': 'SWC_NM_061', 'Date': '230124', 'EID': 'ec0fa759-fb8d-4583-adff-545579d02dce', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(150, 745))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '240124', 'EID': '79a8bb3d-973c-4cc3-a1ed-1be62424d308', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(100, 988))}, #slightly below thresh perf
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '250124', 'EID': '919c4ecc-eba0-419a-806b-9ef7040ea66f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(99, 612))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '260124', 'EID': '4bccc228-5f10-421f-8f98-842d9df965e7', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(79, 524))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '290124', 'EID': '6e2feaad-6735-4cd5-8f1b-ca49c63f869f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(103, 837))}, #below thresh perf
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '300124', 'EID': '65e3d003-86ce-4a3a-97c3-c4dd66b135ef', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(125, 1098))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '310124', 'EID': '62408fb2-51d3-4e21-82f1-e90d0ee8a562', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(102, 939))}, #StimOn times are NaNs for large chunk of experiment???
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '010224', 'EID': 'beb87938-085a-46fb-9b4f-adb18d94b3ff', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(114, 600))}, #slightly truncated for better performance
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '020224', 'EID': 'b867d7a6-c5c9-4419-81db-02e1ef792dcc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(114, 600))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '050224', 'EID': 'e91a39fa-c9c2-463c-91e4-3bfa8a1f266f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(81, 650))}, #poor performance
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '070224', 'EID': '137f9902-2aae-43a2-abef-ad4b00c8b7ee', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(92, 998))}, #laser may have malfunctionaed; check TTLs
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '080224', 'EID': '9045d85d-8be9-4431-961c-454a4ae4c113', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(124, 874))}, #seems like an effect
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '090224', 'EID': 'd1a7305b-c07f-46b6-9bfb-1f34b2876a0f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(86, 1010))}, 
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '120224', 'EID': '59c9ddb4-95fb-430f-8e92-3435e7f11ae2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(118, 1008))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '130224', 'EID': '8e16875a-8f19-4125-87d2-abcceada5bf8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(100, 968))},
    # # {'Mouse_ID': 'SWC_NM_061', 'Date': '140224', 'EID': '13b81964-ee05-41c1-8c65-1fb8bb1d4d97', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(100, 968))}, #all vals NaN???
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '150224', 'EID': '4cdea218-6d55-4265-af23-a38349e84903', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(106, 927))}, #strong effect
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '160224', 'EID': '27d39424-127e-40b3-a600-963f186749ba', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(50, 1102))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '190224', 'EID': 'fd3e76c5-af11-4294-addb-56a122f69b5f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(53, 1091))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '200224', 'EID': '7e13e5d1-a9f1-46de-bf8a-abb3ef9e8f2d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(130, 850))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '210224', 'EID': '87e41888-ec3c-47bc-b083-ee52801bcaec', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(65, 1022))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '220224', 'EID': '9260688e-d0a6-4d66-8f9b-12290b0f5b5a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(41, 1163))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '230224', 'EID': '4fa6ec43-335a-45be-b7b8-67545e3f10d4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(44, 993))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '260224', 'EID': 'effb0de1-e735-4acd-b089-d3fc62aaf7f6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 1144))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '270224', 'EID': 'e3012b9a-2683-46c3-92e3-4b45bd1d216e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(31, 1252))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '280224', 'EID': '38500ad9-7d0d-4c81-9871-19ae2ee5c81d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(153, 878))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '290224', 'EID': '8e49de0e-0464-40e0-8e74-16a72545d4c1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(72, 1184))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '010324', 'EID': '26b9a747-2791-4002-8154-42414913b71a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(35, 829))}, #little obvious effect
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '040324', 'EID': 'f16af7a4-81ca-453f-a8f6-b689d6f37a0a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 734))}, #interesting sided bias
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '050324', 'EID': '70e56f1c-1644-4812-bfb2-19dd92d337e1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(37, 1003))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '060324', 'EID': 'b29e4454-feeb-44b8-ad8a-8baf9ddd5420', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(171, 1000))}, #no obvious effect
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '070324', 'EID': 'a5477ea9-1624-47d0-887f-1fe245eb010b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(66, 600))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '080324', 'EID': '11f74379-a3cd-4f7f-92fd-b9393f23c819', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(25, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '110324', 'EID': 'fe561305-783c-40b2-9de7-90475d469a97', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(25, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '120324', 'EID': '37d78308-a937-417e-ad91-20f924420886', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(15, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '130324', 'EID': '5a882ad3-fd90-42ed-b92e-26a721ae6a71', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '140324', 'EID': '61d63ba2-a411-465f-948b-734f6968456e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '150324', 'EID': '9eefabc2-fb10-42f8-8056-45e76abab886', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '180324', 'EID': 'f2663ef3-c4e5-45af-a5db-1bbbf44039cd', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(9, 9999))},
    # {'Mouse_ID': 'SWC_NM_061', 'Date': '190324', 'EID': 'ec1479f3-2cf6-43ad-ab50-6055b975a974', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'DLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(10, 9999))},
    ### EXTREMELY small infected area: R DLS, L inbetween DLS and DMS. Expression may be negligible...

#potentially strong effect R cont, unclear L cont; potential effect R 50hz, need more data L 50hz

    # {'Mouse_ID': 'SWC_NM_065', 'Date': '190224', 'EID': 'f97c3110-b38d-4b44-bd77-885061a741e1', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 672))}, #no stim
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '200224', 'EID': 'ae7d982d-4f45-4e81-9dc3-5810f3004450', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 716))}, #no stim
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '220224', 'EID': '99c5cd8f-817b-4e7d-97d1-7d89cd54af3e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(39, 864))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '230224', 'EID': '241f00a1-f73f-4c90-908e-e3f548d48664', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(53, 864))}, #no obvious effects from last 2 days
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '260224', 'EID': 'cd998125-3ee8-4b01-b362-66e9f82d0ab8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(27, 800))}, #no obvious effect
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '270224', 'EID': '84c6c1fa-0830-4923-a649-716f79451384', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(56, 762))}, #possible effect, low baseline bias
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '280224', 'EID': '395d7e8b-babe-4f39-b9f7-f62444002e36', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(58, 687))}, #no baseline bias
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '290224', 'EID': 'c34237da-348a-429e-830c-f881553f901e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(39, 679))}, #no baseline bias!
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '010324', 'EID': '5a6f0dae-2bee-439c-9da0-f69a6d1d18dc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(105, 841))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '040324', 'EID': 'e5ff91b5-4338-4ed9-8472-3c06deb4d416', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 625))}, #no stim
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '050324', 'EID': '3751487f-db0a-4905-ba89-0ddbe5b721e3', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 801))}, #no stim
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '060324', 'EID': 'a9e099d3-2159-44f9-9e49-f42f360e6d75', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 886))}, #potentially strong effect
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '070324', 'EID': 'be1b5f79-1d0c-4156-bb85-d659639c5f0d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(133, 1216))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '080324', 'EID': '95f11fa0-a548-4eb5-8fa4-d62e2d1db0f3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(110, 857))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '110324', 'EID': '9cf85b9f-9151-4f38-b59b-1f2cd1fda704', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '120324', 'EID': '09fc5d05-d1a9-41f0-8399-d367a16a0a48', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #strong effect
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '130324', 'EID': '9fec4695-637b-4a22-ab75-f751546e3729', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 934))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '140324', 'EID': '31aaf34d-04ea-4713-b2af-dffddd2ffafd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # # {'Mouse_ID': 'SWC_NM_065', 'Date': '150324', 'EID': '958fe706-71d6-41a9-9927-1dd6303917f2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, #ALF not found
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '180324', 'EID': 'b05d84d0-ee90-478b-b172-02122295fad0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(18, 9999))},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '190324', 'EID': 'e012f6c9-4a7e-40c4-9174-8fcbddd2b21c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '200324', 'EID': '1a4ad434-630b-4b3d-866a-f6b7556b9cd1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '210324', 'EID': '811df538-0391-4c57-9165-d4f6f336da12', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '220324', 'EID': '7776fc4b-88f6-4d1d-bca6-67f1f301259f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '250324', 'EID': '2ee29830-76f1-43dc-9851-c10eccdc12dd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '260324', 'EID': 'aedf9c64-5605-4beb-8fb4-a2ef66ecd4b4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '270324', 'EID': '1f932c9b-17b8-4915-acb9-134735bcd045', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '280324', 'EID': 'c1f650d5-fee2-4ec1-8ed4-d7bb4ce3cb0c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '290324', 'EID': 'a34085ff-e190-46b6-b786-df0be8e0227e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '040424', 'EID': '7405c333-5640-40fd-8f41-b69dc0f2433c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(15, 350))}, ##### can concatenate into 1 session; wanted to separate to show difference between stim intensities
    # # {'Mouse_ID': 'SWC_NM_065', 'Date': '040424', 'EID': '7405c333-5640-40fd-8f41-b69dc0f2433c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(15, 9999))}, #ALF not found
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '050424', 'EID': 'ed7f9aa6-cbb6-4fb0-a96e-b8689c4d8cea', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '080424', 'EID': '75aa4c2f-4c7b-4fb2-b062-aa3f99b3126f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '090424', 'EID': 'e0638e3d-00ca-4338-88ce-8703b1bf779e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '100424', 'EID': '51dba745-99cd-4e76-be99-8b05db536355', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '110424', 'EID': '31aaf34d-04ea-4713-b2af-dffddd2ffafd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '120424', 'EID': '2e4e763c-aa49-4ba0-a194-86f0ae0d537e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, ### getting trials table missing error for this session when running GLM-HMM???
    {'Mouse_ID': 'SWC_NM_065', 'Date': '150424', 'EID': '145f7e0f-6382-4e4e-aaa5-51806621de85', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '160424', 'EID': 'e6854350-cc03-49e8-9c7e-8f5e13c4c757', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '180424', 'EID': '2d3f78c0-b7f8-4045-9bc1-8c76a7ae4a51', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '190424', 'EID': '640c41b6-632b-4c9b-ae0f-595e43b2d5aa', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '220424', 'EID': 'ff3955ec-e7d1-4a50-bfa6-95ea6c7eb4fb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '230424', 'EID': '5525a41a-687d-44ee-9af2-2c46e53a27ce', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '240424', 'EID': 'c70d6be4-a6b0-43e1-8dad-4112e421786d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '250424', 'EID': '799d763e-b415-4766-8e22-36c318c57b3b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '260424', 'EID': '640c41b6-632b-4c9b-ae0f-595e43b2d5aa', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '290424', 'EID': '15ab17c6-d15a-4479-9ccb-6834511d046d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '300424', 'EID': 'c0b113eb-6de8-4606-a910-7adb14004af4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '010524', 'EID': '2184a7ac-dca7-46db-b727-5180a7c6b0d0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '020524', 'EID': '6399109a-f03d-46b8-82fc-fe205b682749', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_065', 'Date': '030524', 'EID': '08e1b2b9-ecc2-424c-871f-78fcca7edb79', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_065', 'Date': '070524', 'EID': '7795ff62-2f62-4452-abf5-ffedbdf0c6aa', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, #poor performance
    ###Posthoc:
    ### Both hemis good expression.
    ### R hemi caudal VLS; cannula over infected site. 
    ### L hemi ok location, though more VMS; cannula NOT above infected site

    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-06-24', 'EID': '98566e39-3e37-4943-8ed3-fa608febc6a2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.3', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 313))}, 
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-06-23', 'EID': '4b0a4d16-86fb-4a2d-a57b-01303e0fd139', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.3', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(330, 344))},
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-07-21', 'EID': 'ffd8912b-7b5f-4f81-aabc-b4ce4aea9ec2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': '0.3', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(254, 508))},
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-08-13', 'EID': '85d98d54-2149-4310-8cb0-02a44c6a4bc4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.05', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(207, 9999))},
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-08-13', 'EID': '85d98d54-2149-4310-8cb0-02a44c6a4bc4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.05', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 197))},
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-08-12', 'EID': 'e801d9af-7d38-46f8-87ca-cb4c89f25d6d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.05', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-08-11', 'EID': '3d7e08ed-d801-4081-bb71-ec4b6a51643e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.05', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(130, 260))},
    {'Mouse_ID': 'SWC_NM_093', 'Date': '2025-08-11', 'EID': '3d7e08ed-d801-4081-bb71-ec4b6a51643e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.05', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(265, 9999))},

    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-22', 'EID': '75876671-a6c4-49ce-96e8-ea860ceff3b9', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-19', 'EID': '4c59db6d-5a1c-4d26-9201-fcd3c74c3bad', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-18', 'EID': 'ef541b2e-e60a-4c92-9953-afdc7c642659', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-17', 'EID': '0a88f2f7-cf09-4dbc-ae3a-92d5dd221d0e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(175, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-16', 'EID': 'df18fbc5-1306-4baf-b463-6252137f7e90', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(259, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-15', 'EID': '6926d194-3d7a-4aa2-a03c-5aa27969cc10', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(203, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-12', 'EID': '63d72a1f-af17-4dac-a2e6-0d852fd0e89a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(177, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-11', 'EID': '01654936-4daf-403b-b55c-ce2baba12a15', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(130, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-10', 'EID': 'c34afa9d-872c-4237-b585-62dac85b333a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(271, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-09', 'EID': '60e8aba2-d738-45c4-be58-8602cdb94873', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(214, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-08', 'EID': 'bbe8ea3d-b942-4d56-b281-baed2f3d3143', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(444, 9999))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-08', 'EID': 'bbe8ea3d-b942-4d56-b281-baed2f3d3143', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(208, 443))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-05', 'EID': 'be392f15-acc6-4f9c-ab8d-03dc7c09dd77', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #### MOUSE ALWAYS TURNS LEFT ON STIM TRIALS
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-04', 'EID': '27726b68-6bc1-46b4-8456-38b7b046363c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #### MOUSE MOSTLY TURNS LEFT ON STIM TRIALS
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-03', 'EID': '7e1987cc-ca9a-4b64-bb5f-a68726e36f52', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #### MOUSE MOSTLY TURNS LEFT ON STIM TRIALS
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-02', 'EID': '9fa6297f-93a9-499d-ae38-2eed6e55565d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(522, 9999))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-02', 'EID': '9fa6297f-93a9-499d-ae38-2eed6e55565d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 522))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-09-01', 'EID': '987d7a03-ac5f-46c2-a2f4-e1e69f1aa1d9', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(200, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-29', 'EID': '677fe3e5-1d1e-4123-9250-28f5e3be2e9b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(136, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-28', 'EID': 'a3a49b17-4218-4a37-953c-db7e772a6c04', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-27', 'EID': '9d67f331-b93f-43a9-a8af-22c48efc338c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(184, 9999))}, 
    # {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-22', 'EID': 'f2bb0cc0-f032-4ceb-b71d-fb7fbbd0693b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(214, 9999))}, ### laser leakage throughout session
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-21', 'EID': '33567616-744f-4c22-b89b-6d3f299e8a79', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-20', 'EID': '221997ed-9cb5-45d1-b7b9-e1af87103a58', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-19', 'EID': '25d98c34-1509-4726-970d-15ce47cf082f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(238, 9999))}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-18', 'EID': '40755583-4d49-40c8-9443-57a918d0199f', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-15', 'EID': '161f9fcc-4d8f-48c0-9ca9-b939dfab1971', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-15', 'EID': 'ee207cfd-ec3e-4339-b528-b9c4cbcf5e05', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-14', 'EID': '17117ae2-7ce0-45a6-8c59-62c9b022031c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(289, 9999))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-14', 'EID': '17117ae2-7ce0-45a6-8c59-62c9b022031c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 288))},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-13', 'EID': 'd01fb7d7-aa75-445b-87b0-d6f9ca4f0749', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-12', 'EID': 'fcf436ec-3081-4022-8f7d-59fce5739b46', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_096', 'Date': '2025-08-11', 'EID': '70ea21e6-0685-4481-82e7-8f482f877551', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(250, 9999))}, #### LASER LEAKAGE FOR THIS SESSION

    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-19', 'EID': 'fb58c66e-7665-45b3-baef-f0b0d37db401', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-18', 'EID': '1ea03aba-66cd-44e6-85ea-bc3d28474da3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-17', 'EID': 'd39a690f-c5f0-4927-807d-a5ce9fbf560a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '1', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-16', 'EID': '46d00485-e888-47bf-891c-caa4e6b7daeb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-15', 'EID': '61ccdca4-de6f-4e43-a95a-f692ca462758', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-12', 'EID': '910a7d48-fe52-4855-94ed-64651b10ee1d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-11', 'EID': '7ec2eda9-6d40-4715-9b7a-1937dd510624', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-10', 'EID': 'e9ad1a64-736b-410b-8592-8adb6ccf74d2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-09', 'EID': '955abb09-d135-46cb-ac39-6b5823fa11f6', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(260, 9999))}, ### no QP effect??
    # {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-08', 'EID': '861166e8-8068-4b36-ba41-8f06de73c4a7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.2', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(709, 9999))},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-08', 'EID': '861166e8-8068-4b36-ba41-8f06de73c4a7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-05', 'EID': '50e9975d-4d1b-4bdf-9700-5193024127a1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.7', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(290, 9999))}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-03', 'EID': '51a8f78c-d7cd-48c5-a91b-fbebfc545680', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-02', 'EID': 'e7b286b2-d85a-44f1-ba60-51067d04ffbc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(480, 9999))},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-02', 'EID': 'e7b286b2-d85a-44f1-ba60-51067d04ffbc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 479))},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-09-01', 'EID': '346fa27e-f31c-4141-94ea-ab3b5efc32ec', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-08-29', 'EID': '6f084e26-ddac-4800-bc72-05ed524df87c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.5', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### responses shifted toward right choices, but bias definitely still present. little QP effect, but significant RT effect
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-08-28', 'EID': '84ceb0bb-9d9b-42e8-9c02-654e565f5e58', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(305, 9999))},  ### responses shifted toward right choices, but bias definitely still present. strong QP and RT effect
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-08-27', 'EID': '9004822e-3c87-4ff5-95fe-81f231598f46', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-08-22', 'EID': '00cebbaf-4690-4658-9f7b-fa5a078bd9bc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(47, 9999))}, 
    {'Mouse_ID': 'SWC_NM_097', 'Date': '2025-08-21', 'EID': '6348cbec-e2bc-4944-af11-7e58087ea42b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': '0.3', 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(227, 9999))},
    #### L hemisphere: obvious QP effect at all stim intensities, but no obvious bias effect...
    #### R hemisphere: similar, but possible block bias effect

    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-10', 'EID': '1c4f2c31-9ed1-4f29-a6f6-313aad758a00', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-09', 'EID': '890959d8-d0d3-4194-9726-a3e47577471f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-08', 'EID': '234a754d-05ec-464b-ad0b-4d9cf111bf31', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-07', 'EID': '2a63e833-6a5e-4335-92d7-d4ebfdae576c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-06', 'EID': '276cf129-81e8-4a46-bef6-b10c8242e8eb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-03', 'EID': 'a3a18538-7b1f-4f70-9dea-26e00733ecdc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-02', 'EID': 'dfbd3890-09c4-4273-a7b5-f90044ce0f0e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-10-01', 'EID': '3047075f-fe45-4a2d-8cf7-7b20210b1073', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-30', 'EID': '8ac1f470-b67c-46aa-a05a-0dc022ddc4cf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-29', 'EID': '7761f18b-7335-4b79-aad8-d8c77c21468a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-26', 'EID': '179ea229-b179-4a9d-ac7a-8bfc60e6dce4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-25', 'EID': '05648028-3a12-4c33-ac0e-62d47ce52779', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-24', 'EID': '9e24f2e8-b3a8-4604-a042-d85eb9f921d6', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-23', 'EID': '63770e4b-7896-48d8-b17d-0bd480df1dc4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-22', 'EID': 'd7eb6ed5-d623-40ef-a822-83e91b4cd0dc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-19', 'EID': '5cc0d75c-302c-4a50-b659-c50fb4fd0181', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-18', 'EID': 'fa1adb19-64a2-487a-8460-20899c15a12b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-17', 'EID': '4c0c3e0c-5431-40fb-adad-2c92759e2b14', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-16', 'EID': 'a677bdd8-81a1-4066-9a9a-bf340450302e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-15', 'EID': 'd66bb33c-d59d-4ab4-827e-2e7550afa856', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-12', 'EID': 'bb6e4032-62e4-4e81-932f-3e306b4b10a4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(4, 9999))}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-11', 'EID': '2853b63d-9306-46a0-aab5-8137ba7111ea', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(30, 9999))}, 
    {'Mouse_ID': 'SWC_NM_098', 'Date': '2025-09-10', 'EID': '13178d45-3a38-4f86-bcfc-b2ee03aeb148', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    #### Assessment (through 6/10/25)
    #### L hemisphere: RT slightly but significantly higher, QP very significantly higher, no obvious effect on bias shift. There's something going on here but not sure what...
    #### R hemisphere: RT significant decrease, QP slightly higher (not significant), no obvious effect on bias shift.
    #### Bilateral: RT no change, QP no change, bias unclear

    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-10', 'EID': '6f37d7b0-8aa4-448f-9469-8ceadf2d7dcb', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-09', 'EID': '956cb2a4-5bda-4d96-b8cd-496d700157eb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-08', 'EID': '627a7116-d41e-406c-ae78-9b13fbca3e89', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-07', 'EID': '06d5f438-7e79-47d1-8cfe-6fbc09cc2b8a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-06', 'EID': '0985a1e9-ed30-4197-bc76-88f4c26a9833', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-03', 'EID': '19422058-3daf-44a0-ad74-63b36312205c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-02', 'EID': '88c1806e-ad89-4c21-8365-c4861d5a612a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-10-01', 'EID': 'd2c3c17a-af3b-42ce-b6ef-b6d1e639bc2f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-30', 'EID': '0df4e3df-3e22-48cd-925a-04740662c707', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-29', 'EID': '6fed1652-f0b2-4194-89d4-21b043e14f92', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-26', 'EID': 'b759d11f-e9ab-414a-9363-996c140a9503', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-25', 'EID': 'd9ac52da-036b-405a-8280-c7a58a578786', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-24', 'EID': 'ab9f1a5c-9637-4837-90d1-dd2a666b08bd', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-23', 'EID': '374bf3c0-c12f-4612-9888-4e4a5cf0d1b8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-22', 'EID': '6686d0c5-079c-495e-939f-cd35f9da09dc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-19', 'EID': 'a9e6ca81-f6ac-4cf2-aefd-56ea2e10fea6', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-18', 'EID': 'f62fcab4-878d-4dc1-8f6f-38bb917ce6cd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-17', 'EID': 'c192f964-f05d-49cf-89c1-ab36f358d282', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-16', 'EID': 'fbb48e96-3e51-4ddd-bdfb-a6593bd933fb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-15', 'EID': '75d0b280-5413-4f4e-b05a-de481b693f85', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-12', 'EID': '16612840-7c5a-4344-939e-dea8d4a43c3e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-11', 'EID': '979436c7-383c-4093-b722-ec44b28750de', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-10', 'EID': 'c1095784-72f3-406b-b0d3-83fd7e305988', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-09', 'EID': 'ef9ea8b9-521f-4c0c-a74e-c797da71c5c4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-08', 'EID': 'd14f301c-2e12-4725-a4ee-d8185a039355', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-05', 'EID': '4801a128-66ae-4849-8611-65e71a19fd3b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1.0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-04', 'EID': '40394d09-a720-454d-959f-f7b4b238e477', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1.0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(254, 9999))}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-03', 'EID': 'bc5cc639-7ea2-4f25-be88-70f7e81e5d4e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.9', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-02', 'EID': '285d1920-3769-4535-931e-7429db4b89d2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.9', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-09-01', 'EID': 'd7c26891-6275-4a30-9584-74d7fada6cd4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-08-29', 'EID': '8ee3b9ba-d327-4583-a46f-02ef9b837d98', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(60, 9999))}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-08-28', 'EID': '363fb0df-7564-40d2-9fa1-d151a7b7d5b0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.9', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(30, 9999))}, 
    {'Mouse_ID': 'SWC_NM_099', 'Date': '2025-08-27', 'EID': '4a9f363e-cc0a-4823-aab9-d632a2c2873a', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    #### Assessment (through 6/10/25)
    #### L hemisphere: Likely partial block bias reduction, RT INCREASE (small magnitude but very significant), QP decrease (not significant)
    #### R hemisphere: Possible bias INCREASE!, RT INCREASE (small magnitude but very significant), no difference in QP
    #### Bilateral: No effect on bias reduction. No visible QP or RT effect

    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-10', 'EID': '43b5d796-81ce-4ffe-b914-473402b1b113', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-09', 'EID': '5db032e9-d6c6-4e33-890b-c4dcc7806174', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-08', 'EID': 'dd0dd584-3b33-4560-8a53-ce2b4264350f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-07', 'EID': '5e628333-71ee-49e3-a733-ae69aaa85efc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.7', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-06', 'EID': '0e6fe1ec-5fe6-4078-8548-acd39c5cfd1e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '1', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-02', 'EID': 'c684a122-d976-458f-a101-23e772abfbc8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-10-01', 'EID': '921cae2f-edd8-47a4-bb6b-de2326625356', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-09-30', 'EID': '96bb0ab8-9671-4d53-8f82-4297b91f45cd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': '0.5', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_100', 'Date': '2025-09-29', 'EID': '76056eba-5ef0-4603-a4ff-1b6efa4eb5a3', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': '0', 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': 'ALL'},
    #### Assessment (through 10/10/25)
    #### L: Likely partial reduction in bias
    #### R: no obvious effect
    #### B: strong RT reduction, slight QP reduction, strong bias reduction (1 session)
    
    {'Mouse_ID': 'SWC_NM_052', 'Date': '220124', 'EID': '0791cb99-2876-4797-b5a2-349334077c57', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(142, 450))}, #truncated for better performance

    # {'Mouse_ID': 'SWC_NM_070', 'Date': '010324', 'EID': 'fc3861a2-8b0a-4223-a17c-40f12e342e17', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 1))}, #no stim
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '?', 'EID': '40b5a7fb-85c7-465e-8c4f-cc8fa0a87647', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 1))}, #no stim
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '050324', 'EID': 'f5df1ac8-46e2-42d2-b245-ba4d13136998', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(120, 1221))}, #no obvious effect
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '060324', 'EID': '2c9b7188-2f5d-4a4d-8e07-b43d497ad9a1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(51, 947))}, #no obvious effect
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '070324', 'EID': '540bf120-c344-4d22-b9a6-b5d1c4e29b76', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(274, 679))}, #maybe slightly lower QP
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '080324', 'EID': 'fddc2483-c44a-432d-aabf-70c99f004b08', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(135, 1154))}, #no obvious effect; bias actually higher
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '110324', 'EID': '15f815a1-af3b-43f5-b694-59ace2532c1b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(6, 863))}, #no baseline bias
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '120324', 'EID': '634325ee-9bfb-4c78-95e4-8dd49adb0b92', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(12, 884))}, #poor performance; possibly weak effect, but low BL bias
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '130324', 'EID': '7de50f80-d6e9-4291-b9ed-c6a182ea7ced', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 847))}, #no obvious effect
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '140324', 'EID': '7fa95cda-c1ef-4c88-875b-a924b5b3d755', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(20, 974))},
    # {'Mouse_ID': 'SWC_NM_070', 'Date': '150324', 'EID': '3ff09241-7792-4ec2-b3af-9f570e916d4e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 1221))}, alf object not found

    # {'Mouse_ID': 'SWC_NM_069', 'Date': '180324', 'EID': '8380a4e0-943d-4c2d-a248-4ade9ab9be0e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(101, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '190324', 'EID': '460f6c9d-d5a5-47da-84ab-cd7abb4b77c6', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(110, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '200324', 'EID': '9edcbec3-b364-415b-9945-568037e6ac31', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '210324', 'EID': 'fed8a88f-371d-401c-90f7-cb8f6745ce5c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '220324', 'EID': 'c62011ee-27be-4227-9bb7-9442106f8a43', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '250324', 'EID': 'ad1fcf7b-5053-4cd0-a1d3-1c8df6d52fd8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '260324', 'EID': '1e4519c7-48ff-43c0-8758-d438acd979dd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '270324', 'EID': 'c96e3ddc-a385-4db7-8119-4829348bad67', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '280324', 'EID': 'be733c7b-cc9a-4aec-b687-9040bad3764c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_069', 'Date': '290324', 'EID': '87f77fc3-3851-4fc8-8629-37736cf22765', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    ### there is a tiny bit of expression in rostral SNr - double check this mouse to see if there were any behavioural effects

    # {'Mouse_ID': 'SWC_NM_066', 'Date': '080424', 'EID': '86fb1af6-6542-4fa6-b693-ef3b720a0aa2', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 620))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '090424', 'EID': '0cbf1727-2b4d-4544-98e7-33784c1759ff', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '100424', 'EID': 'f187b248-4f0c-4158-b872-7ad3232fc376', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # # {'Mouse_ID': 'SWC_NM_066', 'Date': '110424', 'EID': 'd4e83013-41e3-4430-8339-1ab899eeb436', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #session not loading for some reason
    # # {'Mouse_ID': 'SWC_NM_066', 'Date': '120424', 'EID': '0d26211b-8dfb-4fb1-a6ff-04bf721966cc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #session not loading for some reason
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '150424', 'EID': '54a4c67f-d014-4324-bac2-114e747c65e7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '160424', 'EID': '97d57a38-ea49-42a2-9d03-9616397f03d4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '180424', 'EID': 'f4b5ec94-47ee-42e8-b67e-c1976d1eb4cf', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(17, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '190424', 'EID': 'ac041440-61ea-449b-862e-68c1180b6aa0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '220424', 'EID': '802379f3-07f9-4f75-98d8-d57c4ea38174', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '230424', 'EID': 'b5493e77-3f20-414a-aa92-426903724e44', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '240424', 'EID': '0232eace-282d-485e-b4d5-01cef434c304', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '250424', 'EID': 'd56371ec-b39b-4e18-b6d3-5ac93b8686f1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '260424', 'EID': '0c0b8440-191d-466e-8d35-b3abe72fdeb6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '290424', 'EID': '0be8be61-d68e-4ce2-8f62-55657ecde2e0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '300424', 'EID': '286beb01-193b-4175-a9a3-f09e1aafdda0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '010524', 'EID': '1c302eb3-9333-46cc-86c4-49d348363e39', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #not great perf.
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '020524', 'EID': '4d564fb9-7de6-4c13-9102-2e604b030cdf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #not great perf.
    # {'Mouse_ID': 'SWC_NM_066', 'Date': '030524', 'EID': 'f4940470-8672-489f-8dcd-a6a1bb3dc213', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(0, 9999))}, #low baseline bias
    ### NO VISIBLE EXPRESSION

    # # {'Mouse_ID': 'SWC_NM_074', 'Date': '220424', 'EID': '41e0b8b9-d34a-4b22-8c62-0e2c7a4e212f', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 0))}, #no stim
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '230424', 'EID': 'df52e48e-a4fe-4a68-9373-fbb669fb659a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(297, 9999))}, #left hemi questionable
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '240424', 'EID': '3cd052ae-071d-41de-a130-ad94065c2c9a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #no RT effects, but likely bias effects!!
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '250424', 'EID': '1747ca69-78da-4530-ade3-6090d3fdb043', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '260424', 'EID': 'e08cbf02-867c-45a4-9816-26166275975d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #left hemi questionable
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '290424', 'EID': '6d7dd289-04e0-448e-a1cf-67809b1364da', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '300424', 'EID': 'e60a4771-66d5-46c6-a6eb-3a23e558f1ea', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.4, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '010524', 'EID': '5fdfbb1d-f46f-41af-8ee0-79bf7c5323e2', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #left hemi questionable
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '020524', 'EID': '7511b8e8-c10c-42f0-b4c1-83fead7e5073', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '030524', 'EID': '3ebecde4-b12a-410f-83a5-e9dedf00a67d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '070524', 'EID': 'e8b11cf5-5064-493a-9e59-a2210e88b1be', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #left hemi questionable
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '080524', 'EID': '73177d20-98b1-41e4-9a32-91479f325806', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '090524', 'EID': '83e0fa0d-a935-4d4d-8a29-6a2a9233504f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '100524', 'EID': 'aaff1d52-ec73-4bb2-92b9-2fcfbe029dc3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '280524', 'EID': 'dbed6283-d9be-4e2b-bca2-6d3f13af752a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '290524', 'EID': '08bf1ed8-368d-41f2-8ab2-7c40e12dff27', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '300524', 'EID': 'c44bf173-4e4a-4724-bfe5-68fee3a7e613', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '310524', 'EID': 'bb018dcf-2b48-4a60-86c2-88a730f14162', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '030624', 'EID': 'b476b3d8-7989-455a-88ad-fa9701df34d5', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '040624', 'EID': '0c56d5c0-1fe4-4253-a465-c0ecbb336051', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '050624', 'EID': '94fb433f-9fc6-492c-81b5-b687ae3d668b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '060624', 'EID': 'a9d29ef7-9cca-4ebc-9ee9-ec97e293122e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '070624', 'EID': 'b28dded6-dbf2-47b3-8c78-5204e04c808d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '110624', 'EID': '52047688-e58e-4ede-b293-2f52cb6facf8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '120624', 'EID': '627632ff-bc62-4eaf-8611-b25f4bcc4c89', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_074', 'Date': '130624', 'EID': 'e664befb-4eb6-4f49-8949-ac845ada107b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # # {'Mouse_ID': 'SWC_NM_074', 'Date': '140624', 'EID': '3e5c12d2-7603-41ce-8853-a0af27de3772', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # little/no effects seen
    ### NO VISIBLE VIRAL EXPRESSION

    {'Mouse_ID': 'SWC_NM_073', 'Date': '010524', 'EID': '249bc715-8fe4-492e-84dc-3fb2e15a3098', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(35, 500))}, #not great performance
    {'Mouse_ID': 'SWC_NM_073', 'Date': '020524', 'EID': '6a33474e-8093-4cc8-9cbd-866d04fdb511', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(80, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '030524', 'EID': 'f8a05df6-1b8c-4db5-acbf-1a594c5cf459', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '070524', 'EID': 'fe7fd83e-4ab4-4261-9486-0b6ae4d9f106', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(105, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '080524', 'EID': 'ccc33b10-302a-4df1-8465-481c0d227df1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '090524', 'EID': 'f34139fc-421e-45f3-9edf-33c2df9abdef', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 501))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '100524', 'EID': 'c279da4e-2a82-4ff4-8b00-812ee5c014ea', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 230))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '310524', 'EID': '27475e96-4a49-43c9-85c6-ab2fd1ad8bfe', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(100, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '030624', 'EID': '9e04d416-7463-4370-830a-bda8f03ffe17', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 194))}, #shit session
    {'Mouse_ID': 'SWC_NM_073', 'Date': '040624', 'EID': '3fd84daa-3664-4b52-acc9-d9fa30967094', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '050624', 'EID': 'ab3f75e4-4148-484a-927e-b394648c8d9f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(109, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '060624', 'EID': '0c2f75a0-853c-4f19-9334-ca09861f7305', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #behaviour session is 002; need to run code on server
    ### definitely something interesting going on here; looks similar to M2 effects
    {'Mouse_ID': 'SWC_NM_073', 'Date': '070624', 'EID': '2acbd25f-ab61-4fb5-bd2d-db7d2fb04f34', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(6, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '100624', 'EID': '39e1c450-023a-4aea-aa39-ebddcc2abfc8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 168))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '110624', 'EID': '346f7a43-e10b-498f-8f8b-c9802dadeabd', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '120624', 'EID': '9df83e5b-256f-4e48-8e1d-76517005710b', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '130624', 'EID': '464613ff-01f1-407c-9b47-098df406e8f4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(147, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '140624', 'EID': 'cfce8001-7886-4a62-9c0a-371fcbc95eb7', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))}, #not loading
    {'Mouse_ID': 'SWC_NM_073', 'Date': '170624', 'EID': '4a1df54a-92a1-4821-b0b5-3cbd97848e76', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    # {'Mouse_ID': 'SWC_NM_073', 'Date': '180624', 'EID': '6a03b56e-3c81-4189-b1b4-cbb58dea8241', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '190624', 'EID': '0d7b70c5-d484-4bb8-82c9-1eaa185f64d8', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '200624', 'EID': '2c599f47-5f22-4a89-9b9d-a4be933bd46e', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '210624', 'EID': '0f7f4435-5edd-4574-ad1e-1f03918969b8', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '240624', 'EID': '8f83a285-27e1-4d3c-9c5c-edade07d4f89', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_073', 'Date': '250624', 'EID': 'ab329d9a-7c14-4c67-9782-40fc519f9cd3', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D1-Cre', 'Trials_Range': list(range(0, 9999))},

    {'Mouse_ID': 'SWC_NM_075', 'Date': '080524', 'EID': '621b5fa5-099e-4742-bc56-51b420caf624', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '090524', 'EID': 'c440fe25-e089-43a5-addb-15550121c65e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(145, 255))},# + list(range(145, 255))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '100524', 'EID': '59e36c93-4521-4ab8-8976-2a160839a13b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(156, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '280524', 'EID': '0dd034e0-0e62-47f8-8e50-d502490e7e76', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '290524', 'EID': '5eeda094-ba6c-4841-824f-5e4fe510a50c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '300524', 'EID': 'dd1d73a8-6f44-4f7e-8569-d41fd051951b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '310524', 'EID': '659f874e-94fd-4893-94c7-88d1dc7b4ab4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '030624', 'EID': '2fd20dc0-7b3c-4a17-a2cc-26598e19c544', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '040624', 'EID': 'e8aa1538-c06c-49de-a34e-6f8365ed0054', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '050624', 'EID': '9e0a7760-b9bb-42c0-825e-3c5251b207f6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '060624', 'EID': 'f61429f8-a26b-4344-b542-0e2d0ffd146f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    ### appears to be some effects in both hemis, but not super strong... maybe infection is weak?
    {'Mouse_ID': 'SWC_NM_075', 'Date': '070624', 'EID': '0531294d-59c9-40e4-9ed2-9713225adf90', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(6, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '100624', 'EID': '12cf500c-8ff2-4869-9d03-d96cbc3b4b51', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '110624', 'EID': '2c20a300-df9f-4c6a-8ba3-f64ba97c7405', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '120624', 'EID': '17c2ae0d-a544-480a-92d9-b5dd9343ee5f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '130624', 'EID': '987355c5-6a71-4e8c-953a-a10636c90553', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '140624', 'EID': 'e6fa7043-003e-40b1-b5bd-5eee20937516', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))}, #not loading
    {'Mouse_ID': 'SWC_NM_075', 'Date': '170624', 'EID': 'f254cd11-068a-4aa7-84f7-60f40fffeff2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '180624', 'EID': '5e49deab-1a46-4cf3-9e5f-cde55bb8dc87', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '190624', 'EID': '0a9b42c1-d288-4c0e-8d53-9fdf747604fe', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '200624', 'EID': '833111ac-5bec-4972-a8f0-ef6f3c0225a9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '210624', 'EID': 'b75ecd8c-e366-420d-8299-30bbc7588f49', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '250624', 'EID': 'f1247f6e-8a2b-4d0f-b077-cf6a2ca263d0', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '260624', 'EID': 'a08916ed-54fc-4020-b14d-9fe9a7868e62', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-19', 'EID': '8004b03d-e3c8-4ba9-8f0a-bfc0fc596c4d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-16', 'EID': '079033a9-5634-441a-82a5-49edca8f4674', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-15', 'EID': '5fc30fed-fa09-4c79-b982-41eaeb2aef34', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-14', 'EID': '848434da-6be0-4a61-9cec-5f3cf0d0a887', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-13', 'EID': 'cac07f14-10f8-495d-ad84-291432e982d5', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-12', 'EID': '038c4cd0-2045-45e7-b545-44559a278e48', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-09', 'EID': 'a2bfb12a-ccd7-4a18-9fdd-7048a2c534f9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-08', 'EID': 'f9c72e4b-0fa5-4ee1-ac09-cb15dc0e3170', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    #####
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-06', 'EID': '7bb6d657-80d8-49d3-a2c4-308eb502d24f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-08-01', 'EID': 'ec68489e-b842-4891-b607-cf276bf2374c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-31', 'EID': '2e7c3399-2678-40c6-9467-a84f886f63c3', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-30', 'EID': '009eff64-f471-4ddc-8751-3f945cbf0d50', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-29', 'EID': '99f0ac4c-d845-49c4-b4f2-8c46177ba697', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-05', 'EID': '085a856d-27a5-434e-b6bd-11b64b532715', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-04', 'EID': 'ac1161dc-fbb1-4e04-9d94-697ff362df14', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-03', 'EID': 'e7dde8b8-c3f2-43c6-bd0c-f9eba8f930c3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-02', 'EID': '9be8723a-080c-45ed-ada5-7cb234996140', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-07-01', 'EID': 'aab9bc2d-2814-4115-b667-a6ede23cc9a4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-06-28', 'EID': '49c293f3-82c7-46e3-9d95-297644a7deb2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_075', 'Date': '2024-06-27', 'EID': 'e3ae1ed7-0c33-40a3-983d-61c535f1b2ff', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    
    {'Mouse_ID': 'SWC_NM_062', 'Date': '300524', 'EID': '70bc428d-5574-4947-af46-e79a7fbf5ce4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(170, 9999))},
    {'Mouse_ID': 'SWC_NM_062', 'Date': '030624', 'EID': '316520de-7703-4e8a-a713-83b0414cd18f', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_062', 'Date': '040624', 'EID': '14035386-2931-4272-89ac-e708d0b8d69f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    ### some behavioural effects evident from video, but mouse not doing task

    ### sessions are fine, but too lazy for now to normalize #sessions for full analysis
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-18', 'EID': '43bcc3ac-f0c7-4709-bb9a-9e0c3269f354', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-17', 'EID': '22a99058-05c5-499d-b8d8-1e518339e123', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-16', 'EID': 'a022ff94-4504-468a-86d1-c8843855bc1f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-15', 'EID': '86558f58-2797-4b54-b250-6652fecf8660', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.4, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-14', 'EID': '40a66952-1394-4731-bc71-e4ef9e505b3c', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    #### where is this session?
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-10', 'EID': '3c15cfc3-e57b-424d-84b7-2489163dfe19', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-08', 'EID': '558e5a5f-19c8-40b8-9de7-f54f7f00b7a1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-07', 'EID': 'deaf3fc1-fc08-423d-90a1-de9d83660005', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-04', 'EID': '1c59ff14-65c2-4101-a7e7-5461965759b3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-03', 'EID': 'efefdefa-2d45-4ec4-b0f4-f7945a63cc58', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #very strong effect!
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-02', 'EID': '234a7fc3-1a11-4409-9d93-002a23b69ba8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #strong effect, though BL performance below threshold
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-10-01', 'EID': '52bc8761-afd3-4fbb-b228-fcc440920399', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, #strong effect, though BL performance below threshold
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-30', 'EID': 'e4f778d4-f87c-4cdd-aa22-98faa2cd36cd', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-27', 'EID': 'a4a551db-0889-4f4a-9285-1ffc6fd48dda', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-26', 'EID': '40afc774-6d87-462b-9ac5-65e83ef8bdff', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-25', 'EID': '0dafbd97-f8ff-4473-834b-c7578f799980', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-24', 'EID': '5d889cfd-e44c-457b-b2f6-736a16e5405d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-23', 'EID': 'd3553faf-3dc6-4e2a-b327-84c8cc858067', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-20', 'EID': 'de0182da-0533-47dc-8103-fb89cbf5fb06', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-19', 'EID': 'b52455a5-411a-4628-8795-c3508d64e991', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-18', 'EID': '51708c15-7aee-4fa9-a67d-5064f73c408f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(58, 9999))}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-17', 'EID': '0bb12f9f-ba27-4da9-b697-c53965e708fd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-16', 'EID': '701023eb-5a2d-40b5-9830-3cd06c418bb8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-13', 'EID': 'c902ff1d-b68f-4940-9994-9b50db5f5f6e', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-12', 'EID': 'c85dbf9b-a7b1-4219-a576-d8bfb28f8a6f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-11', 'EID': '6d48b94b-61e7-41e7-8fdd-593a89b0fc0d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(277, 9999))}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-11', 'EID': '6d48b94b-61e7-41e7-8fdd-593a89b0fc0d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 277))}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-10', 'EID': '24eb918d-bd6e-49d7-9014-4852e63aa00e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-09', 'EID': '7f33eaca-ea29-4ede-9f98-4e7473e15f33', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.2, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # #####
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-05', 'EID': '4237835d-cf84-4b2a-88d1-58cbf416157f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-04', 'EID': 'ef2d33c6-89e3-4d7d-b626-a3f6b83db72d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-03', 'EID': 'b0dbf8d2-72fc-45af-b9ab-9e28fb2cc953', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-09-02', 'EID': 'dc59ebc0-400d-480a-a886-d727846b8e47', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-30', 'EID': '18a9f2ef-88de-4494-88e7-069e60242202', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-29', 'EID': '4b772b22-f7df-4f0b-a78d-a8db3c60a8a8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-28', 'EID': 'a1b744fd-828f-456c-9a4a-fadfee19de1b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-27', 'EID': 'd5cb4a94-0e4b-44ea-aee9-8fd2f5a70dc2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-23', 'EID': '82c1f04f-ea07-41fa-a8a9-bff69ee72b6a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-22', 'EID': 'a3264491-161d-4add-9c69-5d9c613abec6', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-21', 'EID': '28c7741c-07dc-4972-9a55-cd49460df4fd', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-20', 'EID': '8547e4c3-6cd6-493a-ac0e-395424a8084b', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_080', 'Date': '2024-08-19', 'EID': '6c339ccb-c7ac-47b8-9943-fd4262f620da', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_063', 'Date': '060624', 'EID': 'ffc5253b-70a7-4166-97de-5387d6f50633', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '070624', 'EID': 'da8e7231-8ceb-4efa-a3e1-3e3838b420b6', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '100624', 'EID': 'e6542b28-ffea-4607-b1a2-95162bb26919', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    # {'Mouse_ID': 'SWC_NM_063', 'Date': '110624', 'EID': '1c0a6a2d-0976-4e16-ae7b-f34b0dbdfc19', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(233, 9999))},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '120624', 'EID': 'd57405c3-1e8b-406f-96f3-566d0b8ed5fd', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 0))},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '130624', 'EID': 'f8cb9ec4-9712-4514-a5e2-0ddcaac963e2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 9999))},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '140624', 'EID': '067dafe5-30e7-4f71-9e85-b10f1627df8a', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(0, 574))}, #ALF object not found
    {'Mouse_ID': 'SWC_NM_063', 'Date': '170624', 'EID': '093ab546-12bb-4c63-8d7c-f539cb882615', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '180624', 'EID': '15439251-fc4b-4b02-92cd-02398d7aa80a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '190624', 'EID': 'ef21ee63-faab-449b-a04d-9d042b84c241', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '200624', 'EID': '631c840d-8ce0-453f-829c-9ad7991d964b', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '210624', 'EID': '4caf8316-2847-4997-acc0-685ee99a0bf7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_063', 'Date': '240624', 'EID': '646e5870-ee31-414a-ad4b-4b55c2ad5e25', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'PL', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    ### double check some details here
    ### Virally targeted MOs
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-14', 'EID': 'babbd6b0-dbab-4598-87d4-00b4c723ad3e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(118, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-11', 'EID': '110aaffb-ab9e-4362-9f3b-7b1910a41d1a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, ### switched hemi multiple times
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-10', 'EID': '4a67a51b-dc8c-4216-afad-28f463078be4', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(113, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-09', 'EID': 'ba0ac3a9-7ab0-4d1c-be3a-ddf593fd0241', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(147, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-08', 'EID': 'dacbc9a8-3cf0-4c82-a67f-f1e6baee2aa3', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(98, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-07', 'EID': 'da601e9e-f2a5-4032-8b30-20f994e84487', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(197, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-04', 'EID': '7334eb59-36bf-42ec-93b5-0676005eb422', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-03', 'EID': '81368cca-beda-48f6-8c9b-a16bbe8c7ebf', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(62, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-02', 'EID': 'ab3ee693-82aa-40d4-b215-e0f284d07aaa', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(100, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-08-01', 'EID': '9d55cbc0-7f4c-4dcd-a3a8-525aeb39bca8', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(95, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-31', 'EID': 'af6163b6-1427-4d72-8c78-831d30fffe2f', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(66, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-28', 'EID': '15eb9851-7b17-432e-8c1b-c35798232ec8', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(90, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-27', 'EID': '8024753a-5726-472a-8cb7-3b5c534a35ad', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(110, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-26', 'EID': 'f50db341-bb52-4bb5-959a-4ae1679584cd', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(353, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-25', 'EID': 'e70717a2-406b-4e80-8115-5bd8ef849bc1', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(92, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-24', 'EID': 'b872338e-baf4-408e-a1a2-6cc11cb825b8', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(145, 655))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-21', 'EID': '45a4f3a9-7e87-4267-a586-b197278b9d94', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '20hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(191, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-20', 'EID': '13da8dfb-2b47-47f4-8dea-d979b8969fb9', 'Hemisphere': 'right', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(214, 9999))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-19', 'EID': '291a4e8f-5324-4a8f-83d3-9716f8689d41', 'Hemisphere': 'none', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-18', 'EID': '856843fe-3850-45c5-986d-1ffe9267cae0', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(323, 9999))}, #### switched hemispheres here, need to look into this
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-17', 'EID': '9ee13d3f-3721-4656-9521-3179222c0426', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(7, 454))}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-14', 'EID': 'cc27a197-7556-4479-9764-9083efff6fd2', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(123, 655))}, 
    # {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-14', 'EID': '543e44e1-cc37-4750-a507-998ea8bd5645', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-13', 'EID': 'f7f95217-287e-436b-9df4-9f6945b0e7ca', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_049', 'Date': '2023-07-12', 'EID': 'd4963693-4770-403c-bb6a-ab2c6a309259', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'MOs', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-12-06', 'EID': '151daab8-55c3-4055-a246-2cc0f806d816', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-12-05', 'EID': 'b2b22441-fead-4a99-a20c-00c652be98df', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-12-04', 'EID': '6abd16bd-d86c-4d63-9f45-8f729d8ceff8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.05, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-12-02', 'EID': 'b0ab5744-5d83-437d-a5bb-d65ebb43280e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-29', 'EID': '2dd4debf-f723-40aa-b24b-a138cd8e5d1e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-28', 'EID': 'cc509072-53cb-4e39-b53e-0b5800e0b41f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-27', 'EID': '5796b7b5-6ca4-4ba7-9f3d-027be7820421', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-26', 'EID': 'b898ef30-b35a-47ef-9ba0-3075fba807d8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-25', 'EID': '7f443058-a51a-41f8-a9c0-a04563ceb1a9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-22', 'EID': '71236058-2759-453d-8b3a-6a6664e7094c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-21', 'EID': '94b071cf-0c32-479d-8205-f42bd8a4bc6d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-20', 'EID': '54dcd11c-9137-447e-b0af-eafc8adf6758', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-19', 'EID': '96279cb3-3d4c-4ee3-bb71-5d57327a2608', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-18', 'EID': '9659d3fa-6a50-4817-a997-d59b2caf5a87', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-15', 'EID': '281bdee3-8c31-49e4-8a0b-891e0b3a735b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-14', 'EID': 'b5a251cb-5d10-48ff-a565-0b77ed1d306c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_088', 'Date': '2024-11-13', 'EID': '4f8c6970-65dc-4eb0-a114-4dc7b51c82ce', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-12-06', 'EID': '897c1ade-8ebb-4621-9c73-4b5ab204bdfc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-12-05', 'EID': 'f00a07ca-c5bb-4cb8-a5ca-af72504fa944', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-12-04', 'EID': 'bc467278-6c15-488c-8113-2c21f0201d09', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-12-02', 'EID': '77f65fe9-5650-41cc-983e-79497ec47d9b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-29', 'EID': '7a018614-71ac-4c59-b641-09457360953f', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-28', 'EID': 'ed55c4ec-20cd-42b9-8a41-efa0cfc28484', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-27', 'EID': '6f403baf-ebbd-4467-b8c8-53b7d24e5de8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-26', 'EID': '95a313a8-37f0-4520-bf75-0ec369d2f5ba', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-25', 'EID': '8ac06404-d0b2-41a2-a478-394cf9561dc7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-22', 'EID': '0f97d10d-1576-4873-9fe4-714f02fc491c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-21', 'EID': '38380394-c382-432e-8403-2354edf1c7fb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-20', 'EID': '5a2bcb68-a425-43ef-aab1-e8707c25a6b2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    ### session not extracted?
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-18', 'EID': 'bd8d53d9-c829-4124-8577-eb9bcb7263f6', 'Hemisphere': 'both', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-15', 'EID': 'd3a91403-7c69-4794-982c-8d4e6fe12ba4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-14', 'EID': '369d3a18-44de-42dd-abc4-de4a65dc1ac9', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_089', 'Date': '2024-11-13', 'EID': '5657ea05-3015-4f0c-955b-3fc8dbe96fd4', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-18', 'EID': 'ff4df649-1c27-4102-bbd0-7e13a9d674e7', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-17', 'EID': 'bcb9118d-7428-424c-808f-eb0914c687f4', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-14', 'EID': 'cf2b1b1c-f7bc-4c54-8845-2ef923f5b67d', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-13', 'EID': 'a480cc48-493f-434b-8196-98d22252fc27', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-12', 'EID': '0798878a-ad8d-4fa1-9dc0-5f31b880d850', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-11', 'EID': 'bef93e88-35dd-493d-86d0-48302a8a5953', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-10', 'EID': 'ee50646a-58fb-4f36-8add-6ed74657e5b4', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-07', 'EID': '9e6ba046-d48f-4913-a433-ecca9a1049fc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-02-06', 'EID': 'e2b73d55-9939-477e-9b1f-790737aae7f0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-31', 'EID': 'e0e640b9-5de7-4368-a829-e3d176b0c581', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-30', 'EID': '16bb8349-3adf-4303-917b-8f34c1a66ebc', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-29', 'EID': 'fb3cf5aa-edc8-44ee-9c6a-e62411773355', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-28', 'EID': 'e9022a1d-12d6-4650-87d3-c8ca6067811c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, #may not be a good reason to exclude this session
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-27', 'EID': '6bf1fd36-c5c8-4de2-8c25-b2de24135017', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-24', 'EID': '26000129-a069-4d2a-a127-2ede7b960f7e', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-23', 'EID': '0f27c025-06d3-4650-8cd3-32d70af4cbcb', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-22', 'EID': '275d5a4e-53eb-492b-b280-e488b0107964', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-21', 'EID': 'cfe03720-651d-4dfc-b0b5-48c2b10472b3', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-20', 'EID': 'd62d5bb6-2210-4300-9d38-c6e4bd23abdc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-17', 'EID': 'ff9ed98f-94bf-48bd-b5fc-927c92c3d44e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-15', 'EID': 'bb1a2f7a-f392-4208-993d-335f69dbb6d6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # ###
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-13', 'EID': 'af35bdd9-8039-437d-b4cb-289338b9af47', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-10', 'EID': '6c01ca19-ea75-4ff1-8aa1-20b690ff2db4', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-09', 'EID': '47a49a5a-f0b2-4b5c-94cb-9eb943e24a93', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-08', 'EID': 'c4e0c80c-c00f-47a2-9c96-56c2f39ddba1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont_c', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-07', 'EID': '16a4a16b-5b27-4fcd-aaa0-b482739c2d9e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.2, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    # ### session not extracted?
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-03', 'EID': '187eef62-5567-488a-b5cb-b1af1c9ec925', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-02', 'EID': '98bdaa1e-2090-411c-85d1-f0dfd42c1561', 'Hemisphere': 'none', 'P_Opto': 0, 'Stimulation_Params': 'none', 'Pulse_Params': 'none', 'Laser_V': 0, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2025-01-01', 'EID': 'e00d2e52-ec50-4f96-b97e-bff436c5d169', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-31', 'EID': '89e7ea34-0181-4ffb-ad8c-5a3adeeca918', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-30', 'EID': 'd7008fe3-bc23-4cb4-9bd9-b15727506dfc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-20', 'EID': 'bf0ce134-b9fd-45e1-aec0-505abfefdd49', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': list(range(6, 9999))}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-19', 'EID': 'e90552b8-a0d1-455e-92b4-d2dcc4e9d39d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-18', 'EID': '5d8a1a00-4906-42e3-a9a1-0f9743817002', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-17', 'EID': '3aa941b5-a28e-4621-917d-cd8791480130', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-16', 'EID': '24214686-b5b6-453b-9004-8f6e3e9d9882', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-13', 'EID': '85b45f72-99f4-487b-9ae7-c93bc4d1e32c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-12', 'EID': '6a7bec00-546b-4b78-afa8-7c73d0164653', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-11', 'EID': '3f56560a-16c1-484e-af4d-3caa9fd7aedd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_087', 'Date': '2024-12-10', 'EID': '75999961-3c0b-4c13-a055-36cb83ea8edc', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '220125', 'EID': 'a95342b6-34e0-4986-81c9-3da3b2d3d552', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '230125', 'EID': '5af8e109-6e6a-4584-ab63-8a9982bd0abf', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '240125', 'EID': 'ac98071b-58d3-47df-8738-d59e99dc6fb0', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '270125', 'EID': 'b2c60075-433c-407d-98c1-5c107985c43d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '280125', 'EID': 'cccf0a2f-9921-4c17-bb78-dd210cec5619', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '290125', 'EID': 'd996950a-a35d-4ae9-9594-f077e6be3853', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '300125', 'EID': 'e36935ea-dcfe-4fd6-95ba-405aa211e751', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.1, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  # changed from 0.1V -> 0.5V at trial 625
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '310125', 'EID': 'e3416b27-419c-46ae-a7d0-6eaf8ca12747', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '030225', 'EID': '063e79f0-8a34-4acc-98b8-8df644d24580', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '040225', 'EID': 'b7804bc4-cd95-4b7a-bc89-507b0d1fb290', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '050225', 'EID': '5061926d-b7ce-40b1-9f87-2b195e18ea1c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '060225', 'EID': '0e976843-e0da-4d81-bf4e-392d89495991', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '070225', 'EID': '68c88d54-3a66-41ff-9991-6ae6cd5efb8c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '100225', 'EID': 'da607c74-41f2-4874-b479-10e56ea9b7d8', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '110225', 'EID': '7266bfe3-ee65-45c7-b5b4-9d8a1c4778ae', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '120225', 'EID': 'dc566ee0-a204-49e0-87e1-39385caf6c17', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '130225', 'EID': '6aa8136d-5f7d-4480-bf32-4e8573fac438', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '140225', 'EID': '44804a50-2798-4487-9fd9-3bf486f8dc8d', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # # {'Mouse_ID': 'SWC_AY_006', 'Date': '170225', 'EID': 'f701d4e8-22a6-4437-857b-f81c3d9d6928', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '180225', 'EID': '025647c7-47f6-4ff4-94a9-d8448a44ceb2', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '190225', 'EID': 'd4c811e7-aaa4-40bd-b34f-cac0e9c6a6a6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '200225', 'EID': '800cafdd-b649-47f6-b5c5-e9ab48f20e7e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '210225', 'EID': 'a3a56690-f20b-4301-be9c-c872c92c3e10', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '240225', 'EID': '351e4866-8246-47c9-9e2c-4c3b155020d3', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '250225', 'EID': 'a6532b11-ec0b-4950-8a2c-d42988c94f3b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '260225', 'EID': '419e624e-2b0d-47ba-8dfc-1fe2eaecaa1c', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '270225', 'EID': '14aa23a1-43dc-4163-bd0d-b8af34660e68', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '280225', 'EID': '7fa53427-0011-4204-b2b6-a150f25c4fb1', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '030325', 'EID': 'fbf72af1-c777-403b-ad14-97bc220db751', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '040325', 'EID': 'a8fb5aa3-bf06-40a2-b1ea-5773aa07e374', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '050325', 'EID': '3499d182-132e-4c03-a853-c6e5d1dc12cf', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '060325', 'EID': 'adb6ab8c-c9a5-4e7c-99ee-9c456f4d1b04', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '070325', 'EID': 'b8b0c1f2-c012-42a1-8482-1744496df656', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '110325', 'EID': '17ad0ba8-1ae0-4c5b-984d-b6ad13725d8b', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '120325', 'EID': 'fbf17127-bcd2-4699-897a-80d917093d31', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '130325', 'EID': '19becee2-8876-4577-9237-f6604749df19', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '140325', 'EID': 'ecb6537f-1ac6-4d21-813d-ecb1242031bc', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_006', 'Date': '2025-03-17', 'EID': '9db5ac4e-8746-492e-be70-ed884d1469d7', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 

    # {'Mouse_ID': 'SWC_AY_012', 'Date': '070225', 'EID': '486a6256-4d4f-42f1-af66-4d3362471145', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(185,9999))},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '100225', 'EID': '7e822546-8829-45a2-ba04-4fa0cf2d2121', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(158,9999))},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '210225', 'EID': '162a3579-7fb6-4e13-8b6f-a0645040dc9a', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(165,9999))},  # OR P_Opto = 0.1 ?
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '240225', 'EID': '01e81b6f-0a4e-4aa5-ae1e-329e4c5e000e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '250225', 'EID': '35624143-0761-46e7-8711-56ba6559a5cd', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '260225', 'EID': 'c548b258-fc24-4d8c-96d2-b3239f70e388', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '270225', 'EID': 'a8519c6f-a1cc-4208-a2ab-4e633ebf7bf9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '280225', 'EID': '3d886842-529b-42cd-9147-e3eaddbf9077', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '030325', 'EID': '6dec6739-2ea7-4a12-aa96-dff93b41d917', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '040325', 'EID': '71b141f7-c4ca-4e17-b77f-5c273a94ff53', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '050325', 'EID': 'd6382c68-013f-4714-b784-8a72a1f207f2', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '060325', 'EID': '29413835-6aa1-488d-be91-463a95685e1f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '070325', 'EID': '2c09f398-caab-4f0d-9ab9-aae0a18081c1', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '110325', 'EID': 'f3485eae-dc02-4e30-ae26-7e0289e9ee5a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '120325', 'EID': '8b407f19-062e-44d1-b9d1-17104a053530', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  
    # {'Mouse_ID': 'SWC_AY_012', 'Date': '130325', 'EID': '012cda53-9aa2-4c51-87a4-ff338702af4a', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': 'cont', 'Laser_V': 0.5, 'Opsin': 'GtACR2', 'Brain_Region': 'SNr', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'},  

    # {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-24', 'EID': '336d839b-8ebb-4321-ab3b-69a29f5dac02', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-21', 'EID': '175350fa-6c2c-468e-9e87-ba4ba916810c', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-20', 'EID': 'f4fb120a-dbad-48ff-a9e3-680944aaa79f', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-19', 'EID': '1fb664c8-dcab-4ba8-8991-45d933c31397', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-18', 'EID': 'f11bbc0e-d84b-44cd-b926-bc9643f6b4fa', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-17', 'EID': 'faa36bc9-3f24-4aad-b770-867d3bc04db9', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-14', 'EID': '9cd4ff60-be51-4aff-912d-67a11dd0fc75', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-13', 'EID': 'fb17bd2f-3300-4c36-8071-f5b573b6b627', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-12', 'EID': 'f0147d1f-c8e3-4916-a1c5-5b369dc437b9', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-11', 'EID': '967e1337-9ef2-4334-a36a-f45edbe3e544', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-10', 'EID': '1167154b-86d2-4e56-b5d9-a3504ff87889', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-07', 'EID': 'b049230e-d30b-4458-bd89-dfc114f15869', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-06', 'EID': 'b6e5583d-b69d-4658-b665-9b2a038a77c8', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-05', 'EID': 'a5a82e1a-e012-4a86-a240-3513d9c4cfb6', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-04', 'EID': 'd5d8c0a2-18be-4531-aef4-88651b255d04', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-03-03', 'EID': 'd58b338d-6315-4bc1-b3d3-7995908fa4ae', 'Hemisphere': 'both', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.5, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-28', 'EID': '79f59f2b-3dcc-453b-a841-813760c51c1b', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-27', 'EID': '15194e66-2bb2-4833-9c5b-9f9f2ba8d60d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-26', 'EID': '649e2eec-c69c-4ef4-919e-45cd4ce5bc47', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-25', 'EID': 'a0dce8e3-bbf8-4230-a909-89e30e7a5e1f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-24', 'EID': 'bf81a0a2-8b27-4fc7-9d6f-684063d8c75e', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-21', 'EID': 'e7dee8c0-4fd4-4c36-bca8-48eb22ddd58d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-20', 'EID': 'ebfd7f0d-92f7-4a6d-800e-a2586c8d8237', 'Hemisphere': 'left', 'P_Opto': 0.1, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-19', 'EID': '46e020f3-0246-41cb-9fe3-b33caa29491f', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_NM_083', 'Date': '2025-02-18', 'EID': '052dd6e7-ac9e-450f-8237-314a9e1df35a', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'ChR2', 'Brain_Region': 'VLS', 'Genetic_Line': 'D2-Cre', 'Trials_Range': 'ALL'},

    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-28', 'EID': 'f9e60398-abbb-4802-9d27-bff7ae251b37', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-27', 'EID': '62a546f6-d24f-4ede-8653-b7601962a408', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-23', 'EID': '61566182-9a1c-4fcd-ac4c-c0310424d317', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-22', 'EID': '04c4d54e-6de1-4eab-99cc-d8c283953084', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    # {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-21', 'EID': '6d261904-c5f8-4f7e-a7da-04d4da652a5d', 'Hemisphere': 'nan', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-20', 'EID': 'a1bab615-01e3-43a2-9a44-142e22c2db98', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-19', 'EID': 'a9fef338-5aba-47bf-b42e-7e8e4de6bf75', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-16', 'EID': '580b514f-b902-48aa-9457-864c043d5505', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-15', 'EID': '14618af6-2fb8-42fd-8eff-ffe88a17e7bd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-14', 'EID': '3ffc5016-369b-451c-bc06-4111f24cf4a6', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'SORE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-13', 'EID': 'c5e8ffd4-467f-42ac-984b-aa7e7e89b2bd', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-12', 'EID': '746c32af-43dd-45ab-8232-864be8ea632d', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-09', 'EID': '3791ec3d-fdfe-4a85-910e-28d73b79a919', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-08', 'EID': '7af40267-5d37-442e-8b72-83fe2785e6ad', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-07', 'EID': 'a84553b8-1825-4398-9eb0-8efe3f909154', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': 'ALL'}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-06', 'EID': '2b2a0dca-37ed-4d3a-929a-330ac61535a1', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(309, 9999))}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-02', 'EID': '8931e8b3-c9a7-40d9-bcf7-8c24dced22ad', 'Hemisphere': 'right', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 1, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(309, 9999))}, 
    {'Mouse_ID': 'SWC_AY_016', 'Date': '2025-05-01', 'EID': 'f959d0b5-06aa-4552-b7c2-7e56175ca057', 'Hemisphere': 'left', 'P_Opto': 0.2, 'Stimulation_Params': 'QPRE', 'Pulse_Params': '50hz', 'Laser_V': 0.3, 'Opsin': 'GtACR2', 'Brain_Region': 'ZI', 'Genetic_Line': 'VGAT-Cre', 'Trials_Range': list(range(78, 9999))}
]


# ########### STN excitation (QP)
# ## RIGHT
# eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35'] #25 19/10/22, 21/10/22

# trials_ranges = [list(range(350,402)), list(range(251,372))]

# ### LEFT
# eids = ['7bd7cbf6-e3ab-4222-ade8-458a5afb30f9'] #25 20/10/22

# trials_ranges = [list(range(107,190))]

# ########## STN inhibition
# ## ALL
# eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35', #25 19/10/22, 21/10/22
#         '7bd7cbf6-e3ab-4222-ade8-458a5afb30f9','002e60e1-e646-4f69-b6e3-d3b00f082797', #25 20/10/22, 27/10 R
#         '0068b011-c60f-491f-a29c-245877cd1bc1','abf38955-b5d4-4319-921a-f0658188ad57', #25 26/10/22 L, 25/10/22 R
#         '67688ca2-a5a3-4cea-8131-8da5b920dcff','b6f80439-98e6-41cf-a7e8-7216b1d93feb', #25 28/10/22 L, 31/10/22 R
#         '45b7a288-8bf7-411c-b1ba-178b58fc7f6f','9606af89-12f6-4a57-8cd9-24f733beae8a', #25 2/11/22 R, 3/11/22 LR
#         '3dd68334-84cc-402d-a053-45bd352c14fc','4ac3caaf-1b27-4c89-9020-560b7f6f6df4', #25 7/11, 8/11
#         'c82ceab1-ad8f-42aa-bb2d-c9594315d2cd','47093eb5-2516-4e6f-a66e-92275c52659b', #24 18/1, 27/1
#         '3ca6c201-91f2-4ba9-8b8a-012446bdf7d2','d2f085c3-0a84-48c6-88fa-e6b25bd89938', #24 R 10/2 (excellent), L 9/2 (ok)
#         '81e58c8f-bfbd-4c54-b7ee-56d1d37767cc','b64467f6-0fb9-4d77-8c97-eacb3a15dffe', #24 B 8/2 (good), R 7/2 (borderline)
#         '1dcab41c-9ec6-4a1c-bd4c-67721db91df6', #24 L 14/2 (good)
#         '79468bd8-6fa2-48e4-8151-88951b33a8e0','baf2b96e-c587-49cf-acf7-c2ffb1c332a6', #26 16/1, 18/1
#         '91857de2-766f-43e2-a3cc-ace233485ebd','6b4a1004-9508-4ef4-b7a7-7cd10a676948', #26 20/1, 23/1
#         # '5654a819-d54a-4ef0-ac2d-247624ab4f50' #26 24/1 (below threshold)
#         '455f55c1-81ef-4541-8894-cf6c713a3a82','7aa67b01-67b8-44a2-bf23-2e58152fb8d3', #26 10/2 L, 6/2 R
#         'ce6be632-7986-4e05-b2c3-231d459d4dc4','cab9a767-05b4-4033-b074-225db0d37221'] #26 3/2, 2/2

# trials_ranges = [list(range(269,333)), list(range(131,251)) + list(range(372,497)), #25 19/10/22, 21/10/22
#                  list(range(191,555)), list(range(102,939)), #25 20/10/22, 27/10/22
#                  list(range(146,790)), list(range(188,236)) + list(range(413,597)), #25 26/10/22 L, 25/10/22 R
#                  list(range(150,618)), list(range(100,461)),#25 28/10/22 L, 31/10/22 R
#                  list(range(97,816)), list(range(162,791)), #25 2/11/22 R, 3/11/22 LR
#                  list(range(325,623)), list(range(137, 746)),#25 7/11
#                  list(range(90,409)), list(range(182, 470)), #24 18/1, 27/1
#                  list(range(90, 932)), list(range(90, 897)), #24 R 10/2 (excellent), L 9/2 (ok)
#                  list(range(90, 709)), list(range(90, 586)),#24 B 8/2 (good), R 7/2 (borderline)
#                  list(range(90, 571)), #24 L 14/2 (good)
#                  list(range(90,300)), list(range(90,400)), #26 16/1
#                  list(range(90,450)), list(range(173,308)), #26 20/1, 23/1
#                 #  list(range(90,256)) #26 24/1 (below threshold)
#                  list(range(90,400)), list(range(90,281)), #26 10/2 L, 6/2 R
#                  list(range(90,470)), list(range(90,528))] #26 3/2, 2/2

# ##25
# eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35', #25 19/10/22, 21/10/22
#         '7bd7cbf6-e3ab-4222-ade8-458a5afb30f9','002e60e1-e646-4f69-b6e3-d3b00f082797', #25 20/10/22, 27/10 R
#         '0068b011-c60f-491f-a29c-245877cd1bc1','abf38955-b5d4-4319-921a-f0658188ad57', #25 26/10/22 L, 25/10/22 R
#         '67688ca2-a5a3-4cea-8131-8da5b920dcff','b6f80439-98e6-41cf-a7e8-7216b1d93feb', #25 28/10/22 L, 31/10/22 R
#         '45b7a288-8bf7-411c-b1ba-178b58fc7f6f','9606af89-12f6-4a57-8cd9-24f733beae8a', #25 2/11/22 R, 3/11/22 LR
#         '3dd68334-84cc-402d-a053-45bd352c14fc','4ac3caaf-1b27-4c89-9020-560b7f6f6df4'] #25 7/11, 8/11
# trials_ranges = [list(range(269,333)), list(range(131,251)) + list(range(372,497)), #25 19/10/22, 21/10/22
#                  list(range(191,555)), list(range(102,939)), #25 20/10/22, 27/10/22
#                  list(range(146,790)), list(range(188,236)) + list(range(413,597)), #25 26/10/22 L, 25/10/22 R
#                  list(range(150,618)), list(range(100,461)),#25 28/10/22 L, 31/10/22 R
#                  list(range(97,816)), list(range(162,791)), #25 2/11/22 R, 3/11/22 LR
#                  list(range(325,623)), list(range(137, 746))] #25 7/11

# ##26
# eids = ['79468bd8-6fa2-48e4-8151-88951b33a8e0','baf2b96e-c587-49cf-acf7-c2ffb1c332a6', #26 16/1 R, 18/1 L
#         '91857de2-766f-43e2-a3cc-ace233485ebd','6b4a1004-9508-4ef4-b7a7-7cd10a676948', #26 20/1 B, 23/1 L
#         'cab9a767-05b4-4033-b074-225db0d37221','ce6be632-7986-4e05-b2c3-231d459d4dc4', #26 2/2 L, 3/2 L
#         '7aa67b01-67b8-44a2-bf23-2e58152fb8d3'] #26 6/2 R no baseline bias
#         # '5654a819-d54a-4ef0-ac2d-247624ab4f50','67a7b96c-c3d1-440f-9023-0ad50dfae94b', #26 24/1 L, 12/1 R (both below threshold)
#         # '76862a7b-f07e-47e3-b8ea-dc4588109cef','eacd7f97-f676-4d95-af31-e61b3182cfcf'] #26 17/1 L, 8/2 B (both below threshold)
# trials_ranges = [list(range(90,300)), list(range(90,400)), #26 16/1
#                  list(range(90,450)), list(range(173,308)), #26 20/1, 23/1
#                  list(range(90,528)), list(range(90,470)), #26 2/2 L, 3/2 L
#                  list(range(90,180)) + list(range(181,281))] #26 6/2 R no baseline bias
#                 #  list(range(90,256)), list(range(90,822)), #26 24/1 (below threshold)
#                 #  list(range(90,351)), list(range(90,538))] #26 17/1 (way below threshold)

# ###24
# eids = [#'1ddfaa39-f15b-4eda-9c70-c6d4f874fdb6','bca63bed-244c-4cb6-b173-26661d02e901', #24 L* 16/12 (below threshold), #24 R 19/1 (bad)
#         'c82ceab1-ad8f-42aa-bb2d-c9594315d2cd','47093eb5-2516-4e6f-a66e-92275c52659b', #24 L* 18/1, R* 27/1
#         # 'f62bbff2-a1c6-4646-9306-454f1c5b07a9',#,'7504026d-a0f8-433d-bd4f-f1d35e1cc4e2'] #24 R 20/1 (bad), B 24/1 (below threshold)
#         # '4ab45924-65a7-4178-8723-ab457c6ee242', #24 R 3/2 (bias flipped in control)
#         '3ca6c201-91f2-4ba9-8b8a-012446bdf7d2','d2f085c3-0a84-48c6-88fa-e6b25bd89938', #24 R 10/2 (excellent), L 9/2 (ok)
#         '81e58c8f-bfbd-4c54-b7ee-56d1d37767cc','b64467f6-0fb9-4d77-8c97-eacb3a15dffe',#24 B 8/2 (good), R 7/2 (borderline)
#         '521827e5-e064-4df7-af21-391e7689102e','b754992d-ac3a-477f-a4d9-421e10f34681',#24 L 6/2 (borderline), L* 2/2 (few trials, poor behavior at end)
#         '607afbbc-5fd9-4dae-aaa5-3edd187604f3',#24 R 1/2 (borderline)
#         '2f95753b-06cf-4860-b3a7-82b4d7a9fd45','75615687-3cca-4728-841f-10874bfe78be']#24 L* 10/1 (borderline), R* 11/1 (borderline)
# trials_ranges = [#list(range(90,854)),list(range(90,449)), #24 16/12 (below threshold), #24 19/1 (bad)
#                  list(range(90,409)),list(range(182, 470)), #24 18/1, 27/1
#                 #  list(range(90, 350)),#,list(range(90, 800))] #24 20/1 (bad), 24/1 (below threshold)
#                 #  list(range(90, 377)),#24 R 3/2 (bias flipped in control)
#                  list(range(90, 932)),list(range(90, 897)), #24 R 10/2 (excellent), L 9/2 (ok)
#                  list(range(90, 709)),list(range(90, 586)),#24 B 8/2 (good), R 7/2 (borderline)
#                  list(range(90, 400)),list(range(100, 300)),#24 L 6/2 (borderline), L* 2/2 (few trials, poor behavior at end)
#                  list(range(90, 910)),#24 R 1/2 (borderline)
#                  list(range(90,596)),list(range(90,841))]#24 L* 10/1 (borderline), R* 11/1 (borderline)

# # ############ STN excitation
# ## L Hemisphere
# eids = ['c0892faa-519e-430f-9b40-992b09fd618a',#,'e8db73ec-eff4-4704-a81b-ecbd00c5daf0'] #25 1/11/22 L, 28/10/22 L
#         'cb8f7026-175b-4386-97ae-46858a721197','84734bec-d898-4f50-b659-b4a7b7686fe8', #24 12/1/23, 13/2
#         '3475b385-19af-4be2-a667-4cd9a4ba7527','7791c224-b38d-4a1f-a133-beb043ee1301'] #26 25/1, 13/2

# trials_ranges = [list(range(124,726)),#, list(range(0,204))] #25 1/11/22 L, 28/10/22 L
#                  list(range(418,898)),list(range(90,555)), #24 12/1/23, 13/2
#                  list(range(90, 406)),list(range(90, 367))] #26 25/1

# ## R Hemisphere
# eids = ['c4f246b4-454c-4d42-9e4a-daf2c92b7787', 'bb590645-fd17-4025-84e5-e65d3ef948ea', #25 31/10/22, #25 4/11/22
#         'cb8f7026-175b-4386-97ae-46858a721197', #24 12/1/23
#         '583bf8b4-c500-494e-be90-6548bf26173a', 'f4d0076a-d9ef-4952-92ec-0ec92936fda1', #26 26/1/23 (slightly below threshold), 27/1/23
#         'b6de331a-495a-42b3-b029-ee743a99ac10'] #26 14/2

# trials_ranges = [list(range(0,215)),list(range(50,399)), #25 31/10/22
#                  list(range(90,418)), #24 12/1/23
#                  list(range(90, 364)), list(range(90, 488)), #26 26/1/23 (slightly below threshold)
#                  list(range(90, 397))]

# ## All stim sessions

# eids = ['c0892faa-519e-430f-9b40-992b09fd618a','c4f246b4-454c-4d42-9e4a-daf2c92b7787', 'bb590645-fd17-4025-84e5-e65d3ef948ea',
#         '3475b385-19af-4be2-a667-4cd9a4ba7527','cb8f7026-175b-4386-97ae-46858a721197',
#         '583bf8b4-c500-494e-be90-6548bf26173a', 'f4d0076a-d9ef-4952-92ec-0ec92936fda1']
#         #'784af2de-8082-4117-8149-aa967558b4a3' #26 1/2 (QP to reward/error)

# trials_ranges = [list(range(124,726)),list(range(0,215)),list(range(50,399)),
#                  list(range(90,406)),list(range(90,898)),
#                  list(range(90, 364)), list(range(90, 488))]
#                  #list(range(90, 543))

# #######################################
# ################ ORBvl ################
# ####### 40

# # *ADAL may be broken...

# ### L
# eids = ['f7ead6ad-f280-4e5d-b55f-9ae1e228616e', #40 3/5*
#         'bee5a4ce-334a-4c0d-afaf-df409ab9fe5f','e312f463-f684-45cd-940b-ec7a093134f9'] #40 24/4 (low bias all trials), 20/4 (low bias R trials)
# trials_ranges = [list(range(90, 1018)), #40 3/5*
#                  list(range(90, 805)),list(range(90, 1418))] #40 24/4 (low bias all trials), 20/4 (low bias R trials)

# ## R
# eids = ['977f085d-32a3-4f24-ac0b-dadce0fdf899','54196e48-a045-427e-8239-b68a196a857b', #40 19/4, 25/4
#         # 'cffe2f00-e990-4f67-894e-4397561d5ca3', #40 2/5* (below threshold perf)
#         '793529c3-c0e1-4243-81f9-9155b68b8e73'] #40 5/5*
# trials_ranges = [list(range(293, 1253)),list(range(90, 929)), #40 19/4, 25/4
#                 #  list(range(90, 797)), #40 2/5* (below threshold perf)
#                  list(range(90, 556))] #40 5/5*
# ### little effect. maybe reduction in R bias?

# ## bilateral
# eids = ['df8929c5-b954-41b7-991d-8ccccde7af3f','7ba551e4-010b-46e3-b5da-47e6ea9c6f6b', #40 21/4, 26/4 (no effect?)
#         #'1c669152-2447-4efe-add9-f5dc59c126bd', #40 10/5 (stimOn to exit state; seizure around 280),
#         '85e73183-649a-46b5-a7da-34a1a783b9d0', #28/4 (no bias in all trials)
#         '24ab6988-61cd-449c-a123-663b0322387a'] #40 27/4 (no bias in all trials)
#         # '048e5b8d-6176-41b3-8c74-ed6690f2626f' #40 9/5 below threshold; switch from 50hz to continuous
# trials_ranges = [list(range(90, 818)),list(range(90, 624)), #40 21/4, 26/4 (no effect?)
#                 #  list(range(90, 352)),  #40 10/5 (stimOn to exit state; seizure around 280),
#                  list(range(90, 969)), #40 28/4
#                  list(range(90, 969))] #40 27/4
#                 #  list(range(330, 750)) #40 9/5 below threshold; switch from 50hz to continuous

# ## NO stim
# eids = ['776f1bd6-fb02-47c3-8614-a94772ebed73','28ccaeaf-b459-473e-b679-8c82ce4d6e2d'] #40 12/5, 11/5
# trials_ranges = [list(range(90, 550)),list(range(90, 747))] #40 12/5, 11/5


# # # On continuously (ie, 100% trials)
# # Bilateral 20hz
# eids_stim = ['c9d1c66b-4dfb-4200-8065-49d4b20dfb90', #40 30/5
#         '26e73d77-98e4-491a-8331-c5d00d88ac5c', #40 31/5
#         'd77556ee-5343-48ec-a41b-3e9868694dca', #40 26/5
#         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
#         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
#         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
#         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
#         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
#         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
#         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
#         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
#         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
#         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
#         'f3816e25-61b7-4389-a67c-6a58a0608c90' #40 2/6
# ]
# trials_ranges_stim = [list(range(319, 738)), #40 30/5
#                  list(range(100, 408)), #40 31/5
#                  list(range(300, 641)), #40 26/5
#                  list(range(215, 320)), #40 25/5
#                  list(range(485, 634)), #40 25/5
#                  list(range(397, 540)), #40 23/5
#                  list(range(637, 765)), #40 23/5
#                  list(range(220, 281)), #40 22/5
#                  list(range(360, 461)), #40 22/5
#                  list(range(560, 661)), #40 22/5
#                  list(range(860, 908)), #40 22/5
#                  list(range(225, 308)), #40 19/5
#                  list(range(333, 499)), #40 19/5
#                  list(range(363, 709)) #40 2/6
# ]

# ## Control 
# eids_ctrl = ['c9d1c66b-4dfb-4200-8065-49d4b20dfb90', #40 30/5
#         'd77556ee-5343-48ec-a41b-3e9868694dca', #40 26/5
#         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
#         '48517348-c8cc-465c-9c66-5b7de8a653cb', #40 24/5 (only 297 trials)
#         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
#         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
#         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
#         'f3816e25-61b7-4389-a67c-6a58a0608c90', #40 2/6
#         'd18e332a-bc0f-4ad1-b29c-cd26f79fdacd' #40 1/6 (no stim)
# ]
# trials_ranges_ctrl = [list(range(90, 319)), #40 30/5
#                  list(range(90, 300)), #40 26/5
#                  list(range(90, 215)),# + list(range(320, 485)), #40 25/5
#                  list(range(90, 297)), #40 24/5 (only 297 trials)
#                  list(range(90, 397)),# + list(range(540, 637)) + list(range(765, 931)), #40 23/5
#                  list(range(90, 220)),# + list(range(281, 360)) + list(range(461, 560)) + list(range(661, 860)), #40 22/5
#                  list(range(90, 225)), #40 19/5
#                  list(range(90, 363)), #40 2/6
#                  list(range(90, 426)) #40 2/6
# ]

# #######################################
# ################ PL ###################
# ####### 41

# ### Bilateral
# eids = [#'373a293b-13f7-4c96-9dfb-f7e1fabacc2a', #41, 22/6, still has bias...
#         # '07cbf3ee-2d6b-4ed7-92a1-2e7715bdad60', #41 28/6 (no effect)
#         '50d1b073-b247-4da2-99c1-46ae401c50b9', #41 29/6
#         'dcb26eac-7329-4f06-8d6a-ee20cc43abb2', #41 30/6 (50hz)
#         '35359ed9-98f2-4b13-a4c6-2d252f127bf4', #41 3/7 (50hz)
#         '2fc8c951-e2f6-4541-a2bc-dd57d32bd8cf', #41 4/7 (50hz)
#         '7881b2ce-21ef-4c9c-b466-425f9188e41a', #41 5/7 (0hz)
#         '516116c0-6686-4f65-bfaf-d27b5512ac22', #41, 13/7 (50hz; borderline perf., might be better if cutoff later trials)
#         '20a6ebda-af15-47e9-a6aa-6eaec63eebed', #41, 14/7 (50hz)
#         '61ce5f3b-715e-4c93-a52e-cb087c3927f1', #41, 17/7 (50hz)
#         'aacaac80-4af2-4e70-a672-5f0b9ac680b4', #41, 21/7 (50hz)
#         # '1e3e8e66-761c-41fa-b919-020c0ab3f6f9', #41, 27/7 (50hz) slightly below threshold perf.
#         '3391096e-3d56-4cf0-8034-fb045003c92a', #41 31/7 (50hz) bias still there
#         'e41d31fa-47be-4d18-a28a-4306be9a5095', #41 1/8 (50hz) bias still there
# ]

# trials_ranges = [#list(range(90, 804)), #41 22/6
#                 #  list(range(90, 711)), #41 28/6 (no effect)
#                  list(range(90, 936)), #41 29/6
#                  list(range(219, 773)), #41 30/6 (50hz)
#                  list(range(90, 750)), #41 3/7 (50hz)
#                  list(range(90, 806)), #41 4/7 (50hz)
#                  list(range(90, 1079)), #41 5/7 (0hz)
#                  list(range(90, 638)), #41, 13/7 (50hz; borderline perf., might be better if cutoff later trials)
#                  list(range(90, 536)), #41, 14/7 (50hz)
#                  list(range(90, 880)), #41, 17/7 (50hz)
#                  list(range(90, 630)), #41, 21/7 (50hz)
#                 #  list(range(131, 826)), #41, 27/7 (50hz)
#                  list(range(90, 850)), #41 31/7
#                  list(range(205, 705)), #41 1/8
# ]

# ##### unilateral Left
# eids = ['d4a1314f-bea1-4403-8117-00b56246f9a6', #41, 19/7, 50hz L
#         # '425b02e4-37be-4df5-9445-f70502018bdd', #41, 24/7 (50hz) ALF FILE NOT FOUND
#         '659a83ac-a963-44d6-a59a-d913c995de73', #41, 26/7, 50hz L
#         'ecd81518-3187-4044-8fb8-3da4f4efd806', #41, 28/7, 50hz L
# ]

# trials_ranges = [list(range(90, 824)), #41, 19/7, 50hz L
#                 #  list(range(90, 'end')), #41, 24/7 (50hz) ALF FILE NOT FOUND
#                  list(range(90, 655)), #41, 26/7, 50hz L
#                  list(range(90, 902)), #41, 28/7, 50hz L
# ]

# ##### unilateral Right
# eids = ['3fb3df4c-245c-4503-af0b-d432af3f7540', #41, 18/7, 50hz R
#         '7732ba5c-0cce-4274-90e8-30a35593ee13', #41, 20/7, 50hz R
#         'd19b00d5-559e-4e1d-b355-7252ae765e4a', #41, 25/7, 50hz R
#         'e919ed8b-415b-4aab-a30e-d1f9261b6e48', #41, 2/8, 50hz R
#         # 'd4a1314f-bea1-4403-8117-00b56246f9a6', #41, 19/7, 50hz L
#         # '659a83ac-a963-44d6-a59a-d913c995de73', #41, 26/7, 50hz L
#         # 'ecd81518-3187-4044-8fb8-3da4f4efd806', #41, 28/7, 50hz L
# ]

# trials_ranges = [list(range(90, 658)), #41, 18/7, 50hz R
#                  list(range(90, 761)), #41, 20/7, 50hz R
#                  list(range(90, 499)), #41, 25/7, 50hz R
#                  list(range(90, 790)), #41, 2/8, 50hz R
#                 #  list(range(90, 824)), #41, 19/7, 50hz L
#                 #  list(range(90, 655)), #41, 26/7, 50hz L
#                 #  list(range(90, 902)), #41, 28/7, 50hz L
# ]

# ######## 50
# ### Bilateral
# eids = ['3c079baa-b887-4c93-a63f-a3685119626b', #08/11
#         'af93d8a2-4f50-4763-a925-68452bcf93c4', #09/11
#         '8e88c5cd-3549-4731-96d8-94ccd553e67a', #10/11 - borderline ~80% on R side, but effect very strong
#         '3e83d3f0-9b76-4c06-a62e-e27121c34c30', #13/11 - no effect?
#         'df587223-66de-4948-a4b1-230b118eb510', #14/11 - no effect? trials+1 affected!
#         'cf906e2b-0aa8-4398-9c51-b69287c07063', #16/11 - no effect
#         'c2125631-6ebd-4425-9ac0-a71586332af4', #17/11 - no effect
#         'c2125631-6ebd-4425-9ac0-a71586332af4', #20/11 - no effect?
#         # 'f0bf6511-f3c3-4575-b1f0-ffff9d88f4db', #21/11 - Right hemi
#         # '8d71dfd7-fab1-4b7a-88d1-a2b690b5ece0', #22/11 - Left hemi
#         'c3bd608e-b9dc-43ab-b8a3-92b7f9f5f59a', #24/11 - no effect
# ]

# trials_ranges = [list(range(90, 1131)), #08/11
#                  list(range(90, 812)), #09/11
#                  list(range(90, 970)), #10/11
#                  list(range(90, 599)), #13/11
#                  list(range(100, 698)), #14/11
#                  list(range(125, 948)), #16/11
#                  list(range(160, 763)), #17/11
#                  list(range(90, 658)), #20/11
#                 #  list(range(90, 721)), #21/11
#                 #  list(range(90, 1053)), #22/11
#                  list(range(90, 704)), #24/11
# ]

# #######################################
# ################ M2 ###################
# ####### 49


# ## Bilateral
# eids = ['f7f95217-287e-436b-9df4-9f6945b0e7ca', #49 13/7 (slightly below threshold performance); bias appears gone, but also gone in nonstim trials. Lower QP, higher RT
#         # 'cc27a197-7556-4479-9764-9083efff6fd2', #49 14/7 (well-below threshold perf.; almost always turns left on stim trials; decreased RT??)
#         # 'f328df1d-d736-455c-a09b-a55869cb8723', #49 17/7 (slightly below threshold performance); Lower QP, higher RT; poor performance, very right-biased (left-shifted on stim trials)
#         ### #49 18/7 something weird going on here; only 515 trials, which doesn't make sense?
#         '13da8dfb-2b47-47f4-8dea-d979b8969fb9', #49 20/7 R 50hz
#         # '45a4f3a9-7e87-4267-a586-b197278b9d94', #49 21/7 L 50hz slightly below threshold performance
#         'b872338e-baf4-408e-a1a2-6cc11cb825b8', #49 24/7 bilateral 50hz (left shifted perf, but still within threshold)
#         'e70717a2-406b-4e80-8115-5bd8ef849bc1', #49 25/7 bilateral 50hz bias gone!
#         # 'f50db341-bb52-4bb5-959a-4ae1679584cd', #49 26/7 bilateral (performance slightly below threshold)
#         '8024753a-5726-472a-8cb7-3b5c534a35ad', #49 27/7 bilateral 50hz (left shifted perf, but still within threshold)
#         '15eb9851-7b17-432e-8c1b-c35798232ec8', #49, 28/7, bilateral 50hz
#         # 'af6163b6-1427-4d72-8c78-831d30fffe2f', #49, 31/7, bilateral 50hz, below threshold; mouse turns more left on stim trials
#         '9d55cbc0-7f4c-4dcd-a3a8-525aeb39bca8', #49 01/8 bilateral 50hz
#         '4a67a51b-dc8c-4216-afad-28f463078be4', #49, 10/8, bilateral
# ]

# trials_ranges = [list(range(227, 656)), #49 13/7 (slightly below threshold performance)
#                 #  list(range(123, 655)), #49 14/7 (well-below threshold perf.; almost always turns left on stim trials; decreased RT??)
#                 #  list(range(90, 350)), #49 17/7 (slightly below threshold performance)
#                  ###
#                  list(range(214, 808)), #49 20/7 R 50hz
#                 #  list(range(191, 942)), #49 21/7 L 50hz slightly below threshold performance
#                  list(range(145, 737)), #49 24/7 bilateral
#                  list(range(92, 788)), #49 25/7 bilateral
#                 #  list(range(353, 815)), #49 26/7 bilateral
#                  list(range(110, 898)), #49 27/7 bilateral
#                  list(range(90, 668)), #49 28/7 bilateral
#                 #  list(range(90, 742)), #49, 31/7 bilateral
#                  list(range(95, 785)), #49 01/8 bilateral 50hz
#                  list(range(113, 660)), #49, 10/8, bilateral
# ]


# ## Unilateral
# eids = ['13da8dfb-2b47-47f4-8dea-d979b8969fb9', #49 20/7 R 50hz
#         '45a4f3a9-7e87-4267-a586-b197278b9d94', #49 21/7 L 50hz slightly below threshold performance
#         '81368cca-beda-48f6-8c9b-a16bbe8c7ebf', #49 3/8 L 20hz borderline perf; little bias at baseline
# ]

# trials_ranges = [list(range(214, 808)), #49 20/7 R 50hz
#                  list(range(191, 942)), #49 21/7 L 50hz slightly below threshold performance
#                  list(range(90, 600)), #49 3/8 L
# ]
# #unilateral StimOn
# # '110aaffb-ab9e-4362-9f3b-7b1910a41d1a'
# # list(range(186, 361)) + list(range(597, 803)) #right

# # ################### 51
# eids = [#'26795a4a-c0dd-4423-87d2-6bfc6b03b528', #25/9
#         'd23014c6-ea5a-4cc9-98bc-70916879ce7f', #26/9
#         'a014ef1e-7710-40ac-afd4-0402f1e12a7c', #27/9 (10%)
#         '3df2cc80-cdfa-47d0-bd36-863174255547', #2/10
#         # '7b9b5248-4239-4e4b-bdf5-baa56c59c69d', #3/10 only 300 trials, perf. borderline
#         'a1d962cc-4669-470b-af40-509a0d411268', #5/10
#         '7f560157-d9d8-4ccd-94fb-5c3b55dad328', #6/10
#         '83b50d6a-c88e-4454-b250-233a1d6a11e2', #10/10 very little baseline bias?
#         '946686f5-b9aa-4303-acff-c6fa89a32bae', #16/10; great performance, no bias reduction
#         '16c38a87-e4aa-4302-8f41-875191866786', #17/10; great performance, no bias reduction (maybe even an increase!)
#         'e4ddae43-7dbc-4ae3-983d-358cd803d508', #18/10; slight bias reduction
#         '31cf80ae-7ce4-47c6-896d-68d487a3392c', #19/10
#         # 'b387890e-dedc-4a88-9b20-ccf379afbe1b', #24/10 left hemi (no effect)
#         '76f534af-c133-4a30-8e2f-42f03d939fe2', #25/10 no effect
#         '02a94670-7cbd-4014-a496-ae9470f8e9e0', #26/10 low baseline bias (though possibly an effect)
#         # '322486ef-1d69-4d9f-8265-bf62953cb284', #27/10 no baseline bias
#         '873b7120-fa34-4a86-9d68-31150ef7ee4c', #30/10 little/no baseline bias
#         '86d8e1f4-de97-4cb6-9c26-373c1de977f6', #31/10 low baseline bias
#         # '86d8e1f4-de97-4cb6-9c26-373c1de977f6', #02/11 borderline perf.; no baseline bias
#         'e9bfb7ba-4ab4-4634-b782-e0d7c085986c', #6/11
# ]

# trials_ranges = [#list(range(94, 603)), #25/9
#                  list(range(100, 783)), #26/9
#                  list(range(90, 472)), #27/9
#                  list(range(94, 639)), #2/10
#                 #  list(range(90, 300)), #3/10
#                  list(range(90, 712)), #5/10
#                  list(range(90, 645)), #6/10 need to check when laser came on
#                  list(range(90, 652)), #10/10
#                  list(range(90, 701)), #16/10
#                  list(range(90, 705)), #17/10
#                  list(range(90, 871)), #18/10
#                  list(range(90, 786)), #19/10
#                 #  list(range('check trials')), #24/10
#                  list(range(90, 535)), #25/10
#                  list(range(90, 693)), #26/10
#                 #  list(range(90, 558)), #27/10
#                  list(range(90, 448)), #30/10
#                  list(range(90, 498)), #31/10
#                 #  list(range(100, 409)), #02/11
#                  list(range(100, 667)), #6/11
# ]



# ###############################################################################################
# ############ OLD METADATA


# ###################################
# # #008

# # # #inhibition whole trial
# # ## '124cddb8-22d2-4632-be4d-92181901a65e', #9/14 (30% chance)
# # eids = ['5a6457b5-95bb-4026-b825-c38d8adc49e4','8a09bb30-a040-41b4-bfe0-492a0cc921e7', #9/8, 9/9
# #         'ed27c5bf-7b72-40de-9167-a74eac48a4c8','2bbae950-9555-43d0-9891-03e47f18b286', #9/13, #9/10
# #         '5c78ef8b-50d5-4e34-9e05-1ac6964aa551', # 9/17
# #         '1cceaf57-cd56-410e-bddb-634ee9840c50','67a3d9a8-5ec5-4ed6-9473-f3c16f62d087'] #9/24, 10/19
# #         #'115d98e8-1356-472c-821a-48ad855f0bfc','409dc01a-c5dc-40cb-8356-e19372e4f546'] #10/20, 10/22
# # trials_ranges = ['ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL',
# #                 range(0,495),'ALL']#,'ALL']
# #                 #'ALL','ALL']

# # # #inhibition just during quiescent period
# # eids = ['238a0a48-392e-4d18-836a-eb5fe0853bfe','318bffb7-9bca-4145-affe-b52588a5dc1c','8e71c2f4-f931-4b1b-8f45-1ccb8b2460e8'] #9/30, 10/1, 10/7
# # trials_ranges = ['ALL','ALL','ALL']

# # # bilateral excitation only during quiescent period
# # eids = ['96aaa6e1-1b1d-46e9-b8a0-47de29d195a7','448d7b48-af08-47e0-bace-3167ba4ba9cc','be7b5af4-be82-4be4-903d-678c59d8d365'] #9/29, 10/4, 10/5
# # trials_ranges = ['ALL','ALL','ALL']

# # # unilateral RIGHT excitation only during quiescent period
# # eids = ['52f21cc6-6b1c-4fdc-b26e-c04bd4a4ce99'] #10/6
# # trials_ranges = ['ALL']

# # # unilateral LEFT excitation only during quiescent period
# # eids = ['05edb069-980d-42de-b9fa-178ef0648a21','6f7e2e29-68d1-4c8c-a7a5-4ec0baad08eb'] #10/11,10/13
# # trials_ranges = ['ALL','ALL']

# #################################################
# # # 003
# # # inhibition during whole trial
# # eids = ['a7222f4a-93aa-42f8-ab93-df0b7868bc25','3e3535fb-b06f-4e57-9460-cbe071984171',
# #         '3f704200-a246-4276-ae7f-c47c33e29f63','3cf488ae-c327-4e58-b6f6-7b7d81721628',
# #         'bb3a4433-65db-4640-8690-5bbc81ef8d49','87d94eeb-3754-414a-9dba-453f84b0f5fe',
# #         '205e8076-40b3-4432-8044-0dd890839db7','05edb069-980d-42de-b9fa-178ef0648a21',
# #         'd9dab492-0243-4135-b6aa-09ddc92e2d77','6f7e2e29-68d1-4c8c-a7a5-4ec0baad08eb',
# #         '8b0545fa-3a21-43b2-bfcb-7cfed09961cb','411d5f71-4f16-4ca5-ae20-a9789a4b49a6',
# #         '335a0eda-f61d-45d2-b1df-1aea44c5abcb','2b920090-8256-4a13-9923-a4b57952faa7'] #10/21, 10/22
# # trials_ranges = ['ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL']

# # # unilateral LEFT excitation whole trial
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289'] #9/27
# # trials_ranges = [range(0,388)]

# # # unilateral RIGHT excitation whole trial
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289'] #9/27
# # trials_ranges = [range(388,676)]

# # # all LEFT excitation
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289','c9f6d00a-b6ca-4d83-a1fd-6082453445ee'] #9/27, 10/26
# # trials_ranges = [range(0,388),'ALL']

# # # all RIGHT excitation
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289','51a67fc5-0930-43d9-8458-5ec54578b773'] #9/27, 10/28
# # trials_ranges = [range(388,676),'ALL']

# # # all trials
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289','51a67fc5-0930-43d9-8458-5ec54578b773', #9/27, 10/28
# #         'ba7bbd72-c41a-4dbd-9992-4a51489f4289','c9f6d00a-b6ca-4d83-a1fd-6082453445ee'] #9/27, 10/26
# # trials_ranges = [range(388,676),'ALL',
# #                 range(0,388),'ALL']

# # # just whole trial stim
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289', #9/27
# #         'ba7bbd72-c41a-4dbd-9992-4a51489f4289',] #9/27
# # trials_ranges = [range(388,676),
# #                 range(0,388)]

# # # just stimOn
# # eids = ['51a67fc5-0930-43d9-8458-5ec54578b773', #10/28
# #         'c9f6d00a-b6ca-4d83-a1fd-6082453445ee'] #10/26
# # trials_ranges = ['ALL',
# #                 'ALL']

# # # just L stimOn
# # eids = ['c9f6d00a-b6ca-4d83-a1fd-6082453445ee'] #10/26
# # trials_ranges = ['ALL']

# # # just R stimOn
# # eids = ['51a67fc5-0930-43d9-8458-5ec54578b773'] #10/26
# # trials_ranges = ['ALL']

# #################################################
# # 004
# # inhibition during whole trial
# ## '35cd3f60-267d-42b4-8606-a3eb2d763bab','9264704f-85f4-46b9-a269-e09cdba76e02' 10/25 (R), 11/09 (R)
# # eids = ['8c2163f0-41c3-4c2c-8293-b6523790bfb4','f78cbd4c-4a96-4da4-b2fd-b8d140150841', #10/22 #11/16
# #         'e098791a-305b-4338-9f3f-562a89948603','034bf182-47bb-4866-8340-1e910bdc79c6', #10/26 (poor BL performance), 10/27
# #         '23520eca-b5b1-45fb-a629-3ebf3a620c2f','88726cf3-2821-4075-8bfa-bdfcf1c6bfd8'] #11/10 (poor BL performance), 11/15 (borderline)
# #         #'b1dd1c50-6fbe-4f9b-8267-0b48a819c78e','c90780f1-9304-4bcf-b74b-6ec9cae581ad'] #10/20, 10/21 (both poor BL performance)
# #         # 'f483a2d6-0dd3-42cf-988b-aaf99824abd5'] #11/11

# # trials_ranges = ['ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',]
# #                 #'ALL','ALL']
# #                 # 'ALL']

# #################################################
# # # 011
# # # # inhibition during whole trial
# # eids = ['f0780250-d261-4337-b736-303658a7848a','16bb91ac-5701-48c4-8098-1861660d8ccb', #11/12, 11/17
# #         '997bed88-f960-4d40-9e3b-872727784e3c','60e0089d-d755-4e32-8a2b-f5dbd6b3a520', #11/19 (weird), 11/22 (B)
# #         '7dd4db33-7c27-4491-b0b5-3b5af9f526dd','3debc803-cabb-444a-ad4b-62b52f34dc1f', #11/18, 11/08
# #         #'28d3ceed-1edb-4ac6-b7c8-e3647ad36370', #'7373f901-2f6e-48f4-981c-30192a9299de',#11/26, 11/25 (poor BL performance both)
# #         'd71ec5e3-f257-47e2-8690-f943d13e0c13','269798e4-4837-42f0-80a8-12feafb5325e', #11/4 (R), #11/10 (R)
# #         'fddf4805-46fe-482c-ae12-b0a717f0d6a8'] #11/23 (B)
# # ### while effect is significant either way, it may be best to remove R and B hemisphere stims from this mouse
# # ### as there is significant off-target expression in R hemisphere caudal to SNr

# # trials_ranges = ['ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 #'ALL',
# #                 'ALL','ALL',
# #                 list(range(96,784))]

# # #################################################

# ### 010 (ZI)

# # # # inhibition during whole trial
# # eids = ['8e6c8994-6a12-4e2c-b066-958b9f84ab67', '330ebac8-a94e-4a0c-a50a-c571fb162b02', #2/3, 2/15
# #         '8b4f0ea4-9185-44eb-a27e-40238563bef7', '2aa240a4-0d31-4271-845d-c33e951e9118'] #2/18, 2/21
# # trials_ranges = ['ALL', 'ALL',
# #                  'ALL', 'ALL']

# # # # unilateral R excitation (starting at visual stim on)
# # eids = ['5e37ce85-aa69-4651-b8a0-03101faf4d33'] #2/16
# # trials_ranges = ['ALL', 'ALL']

# # # # unilateral L excitation (starting at visual stim on)
# # eids = ['b2da6e36-e25c-4b2a-9937-2ab30003ac48'] #2/17
# # trials_ranges = ['ALL', 'ALL']

# ###################################################

# ### 012 (SNr)

# # # # inhibition during whole trial
# # # # sessions w/ good performance during stim trials
# # eids = ['a4501dd7-8613-4cdf-99ef-ca56971557c5', '288b4537-a539-49f3-a56c-c67c80b3704c', #2/3, 2/16
# #         '186f7c0a-81ca-488a-92c0-14d41263edbe', '6c01b126-12cf-4739-8aa3-120bc62e2aee'] #2/18, 2/21
# # trials_ranges = ['ALL', 'ALL',
# #                  'ALL', 'ALL']

# # # # all sessions
# # eids = ['a4501dd7-8613-4cdf-99ef-ca56971557c5', '95acdc6e-8959-4d9a-b039-9c28a9f06ee0', #2/3, 2/7
# #         'ccf42b1c-8ed4-4265-afe6-2afb25d10d08', 'ef962323-9464-483f-992c-6a3de096a963', #2/8, 2/9
# #         '15f0c551-0bc2-4423-ab09-90e03dd240c5', '288b4537-a539-49f3-a56c-c67c80b3704c', #2/15, 2/16
# #         '186f7c0a-81ca-488a-92c0-14d41263edbe', '6c01b126-12cf-4739-8aa3-120bc62e2aee', #2/18, 2/21
# #         'ff54300e-0061-4ab3-9bee-b56a54d71376', 'a418eb79-b949-4fdf-9fad-b5d8b240e638', #2/22, 2/23
# #         '2a2efcbf-0269-477b-97f2-89f8ef04decf'] #2/24
# # trials_ranges = ['ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL']

# # # # unilateral R excitation
# # eids = ['2aed2d49-fced-4465-b3bb-58b225079748', '03bd9265-4e9e-4c96-8e57-4cc3827aa0d8'] #2/4, 2/11
# # trials_ranges = ['ALL', 'ALL']

# # # # # unilateral L excitation
# # eids = ['1f19e366-46b0-46ea-a137-1bf58a3d83c5', '04260f14-4329-4d71-9061-092cc441e2d7'] #2/2, 2/10
# # trials_ranges = ['ALL', 'ALL']

# ###################################################

# ### 018 (SNr)

# # # # inhibition during whole trial
# # eids = ['e059b876-c4ef-4a6b-aa1e-6ffc496ed9fc', 'e418cf94-e626-4a1e-9796-e9dcb35a5ad1', #30/03, 31/03
# #         '028cca41-d6cf-4487-b0d1-817a3c2ee94f', '8c070089-7fb4-4bd9-b88e-c99b498f7acf', #01/04, 7/4
# #         'b4dd0cff-3aed-4b74-973a-0a015cc2ad11'] #6/4
# # trials_ranges = ['ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL']
# ###################################################
# ### 016 (SNr)

# # # # # inhibition during whole trial
# # eids = ['efeef8a4-af69-44ef-9cfa-44c91ab67926', #08/04, borderline perf
# #         '9934246e-0e5a-4fe9-90dc-bf179c84482f', #11/4, borderline, mouse mostly moves right stim trials
# #         'ca97595c-1ae9-4bf5-8703-4368abe28c9e', #12/04 well below threshold performance
# #         '1f05c49c-1b40-418b-ab59-89232916710a'] #14/04 well below threshold
# # trials_ranges = [list(range(197,756)), 
# #                  list(range(122,830)), #11/4
# #                  list(range(122,794)),
# #                  list(range(159,545))]

# ###################################################
# ### 039 (SNr??)

# # # # # Continuous L hemisphere
# # eids = ['b8dea861-1d28-4db8-99fb-179bec03cede'] #39 21/4 (always left?? both RT and QP high??)
# # trials_ranges = [list(range(90,757))] #39 21/4

# # eids = ['ac4a1b85-ca72-4511-8ebf-7905aa563d10'] #39 20/4 (always right?? QP high but RT low??)
# # trials_ranges = [list(range(90,899))] #39 20/4

# # # # # 50hz L hemisphere
# # eids = ['461bdbb0-a13e-42b8-abe2-62a067c97cca','235b71ac-0bd9-488d-8043-95486bd911d0', #39 28/4 (always right!; trials+1 bias gone!), 24/4
# #         '3af5632f-e269-4b85-bcf4-c2be53cb05bb'] #39 19/4 (always right; trials+1 bias gone?)
# # trials_ranges = [list(range(90,963)),list(range(90,597)), #39 28/4, 24/4
# #                  list(range(90,716))] #39 19/4 (always right)

# # # # # 50hz R hemisphere
# # eids = ['1c49eb46-8b5e-4a6c-a1f1-1919a08a1cc3'] #39 25/4 (more typical SNr; always turns left)
# # #       '8f553d3c-fa0d-4679-a2ea-1f41f1b34cce' #39 18/4 (same as others but below threshold)
# # trials_ranges = [list(range(90,806))] #39 25/4 (more typical SNr; always turns left)
# # #               list(range(90,740)) #39 18/4 (same as others but below threshold)

# # # # # 50hz Bilateral
# # eids = ['250f9fbf-b3c3-4e7e-95ac-871bcff5ad3d'] #39 26/4 (VERY long RT, yet ok performance??)
# # trials_ranges = [list(range(90,433))] #39 26/4 (VERY long RT, yet ok performance??)

# ############### 44 (SNr) ###################

# # eids = ['a0b60046-8e5e-49f1-9ced-cfcc337bbe94', #8/9
# #         'a92b2424-b717-4cff-b5c5-9a59a776ac92', #11/9
# #         'c2bb6692-5b1a-4b3e-87f1-3890d0aaecee', #12/9
# #         '4bdc23e3-6f83-45c4-a7c1-9fb8fe9222a6', #13/9
# #         '94788e46-bfd4-4001-98b7-58dac45814d9', #14/9
# #         'd2662d15-f963-47f4-b5b9-14a43b79b049', #15/9 borderline perf.
# #         '45dfee80-5e5a-4248-9a8c-15c17f4b127a', #20/9 below thresh but strong effect
# #         '5c48d132-56c0-4ed3-a94f-230675a5743a', #22/9 
# #         # 'dab39ad1-79a8-4782-868e-9f453a1b741a', #26/9 unilateral L (still strong bias)
# #         # '36430bee-7242-458d-9823-b9644af95a15', #27/9 unilateral R (still strong bias)
# # ]
# # trials_ranges = [list(range(94,494)), #8/9
# #                  list(range(90,601)), #11/9
# #                  list(range(90,836)), #12/9
# #                  list(range(169,793)), #13/9
# #                  list(range(90,600)), #14/9
# #                  list(range(90,868)), #15/9
# #                  list(range(90,492)), #20/9
# #                  list(range(114,694)), #22/9
# #                 #  list(range(90,576)), #26/9
# #                 #  list(range(90,808)), #27/9
# # ]


# ###################################################
# ### All ZI mice

# # # unilateral LEFT excitation whole trial
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289'] #9/27
# # trials_ranges = [range(0,388)]

# # # unilateral RIGHT excitation whole trial
# # eids = ['ba7bbd72-c41a-4dbd-9992-4a51489f4289'] #9/27
# # trials_ranges = [range(388,676)]

# # # # unilateral R excitation (starting at visual stim on)
# # eids = ['5e37ce85-aa69-4651-b8a0-03101faf4d33','51a67fc5-0930-43d9-8458-5ec54578b773', #10 2/16, 3 10/28
# #         'ba7bbd72-c41a-4dbd-9992-4a51489f4289','95b46097-4cc0-4574-9ed3-7d9a2fd4b5ca'] #3 27/9, #22 effect is very weak - cannula placement is poor
# # trials_ranges = ['ALL', 'ALL',
# #                 list(range(388,676)),list(range(0,426))]


# # ### unilateral L excitation (starting at visual stim on)
# # eids = ['b2da6e36-e25c-4b2a-9937-2ab30003ac48','c9f6d00a-b6ca-4d83-a1fd-6082453445ee', #10 2/17, 3 10/26
# #         'ba7bbd72-c41a-4dbd-9992-4a51489f4289','17cd8693-ab43-41fd-9667-b1c1b2cacc0a'] #3 27/9, #22 effect is very weak - cannula placement is poor
# # trials_ranges = ['ALL', 'ALL',
# #                 list(range(0,388)),list(range(0,410))]

# # ## all stim sessions
# # eids = ['b2da6e36-e25c-4b2a-9937-2ab30003ac48','c9f6d00a-b6ca-4d83-a1fd-6082453445ee', #10 2/17, 3 10/26
# #         '5e37ce85-aa69-4651-b8a0-03101faf4d33','51a67fc5-0930-43d9-8458-5ec54578b773', #10 2/16, 3 10/28
# #         '95b46097-4cc0-4574-9ed3-7d9a2fd4b5ca','17cd8693-ab43-41fd-9667-b1c1b2cacc0a'] #22
# # trials_ranges = ['ALL', 'ALL',
# #                 'ALL','ALL',
# #                 list(range(0,426)),list(range(0,410))] #22

# # # # inhibition during whole trial
# # eids = ['8e6c8994-6a12-4e2c-b066-958b9f84ab67', '330ebac8-a94e-4a0c-a50a-c571fb162b02', #2/3, 2/15
# #         '8b4f0ea4-9185-44eb-a27e-40238563bef7', '2aa240a4-0d31-4271-845d-c33e951e9118', #10 2/18, 2/21
# #         'a7222f4a-93aa-42f8-ab93-df0b7868bc25','3e3535fb-b06f-4e57-9460-cbe071984171', #3
# #         '3f704200-a246-4276-ae7f-c47c33e29f63','3cf488ae-c327-4e58-b6f6-7b7d81721628',
# #         'bb3a4433-65db-4640-8690-5bbc81ef8d49','87d94eeb-3754-414a-9dba-453f84b0f5fe', #3
# #         '205e8076-40b3-4432-8044-0dd890839db7','05edb069-980d-42de-b9fa-178ef0648a21',
# #         'd9dab492-0243-4135-b6aa-09ddc92e2d77','6f7e2e29-68d1-4c8c-a7a5-4ec0baad08eb',
# #         '8b0545fa-3a21-43b2-bfcb-7cfed09961cb','411d5f71-4f16-4ca5-ae20-a9789a4b49a6',
# #         '335a0eda-f61d-45d2-b1df-1aea44c5abcb','2b920090-8256-4a13-9923-a4b57952faa7', #10/21, 10/22
# #         '681a022d-7158-40de-9ffc-a780ebe3a26d','81d6093f-29ca-496f-82d5-82cd70b13316', #22 31/8, 1/9
# #         '3c7bfbf6-bff7-4a9e-88ed-71d533e1aee8','5388bcbc-b4e6-4a3d-bfff-8f38440e1368'] #22 2/9, 9/9
# # trials_ranges = ['ALL', 'ALL',
# #                  'ALL', 'ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL',
# #                  'ALL','ALL', #22 31/8
# #                  'ALL','ALL']


# ################################################## SNr
# # # all SNr mice, unilateral LEFT excitation whole trial
# # eids = ['02af576e-0aa1-4784-b631-adbc3792f4d5','7373f901-2f6e-48f4-981c-30192a9299de', #011: 11/24 11/25
# #         '847cdd72-0859-4bb4-9bba-c3b11045d7c8','9e4b80e4-ae85-4e5e-8e1d-519eb68347be', #011: 11/16, 11/5
# #         'edcaf465-4d4e-4d0d-86a0-aec5733ccd13','a8f4b965-89b6-4905-b953-3f6f7c42bbb7', #004: 10/19, 11/01
# #         'd20889b9-2e2e-43a4-9917-2114b7f05c83','fb1c5429-6329-4370-8e68-b9f864cb2319', #004: 11/12, #008: 9/28
# #         '1f19e366-46b0-46ea-a137-1bf58a3d83c5', '04260f14-4329-4d71-9061-092cc441e2d7', #12 2/2, 2/10
# #         '9428f5fc-a6b9-4689-8200-b0a846933a1d', 'efeef8a4-af69-44ef-9cfa-44c91ab67926'] #18 29/3, 16 8/4

# # trials_ranges = [list(range(0,229))+list(range(349,409))+list(range(576,647)),list(range(0,114))+list(range(390,527)),
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL',list(range(0,462)),
# #                 'ALL', 'ALL',
# #                 list(range(184,794)), list(range(85,197))]


# # # all SNr mice, unilateral RIGHT excitation whole trial
# # eids = ['7e704fd4-cefd-4314-bd5a-e79212c94836', '1cceaf57-cd56-410e-bddb-634ee9840c50', #008: 9/23, 9/24
# #         'bb8d5380-69be-40e2-b26b-918f5f48dd5d', '3d965f9d-e89d-402f-ae15-c985b1149967', #008 9/27, 18 28/3
# #         '2aed2d49-fced-4465-b3bb-58b225079748', '03bd9265-4e9e-4c96-8e57-4cc3827aa0d8', #12 2/4, 2/11
# #         '0ff9161b-bae8-4ff1-a080-2928fc45cc54'] #16 7/4
# # trials_ranges = [list(range(423,798)),list(range(495,895)),
# #                 list(range(0,175)),list(range(155,735)),
# #                 'ALL','ALL',
# #                 list(range(0,342))]

# # # all SNr trials excitation
# # eids = ['02af576e-0aa1-4784-b631-adbc3792f4d5',#'7373f901-2f6e-48f4-981c-30192a9299de', #011: 11/24 11/25 (poor BL performance)
# #         '847cdd72-0859-4bb4-9bba-c3b11045d7c8', '9e4b80e4-ae85-4e5e-8e1d-519eb68347be', #011: 11/16, 11/5
# #         'edcaf465-4d4e-4d0d-86a0-aec5733ccd13', 'a8f4b965-89b6-4905-b953-3f6f7c42bbb7', #004: 10/19, 11/01
# #         'd20889b9-2e2e-43a4-9917-2114b7f05c83', 'fb1c5429-6329-4370-8e68-b9f864cb2319', #004: 11/12, #008: 9/28
# #         '7e704fd4-cefd-4314-bd5a-e79212c94836', '1cceaf57-cd56-410e-bddb-634ee9840c50', #8
# #         'bb8d5380-69be-40e2-b26b-918f5f48dd5d', #8,
# #         '2aed2d49-fced-4465-b3bb-58b225079748', '03bd9265-4e9e-4c96-8e57-4cc3827aa0d8', #12 2/4, 2/11
# #         '1f19e366-46b0-46ea-a137-1bf58a3d83c5', '04260f14-4329-4d71-9061-092cc441e2d7', #12 2/2, 2/10
# #         '9428f5fc-a6b9-4689-8200-b0a846933a1d', '3d965f9d-e89d-402f-ae15-c985b1149967', #18 7/4, 18 28/3
# #         'efeef8a4-af69-44ef-9cfa-44c91ab67926''0ff9161b-bae8-4ff1-a080-2928fc45cc54'] #16 8/4 , 16 29/3

# # trials_ranges = [list(range(0,229))+list(range(349,409))+list(range(576,647)),#list(range(0,114))+list(range(390,527)),
# #                 'ALL','ALL',
# #                 'ALL','ALL',
# #                 'ALL',list(range(0,462)),
# #                 list(range(423,798)),list(range(495,895)),
# #                 list(range(0,175)),list(range(155,735)),
# #                 'ALL','ALL',
# #                 'ALL', 'ALL',
# #                 list(range(0,342)),list(range(184,794)),
# #                 list(range(85,197)),list(range(0,342))]

# # ###0-7,7-12,12-15,15-22,22-23,23-28
# # #all SNr inhibition sessions
# # eids = [
# #         '5a6457b5-95bb-4026-b825-c38d8adc49e4','8a09bb30-a040-41b4-bfe0-492a0cc921e7', #8 9/8, 9/9
# #         'ed27c5bf-7b72-40de-9167-a74eac48a4c8','2bbae950-9555-43d0-9891-03e47f18b286', #8 9/13, #9/10
# #         '5c78ef8b-50d5-4e34-9e05-1ac6964aa551','67a3d9a8-5ec5-4ed6-9473-f3c16f62d087', #8 9/17, 10/19
# #         '1cceaf57-cd56-410e-bddb-634ee9840c50', # 8 24/9 poor baseline accuracy remove,
# #         '997bed88-f960-4d40-9e3b-872727784e3c', # 11 19/11
# #         'f0780250-d261-4337-b736-303658a7848a','16bb91ac-5701-48c4-8098-1861660d8ccb', # 11/ 12/11, 11 17/11
# #         '7dd4db33-7c27-4491-b0b5-3b5af9f526dd','3debc803-cabb-444a-ad4b-62b52f34dc1f', #11 18/11, 11 8/11
# #         '28d3ceed-1edb-4ac6-b7c8-e3647ad36370', #11 26/11 poor BL performance
# #         '8c2163f0-41c3-4c2c-8293-b6523790bfb4','f78cbd4c-4a96-4da4-b2fd-b8d140150841', #4
# #         '034bf182-47bb-4866-8340-1e910bdc79c6', #'e098791a-305b-4338-9f3f-562a89948603', #4 27/10 (borderline), 4 26/10 poor BL performance
# #         '23520eca-b5b1-45fb-a629-3ebf3a620c2f','88726cf3-2821-4075-8bfa-bdfcf1c6bfd8', #4 10/11 (poor BL performance), 4 15/11 (borderline)
# #         'b1dd1c50-6fbe-4f9b-8267-0b48a819c78e','c90780f1-9304-4bcf-b74b-6ec9cae581ad', #4 20/10 & 21/10 (poor BL performance)
# #         'e059b876-c4ef-4a6b-aa1e-6ffc496ed9fc', 'e418cf94-e626-4a1e-9796-e9dcb35a5ad1', #18 30/03, 31/03
# #         '028cca41-d6cf-4487-b0d1-817a3c2ee94f', '8c070089-7fb4-4bd9-b88e-c99b498f7acf', #18 01/04, 7/4
# #         'b4dd0cff-3aed-4b74-973a-0a015cc2ad11', '9934246e-0e5a-4fe9-90dc-bf179c84482f', #18 6/4, 18 16/6 (ephys)
# #         'efeef8a4-af69-44ef-9cfa-44c91ab67926', '25863f4c-20d6-43e1-903d-088bcbfdc441', #16 8/4,  #16 11/4 (borderline) #consider removing 16
# #         'a4501dd7-8613-4cdf-99ef-ca56971557c5', #'95acdc6e-8959-4d9a-b039-9c28a9f06ee0'] #12 2/3, 2/7
# #         #'ccf42b1c-8ed4-4265-afe6-2afb25d10d08', 'ef962323-9464-483f-992c-6a3de096a963', #2/8, 2/9 both poor BL and stim accuracy?
# #         '15f0c551-0bc2-4423-ab09-90e03dd240c5', '288b4537-a539-49f3-a56c-c67c80b3704c', #2/15, 2/16
# #         '186f7c0a-81ca-488a-92c0-14d41263edbe', '6c01b126-12cf-4739-8aa3-120bc62e2aee', #2/18, 2/21
# #         # 'ff54300e-0061-4ab3-9bee-b56a54d71376', 'a418eb79-b949-4fdf-9fad-b5d8b240e638', #2/22, 2/23
# #         # '2a2efcbf-0269-477b-97f2-89f8ef04decf', #2/24
# # ]
 

# # trials_ranges = [
# #                 'ALL','ALL', #8
# #                 'ALL','ALL', #8
# #                 'ALL','ALL', #8
# #                 range(0,495),#8
# #                 'ALL', #11
# #                 'ALL','ALL', #11
# #                 'ALL','ALL', #11
# #                 'ALL', #11
# #                 'ALL','ALL', #4
# #                 'ALL',#'ALL', #4
# #                 'ALL','ALL', #4
# #                 'ALL','ALL', #4
# #                 'ALL','ALL', #18
# #                 'ALL','ALL', #18
# #                 'ALL',list(range(121,283)) + list(range(423,528)) + list(range(660,767)), #18
# #                 'ALL',list(range(122,798)), #16
# #                 'ALL', #'ALL'] #12
# #                 #'ALL', 'ALL',
# #                 'ALL', 'ALL', #12
# #                 'ALL', 'ALL', #12
# #                 # 'ALL', 'ALL',
# #                 # 'ALL',
# # ]

# # # all SNr mice, bilateral inhibition
# # eids = ['2bbae950-9555-43d0-9891-03e47f18b286', #8, 10/9
# #         '1cceaf57-cd56-410e-bddb-634ee9840c50', #8, 24/9
# #         '15f0c551-0bc2-4423-ab09-90e03dd240c5', #12, 15/2
# #         '288b4537-a539-49f3-a56c-c67c80b3704c', #12, 16/2
# #         '186f7c0a-81ca-488a-92c0-14d41263edbe', #12, 18/2
# #         '6c01b126-12cf-4739-8aa3-120bc62e2aee', #12, 21/2
# #         'e059b876-c4ef-4a6b-aa1e-6ffc496ed9fc', #18, 30/3
# #         'b4dd0cff-3aed-4b74-973a-0a015cc2ad11', #18, 6/4
# #         '25863f4c-20d6-43e1-903d-088bcbfdc441' #16, 11/4
# # ]

# # trials_ranges = ['ALL', #8, 10/9
# #                  list(range(0,495)), #8, 24/9
# #                  'ALL', #12, 15/2
# #                  'ALL', #12, 16/2
# #                  'ALL', #12, 18/2
# #                  'ALL', #12, 21/2
# #                  'ALL', #18, 30/3
# #                  'ALL', #18, 6/4
# #                  list(range(122,798)) #16, 11/4
# # ]


# # # # # ###all SNr unilateral RIGHT inhibition sessions
# # eids = ['5a6457b5-95bb-4026-b825-c38d8adc49e4', 'ed27c5bf-7b72-40de-9167-a74eac48a4c8', #8 8/9, 8 13/9
# #         '5c78ef8b-50d5-4e34-9e05-1ac6964aa551', 'd71ec5e3-f257-47e2-8690-f943d13e0c13', #8 17/9, 11 4/11
# #         '269798e4-4837-42f0-80a8-12feafb5325e', '028cca41-d6cf-4487-b0d1-817a3c2ee94f', #11 10/11 #18 01/04
# #         '8c070089-7fb4-4bd9-b88e-c99b498f7acf'] #18 7/4

# # trials_ranges = ['ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 'ALL']

# # # # # ###all SNr unilateral LEFT inhibition sessions
# # eids = ['8a09bb30-a040-41b4-bfe0-492a0cc921e7', '67a3d9a8-5ec5-4ed6-9473-f3c16f62d087', #8 9/9, 8 19/10
# #         '997bed88-f960-4d40-9e3b-872727784e3c', 'f0780250-d261-4337-b736-303658a7848a', #11 19/11, 11 12/11
# #         '16bb91ac-5701-48c4-8098-1861660d8ccb', '7dd4db33-7c27-4491-b0b5-3b5af9f526dd', #11 17/11, 11 18/11
# #         '3debc803-cabb-444a-ad4b-62b52f34dc1f', 'f78cbd4c-4a96-4da4-b2fd-b8d140150841',#11 08/11, 4 16/11
# #         '88726cf3-2821-4075-8bfa-bdfcf1c6bfd8', 'e418cf94-e626-4a1e-9796-e9dcb35a5ad1',#4 15/11 (borderline), 18 31/3
# #         'efeef8a4-af69-44ef-9cfa-44c91ab67926']

# # trials_ranges = ['ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 'ALL', 'ALL',
# #                 list(range(197,756))]

# # # # # ###all SNr inhibition only during QP
# # eids = ['d1a66312-dad9-4951-8a9c-7497c3aaf69f', '318bffb7-9bca-4145-affe-b52588a5dc1c', #18 5/5, #8 1/10
# #         '8e71c2f4-f931-4b1b-8f45-1ccb8b2460e8'] #8 7/10

# # trials_ranges = [list(range(157,865)), 'ALL',
# #                 'ALL']

# # # # ###all SNr inhibition only during ITI
# # eids = ['9cc77c22-08f2-49cd-b37d-905397fab334','6e104af9-7c6b-49a0-98ac-bf09489851d3'] #16, #8

# # trials_ranges = ['ALL', 'ALL']

# ############ STN excitation (QP)
# # ## RIGHT
# # eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35'] #25 19/10/22, 21/10/22

# # trials_ranges = [list(range(350,402)), list(range(251,372))]

# # ### LEFT
# # eids = ['7bd7cbf6-e3ab-4222-ade8-458a5afb30f9'] #25 20/10/22

# # trials_ranges = [list(range(107,190))]

# ########### STN inhibition
# ### ALL
# # eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35', #25 19/10/22, 21/10/22
# #         '7bd7cbf6-e3ab-4222-ade8-458a5afb30f9','002e60e1-e646-4f69-b6e3-d3b00f082797', #25 20/10/22, 27/10 R
# #         '0068b011-c60f-491f-a29c-245877cd1bc1','abf38955-b5d4-4319-921a-f0658188ad57', #25 26/10/22 L, 25/10/22 R
# #         '67688ca2-a5a3-4cea-8131-8da5b920dcff','b6f80439-98e6-41cf-a7e8-7216b1d93feb', #25 28/10/22 L, 31/10/22 R
# #         '45b7a288-8bf7-411c-b1ba-178b58fc7f6f','9606af89-12f6-4a57-8cd9-24f733beae8a', #25 2/11/22 R, 3/11/22 LR
# #         '3dd68334-84cc-402d-a053-45bd352c14fc','4ac3caaf-1b27-4c89-9020-560b7f6f6df4', #25 7/11, 8/11
# #         'c82ceab1-ad8f-42aa-bb2d-c9594315d2cd','47093eb5-2516-4e6f-a66e-92275c52659b', #24 18/1, 27/1
# #         '3ca6c201-91f2-4ba9-8b8a-012446bdf7d2','d2f085c3-0a84-48c6-88fa-e6b25bd89938', #24 R 10/2 (excellent), L 9/2 (ok)
# #         '81e58c8f-bfbd-4c54-b7ee-56d1d37767cc','b64467f6-0fb9-4d77-8c97-eacb3a15dffe', #24 B 8/2 (good), R 7/2 (borderline)
# #         '1dcab41c-9ec6-4a1c-bd4c-67721db91df6', #24 L 14/2 (good)
# #         '79468bd8-6fa2-48e4-8151-88951b33a8e0','baf2b96e-c587-49cf-acf7-c2ffb1c332a6', #26 16/1, 18/1
# #         '91857de2-766f-43e2-a3cc-ace233485ebd','6b4a1004-9508-4ef4-b7a7-7cd10a676948', #26 20/1, 23/1
# #         # '5654a819-d54a-4ef0-ac2d-247624ab4f50' #26 24/1 (below threshold)
# #         '455f55c1-81ef-4541-8894-cf6c713a3a82','7aa67b01-67b8-44a2-bf23-2e58152fb8d3', #26 10/2 L, 6/2 R
# #         'ce6be632-7986-4e05-b2c3-231d459d4dc4','cab9a767-05b4-4033-b074-225db0d37221'] #26 3/2, 2/2

# # trials_ranges = [list(range(269,333)), list(range(131,251)) + list(range(372,497)), #25 19/10/22, 21/10/22
# #                  list(range(191,555)), list(range(102,939)), #25 20/10/22, 27/10/22
# #                  list(range(146,790)), list(range(188,236)) + list(range(413,597)), #25 26/10/22 L, 25/10/22 R
# #                  list(range(150,618)), list(range(100,461)),#25 28/10/22 L, 31/10/22 R
# #                  list(range(97,816)), list(range(162,791)), #25 2/11/22 R, 3/11/22 LR
# #                  list(range(325,623)), list(range(137, 746)),#25 7/11
# #                  list(range(90,409)), list(range(182, 470)), #24 18/1, 27/1
# #                  list(range(90, 932)), list(range(90, 897)), #24 R 10/2 (excellent), L 9/2 (ok)
# #                  list(range(90, 709)), list(range(90, 586)),#24 B 8/2 (good), R 7/2 (borderline)
# #                  list(range(90, 571)), #24 L 14/2 (good)
# #                  list(range(90,300)), list(range(90,400)), #26 16/1
# #                  list(range(90,450)), list(range(173,308)), #26 20/1, 23/1
# #                 #  list(range(90,256)) #26 24/1 (below threshold)
# #                  list(range(90,400)), list(range(90,281)), #26 10/2 L, 6/2 R
# #                  list(range(90,470)), list(range(90,528))] #26 3/2, 2/2

# ###25
# # eids = ['3ce813d3-75f1-4558-83ea-c125f71f6bba','80a2e5c9-285f-49b9-abef-57a5bc594f35', #25 19/10/22, 21/10/22
# #         '7bd7cbf6-e3ab-4222-ade8-458a5afb30f9','002e60e1-e646-4f69-b6e3-d3b00f082797', #25 20/10/22, 27/10 R
# #         '0068b011-c60f-491f-a29c-245877cd1bc1','abf38955-b5d4-4319-921a-f0658188ad57', #25 26/10/22 L, 25/10/22 R
# #         '67688ca2-a5a3-4cea-8131-8da5b920dcff','b6f80439-98e6-41cf-a7e8-7216b1d93feb', #25 28/10/22 L, 31/10/22 R
# #         '45b7a288-8bf7-411c-b1ba-178b58fc7f6f','9606af89-12f6-4a57-8cd9-24f733beae8a', #25 2/11/22 R, 3/11/22 LR
# #         '3dd68334-84cc-402d-a053-45bd352c14fc','4ac3caaf-1b27-4c89-9020-560b7f6f6df4'] #25 7/11, 8/11
# # trials_ranges = [list(range(269,333)), list(range(131,251)) + list(range(372,497)), #25 19/10/22, 21/10/22
# #                  list(range(191,555)), list(range(102,939)), #25 20/10/22, 27/10/22
# #                  list(range(146,790)), list(range(188,236)) + list(range(413,597)), #25 26/10/22 L, 25/10/22 R
# #                  list(range(150,618)), list(range(100,461)),#25 28/10/22 L, 31/10/22 R
# #                  list(range(97,816)), list(range(162,791)), #25 2/11/22 R, 3/11/22 LR
# #                  list(range(325,623)), list(range(137, 746))] #25 7/11

# ###26
# # eids = ['79468bd8-6fa2-48e4-8151-88951b33a8e0','baf2b96e-c587-49cf-acf7-c2ffb1c332a6', #26 16/1 R, 18/1 L
# #         '91857de2-766f-43e2-a3cc-ace233485ebd','6b4a1004-9508-4ef4-b7a7-7cd10a676948', #26 20/1 B, 23/1 L
# #         'cab9a767-05b4-4033-b074-225db0d37221','ce6be632-7986-4e05-b2c3-231d459d4dc4', #26 2/2 L, 3/2 L
# #         '7aa67b01-67b8-44a2-bf23-2e58152fb8d3'] #26 6/2 R no baseline bias
# #         # '5654a819-d54a-4ef0-ac2d-247624ab4f50','67a7b96c-c3d1-440f-9023-0ad50dfae94b', #26 24/1 L, 12/1 R (both below threshold)
# #         # '76862a7b-f07e-47e3-b8ea-dc4588109cef','eacd7f97-f676-4d95-af31-e61b3182cfcf'] #26 17/1 L, 8/2 B (both below threshold)
# # trials_ranges = [list(range(90,300)), list(range(90,400)), #26 16/1
# #                  list(range(90,450)), list(range(173,308)), #26 20/1, 23/1
# #                  list(range(90,528)), list(range(90,470)), #26 2/2 L, 3/2 L
# #                  list(range(90,180)) + list(range(181,281))] #26 6/2 R no baseline bias
# #                 #  list(range(90,256)), list(range(90,822)), #26 24/1 (below threshold)
# #                 #  list(range(90,351)), list(range(90,538))] #26 17/1 (way below threshold)

# # ###24
# # eids = [#'1ddfaa39-f15b-4eda-9c70-c6d4f874fdb6','bca63bed-244c-4cb6-b173-26661d02e901', #24 L* 16/12 (below threshold), #24 R 19/1 (bad)
# #         'c82ceab1-ad8f-42aa-bb2d-c9594315d2cd','47093eb5-2516-4e6f-a66e-92275c52659b', #24 L* 18/1, R* 27/1
# #         # 'f62bbff2-a1c6-4646-9306-454f1c5b07a9',#,'7504026d-a0f8-433d-bd4f-f1d35e1cc4e2'] #24 R 20/1 (bad), B 24/1 (below threshold)
# #         # '4ab45924-65a7-4178-8723-ab457c6ee242', #24 R 3/2 (bias flipped in control)
# #         '3ca6c201-91f2-4ba9-8b8a-012446bdf7d2','d2f085c3-0a84-48c6-88fa-e6b25bd89938', #24 R 10/2 (excellent), L 9/2 (ok)
# #         '81e58c8f-bfbd-4c54-b7ee-56d1d37767cc','b64467f6-0fb9-4d77-8c97-eacb3a15dffe',#24 B 8/2 (good), R 7/2 (borderline)
# #         '521827e5-e064-4df7-af21-391e7689102e','b754992d-ac3a-477f-a4d9-421e10f34681',#24 L 6/2 (borderline), L* 2/2 (few trials, poor behavior at end)
# #         '607afbbc-5fd9-4dae-aaa5-3edd187604f3',#24 R 1/2 (borderline)
# #         '2f95753b-06cf-4860-b3a7-82b4d7a9fd45','75615687-3cca-4728-841f-10874bfe78be']#24 L* 10/1 (borderline), R* 11/1 (borderline)
# # trials_ranges = [#list(range(90,854)),list(range(90,449)), #24 16/12 (below threshold), #24 19/1 (bad)
# #                  list(range(90,409)),list(range(182, 470)), #24 18/1, 27/1
# #                 #  list(range(90, 350)),#,list(range(90, 800))] #24 20/1 (bad), 24/1 (below threshold)
# #                 #  list(range(90, 377)),#24 R 3/2 (bias flipped in control)
# #                  list(range(90, 932)),list(range(90, 897)), #24 R 10/2 (excellent), L 9/2 (ok)
# #                  list(range(90, 709)),list(range(90, 586)),#24 B 8/2 (good), R 7/2 (borderline)
# #                  list(range(90, 400)),list(range(100, 300)),#24 L 6/2 (borderline), L* 2/2 (few trials, poor behavior at end)
# #                  list(range(90, 910)),#24 R 1/2 (borderline)
# #                  list(range(90,596)),list(range(90,841))]#24 L* 10/1 (borderline), R* 11/1 (borderline)

# # # ############ STN excitation
# ### L Hemisphere
# # eids = ['c0892faa-519e-430f-9b40-992b09fd618a',#,'e8db73ec-eff4-4704-a81b-ecbd00c5daf0'] #25 1/11/22 L, 28/10/22 L
# #         'cb8f7026-175b-4386-97ae-46858a721197','84734bec-d898-4f50-b659-b4a7b7686fe8', #24 12/1/23, 13/2
# #         '3475b385-19af-4be2-a667-4cd9a4ba7527','7791c224-b38d-4a1f-a133-beb043ee1301'] #26 25/1, 13/2

# # trials_ranges = [list(range(124,726)),#, list(range(0,204))] #25 1/11/22 L, 28/10/22 L
# #                  list(range(418,898)),list(range(90,555)), #24 12/1/23, 13/2
# #                  list(range(90, 406)),list(range(90, 367))] #26 25/1

# # ## R Hemisphere
# # eids = ['c4f246b4-454c-4d42-9e4a-daf2c92b7787', 'bb590645-fd17-4025-84e5-e65d3ef948ea', #25 31/10/22, #25 4/11/22
# #         'cb8f7026-175b-4386-97ae-46858a721197', #24 12/1/23
# #         '583bf8b4-c500-494e-be90-6548bf26173a', 'f4d0076a-d9ef-4952-92ec-0ec92936fda1', #26 26/1/23 (slightly below threshold), 27/1/23
# #         'b6de331a-495a-42b3-b029-ee743a99ac10'] #26 14/2

# # trials_ranges = [list(range(0,215)),list(range(50,399)), #25 31/10/22
# #                  list(range(90,418)), #24 12/1/23
# #                  list(range(90, 364)), list(range(90, 488)), #26 26/1/23 (slightly below threshold)
# #                  list(range(90, 397))]

# ### All stim sessions

# # eids = ['c0892faa-519e-430f-9b40-992b09fd618a','c4f246b4-454c-4d42-9e4a-daf2c92b7787', 'bb590645-fd17-4025-84e5-e65d3ef948ea',
# #         '3475b385-19af-4be2-a667-4cd9a4ba7527','cb8f7026-175b-4386-97ae-46858a721197',
# #         '583bf8b4-c500-494e-be90-6548bf26173a', 'f4d0076a-d9ef-4952-92ec-0ec92936fda1']
# #         #'784af2de-8082-4117-8149-aa967558b4a3' #26 1/2 (QP to reward/error)

# # trials_ranges = [list(range(124,726)),list(range(0,215)),list(range(50,399)),
# #                  list(range(90,406)),list(range(90,898)),
# #                  list(range(90, 364)), list(range(90, 488))]
# #                  #list(range(90, 543))

# ##################################################
# ################# D1 Manipulation ################

# ############ 36
# ###### continuous
# ## R
# # eids = ['74c09dd3-1037-4020-a4d9-b499fd6599be','0a161756-e61a-4211-9f39-59987caac9b2', #36 9/3 R, 13/3 R
# #         'a5c3a7bf-23af-44ba-aa17-6814a84264c7','37f0bd30-767f-45d2-a667-ac14a2a0787e', #36 15/3 R, 21/3 R
# #         '7f37d94b-a3f8-4ad3-af45-d5b2fce5119d','20ed1969-96f6-4f57-9ae7-66ee094e47d7']#, #36 3/4 R, 5/4 R
# #         # 'fa418725-acfd-4853-975d-66041008affa'] #36 21/4 (session may be void)
# # trials_ranges = [list(range(100, 676)),list(range(90, 609)), #36 9/3 R, 13/3 R
# #                  list(range(90, 781)),list(range(90, 685)), #36 15/3 R, 21/3 R
# #                  list(range(90, 900)),list(range(90, 580))]#, #36 3/4 R, 5/4 R
# #                 #  list(range(90, 844))]

# # ## L
# # eids = ['63504410-3830-40f4-9e7b-8b15e73b476c','3ffd2a46-cbc5-4a6b-965f-c3baeb4c4899', #36 10/3 L, 14/3 L
# #         'c2c3cc18-e125-42e3-b2ac-fc6b6e1e70b8','46dd2112-a336-4221-b1f1-601e57fbd972', #36 4/4 L, #36 12/4
# #         'a079d54f-825f-4267-925b-a2ec3ba1b631','2fc30f24-10ee-4f3d-bc03-a42e2a1eb51e'] #36 13/4, #36 14/4
# #         # '51c8f945-560c-4d9d-8079-7eed0ac3573a', #36 20/3 L
# # trials_ranges = [list(range(90, 734)), list(range(90, 674)), #36  10/3, 14/3
# #                  list(range(90, 918)),list(range(90, 468)), #36 4/4 L, #36 12/4
# #                  list(range(90, 753)),list(range(90, 914))] #36 13/4

# # Bilateral
# # eids = ['4e5e7d0b-6bc4-445a-8975-d1c1a3caaa26',#, #'a34c3639-4a0c-4bb2-b369-dd72487e4e1f' #36 17/3, 16/3
# #         '19aaab85-9ee4-4959-9592-2fdcc9101264','2845f8ed-6f0b-4b48-85a2-974b07c6a0a0', #36 31/3 bilateral, 6/4 bilateral
# #         'cf3a1d93-486a-4f76-99bd-41539d29c4d3','be50456b-7477-4638-887e-a8895e34b7b2', #36 07/4 bilateral, #36 30/3 bilateral
# #         '74586452-6ce3-4be5-a86c-ed0ffb6b0be9'] #36 17/4 bilateral (more bias on stim trials! weird)
# # trials_ranges = [list(range(90, 743)),#,# list(range(90, 975))] #36  17/3, 16/3
# #                  list(range(90, 649)),list(range(130, 664)), #36 31/3 bilateral, 6/4 bilateral
# #                  list(range(130, 992)),list(range(90, 658)), #36 07/4 bilateral, #36 30/3 bilateral
# #                  list(range(90, 653))] #36 17/4 bilateral (more bias on stim trials! weird)

# # # ### not a huge effect...

# # # ###### 50hz
# # # ### L
# # eids = ['61c10489-929f-4bdb-bc0e-a5feaf075183','bef903f8-fedb-42b7-83e7-c06446bb766b', #36 22/3 L (no effect?), #36 24/3 L
# #         '23c27379-e440-4013-9a1b-6ee05eed33b3']#, #36 19/4 L (near threshold performance, very biased)
# # trials_ranges = [list(range(90, 958)),list(range(90, 794)), #36 22/3 L (no effect?), #36 24/3 L
# #                  list(range(90, 878))]#, #36 19/4 L (near threshold performance, very biased)

# # # ### R
# # eids = ['84c5c7e8-c19b-490f-a878-7672047440da'] #36 23/3 R? (no effect?)
# # trials_ranges = [list(range(90, 735))] #36 23/3 R? (no effect?)

# ## Bilateral
# # eids = ['7ae2b0ea-9982-4fb8-8d02-c918f6d09a44','b9bc150e-ebac-46f5-83e6-8146aa8d96f5', #36 27/3 L (no effect?), 28/3 bilateral
# #         '82e041f8-b677-48a2-84d6-b42deb4803b7','3e3b5e27-032c-4ee0-8db1-c61bf2b6aade'] #36 29/3 bilateral, #36 20/4 bilateral
# # trials_ranges = [list(range(90, 859)), list(range(90, 458)), #36 27/3 L (no effect?), 28/3 bilateral
# #                  list(range(90, 709)), list(range(90, 675))] #36 29/3 bilateral, #36 20/4 bilateral

# ## On continuously (ie, 100% trials)
# # Bilateral 20hz
# # eids_stim = ['8da6bdde-bec9-4310-bf4e-a5817f54035b', #36 22/5
# #         '20938807-1be8-4a4b-ba8a-5d2d327e5f7b', #36 26/5
# #         'e7bc20be-4d5f-4e87-8c46-e139582f117e', #36 19/5
# #         'd2355102-58a5-47c8-a696-cab40c54a348', #36 23/5 (L hemi!)
# #         '7759d9f9-df87-4dd9-9406-a8d9c7f8a6a3', #36 24/5 (R hemi!)
# #         'e92b5990-6955-4524-9679-6008c1303ea4', #36 30/5
# #         '5d46b01b-2fdb-4075-999a-12af5e446b0a' #36 31/5
# # ]
# # trials_ranges_stim = [list(range(576, 809)), #36 22/5
# #                  list(range(379, 885)), #36 26/5
# #                  list(range(162, 265)) + list(range(308, 430)) + list(range(591, 638)), #36 19/5 (last 2 are continuous!)
# #                  list(range(250, 685)), #36 23/5 (L hemi!)
# #                  list(range(380, 550)), #36 24/5 (R hemi!)
# #                  list(range(439, 501)), #36 30/5
# #                  list(range(309, 444)) #36 31/5
# # ]

# # ## Control 
# # eids_ctrl = ['8da6bdde-bec9-4310-bf4e-a5817f54035b', #36 22/5
# #         # '49d29315-cd59-46f8-88c1-af07cca74a05', #36 18/5 performance likely below threshold
# #         '20938807-1be8-4a4b-ba8a-5d2d327e5f7b', #36 26/5
# #         'e7bc20be-4d5f-4e87-8c46-e139582f117e', #36 19/5
# #         'd2355102-58a5-47c8-a696-cab40c54a348', #36 23/5
# #         '7759d9f9-df87-4dd9-9406-a8d9c7f8a6a3', #36 24/5
# #         'e92b5990-6955-4524-9679-6008c1303ea4', #36 30/5
# #         '5d46b01b-2fdb-4075-999a-12af5e446b0a' #36 31/5
# # ]
# # trials_ranges_ctrl = [list(range(90, 576)), #36 22/5
# #                 #  list(range(90, 576)), #36 18/5
# #                 list(range(90, 379)), #36 26/5
# #                 list(range(90, 162)) + list(range(266, 308)) + list(range(431, 591)), #36 19/5
# #                 list(range(90, 250)), #36 23/5
# #                 list(range(90, 380)), #36 24/5
# #                 list(range(90, 439)), #36 30/5
# #                 list(range(90, 309)) #36 31/5
# # ]


# ############ 35

# ##### continuous
# # R
# # eids = ['5f0964f7-7018-44f9-9310-1819055c88a4',#'64a9517f-fefb-43dc-98d5-e0041e38e906', #35 9/3 R, 1/3 R
# #         '42413192-cad7-44bf-a759-9f761a3b973d','b1b0a076-1527-4d1e-a714-27adbfff6219', #35 13/3 R, 16/3 (somewhat below threshold)
# #         'b4cff50c-934f-4855-9aa3-9b04d989de59','631af73a-23bf-4c63-b3b6-29382e3ec992'] #35 20/3 R, 3/4 R
# #         #'6d2652ab-abdc-4e34-9f82-1be1ae95393e' #35 5/4 R performance borderline
# # trials_ranges = [list(range(90, 761)),#list(range(321, 451)), #35 9/3 R, 1/3 R, 
# #                  list(range(131, 1055)),list(range(170, 867)), #35 13/3 R, 16/3 (somewhat below threshold)
# #                  list(range(90, 545)),list(range(110, 844))] #35 20/3 R, 3/4 R
# #                  #list(range(90, 535)) #35 5/4 R performance borderline
# # ## no effect; pretty clearly

# # L
# # eids = ['4535379c-1216-40f8-a0fd-054cc27799f0',#'8fc44e79-5d11-40c5-b338-87dfd1c115d3', ##35 8/3 L, 35 2/3 L
# #         '252731b9-9b96-4bea-a2b2-056683506cf7','b8bbf15b-115c-495a-86b4-818bbacb39fe', #35 10/3 L, 17/3 L (somewhat below threshold)
# #         'a6fe82bf-8d76-4a07-8dfe-0da5cb168e06','56445d1b-8e49-4358-8cb7-4b85ba68c0a5'] #35 21/3 L, 4/4 L
# # trials_ranges = [list(range(100, 922)),#list(range(538, 669)), #35 8/3 L #35 2/3 L, 
# #                  list(range(90, 396)),list(range(90, 795)), #35 10/3 L
# #                  list(range(90, 482)),list(range(90, 929))] #35 21/3 L, 4/4 L
# # difference is subtle, but lower bias on R side. Also, higher bias on L high contrasts, no bias on R high contrasts

# ### Continuous Bilateral
# # eids = ['e56d0d56-00ac-4cba-8ea5-3429632d87d4','8e3bec84-9a1e-4d97-a22d-f08793b1dc6d', #35 14/3, 30/3
# #         '3f4d8647-1701-4763-9630-3aee0b7b8f88','95f3745b-64c8-46db-924a-3cb867349804', #35 6/4 no obvious effect, 7/4
# #         'da0ccad4-33fb-45f5-be60-434789df1758']#,'76af3bdb-0842-4418-b06b-1ca45c519c53'] #35 31/3, 17/4
# # trials_ranges = [list(range(90, 728)),list(range(90, 744)), #35 14/3, 30/3
# #                  list(range(300, 960)),list(range(170, 491)), #35 6/4 no obvious effect, 7/4
# #                  list(range(90, 654))]#,list(range(90, 546))] #35 31/3, 17/4
# # ## very little difference, though high variability

# # ###### 50hz
# # R
# # eids = ['1f36b80d-dfb5-4842-a7fc-8af8f10ce602','e49d896c-e724-4966-98d9-6bfd9691a70f', #35 22/3 no obvious effect, 23/3
# #         '9e2ebea3-450d-41da-8066-77cbbc3b46c7']#,'48d99226-0974-40b6-8357-a5876f7765df'] #35 24/3, 27/3
# # trials_ranges = [list(range(90, 787)),list(range(90, 663)), #35 22/3 no obvious effect, 23/3
# #                  list(range(118, 966))]#,[]] #35 24/3, 27/3
# ## psychometric curves nearly the same
# ## overall, bias is low however, even on non-stim trials

# # # L
# # eids = ['192eb333-4a1b-4db2-9e0d-72f86ff0fd62'] #35 12/4 no effect
# # trials_ranges = [list(range(165, 651))] #35 12/4 no effect

# # ## 50hz Bilateral
# # eids = ['c2a819bb-0cdf-4f91-8646-d227f65f6c78','c0e0f994-7f1f-4c71-a781-9843f034ef50', #35 6/3 Bilateral, 3/3 Bilateral
# #         '96468f7e-df40-4b3f-9651-cfb25d8d0b3e','d9bb48d5-d886-499e-bd4a-203c5277f64f', #35 15/3 Bilateral, 28/3 Bilateral
# #         'a0f4b0fb-388e-4a15-a3fc-4792814f18ac'] #35 29/3 Bilateral
# # trials_ranges = [list(range(134,788)),list(range(460, 829)), #35 6/3, 3/3 Bilateral
# #                  list(range(90,741)),list(range(100,672)), #35 15/3 Bilateral, 28/3 Bilateral
# #                  list(range(90,907))] #35 29/3 Bilateral
# # ## very little difference


# # #### ALL RIGHT INHIBITION
# # eids = ['74c09dd3-1037-4020-a4d9-b499fd6599be','0a161756-e61a-4211-9f39-59987caac9b2', #36 9/3 R, 13/3 R
# #         'a5c3a7bf-23af-44ba-aa17-6814a84264c7','37f0bd30-767f-45d2-a667-ac14a2a0787e'] #36 15/3 R, 21/3 R
# #         # '5f0964f7-7018-44f9-9310-1819055c88a4','b4cff50c-934f-4855-9aa3-9b04d989de59', #35 9/3 R, #35 20/3 R
# #         # '42413192-cad7-44bf-a759-9f761a3b973d','b1b0a076-1527-4d1e-a714-27adbfff6219'] #35 13/3 R, 16/3 (somewhat below threshold)
# # trials_ranges = [list(range(100, 676)),list(range(90, 609)), #36 9/3 R, 13/3 R
# #                  list(range(90, 781)),list(range(90, 685))] #36 15/3 R, 21/3 R
# #                 #  list(range(90, 761)),list(range(90, 545)), #35 9/3 R, #35 20/3 R
# #                 #  list(range(131, 1055)),list(range(170, 867))] #35 13/3 R, 16/3 (somewhat below threshold)

# # #### ALL LEFT INHIBITION
# # eids = ['63504410-3830-40f4-9e7b-8b15e73b476c','3ffd2a46-cbc5-4a6b-965f-c3baeb4c4899', #36 10/3 L, 14/3 L
# #         '4535379c-1216-40f8-a0fd-054cc27799f0',#'8fc44e79-5d11-40c5-b338-87dfd1c115d3', ##35 8/3 L, 35 2/3 L
# #         '252731b9-9b96-4bea-a2b2-056683506cf7','b8bbf15b-115c-495a-86b4-818bbacb39fe', #35 10/3 L, 17/3 L (somewhat below threshold)
# #         'a6fe82bf-8d76-4a07-8dfe-0da5cb168e06','e56d0d56-00ac-4cba-8ea5-3429632d87d4'] #35 21/3 L, #35 14/3 B
# # trials_ranges = [list(range(90, 734)), list(range(90, 674)), #36  10/3, 14/3
# #                  list(range(100, 922)),#list(range(538, 669)), #35 8/3 L #35 2/3 L, 
# #                  list(range(90, 396)),list(range(90, 795)), #35 10/3 L
# #                  list(range(90, 482)),list(range(90, 728))] #35 21/3 L, #35 14/3 B

# # ##### ALL BILATERAL 50hz
# # eids = ['7ae2b0ea-9982-4fb8-8d02-c918f6d09a44','b9bc150e-ebac-46f5-83e6-8146aa8d96f5', #36 27/3 L (no effect?), 28/3 bilateral
# #         '82e041f8-b677-48a2-84d6-b42deb4803b7','3e3b5e27-032c-4ee0-8db1-c61bf2b6aade', #36 29/3 bilateral, #36 20/4 bilateral
# #         'c2a819bb-0cdf-4f91-8646-d227f65f6c78','c0e0f994-7f1f-4c71-a781-9843f034ef50', #35 6/3 Bilateral, 3/3 Bilateral
# #         '96468f7e-df40-4b3f-9651-cfb25d8d0b3e','d9bb48d5-d886-499e-bd4a-203c5277f64f', #35 15/3 Bilateral, 28/3 Bilateral
# #         'a0f4b0fb-388e-4a15-a3fc-4792814f18ac'] #35 29/3 Bilateral
# # trials_ranges = [list(range(90, 859)), list(range(90, 458)), #36 27/3 L (no effect?), 28/3 bilateral
# #                  list(range(90, 709)), list(range(90, 675)), #36 29/3 bilateral, #36 20/4 bilateral
# #                  list(range(134,788)),list(range(460, 829)), #35 6/3, 3/3 Bilateral
# #                  list(range(90,741)),list(range(100,672)), #35 15/3 Bilateral, 28/3 Bilateral
# #                  list(range(90,907))] #35 29/3 Bilateral

# # ### ALL Bilateral CONTINUOUS
# # eids = ['e56d0d56-00ac-4cba-8ea5-3429632d87d4','8e3bec84-9a1e-4d97-a22d-f08793b1dc6d', #35 14/3, 30/3
# #         '3f4d8647-1701-4763-9630-3aee0b7b8f88','95f3745b-64c8-46db-924a-3cb867349804', #35 6/4 no obvious effect, 7/4
# #         'da0ccad4-33fb-45f5-be60-434789df1758',#,'76af3bdb-0842-4418-b06b-1ca45c519c53'] #35 31/3, 17/4
# #         '4e5e7d0b-6bc4-445a-8975-d1c1a3caaa26',#, #'a34c3639-4a0c-4bb2-b369-dd72487e4e1f' #36 17/3, 16/3
# #         '19aaab85-9ee4-4959-9592-2fdcc9101264','2845f8ed-6f0b-4b48-85a2-974b07c6a0a0', #36 31/3 bilateral, 6/4 bilateral
# #         'cf3a1d93-486a-4f76-99bd-41539d29c4d3','be50456b-7477-4638-887e-a8895e34b7b2', #36 07/4 bilateral, #36 30/3 bilateral
# #         '74586452-6ce3-4be5-a86c-ed0ffb6b0be9'] #36 17/4 bilateral (more bias on stim trials! weird)

# # trials_ranges = [list(range(90, 728)),list(range(90, 744)), #35 14/3, 30/3
# #                  list(range(300, 960)),list(range(170, 491)), #35 6/4 no obvious effect, 7/4
# #                  list(range(90, 654)),#,list(range(90, 546))] #35 31/3, 17/4
# #                  list(range(90, 743)),#,# list(range(90, 975))] #36  17/3, 16/3
# #                  list(range(90, 649)),list(range(130, 664)), #36 31/3 bilateral, 6/4 bilateral
# #                  list(range(130, 992)),list(range(90, 658)), #36 07/4 bilateral, #36 30/3 bilateral
# #                  list(range(90, 653))] #36 17/4 bilateral (more bias on stim trials! weird)

# ############ 37

# # ### unilateral R
# # eids = ['aabe7656-2d2f-44ee-9e87-bd5ca4102523', #37 17/7
# #         '1ce32560-314a-49c5-afac-57cc7f5cdb9b', #37 R 31/7
# # ]

# # trials_ranges = [list(range(252, 401)), #37 17/7
# #                  list(range(148, 689)), #37 31/7                
# # ]

# # ### unilateral L
# # eids = ['69d52afd-957b-4e91-8bf3-2f83c0053682', #37 14/7
# #         # 'e4786276-0cb8-45fa-97cb-182658596d3f', #37 26/7 (doesn't always turn L? no large increase in QP?)
# #         '4cf61029-b073-4418-8207-1ec86ff80226', #37 28/7 - almost always turns left, though not on HC L trials?
# # ]

# # trials_ranges = [list(range(90, 189)), #37 14/7
# #                 #  list(range(90, 755)), #37 26/7
# #                  list(range(90, 985)), #37 28/7
# # ]

# # ## all unilateral
# # eids = ['aabe7656-2d2f-44ee-9e87-bd5ca4102523', #37 17/7
# #         '1ce32560-314a-49c5-afac-57cc7f5cdb9b', #37 R 31/7
# #         '69d52afd-957b-4e91-8bf3-2f83c0053682', #37 14/7
# #         'e4786276-0cb8-45fa-97cb-182658596d3f', #37 26/7 (doesn't always turn L? no large increase in QP?)
# #         '4cf61029-b073-4418-8207-1ec86ff80226', #37 28/7 - almost always turns left, though not on HC L trials?
# # ]

# # trials_ranges = [list(range(252, 401)), #37 17/7
# #                  list(range(148, 689)), #37 31/7    
# #                  list(range(90, 189)), #37 14/7
# #                  list(range(90, 755)), #37 26/7
# #                  list(range(90, 985)), #37 28/7            
# # ]


# # # eids = ['97555715-ddfd-4e98-be18-c5616125cde5', #37 21/7, unilateral R, low voltage, borderline perf
# # # ]

# # # trials_ranges = [list(range(185, 641)), #37 21/7
# # # ]

# # ### bilateral
# # eids = ['da48644d-6859-4838-8e2c-5435e5e83764', #37 13/7 bilateral; ALWAYS turns right
# #         '36d25914-b9d7-4660-929e-6b6abe64d7c6', #37 25/7, bilateral, 0.03V, 20hz (mouse almost exclusively turns left)
# #         '33201ab9-04fe-455b-827b-8aea51949a70', #37 27/7, bilateral, 0.1V, 20hz (mouse mostly turns right!)
# #         '1f87f9fa-da91-41c9-92ae-8e1be72766dd', #37 1/8, bilateral, 0.1V, 20hz (mouse moves both directions!)
# # ]

# # trials_ranges = [list(range(176, 308)), #37 13/7
# #                  list(range(200, 824)), #37 25/7 not sure what trial laser started
# #                  list(range(136, 662)), #37 27/7
# #                  list(range(132, 551)), #37 1/8
# # ]

# # ###all decent performance
# # eids = ['aabe7656-2d2f-44ee-9e87-bd5ca4102523', #37 17/7
# #         # 'da48644d-6859-4838-8e2c-5435e5e83764', #37 13/7 bilateral; ALWAYS turns right
# #         '69d52afd-957b-4e91-8bf3-2f83c0053682', #37 14/7
# #         '97555715-ddfd-4e98-be18-c5616125cde5', #37 21/7, unilateral R, low voltage, borderline perf
# #         '1ce32560-314a-49c5-afac-57cc7f5cdb9b', #37 R 31/7
# # ]

# # trials_ranges = [list(range(252, 401)), #37 17/7
# #                 #  list(range(176, 308)), #37 13/7
# #                  list(range(90, 189)), #37 14/7
# #                  list(range(185, 641)), #37 21/7
# #                  list(range(90, 689)), #37 31/7 (not sure when laser started) - mouse moves both directions
# # ]

# ############ 38

# # ## Left hemi 50hz
# # eids = ['1a5b1972-bc01-4abd-8124-0a31ea814912', #38, 27/6 (50hz)
# # ]

# # trials_ranges = [list(range(90, 364)), #38, 27/6 (50hz)
# # ]

# # # ## Right hemi 50hz
# # eids = ['77828eaf-27bb-41bb-a111-c56f2c500233', #38, 28/7 R (50hz) (bias definitely still there)
# # ]

# # trials_ranges = [list(range(214, 405)), #38, 28/7 R (50hz)
# # ]


# # # ##bilateral 50hz
# # eids_ex_38 = [
# #         # '6b0b342d-5bb3-403b-85bd-22996e3d03f5', #38, 7/6 slightly below threshold perf; no bias on nonstim trials?
# #         'aae41bc3-6965-4629-a02f-71ea8eeeac26', #38, 12/6 (50hz) borderline perf
# #         'd1b1cf5a-c68d-416a-9a92-b3a77f5145f6', #38, 15/6 (50hz)
# #         '34478c65-c8e9-4343-9e1a-492bbcdd4fa7', #38 29/6 (50hz) borderline perf
# #         '1a5b1972-bc01-4abd-8124-0a31ea814912', #38, 27/6 (50hz, LEFT HEMI)
# #         'f29f284d-2cf9-42ac-8a71-24c2d4a2d241', #38, 3/7 (50hz)
# #         # '4721f49b-6772-400f-b9e9-fd8c65fc2183', #38, 5/7 (50hz, below threshold performance)
# #         # '21a01c43-d4ff-4f64-8b69-931cfd91ecb3', #38, 12/7 (50hz, borderline perf.; few trials)
# #         # 'f328df1d-d736-455c-a09b-a55869cb8723', #38, 17/7 (50hz, borderline perf.; few trials)
# #         'a5b427bf-e4ae-428d-8955-b2bfa534011b', #38, 21/7 (50hz)
# #         '33326079-f197-4dea-a319-b3377dd2996e', #38, 24/7 (50hz) ALF OBJECT NOT FOUND
# #         '7a898aeb-e6d0-4241-9bdd-e593720fbb3c', #38, 26/7 (bias still appears to be there)
# #         'd873e6c7-4e61-46a3-9c0d-038cc5544b1e', #38, 31/7 50hz (slightly below threshold perf? at least borderline)
# #         'aa645856-a18c-4564-a046-0d8793404106', #4/8
# # ]

# # trials_ranges_ex_38 = [
# #                 #  list(range(195, 527)), #38, 7/6
# #                  list(range(129, 618)), #38, 12/6 (50hz)
# #                  list(range(102, 555)), #38, 15/6 (50hz)
# #                  list(range(90, 400)), #38 29/6 (50hz)
# #                  list(range(90, 364)), #38, 27/6 (50hz)
# #                  list(range(90, 450)), #38, 27/6 (50hz)
# #                 #  list(range(90, 615)), #38, 5/7 (50hz)
# #                 #  list(range(90, 250)), #38, 12/7 (50hz, borderline perf.; few trials)
# #                 #  list(range(90, 300)), #38, 17/7 (50hz, borderline perf.; few trials)
# #                  list(range(90, 597)), #38, 21/7 (50hz)
# #                  list(range(126, 562)), #38, 24/7 (50hz)
# #                  list(range(113, 457)), #38, 26/7 (bias still appears to be there)
# #                  list(range(91, 408)), #38, 31/7
# #                  list(range(103, 539)), #38, 4/8
# # ]

# # # ## Right hemi 0hz
# # # eids = ['c84b3e0d-93be-42e7-9dc4-49bc87e12005', #38, 14/6
# # # ]

# # # trials_ranges = [list(range(90, 405)), #38, 14/6
# # # ]


# # bilateral 0hz
# eids_in_38 = ['1f5bc7a5-1703-492a-8df4-f1aaa17e8935', #38, 9/6
#         '6f2a676d-7524-4d5e-b965-4a744c65eab2', #38, 16/6
#         'c84b3e0d-93be-42e7-9dc4-49bc87e12005', #38, 14/6 (RIGHT HEMI)
#         '86029b2d-4855-4fb0-b2a7-1b4c0da70c6c', #38, 28/6
#         'e0c7b3ed-bf0c-48af-922c-48e3aab76086', #38, 30/6
#         '2bd9be29-02c5-4727-929c-045c6acb2d90', #38, 4/7 borderline perf, consider removal
#         '71aa1c84-0174-4e6b-b394-0dc883391452', #38, 13/7 (few trials))
#         '7e6e6ea5-c138-4514-9ac1-8ab369979782', #38, 19/7
#         # '65fb2455-2764-4972-9a4c-cd23decbff32', #38, 20/7 (only 10% stim trials)
#         '4cdfca10-c1b2-4e57-bbe4-1bf3e325de91', #38, 25/7 borderline performance
#         '0cb59f03-761d-4a65-98a5-3a38d3a31def', #38, 1/8 
#         # '77de0838-d155-40a1-9b5d-7cd663012188', #3/8 outlier?
# ]

# trials_ranges_in_38 = [list(range(110, 604)), #38, 9/6
#                  list(range(126, 501)), #38, 16/6
#                  list(range(90, 405)), #38, 14/6
#                  list(range(90, 341)), #38, 28/6
#                  list(range(90, 667)), #38, 30/6
#                  list(range(250, 586)), #38, 30/6
#                  list(range(90, 275)), #38, 13/7 (few trials))
#                  list(range(245, 699)), #38, 19/7
#                 #  list(range(189, 596)), #38, 19/7
#                  list(range(90, 436)), #38, 25/7 
#                  list(range(90, 637)), #38, 1/8 
#                 #  list(range(90, 503)), # 3/8 outlier?
# ]

# ############ 54

# # ## 50hz stim, bilateral
# # eids_ex_54 = ['e93d6e9b-80c2-449f-860d-4fb59567914b', #3/10
# #         # '2cbd0ae3-69e0-4586-9de2-a68dca14f878', #5/10 #low baseline bias
# #         'e9e44d2d-b15c-46be-8442-dd2dda5d5723', #6/10
# #         #'3daacb5c-9de8-4434-a3bb-269e0adb034f', #10/10 no baseline bias?
# #         '2439b61f-83ca-48e0-af89-3d701fb74b76', #19/10
# #         # '58f72a9f-471a-4889-a986-49edf7732fc9', #20/10
# #         '8424a850-ba6e-42a4-8731-c5f2cbc38833', #23/10
# #         'b5195c82-0269-4c4b-87c0-c1d7eaa9f1fc', #31/10
# #         '5e0bc149-ad12-4aaa-a7e8-5cdf0cf2f16b', #02/11
# #         '9d1fad67-c822-4cb7-9d63-69324f79a38e', #09/11 - seems like an effect - QP lower, RT higher
# #         # '58c96b89-b575-4998-a883-87bb0980ebdc', #10/11 - suspiciously no effect; no RT or QP effect either
# #         'f2f59a40-c08f-4504-b709-52cf4383072a', #15/11
# #         '07d19e88-6d3b-493f-b005-9ce458771265', #17/11 - few trials - low baseline bias
# #         '0e1daaaf-2e18-444f-a2f0-991c74c77055', #20/11 - borderline perf; late trials removed for better accuracy
# # ]
    
# # trials_ranges_ex_54 = [list(range(90, 862)), #3/10
# #                 #  list(range(90, 799)), #5/10 need to check when laser on
# #                  list(range(200, 1116)), #6/10 need to check when laser on
# #                  #list(range(90, 658)), #10/10
# #                  list(range(119, 887)), #19/10
# #                 #  list(range(500, 851)), #20/10
# #                  list(range(205, 663)), #23/10
# #                  list(range(90, 718)), #31/10
# #                  list(range(120, 893)), #02/11
# #                  list(range(154, 680)), #09/11
# #                 #  list(range(90, 939)), #10/11
# #                  list(range(99, 544)), #15/11
# #                  list(range(216, 400)), #17/11 - slightly truncated
# #                  list(range(141, 500)), #20/11 - late trials removed for better accuracy
# # ]
                 
# # ### 0hz stim, bilateral
# # eids_in_54 = [#'3547f202-eaed-48e8-b20d-e209c8e61386', #4/10 no baseline bias
# #         # 'fc7e0d7b-36ef-4a9b-a451-6e2e8b87fb33', #9/10 no baseline bias; also, maybe not 0hz?
# #         'c86f4ece-cb61-4f61-a32b-044cc5a7a83f', #17/10
# #         '4e317696-79b1-40ec-90d9-5712dc799948', #18/10 very strong baseline bias
# #         '58f72a9f-471a-4889-a986-49edf7732fc9', #20/10 - some baseline bias, bias higher on stim trials!
# #         '9251ad04-0d88-40c1-b9e0-3b0350caefe2', #24/10
# #         '37208000-0476-42ef-8282-322272040e5b', #25/10
# #         'b8a984ea-4e15-492f-b646-e5899aa66e85', #30/10
# #         # '9c2df030-e9d9-4d1d-b7c3-b4b302cd8f7f', #3/11 little effect?
# #         # '30ba5777-9504-4653-a37f-0317c4eb5ced', #6/11 
# #         # '1edede50-ccf9-4b75-92d9-9c0d8945e84d', #8/11 - effect opposite as expected? - QP lower, RT higher
# #         '5e3e4a98-3d79-4ffa-8e16-0c44a167440b', #13/11 borderline performance
# #         '128c872c-5e79-4e60-b644-b53d5854189d', #14/11
# #         'a5e48872-2376-4c8e-b1db-8c31f8cd069b', #16/11
# #         'c4a31290-90ab-42d4-83ce-341bc6c980ce', #21/11
# #         '21861d63-c3be-40f4-961b-421cb5fc3913', #23/11 - borderline perf though strong effect
# #         'b1582929-1117-4e44-862e-c775008ca548', #01/12 - strong effect
# # ]
    
# # trials_ranges_in_54 = [#list(range(189, 757)), #4/10
# #                 #  list(range(90, 654)), #9/10
# #                  list(range(95, 588)), #17/10
# #                  list(range(246, 611)), #18/10
# #                  list(range(100, 500)), #20/10
# #                  list(range(112, 500)), #24/10 #691
# #                  list(range(90, 900)), #25/10
# #                  list(range(115, 802)), #30/10
# #                 #  list(range(100, 571)), #3/11
# #                 #  list(range(145, 440)), #6/11; range truncated; mouse changes strategy toward end of session
# #                 #  list(range(127, 741)), #8/11
# #                  list(range(121, 450)), #13/11 - trials truncated for better performance
# #                  list(range(147, 667)), #14/11
# #                  list(range(90, 656)), #16/11
# #                  list(range(150, 563)), #21/11
# #                  list(range(120, 500)), #23/11 - late trials removed for better accuracy
# #                  list(range(90, 731)), #01/12
                 
# # ]


# # # # # # # ############ 53

# # eids_ex_53 = [#'0a5d156f-696c-442d-a3e5-a1ec0535edd2', #17/10 unilateral R 50hz (no sidedness afaik)
# #         #'0829492a-84cd-40d9-a17d-e2ba77a28a8c', #18/10 unilateral L 50hz (no sidedness afaik)
# #         # 'a6a3ac50-c5a2-4e40-a7d1-f66c041d5f89', #19/10 baseline bias gone
# #         '49ed175c-9f47-4048-9ea2-af267f7ca445', #20/10 10%
# #         '4cef1a10-acd0-48af-bd8b-a5c1a1d2fef6', #23/10 10%
# #         '6a971abe-3287-487b-b1ee-faef050303e4', #24/10 10%, bias still there?
# #         '1978c5fc-239e-47e4-9d97-b0c1473a7b78', #25/10 15%
# #         'ea0eb232-5d95-4702-888d-b014c96419a2', #26/10 15%
# #         '00b8057d-117d-434a-82e3-94cf7eb5f020', #27/10 15%
# #         # '8b2214be-2ff3-42c0-829f-f6441d02e0be', #30/10 15% no baseline bias
# #         '413bda0c-0b1c-4d2f-9bd2-fff32a2e928c', #31/10 15%
# #         'e170ea22-f828-4435-99e9-36220d050c4c', #1/11 15% low baseline bias; borderline
# #         # '5428d5e7-7a1f-46a3-af91-323226f28f25', #3/11 15% low baseline bias
# #         # 'e73998dd-cff2-40d6-80ab-8f87aad0db7a', #6/11 15% no baseline bias; mouse impulsive
# #         '56b6f822-4538-43c6-9f14-7831cedcb1bc', #08/11 15% little baseline bias
# #         '0974d094-1011-4ab0-a093-f96bdf257b67', #10/11 15%
# #         '3693330f-2dee-4943-8713-2ee908736a06', #13/11 15% appears to be an effect
# #         'd5b2ce58-65d4-42f3-841d-59358e386090', #14/11 15% unclear if effect; earlier trials not more biased
# #         'af0e43f5-d3a4-44af-9924-20eecff02744', #16/11 15% little baseline bias; earlier trials might be ok
# #         'ef77efd8-d1ba-4904-ad7b-565e1425198b', #17/11 15% very little baseline bias; early trials fine!
# #         'c558a4bd-0960-49c4-94ec-7964168a05a7', #20/11 15% low baseline bias
# #         '96ff08d6-b9f1-4596-bc70-ee10c7502670', #21/11 low baseline bias; appears to be effect
# #         '9a6f6206-5958-450f-84a0-9689d1ef34c3', #22/11 low baseline bias; little effect
# #         '94a30725-7b79-4eb2-8938-7838e874f367', #23/11 low baseline bias
# #         '5c476c28-c6f1-454b-92bf-b790c81f1eb2', #24/11 low baseline bias
# #         '2630a3ef-20fb-4511-bd40-5baae2e2f33e', #27/11
# #         # '98e16563-a739-4c72-864e-bb2b4e8425fd', #14/12 unilateral R 0hz low baseline bias; no obvious QP effect?
# #         '5a1c0170-68c3-4e64-8b46-4f4c37a47c5e', #13/12 unilateral L 0hz, obvious QP/RT effect!
        
# # ]
    
# # trials_ranges_ex_53 = [#list(range(146, 863)), #17/10
# #                  #list(range(90, 888)), #18/10
# #                 #  list(range(90, 534)), #19/10
# #                  list(range(124, 769)), #20/10
# #                  list(range(90, 598)), #23/10
# #                  list(range(100, 829)), #24/10
# #                  list(range(113, 749)), #25/10
# #                  list(range(127, 849)), #26/10
# #                  list(range(148, 941)), #27/10
# #                 #  list(range(106, 722)), #30/10
# #                  list(range(95, 530)), #31/10
# #                  list(range(122, 670)), #01/11
# #                 #  list(range(104, 901)), #03/11
# #                 #  list(range(101, 675)), #06/11
# #                 #  list(range(105, 718)), #08/11
# #                  list(range(105, 300)), #08/11; alt early trials; still very little baseline bias
# #                  list(range(159, 800)), #10/11
# #                  list(range(124, 668)), #13/11
# #                  list(range(106, 623)), #14/11
# #                 #  list(range(90, 756)), #16/11
# #                  list(range(90, 600)), #16/11; alt early trials
# #                 #  list(range(90, 799)), #17/11
# #                  list(range(90, 350)), #17/11; alt early trials
# #                  list(range(265, 700)), #20/11; removed late trials for better performance accuracy
# #                  list(range(150, 450)), #20/11; removed later trials to improve BL bias
# #                  list(range(111, 805)), #22/11
# #                  list(range(108, 767)), #23/11
# #                  list(range(90, 767)), #24/11
# #                  list(range(123, 887)), #27/11
# #                  list(range(90, 944)), #14/12
# #                  list(range(90, 859)), #13/12
# # ]

# # ### from stimOn
# # eids_stimOn_53 = ['3ad1c330-a34e-460b-894c-1c50d04e6d38', #28/11
# #                 #   'b4ef9d1c-4897-4b7e-9c05-40867cc1888d', #29/11 strange effect; check TTLs?
# #                   '37af82ca-2b18-463c-b4a8-8c3ac2242c30', #30/11 LEFT HEMI
# #                 #   'f264b806-07f1-40a7-9fe3-4c1eb063b9b6', #01/12 RIGHT HEMI; no RT effect, maybe laser wasn't on? check TTLs
# #                   'b09b7f9b-4833-426c-b395-1599b2e015f9', #04/12
# #                   '45e79f8f-d7ae-4329-921f-4470278d7723', #05/12
# #                 #   '7d7193a8-bee8-4b37-90e4-9c26c17b7387', #06/12; no RT effect? check TTLs
# #                 #   'ffa1825c-a520-4f2f-bd70-33c3d53aa8a1', #07/12; no RT effect

# # ]

# # trials_ranges_stimOn_53 = [list(range(90, 738)), #28/11
# #                         #    list(range(90, 978)), #29/11
# #                            list(range(90, 788)), #30/11 LEFT HEMI
# #                         #    list(range(90, 532)), #01/12
# #                            list(range(90, 400)), #04/12, truncated for much better performance
# #                            list(range(90, 758)), #05/12
# #                         #    list(range(90, 588)), #06/12
# #                         #    list(range(90, 926)), #07/12
# # ]

# # ### NO STIM
# # eids = ['3782e7ff-55d8-42ff-b818-e108f78557d8', #02/11
# #         'c08a956b-869c-4266-9a5c-09818b2263d7', #13/10
# #         'b2133729-d675-4bb5-8529-ccd538c5f14c', #16/10
        
# # ]
    
# # trials_ranges = [list(range(90, 770)), #02/11
# #                  list(range(90, 804)), #13/10
# #                  list(range(90, 806)), #16/10
# # ]

# # #### ALL D1
# # ### 0hz stim
# # eids = ['1f5bc7a5-1703-492a-8df4-f1aaa17e8935', #38, 9/6
# #         '6f2a676d-7524-4d5e-b965-4a744c65eab2', #38, 16/6
# #         # 'c84b3e0d-93be-42e7-9dc4-49bc87e12005', #38, 14/6 (RIGHT HEMI)
# #         '86029b2d-4855-4fb0-b2a7-1b4c0da70c6c', #38, 28/6
# #         'e0c7b3ed-bf0c-48af-922c-48e3aab76086', #38, 30/6
# #         '2bd9be29-02c5-4727-929c-045c6acb2d90', #38, 4/7 borderline perf, consider removal
# #         # '71aa1c84-0174-4e6b-b394-0dc883391452', #38, 13/7 (few trials))
# #         '7e6e6ea5-c138-4514-9ac1-8ab369979782', #38, 19/7
# #         # '65fb2455-2764-4972-9a4c-cd23decbff32', #38, 20/7 (only 10% stim trials)
# #         '4cdfca10-c1b2-4e57-bbe4-1bf3e325de91', #38, 25/7 borderline performance
# #         '0cb59f03-761d-4a65-98a5-3a38d3a31def', #38, 1/8 
# #         # '77de0838-d155-40a1-9b5d-7cd663012188', #3/8 outlier?
# #         #'3547f202-eaed-48e8-b20d-e209c8e61386', #54 #4/10 no baseline bias
# #         # 'fc7e0d7b-36ef-4a9b-a451-6e2e8b87fb33', #54 #9/10
# #         'c86f4ece-cb61-4f61-a32b-044cc5a7a83f', #54 #17/10
# #         '4e317696-79b1-40ec-90d9-5712dc799948', #54 #18/10 very strong baseline bias
# #         '58f72a9f-471a-4889-a986-49edf7732fc9', #54 #20/10 - some baseline bias, bias higher on stim trials!
# #         '9251ad04-0d88-40c1-b9e0-3b0350caefe2', #54 24/10
# # ]

# # trials_ranges = [list(range(110, 604)), #38, 9/6
# #                  list(range(126, 501)), #38, 16/6
# #                 #  list(range(90, 405)), #38, 14/6
# #                  list(range(90, 341)), #38, 28/6
# #                  list(range(90, 667)), #38, 30/6
# #                  list(range(250, 586)), #38, 30/6
# #                 #  list(range(90, 275)), #38, 13/7 (few trials))
# #                  list(range(245, 699)), #38, 19/7
# #                 #  list(range(189, 596)), #38, 19/7
# #                  list(range(90, 436)), #38, 25/7 
# #                  list(range(90, 637)), #38, 1/8 
# #                 #  list(range(90, 503)), # 3/8 outlier?
# #                 #list(range(189, 757)), #54 #4/10
# #                 #  list(range(90, 654)),#54  #9/10
# #                  list(range(95, 588)), #54 #17/10
# #                  list(range(246, 611)), #54 #18/10
# #                  list(range(100, 500)), #54 #20/10
# #                  list(range(112, 691)), #54 24/10
# # ]

# # ###50hz stim
# # eids = ['e93d6e9b-80c2-449f-860d-4fb59567914b', #54 3/10
# #         # '2cbd0ae3-69e0-4586-9de2-a68dca14f878', #54 5/10 #low baseline bias
# #         'e9e44d2d-b15c-46be-8442-dd2dda5d5723', #54 6/10
# #         #'3daacb5c-9de8-4434-a3bb-269e0adb034f', #54 10/10 no baseline bias?
# #         '2439b61f-83ca-48e0-af89-3d701fb74b76', #54 19/10
# #         # '58f72a9f-471a-4889-a986-49edf7732fc9', #54 20/10
# #         '8424a850-ba6e-42a4-8731-c5f2cbc38833', #54 23/10
# #         'd1b1cf5a-c68d-416a-9a92-b3a77f5145f6', #38, 15/6 (50hz)
# #         'f29f284d-2cf9-42ac-8a71-24c2d4a2d241', #38, 3/7 (50hz)
# #         'a5b427bf-e4ae-428d-8955-b2bfa534011b', #38, 21/7 (50hz)
# #         '33326079-f197-4dea-a319-b3377dd2996e', #38, 24/7 (50hz) ALF OBJECT NOT FOUND
# #         # '7a898aeb-e6d0-4241-9bdd-e593720fbb3c', #38, 26/7 (bias still appears to be there)
# #         # 'aa645856-a18c-4564-a046-0d8793404106', #38 4/8
# # ]
    
# # trials_ranges = [list(range(90, 862)), #54 3/10
# #                 #  list(range(90, 799)), #54 5/10 need to check when laser on
# #                  list(range(200, 1116)), #54 6/10 need to check when laser on
# #                  #list(range(90, 658)), #54 10/10
# #                  list(range(119, 887)), #54 19/10
# #                 #  list(range(500, 851)), #54 20/10
# #                  list(range(205, 663)), #54 23/10
# #                  list(range(102, 555)), #38, 15/6 (50hz)
# #                  list(range(90, 450)), #38, 27/6 (50hz)
# #                  list(range(90, 597)), #38, 21/7 (50hz)
# #                  list(range(126, 562)), #38, 24/7 (50hz)
# #                 #  list(range(113, 457)), #38, 26/7 (bias still appears to be there)
# #                 #  list(range(103, 539)), #38, 4/8
# # ]


# ##################################################
# ################# D2 Manipulation ################
# ######## 42

# # # 0hz stim, bilateral
# # eids = ['d0d3ac54-9986-47c5-a76c-14085134afd9', #42, 31/5
# #         '779182c1-64c8-431f-87dd-b23964232795', #42, 30/5
# #         'b0734d14-c1c0-4291-94e6-96a5f7d7d86a' #42, 26/5
# # ]
# # trials_ranges = [list(range(90, 758)), #42, 31/5
# #                  list(range(95, 700)), #42, 30/5
# #                  list(range(111, 623)) #42, 26/5
# # ]

# # ### 20hz stim, Left hemisphere
# # eids = ['d3542e8b-c171-4e20-bbaf-d6487785e9f5' #42 9/6, no effect
# # ]
# # trials_ranges = [list(range(123, 654)) #42 9/6
# # ]

# # ### 20hz stim, Right hemisphere
# # eids = ['947bf043-ff1d-4dc7-8db3-ec05164ccfb7' #42 8/6, no effect
# # ]
# # trials_ranges = [list(range(98, 640)) #42 8/6
# # ]

# # ### 20hz stim, bilateral
# # eids = ['38dd63f0-297b-44a8-b469-2c16c76461ac', #42 2/6
# #         '84911885-3efa-4398-a699-4805b3ad9a93', #42 1/6
# #         'e7c61b0e-b713-480f-8acc-0f480620f895', #42 7/6 performance borderline
# #         '63e2a4ae-80c3-4a87-8bee-64e4f604e389' #42 6/6
# # ]
# # trials_ranges = [list(range(148, 621)), #42 2/6
# #                  list(range(120, 645)), #42 1/6
# #                  list(range(158, 499)), #42 7/6
# #                  list(range(161, 598)) #42 6/6
# # ]

# ######## 43 ###########

# ### 50hz stim, bilateral

# # eids = ['eee1e6d6-4ab7-4a17-860e-209f1cf2ca31', #10/8
# #         'a0343dc0-911a-4ba8-a968-105274075537', #14/8
# #         '380311ce-5021-412d-b9d7-d2f1e048ec63', #15/8
# #         'ca498612-10c7-4921-b394-87259e6ca735', #11/9 wonky and slightly below threshold
# #         # '949ffb0c-a81a-49ea-a5c8-b0f50400e955', #8/8 unilateral L, no obvs effect
# #         'a775f6d4-d83e-4ef4-ae98-8a72a79d6517', #9/8 unilateral R
# #         '336a7390-5f64-4217-a9ba-832083f1cb16', #14/9
# # ]
        
# # trials_ranges = [list(range(122, 696)), #10/8
# #                  list(range(169, 737)), #10/8
# #                  list(range(98, 657)), #15/8
# #                  list(range(146, 815)), #11/9
# #                 #  list(range(172, 378)), #8/8
# #                  list(range(127, 534)), #11/9
# #                  list(range(103, 523)), #14/9
# # ]


# ########################################
# ################# ORBvl ################
# ######## 40

# # *ADAL may be broken...

# # ### L
# # eids = ['f7ead6ad-f280-4e5d-b55f-9ae1e228616e', #40 3/5*
# #         'bee5a4ce-334a-4c0d-afaf-df409ab9fe5f','e312f463-f684-45cd-940b-ec7a093134f9'] #40 24/4 (low bias all trials), 20/4 (low bias R trials)
# # trials_ranges = [list(range(90, 1018)), #40 3/5*
# #                  list(range(90, 805)),list(range(90, 1418))] #40 24/4 (low bias all trials), 20/4 (low bias R trials)

# ### R
# # eids = ['977f085d-32a3-4f24-ac0b-dadce0fdf899','54196e48-a045-427e-8239-b68a196a857b', #40 19/4, 25/4
# #         # 'cffe2f00-e990-4f67-894e-4397561d5ca3', #40 2/5* (below threshold perf)
# #         '793529c3-c0e1-4243-81f9-9155b68b8e73'] #40 5/5*
# # trials_ranges = [list(range(293, 1253)),list(range(90, 929)), #40 19/4, 25/4
# #                 #  list(range(90, 797)), #40 2/5* (below threshold perf)
# #                  list(range(90, 556))] #40 5/5*
# # ### little effect. maybe reduction in R bias?

# # ## bilateral
# # eids = ['df8929c5-b954-41b7-991d-8ccccde7af3f','7ba551e4-010b-46e3-b5da-47e6ea9c6f6b', #40 21/4, 26/4 (no effect?)
# #         #'1c669152-2447-4efe-add9-f5dc59c126bd', #40 10/5 (stimOn to exit state; seizure around 280),
# #         '85e73183-649a-46b5-a7da-34a1a783b9d0', #28/4 (no bias in all trials)
# #         '24ab6988-61cd-449c-a123-663b0322387a'] #40 27/4 (no bias in all trials)
# #         # '048e5b8d-6176-41b3-8c74-ed6690f2626f' #40 9/5 below threshold; switch from 50hz to continuous
# # trials_ranges = [list(range(90, 818)),list(range(90, 624)), #40 21/4, 26/4 (no effect?)
# #                 #  list(range(90, 352)),  #40 10/5 (stimOn to exit state; seizure around 280),
# #                  list(range(90, 969)), #40 28/4
# #                  list(range(90, 969))] #40 27/4
# #                 #  list(range(330, 750)) #40 9/5 below threshold; switch from 50hz to continuous

# ### NO stim
# # eids = ['776f1bd6-fb02-47c3-8614-a94772ebed73','28ccaeaf-b459-473e-b679-8c82ce4d6e2d'] #40 12/5, 11/5
# # trials_ranges = [list(range(90, 550)),list(range(90, 747))] #40 12/5, 11/5


# # # # On continuously (ie, 100% trials)
# # # Bilateral 20hz
# # eids_stim = ['c9d1c66b-4dfb-4200-8065-49d4b20dfb90', #40 30/5
# #         '26e73d77-98e4-491a-8331-c5d00d88ac5c', #40 31/5
# #         'd77556ee-5343-48ec-a41b-3e9868694dca', #40 26/5
# #         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
# #         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
# #         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
# #         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
# #         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
# #         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
# #         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
# #         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
# #         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
# #         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
# #         'f3816e25-61b7-4389-a67c-6a58a0608c90' #40 2/6
# # ]
# # trials_ranges_stim = [list(range(319, 738)), #40 30/5
# #                  list(range(100, 408)), #40 31/5
# #                  list(range(300, 641)), #40 26/5
# #                  list(range(215, 320)), #40 25/5
# #                  list(range(485, 634)), #40 25/5
# #                  list(range(397, 540)), #40 23/5
# #                  list(range(637, 765)), #40 23/5
# #                  list(range(220, 281)), #40 22/5
# #                  list(range(360, 461)), #40 22/5
# #                  list(range(560, 661)), #40 22/5
# #                  list(range(860, 908)), #40 22/5
# #                  list(range(225, 308)), #40 19/5
# #                  list(range(333, 499)), #40 19/5
# #                  list(range(363, 709)) #40 2/6
# # ]

# # ## Control 
# # eids_ctrl = ['c9d1c66b-4dfb-4200-8065-49d4b20dfb90', #40 30/5
# #         'd77556ee-5343-48ec-a41b-3e9868694dca', #40 26/5
# #         '24eb1215-799b-48ae-ba6e-d103959154eb', #40 25/5
# #         '48517348-c8cc-465c-9c66-5b7de8a653cb', #40 24/5 (only 297 trials)
# #         '61360604-ea02-4b23-bfa5-595be5dbb1db', #40 23/5
# #         'e8f9bf8e-362e-45ab-88f3-37b8428c3540', #40 22/5
# #         'd305053f-c344-4179-ae91-824d6fc1bd65', #40 19/5
# #         'f3816e25-61b7-4389-a67c-6a58a0608c90', #40 2/6
# #         'd18e332a-bc0f-4ad1-b29c-cd26f79fdacd' #40 1/6 (no stim)
# # ]
# # trials_ranges_ctrl = [list(range(90, 319)), #40 30/5
# #                  list(range(90, 300)), #40 26/5
# #                  list(range(90, 215)),# + list(range(320, 485)), #40 25/5
# #                  list(range(90, 297)), #40 24/5 (only 297 trials)
# #                  list(range(90, 397)),# + list(range(540, 637)) + list(range(765, 931)), #40 23/5
# #                  list(range(90, 220)),# + list(range(281, 360)) + list(range(461, 560)) + list(range(661, 860)), #40 22/5
# #                  list(range(90, 225)), #40 19/5
# #                  list(range(90, 363)), #40 2/6
# #                  list(range(90, 426)) #40 2/6
# # ]

# ########################################
# ################# PL ###################
# ######## 41

# # ### Bilateral
# # eids = [#'373a293b-13f7-4c96-9dfb-f7e1fabacc2a', #41, 22/6, still has bias...
# #         # '07cbf3ee-2d6b-4ed7-92a1-2e7715bdad60', #41 28/6 (no effect)
# #         '50d1b073-b247-4da2-99c1-46ae401c50b9', #41 29/6
# #         'dcb26eac-7329-4f06-8d6a-ee20cc43abb2', #41 30/6 (50hz)
# #         '35359ed9-98f2-4b13-a4c6-2d252f127bf4', #41 3/7 (50hz)
# #         '2fc8c951-e2f6-4541-a2bc-dd57d32bd8cf', #41 4/7 (50hz)
# #         '7881b2ce-21ef-4c9c-b466-425f9188e41a', #41 5/7 (0hz)
# #         '516116c0-6686-4f65-bfaf-d27b5512ac22', #41, 13/7 (50hz; borderline perf., might be better if cutoff later trials)
# #         '20a6ebda-af15-47e9-a6aa-6eaec63eebed', #41, 14/7 (50hz)
# #         '61ce5f3b-715e-4c93-a52e-cb087c3927f1', #41, 17/7 (50hz)
# #         'aacaac80-4af2-4e70-a672-5f0b9ac680b4', #41, 21/7 (50hz)
# #         # '1e3e8e66-761c-41fa-b919-020c0ab3f6f9', #41, 27/7 (50hz) slightly below threshold perf.
# #         '3391096e-3d56-4cf0-8034-fb045003c92a', #41 31/7 (50hz) bias still there
# #         'e41d31fa-47be-4d18-a28a-4306be9a5095', #41 1/8 (50hz) bias still there
# # ]

# # trials_ranges = [#list(range(90, 804)), #41 22/6
# #                 #  list(range(90, 711)), #41 28/6 (no effect)
# #                  list(range(90, 936)), #41 29/6
# #                  list(range(219, 773)), #41 30/6 (50hz)
# #                  list(range(90, 750)), #41 3/7 (50hz)
# #                  list(range(90, 806)), #41 4/7 (50hz)
# #                  list(range(90, 1079)), #41 5/7 (0hz)
# #                  list(range(90, 638)), #41, 13/7 (50hz; borderline perf., might be better if cutoff later trials)
# #                  list(range(90, 536)), #41, 14/7 (50hz)
# #                  list(range(90, 880)), #41, 17/7 (50hz)
# #                  list(range(90, 630)), #41, 21/7 (50hz)
# #                 #  list(range(131, 826)), #41, 27/7 (50hz)
# #                  list(range(90, 850)), #41 31/7
# #                  list(range(205, 705)), #41 1/8
# # ]

# # ##### unilateral Left
# # eids = ['d4a1314f-bea1-4403-8117-00b56246f9a6', #41, 19/7, 50hz L
# #         # '425b02e4-37be-4df5-9445-f70502018bdd', #41, 24/7 (50hz) ALF FILE NOT FOUND
# #         '659a83ac-a963-44d6-a59a-d913c995de73', #41, 26/7, 50hz L
# #         'ecd81518-3187-4044-8fb8-3da4f4efd806', #41, 28/7, 50hz L
# # ]

# # trials_ranges = [list(range(90, 824)), #41, 19/7, 50hz L
# #                 #  list(range(90, 'end')), #41, 24/7 (50hz) ALF FILE NOT FOUND
# #                  list(range(90, 655)), #41, 26/7, 50hz L
# #                  list(range(90, 902)), #41, 28/7, 50hz L
# # ]

# # ##### unilateral Right
# # eids = ['3fb3df4c-245c-4503-af0b-d432af3f7540', #41, 18/7, 50hz R
# #         '7732ba5c-0cce-4274-90e8-30a35593ee13', #41, 20/7, 50hz R
# #         'd19b00d5-559e-4e1d-b355-7252ae765e4a', #41, 25/7, 50hz R
# #         'e919ed8b-415b-4aab-a30e-d1f9261b6e48', #41, 2/8, 50hz R
# #         # 'd4a1314f-bea1-4403-8117-00b56246f9a6', #41, 19/7, 50hz L
# #         # '659a83ac-a963-44d6-a59a-d913c995de73', #41, 26/7, 50hz L
# #         # 'ecd81518-3187-4044-8fb8-3da4f4efd806', #41, 28/7, 50hz L
# # ]

# # trials_ranges = [list(range(90, 658)), #41, 18/7, 50hz R
# #                  list(range(90, 761)), #41, 20/7, 50hz R
# #                  list(range(90, 499)), #41, 25/7, 50hz R
# #                  list(range(90, 790)), #41, 2/8, 50hz R
# #                 #  list(range(90, 824)), #41, 19/7, 50hz L
# #                 #  list(range(90, 655)), #41, 26/7, 50hz L
# #                 #  list(range(90, 902)), #41, 28/7, 50hz L
# # ]

# # ######## 50
# # ### Bilateral
# # eids = ['3c079baa-b887-4c93-a63f-a3685119626b', #08/11
# #         'af93d8a2-4f50-4763-a925-68452bcf93c4', #09/11
# #         '8e88c5cd-3549-4731-96d8-94ccd553e67a', #10/11 - borderline ~80% on R side, but effect very strong
# #         '3e83d3f0-9b76-4c06-a62e-e27121c34c30', #13/11 - no effect?
# #         'df587223-66de-4948-a4b1-230b118eb510', #14/11 - no effect? trials+1 affected!
# #         'cf906e2b-0aa8-4398-9c51-b69287c07063', #16/11 - no effect
# #         'c2125631-6ebd-4425-9ac0-a71586332af4', #17/11 - no effect
# #         'c2125631-6ebd-4425-9ac0-a71586332af4', #20/11 - no effect?
# #         # 'f0bf6511-f3c3-4575-b1f0-ffff9d88f4db', #21/11 - Right hemi
# #         # '8d71dfd7-fab1-4b7a-88d1-a2b690b5ece0', #22/11 - Left hemi
# #         'c3bd608e-b9dc-43ab-b8a3-92b7f9f5f59a', #24/11 - no effect
# # ]

# # trials_ranges = [list(range(90, 1131)), #08/11
# #                  list(range(90, 812)), #09/11
# #                  list(range(90, 970)), #10/11
# #                  list(range(90, 599)), #13/11
# #                  list(range(100, 698)), #14/11
# #                  list(range(125, 948)), #16/11
# #                  list(range(160, 763)), #17/11
# #                  list(range(90, 658)), #20/11
# #                 #  list(range(90, 721)), #21/11
# #                 #  list(range(90, 1053)), #22/11
# #                  list(range(90, 704)), #24/11
# # ]

# ########################################
# ################# M2 ###################
# ######## 49


# # ## Bilateral
# # eids = ['f7f95217-287e-436b-9df4-9f6945b0e7ca', #49 13/7 (slightly below threshold performance); bias appears gone, but also gone in nonstim trials. Lower QP, higher RT
# #         # 'cc27a197-7556-4479-9764-9083efff6fd2', #49 14/7 (well-below threshold perf.; almost always turns left on stim trials; decreased RT??)
# #         # 'f328df1d-d736-455c-a09b-a55869cb8723', #49 17/7 (slightly below threshold performance); Lower QP, higher RT; poor performance, very right-biased (left-shifted on stim trials)
# #         ### #49 18/7 something weird going on here; only 515 trials, which doesn't make sense?
# #         '13da8dfb-2b47-47f4-8dea-d979b8969fb9', #49 20/7 R 50hz
# #         # '45a4f3a9-7e87-4267-a586-b197278b9d94', #49 21/7 L 50hz slightly below threshold performance
# #         'b872338e-baf4-408e-a1a2-6cc11cb825b8', #49 24/7 bilateral 50hz (left shifted perf, but still within threshold)
# #         'e70717a2-406b-4e80-8115-5bd8ef849bc1', #49 25/7 bilateral 50hz bias gone!
# #         # 'f50db341-bb52-4bb5-959a-4ae1679584cd', #49 26/7 bilateral (performance slightly below threshold)
# #         '8024753a-5726-472a-8cb7-3b5c534a35ad', #49 27/7 bilateral 50hz (left shifted perf, but still within threshold)
# #         '15eb9851-7b17-432e-8c1b-c35798232ec8', #49, 28/7, bilateral 50hz
# #         # 'af6163b6-1427-4d72-8c78-831d30fffe2f', #49, 31/7, bilateral 50hz, below threshold; mouse turns more left on stim trials
# #         '9d55cbc0-7f4c-4dcd-a3a8-525aeb39bca8', #49 01/8 bilateral 50hz
# #         '4a67a51b-dc8c-4216-afad-28f463078be4', #49, 10/8, bilateral
# # ]

# # trials_ranges = [list(range(227, 656)), #49 13/7 (slightly below threshold performance)
# #                 #  list(range(123, 655)), #49 14/7 (well-below threshold perf.; almost always turns left on stim trials; decreased RT??)
# #                 #  list(range(90, 350)), #49 17/7 (slightly below threshold performance)
# #                  ###
# #                  list(range(214, 808)), #49 20/7 R 50hz
# #                 #  list(range(191, 942)), #49 21/7 L 50hz slightly below threshold performance
# #                  list(range(145, 737)), #49 24/7 bilateral
# #                  list(range(92, 788)), #49 25/7 bilateral
# #                 #  list(range(353, 815)), #49 26/7 bilateral
# #                  list(range(110, 898)), #49 27/7 bilateral
# #                  list(range(90, 668)), #49 28/7 bilateral
# #                 #  list(range(90, 742)), #49, 31/7 bilateral
# #                  list(range(95, 785)), #49 01/8 bilateral 50hz
# #                  list(range(113, 660)), #49, 10/8, bilateral
# # ]


# # ## Unilateral
# # eids = ['13da8dfb-2b47-47f4-8dea-d979b8969fb9', #49 20/7 R 50hz
# #         '45a4f3a9-7e87-4267-a586-b197278b9d94', #49 21/7 L 50hz slightly below threshold performance
# #         '81368cca-beda-48f6-8c9b-a16bbe8c7ebf', #49 3/8 L 20hz borderline perf; little bias at baseline
# # ]

# # trials_ranges = [list(range(214, 808)), #49 20/7 R 50hz
# #                  list(range(191, 942)), #49 21/7 L 50hz slightly below threshold performance
# #                  list(range(90, 600)), #49 3/8 L
# # ]
# # #unilateral StimOn
# # '110aaffb-ab9e-4362-9f3b-7b1910a41d1a'
# # list(range(186, 361)) + list(range(597, 803)) #right

# # # ################### 51
# # eids = [#'26795a4a-c0dd-4423-87d2-6bfc6b03b528', #25/9
# #         'd23014c6-ea5a-4cc9-98bc-70916879ce7f', #26/9
# #         'a014ef1e-7710-40ac-afd4-0402f1e12a7c', #27/9 (10%)
# #         '3df2cc80-cdfa-47d0-bd36-863174255547', #2/10
# #         # '7b9b5248-4239-4e4b-bdf5-baa56c59c69d', #3/10 only 300 trials, perf. borderline
# #         'a1d962cc-4669-470b-af40-509a0d411268', #5/10
# #         '7f560157-d9d8-4ccd-94fb-5c3b55dad328', #6/10
# #         '83b50d6a-c88e-4454-b250-233a1d6a11e2', #10/10 very little baseline bias?
# #         '946686f5-b9aa-4303-acff-c6fa89a32bae', #16/10; great performance, no bias reduction
# #         '16c38a87-e4aa-4302-8f41-875191866786', #17/10; great performance, no bias reduction (maybe even an increase!)
# #         'e4ddae43-7dbc-4ae3-983d-358cd803d508', #18/10; slight bias reduction
# #         '31cf80ae-7ce4-47c6-896d-68d487a3392c', #19/10
# #         # 'b387890e-dedc-4a88-9b20-ccf379afbe1b', #24/10 left hemi (no effect)
# #         '76f534af-c133-4a30-8e2f-42f03d939fe2', #25/10 no effect
# #         '02a94670-7cbd-4014-a496-ae9470f8e9e0', #26/10 low baseline bias (though possibly an effect)
# #         # '322486ef-1d69-4d9f-8265-bf62953cb284', #27/10 no baseline bias
# #         '873b7120-fa34-4a86-9d68-31150ef7ee4c', #30/10 little/no baseline bias
# #         '86d8e1f4-de97-4cb6-9c26-373c1de977f6', #31/10 low baseline bias
# #         # '86d8e1f4-de97-4cb6-9c26-373c1de977f6', #02/11 borderline perf.; no baseline bias
# #         'e9bfb7ba-4ab4-4634-b782-e0d7c085986c', #6/11
# # ]

# # trials_ranges = [#list(range(94, 603)), #25/9
# #                  list(range(100, 783)), #26/9
# #                  list(range(90, 472)), #27/9
# #                  list(range(94, 639)), #2/10
# #                 #  list(range(90, 300)), #3/10
# #                  list(range(90, 712)), #5/10
# #                  list(range(90, 645)), #6/10 need to check when laser came on
# #                  list(range(90, 652)), #10/10
# #                  list(range(90, 701)), #16/10
# #                  list(range(90, 705)), #17/10
# #                  list(range(90, 871)), #18/10
# #                  list(range(90, 786)), #19/10
# #                 #  list(range('check trials')), #24/10
# #                  list(range(90, 535)), #25/10
# #                  list(range(90, 693)), #26/10
# #                 #  list(range(90, 558)), #27/10
# #                  list(range(90, 448)), #30/10
# #                  list(range(90, 498)), #31/10
# #                 #  list(range(100, 409)), #02/11
# #                  list(range(100, 667)), #6/11
# # ]



# ###################################################
# ### 039 (SNr)

# # # # Continuous L hemisphere
# eids = ['b8dea861-1d28-4db8-99fb-179bec03cede'] #39 21/4 (always left?? both RT and QP high??)
# trials_ranges = [list(range(90,757))] #39 21/4

# eids = ['ac4a1b85-ca72-4511-8ebf-7905aa563d10'] #39 20/4 (always right?? QP high but RT low??)
# trials_ranges = [list(range(90,899))] #39 20/4

# # # # 50hz L hemisphere
# eids = ['461bdbb0-a13e-42b8-abe2-62a067c97cca','235b71ac-0bd9-488d-8043-95486bd911d0', #39 28/4 (always right!; trials+1 bias gone!), 24/4
#         '3af5632f-e269-4b85-bcf4-c2be53cb05bb'] #39 19/4 (always right; trials+1 bias gone?)
# trials_ranges = [list(range(90,963)),list(range(90,597)), #39 28/4, 24/4
#                  list(range(90,716))] #39 19/4 (always right)

# # # # 50hz R hemisphere
# eids = ['1c49eb46-8b5e-4a6c-a1f1-1919a08a1cc3'] #39 25/4 (more typical SNr; always turns left)
# #       '8f553d3c-fa0d-4679-a2ea-1f41f1b34cce' #39 18/4 (same as others but below threshold)
# trials_ranges = [list(range(90,806))] #39 25/4 (more typical SNr; always turns left)
# #               list(range(90,740)) #39 18/4 (same as others but below threshold)

# # # # 50hz Bilateral
# eids = ['250f9fbf-b3c3-4e7e-95ac-871bcff5ad3d'] #39 26/4 (VERY long RT, yet ok performance??)
# trials_ranges = [list(range(90,433))] #39 26/4 (VERY long RT, yet ok performance??)

# ############### 44 (SNr) ###################

# eids = ['a0b60046-8e5e-49f1-9ced-cfcc337bbe94', #8/9
#         'a92b2424-b717-4cff-b5c5-9a59a776ac92', #11/9
#         'c2bb6692-5b1a-4b3e-87f1-3890d0aaecee', #12/9
#         '4bdc23e3-6f83-45c4-a7c1-9fb8fe9222a6', #13/9
#         '94788e46-bfd4-4001-98b7-58dac45814d9', #14/9
#         'd2662d15-f963-47f4-b5b9-14a43b79b049', #15/9 borderline perf.
#         '45dfee80-5e5a-4248-9a8c-15c17f4b127a', #20/9 below thresh but strong effect
#         '5c48d132-56c0-4ed3-a94f-230675a5743a', #22/9 
#         # 'dab39ad1-79a8-4782-868e-9f453a1b741a', #26/9 unilateral L (still strong bias)
#         # '36430bee-7242-458d-9823-b9644af95a15', #27/9 unilateral R (still strong bias)
# ]
# trials_ranges = [list(range(94,494)), #8/9
#                  list(range(90,601)), #11/9
#                  list(range(90,836)), #12/9
#                  list(range(169,793)), #13/9
#                  list(range(90,600)), #14/9
#                  list(range(90,868)), #15/9
#                  list(range(90,492)), #20/9
#                  list(range(114,694)), #22/9
#                 #  list(range(90,576)), #26/9
#                 #  list(range(90,808)), #27/9
# ]


# ########### 36
# ##### continuous

# ## On continuously (ie, 100% trials)
# # Bilateral 20hz
# # eids_stim = ['8da6bdde-bec9-4310-bf4e-a5817f54035b', #36 22/5
# #         '20938807-1be8-4a4b-ba8a-5d2d327e5f7b', #36 26/5
# #         'e7bc20be-4d5f-4e87-8c46-e139582f117e', #36 19/5
# #         'd2355102-58a5-47c8-a696-cab40c54a348', #36 23/5 (L hemi!)
# #         '7759d9f9-df87-4dd9-9406-a8d9c7f8a6a3', #36 24/5 (R hemi!)
# #         'e92b5990-6955-4524-9679-6008c1303ea4', #36 30/5
# #         '5d46b01b-2fdb-4075-999a-12af5e446b0a' #36 31/5
# # ]
# # trials_ranges_stim = [list(range(576, 809)), #36 22/5
# #                  list(range(379, 885)), #36 26/5
# #                  list(range(162, 265)) + list(range(308, 430)) + list(range(591, 638)), #36 19/5 (last 2 are continuous!)
# #                  list(range(250, 685)), #36 23/5 (L hemi!)
# #                  list(range(380, 550)), #36 24/5 (R hemi!)
# #                  list(range(439, 501)), #36 30/5
# #                  list(range(309, 444)) #36 31/5
# # ]

# # ## Control 
# # eids_ctrl = ['8da6bdde-bec9-4310-bf4e-a5817f54035b', #36 22/5
# #         # '49d29315-cd59-46f8-88c1-af07cca74a05', #36 18/5 performance likely below threshold
# #         '20938807-1be8-4a4b-ba8a-5d2d327e5f7b', #36 26/5
# #         'e7bc20be-4d5f-4e87-8c46-e139582f117e', #36 19/5
# #         'd2355102-58a5-47c8-a696-cab40c54a348', #36 23/5
# #         '7759d9f9-df87-4dd9-9406-a8d9c7f8a6a3', #36 24/5
# #         'e92b5990-6955-4524-9679-6008c1303ea4', #36 30/5
# #         '5d46b01b-2fdb-4075-999a-12af5e446b0a' #36 31/5
# # ]
# # trials_ranges_ctrl = [list(range(90, 576)), #36 22/5
# #                 #  list(range(90, 576)), #36 18/5
# #                 list(range(90, 379)), #36 26/5
# #                 list(range(90, 162)) + list(range(266, 308)) + list(range(431, 591)), #36 19/5
# #                 list(range(90, 250)), #36 23/5
# #                 list(range(90, 380)), #36 24/5
# #                 list(range(90, 439)), #36 30/5
# #                 list(range(90, 309)) #36 31/5
# # ]
