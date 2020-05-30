#! python3

import os, openpyxl, bs4, requests

gameList = [
    {
        'game': 'halo3-campaign', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'i': 3
    },
    {
        'game': 'halo3-gmp',
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'i': 0
    },
    {
        'game': 'halo3-omp',
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'i': 1
    },
    {
        'game': 'odst', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'i': 2
    },
    {
        'game': 'reach', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Reach_Medals',
        'i': 0
    },
    {
        'game': 'halo4', 
        'url': 'https://www.halopedia.org/List_of_Halo_4_Medals',
        'i': 0
    },
    {
        'game': 'spartan-assault', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Assault_Medals',
        'i': 0
    },
    {
        'game': 'spartan-strike', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Strike_Medals',
        'i': 0
    }
]

test = [
    {
        'game': 'halo3', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'i': 3
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

def getSoup(link):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    res = requests.get(link, headers=headers)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'html.parser')

def getTable(game, res):
    elems = res.select('#mw-content-text > table table tbody')
    return elems[game['i']]

#TODO: Find all tr elements that contain td elements. For each qualifying tr:
    #TODO: Collect name and win condition, then append to Excel file.
    #TODO: Navigate to image page, download image, and record file name.
    #TODO: Add name to correct line on Excel file.
    #TODO: Log any missing medal images on separate sheet by game and medal name.
    #TODO: Mark each game done when complete on checklist page.

def scrapeMedals(games):
    global wb
    wb = openpyxl.load_workbook('medal-list.xlsx')
    for game in games:
        #makeFolder(game['game'])
        makeSheets(game['game'])
        #table = getTable(game, getSoup(game['url']))
    wb.save('medal-list.xlsx')
    wb.close()
    

if __name__ == "__main__":
    scrapeMedals(test) #switch to gameList when complete