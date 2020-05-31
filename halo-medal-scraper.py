#! python3

import os, openpyxl, bs4, requests, urllib

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
        'game': 'spartan-assault', 
        'url': 'https://www.halopedia.org/List_of_Halo:_Spartan_Assault_Medals',
        'i': 0
    }
]

def saveFile():
    wb.save('medal-list.xlsx')
    print('File saved.')

def makeFolder(gameName):
    dir = os.path.join('.', 'medals', str(gameName))
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir
    
def makeSheet(gameName):
    sheets = wb.sheetnames
    if gameName not in sheets:
        sheet = wb.create_sheet(gameName)
        sheet['A1'] = 'file name'
        sheet['B1'] = 'medal name'
        sheet['C1'] = 'requirement'
        saveFile()

def getSoup(link):
    res = requests.get(link)
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
    print('Logging medals for ' + game['game'] + '.')
    dir = makeFolder(game['game'])
    makeSheet(game['game'])
    for medal in medals:
        try:
            fileName = saveMedalPic(dir, medal.select('a')[0])
        except IndexError as e:
            fileName = 'No image.'
        try:
            logMedalInfo(game['game'], fileName, medal.select('td')[1].text.strip(), medal.select('td')[2].text.strip())
        except IndexError:
            continue
    markComplete(game['game'])

def saveMedalPic(dir, medal):
    fileName = medal.get('href')[6:]
    base = 'https://www.halopedia.org'
    soup = getSoup(urllib.parse.urljoin(base, medal.get('href')))
    imgLink = soup.select('#file > a > img')[0].get('src')
    res = requests.get(urllib.parse.urljoin(base, imgLink))
    res.raise_for_status()
    img = open(os.path.join(dir, fileName), 'wb')
    img.write(res.content)
    img.close()
    return fileName

def logMedalInfo(sheetName, fileName, medalName, requirement):
    sheet = wb[sheetName]
    row = (fileName, medalName, requirement)
    sheet.append(row)

def markComplete(gameName):
    sheet = wb['checklist']
    sheet.append([gameName])
    saveFile()
    print('All medals logged for ' + gameName + '.')

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
    scrapeMedals(test)