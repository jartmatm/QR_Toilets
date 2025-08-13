import pandas as pd


COLUMNAS_RENAME_BINS = {
    'Please type your name': 'Reporter Name',
    'Please select type of clean ': 'Report Type',
    'Comments ': 'Description',
    'Did you find any damaged or missing bins or liners?' : 'Damaged or Missing bins or liners',
    'Which platform are you currently working on?' : 'Platform',
    ' Did you notice any spills or mess around the bin area that required extra cleaning?' : 'Spill or mess around the bin',
    'Were bins stations emptied and replaced with a new liner?' : 'Were bins stations emptied and replaced with a new liner?temp'
    
}
COLUMNAS_RENAME_GRAFITTI = {
    'Who is reporting ? ': 'Reporter Company',
    'Please type your name ': 'Reporter Name',
    'What are you reporting ?': 'Status',
    'Please describe Graffiti': 'Description'
}
COLUMNAS_RENAME_SPILL = {
    'Who is reporting ? ': 'Reporter Company',
    'Please type your name ': 'Reporter Name',
    'What are you reporting ?': 'Report Type',
    'Please describe your response ': 'Description'
}
COLUMNAS_RENAME_TOILETS = {
    'Please type your name': 'Cleaner name',
    'Please Select': 'Gender bathroom',
    
}
COLUMNAS_RENAME_COMPACTOR = {
    'Please type your name':'Reporter Name'
}
COLUMNAS_ELIMINAR_GRAFITTI = ['Name', 'Email']
COLUMNAS_ELIMINAR_BINS = ['Name',
              'Email',
              'Were bins stations emptied and replaced with a new liner?temp',
              'Were bins stations emptied and replaced with a new liner?2',
              'Were bins stations emptied and replaced with a new liner?3',
              'Please list the bins you emptied3',
              'Please list the bins you emptied2',
              'Please list the bins you emptied4']
COLUMNAS_ELIMINAR_TOILETS = [
    'Email', 'I am ...', 'Handwash basin, bench, and mirrors cleaned as required ?',
    'Have toilet pans, toilet cubicles and urinals been check and spot clean ?',
    'Cleaning and disinfection of Urinals including flush buttons, Urinal treads?',
    'Have the floor been cleared or litter and spills mopped ?', 'Have the towel/paper bins been emptied ?',
    'Hand towel/ Toilet Paper/ Hand Soap fully restocked ?', 'Have graffiti, gum and cobwebs been removed as required ?',
    'Comments', 'Have the sharp dispensers been checked\xa0 ?', 'Name', 'Column', 'Cleaning Check', 'Guest Feedback',
    'Please Select2', 'Cleanliness of handwash basins and mirrors', 'Cleanliness of toilet cubicles', 'Cleanliness of floors',
    '\xa0Towel/paper bins clear', 'Hand Towel', 'Toilet Rolls', 'Hand Soap', 'Comments2'       
]
COLUMNAS_ELIMINAR_COMPACTOR = [
    'Email', 'Name', 'Last modified time', 'Comments or additional information'
]
BINS_DICT = {
    'All_Bins_Listed': 'All bins listed.',
    'Bin1_Collins_GW': 'Bin 1: Collins. General Waste (Red lid).',
    'Bin1_Collins_RW': 'Bin 1: Collins. Recycling Waste (Yellow lid).',
    'Bin2_BSB_GW': 'Bin 2: BSB. General Waste (Red lid).',
    'Bin2_BSB_RW': 'Bin 2: BSB. Recycling Waste (Yellow lid)',
    'Bin3_Vending_GW': 'Bin 3: Near vending machine. General Waste (Red lid).',
    'Bin3_Vending_RW': 'Bin 3: Near vending machine. Recycling Waste (Yellow lid).',
    'Bin4_End_GW': 'Bin 4: At the end. General Waste (Red lid).',
    'Bin4_End_RW': 'Bin 4:  At the end. Recycling Waste. (Yellow lid).',
    'Bin2_Zone1_GW': 'Bin 2: Services ramp to zone 1. General Waste (Red lid).',
    'Bin2_Zone1_RW': 'Bin 2: Services ramp to zone 1. Recycling Waste (Yellow lid).',
    'Bin2_Middle_GW': 'Bin 2: Middle. General Waste (Red lid).',
    'Bin2_Middle_RW': 'Bin 2: Middle. Recycling Waste (Yellow lid).',
    'Bin3_BSB_GW': 'Bin 3: BSB. General Waste (Red lid).',
    'Bin3_BSB_RW': 'Bin 3: BSB. Recycling Waste (Yellow lid).',
    'Bin4_Vending_GW': 'Bin 4:  Near vending machine. General Waste (Red lid).',
    'Bin4_Vending_RW': 'Bin 4:   Near vending machine. Recycling Waste. (Yellow lid).',
    'Bin5_End_GW': 'Bin 5: At the end. General Waste (Red lid).',
    'Bin5_End_RW': 'Bin 5: At the end. Recycling Waste. (Yellow lid).'
}

COLUMNS_TO_CAPITALIZE_BINS = ['Description', 'Reporter Name']
COLUMNS_TO_CAPITALIZE_SPILL = ['Status', 'Comments', 'Reporter Name']
COLUMNS_TO_CAPITALIZE_GRAFITTI = ['Reporter Name']

