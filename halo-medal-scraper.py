#! python3

import os, openpyxl, bs4, requests, selenium
wb = openpyxl.load_workbook('medal-list.xlsx')

gameList = [
    {
        'game': 'halo3-campaign', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table:nth-child(15)'
    },
    {
        'game': 'halo3-gmp',
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table:nth-child(7)'
    },
    {
        'game': 'halo3-omp',
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table:nth-child(9)'
    },
    {
        'game': 'odst', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table:nth-child(13)'
    },
    {
        'game': 'reach', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Reach_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table:nth-child(6)'
    },
    {
        'game': 'halo4', 
        'url': 'https://www.halopedia.org/List_of_Halo_4_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table'
    },
    {
        'game': 'spartan-assault', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Assault_Medals',
        'selector': '#mw-content-text > table:nth-child(2) > tbody > tr > td > div > table'
    },
    {
        'game': 'spartan-strike', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Strike_Medals',
        'selector': '#mw-content-text > table > tbody > tr > td > div > table'
    }
]

test = [
    {
        'game': 'halo3', 
        'url': 'https://www.halopedia.org/List_of_Halo_3_and_Halo_3:_ODST_Medals',
        'selector': '#mw-content-text > table table tbody'
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
    if res.raise_for_status(): # This may be an exception on its own.
        raise Exception('The web fetch request failed.') 
    else:
        return bs4.BeautifulSoup(res.text, 'html.parser')

def getElems(game, res):
    elems = res.select(game['selector'])
    print(elems[3])

#TODO: Range over table on URL page.
#TODO: For each table row:
    #TODO: Collect name and win condition, then append to Excel file.
        # Make sure to ignore section headers.
    #TODO: Navigate to image page, download image, and record file name.
    #TODO: Add name to correct line on Excel file.
    #TODO: Log any missing medal images on separate sheet by game and medal name.
    #TODO: Mark each game done when complete on checklist page.

def scrapeMedals(games):
    for game in games:
        #makeFolder(game['game'])
        #makeSheets(game['game'])
        getElems(game, getSoup(game['url']))

if __name__ == "__main__":
    scrapeMedals(test) #switch to gameList when complete