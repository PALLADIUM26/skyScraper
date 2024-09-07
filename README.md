# skyScraper

This is like a side-quest for something big.

## This project consists of codes for:
<ol>
  <li>Searching through google using Python</li>
  <li>Websraping using Python</li>
  <li>Summarizing paragraph using Gemini API</li>
</ol>
<br>

### 1. Contents of <a href="https://github.com/PALLADIUM26/skyScraper/blob/main/SearchAndWebscraping.ipynb">SearchAndWebscraping.ipynb</a><br>
 - Import libraries for using `Google`
 - Searching according to some keyword
 - Search according to user input
 - Search according to some keyword and provide number links given by user
 - Remaining parts are related to websraping which will be discussed in the following section
 
### 2. Contents of <a href="https://github.com/PALLADIUM26/skyScraper/blob/main/WebscrapingAndSummarizing.ipynb">WebscrapingAndSummarizing.ipynb</a><br>
 - Import libraries for `webscraping`
 - Get link through google with user given input
 - Send an `HTTP` request to the URL of the webpage you want to access
 - Parse the `HTML` content using `BeautifulSoup`
 - Extract the text content of the webpage
 - Print the text

### 3. Contents of <a href="https://github.com/PALLADIUM26/skyScraper/blob/main/Webscraping.ipynb">Webscraping.ipynb</a>
 - Import libraries for using `Gemini API`
 - Securely store your API key
 - Fetch an environment variable for `API key`
 - Load model `Gemini-Pro`
 - Search according to input given by user
 - Perform webscraping
 - Summarize the extracted text and display

### 4. Contents of <a href="https://github.com/PALLADIUM26/skyScraper/blob/main/websraper.py">websraper.py</a>
 - Import libraries
 - Open webpage in default browser
 - Wait so that webpage is fully loaded
 - Use shortkeys for select all and copy automatically
 - Store copied content from clipboard in a variable

<br>

## Import Libraries:
```
pip install -r requirements.txt
```
<br>

## `.py` files are also provided
