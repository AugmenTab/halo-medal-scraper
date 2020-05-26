


gameList = [
    ('halo3', 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals'),
    ('odst', 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals'),
    ('reach', 'https://www.halopedia.org/List_of_Halo:_Reach_Medals'),
    ('halo4', 'https://www.halopedia.org/List_of_Halo_4_Medals'),
    ('spartanassault', 'https://www.halopedia.org/List_of_Halo:_Spartan_Assault_Medals'),
    ('spartanstrike', 'https://www.halopedia.org/List_of_Halo:_Spartan_Strike_Medals')
]


#TODO: Check if folder matching game name exists, make one if not.
#TODO: Check if sheet on Excel file sheets, make one if not.
#TODO: Range over table on URL page.
#TODO: For each:
    #TODO: Collect name and win condition, then append to Excel file.
        # Make sure to ignore section headers.
    #TODO: Navigate to image page, download image, and record file name.
    #TODO: Add name to correct line on Excel file.