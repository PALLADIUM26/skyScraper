import webbrowser
import pyautogui
import time
import pyperclip

# webbrowser.open('https://archive.org/details/Deadpool-LivBs')  # open webpage in default browser
# webbrowser.open('https://github.com/PALLADIUM26')
webbrowser.open('https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/')
time.sleep(5) #wait for 5s so webpage is fully loaded
pyautogui.hotkey("ctrl", "a") #using shortcut keys for selecting content of webpage
pyautogui.hotkey("ctrl", "c") #using shortcut keys for copying content of webpage
x = pyperclip.paste() #pasting from clipboard in a variable
print(x) #print result in terminal
