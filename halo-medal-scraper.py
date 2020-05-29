#! python3

import os, openpyxl
wb = openpyxl.load_workbook('medal-list.xlsx')

gameList = [
    {
        'game': 'halo3', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals'
    },
    {
        'game': 'odst', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals'},
    {
        'game': 'reach', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Reach_Medals'
    },
    {
        'game': 'halo4', 
        'url': 'https://www.halopedia.org/List_of_Halo_4_Medals'
    },
    {
        'game': 'spartan-assault', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Assault_Medals'
    },
    {
        'game': 'spartan-strike', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Strike_Medals'
    }
]

test = [
    {
        'game': 'halo3', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals'
    }
]

def makeFolder(gameName):
    dir = os.path.join('.', 'medals', str(gameName))
    if not os.path.exists(dir):
        os.mkdir(dir)
    
def makeSheets(gameName):
    sheets = wb.sheetnames
    if gameName not in sheets:
        wb.create_sheet(gameName)
        wb.save('medal-list.xlsx')

#TODO: Range over table on URL page.
#TODO: For each table row:
    #TODO: Collect name and win condition, then append to Excel file.
        # Make sure to ignore section headers.
    #TODO: Navigate to image page, download image, and record file name.
    #TODO: Add name to correct line on Excel file.


def scrapeMedals(games):
    for game in games:
        #makeFolder(game['game'])
        makeSheets(game['game'])


if __name__ == "__main__":
    scrapeMedals(test) #switch to gameList when complete