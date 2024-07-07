"""
Objective - Install the bs4 module and watch it make the HTML pretty

What if we want a module outside the standard?
Thankfully, Python comes with a installer for this called pip.

To install a module, you can install this by opening a terminal and running the command:
pip install [ModuleName]

in this case:

pip install bs4

In PyCharm, you can easily open the terminal at the bottom-left or by pressing Alt+F12.

Good luck!
"""

import bs4

raw_html = "<!DOCTYPE html><html><body><h1>Wow</h1><p>Who</p></body></html>"
print("Raw HTML:")
print(raw_html)

bs = bs4.BeautifulSoup(raw_html, 'html.parser')

print("Pretty HTML")
print(type(bs))
print(bs.prettify())
