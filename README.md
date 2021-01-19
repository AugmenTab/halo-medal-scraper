# Halo Medal Scraper

## Overview

This was a small project I did just after completing my first Python course, ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart. It goes through the [Halopedia](https://www.halopedia.org/) website and retrieves information on each of the multiplayer and campaign medals from the mainline Halo games, which gets recorded in an Excel spreadsheet. It then downloads an image of that medal and saves it locally with a specific file name, organized into folders by game. Update messages are printed to the console to report on progress as games are completed, and a timer runs in the background, keeping track of how long it takes to run the program from start to finish.

### Uses

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to traverse the Halopedia site.
* [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) is used to read and write to Excel files.
