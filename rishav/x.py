import random
import webbrowser
import random

lines = open(r"C:\Users\ASUS\OneDrive\Desktop\mini_project\url.txt").read().splitlines()
url =random.choice(lines)
webbrowser.open_new(url)