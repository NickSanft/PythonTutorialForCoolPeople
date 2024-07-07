import bs4

raw_html = "<!DOCTYPE html><html><body><h1>Wow</h1><p>Who</p></body></html>"
print("Raw HTML:")
print(raw_html)

bs = bs4.BeautifulSoup(raw_html, 'html.parser')

print("Pretty HTML")
print(type(bs))
print(bs.prettify())

"""
You got it running!

Do you see that odd part on line 7? BeautifulSoup is not actually a function but instead an Object. 

We will talk about that next!
"""