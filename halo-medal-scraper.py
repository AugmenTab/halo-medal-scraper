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

def saveFile():
    wb.save('medal-list.xlsx')
    print('File saved.')

def makeFolder(gameName):
    dir = os.path.join('.', 'medals', str(gameName))
    if not os.path.exists(dir):
        os.mkdir(dir)
    
def makeSheet(gameName):
    sheets = wb.sheetnames
    if gameName not in sheets:
        sheet = wb.create_sheet(gameName)
        sheet['A1'] = 'file name'
        sheet['B1'] = 'medal name'
        sheet['C1'] = 'requirement'
        saveFile()

def getSoup(link):
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    res = requests.get(link, headers=headers)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'html.parser')

def getTable(game, res):
    elems = res.select('#mw-content-text > table table tbody')
    return elems[game['i']]

def getMedals(table):
    rows = table.select('tr')
    medals = []
    for row in rows:
        if row.find('td'):
            medals.append(row)
    return medals

def logMedals(game, medals):
    #makeFolder(game['game'])
    makeSheet(game['game'])
    test = 'test'
    for medal in medals:
        #function that saves the medal picture
        logMedalInfo(game['game'], test, medal.select('td')[1].text.strip(), medal.select('td')[2].text.strip())
    #print('All medals logged for ' + game['game'] + '.')
    #function that marks game complete on checklist page.

#TODO: Navigate to image page, download image, and return file name.
#def saveMedalPic(?)

#TODO: Append file name, medal name, and win condition in Excel sheet.
def logMedalInfo(sheetName, fileName, medalName, requirement):
    sheet = wb[sheetName]
    row = (fileName, medalName, requirement)
    sheet.append(row)

#TODO: Mark each game done when complete on checklist page.
#def markComplete(game)

#TODO: Get the "no medals" medal?

def scrapeMedals(games):
    global wb
    wb = openpyxl.load_workbook('medal-list.xlsx')
    for game in games:
        table = getTable(game, getSoup(game['url']))
        medals = getMedals(table)
        logMedals(game, medals)
    saveFile()
    wb.close()
    
if __name__ == "__main__":
    scrapeMedals(test) #switch to gameList when complete