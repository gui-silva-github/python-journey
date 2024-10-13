import pyshorteners

url = 'https://sites.google.com/guidoexcel/'

s = pyshorteners.Shortener()

shortUrl = s.tinyurl.short(url)
print(f"URL Encurtada: {shortUrl}")