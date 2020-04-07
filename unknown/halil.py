from bs4 import BeautifulSoup


html_source = ""
with open("source.html", "r") as html:
    html_source = html.read()

soup = BeautifulSoup(html_source, 'html.parser')
article = soup.find("div", {"id": "articlecontentonly"})

item = {"h2": "", "p": []}
list_item = []
first_h2 = False

for i in article:
    if i.name == "h2" and not first_h2:
        first_h2 = True
        item["h2"] = i.text
    elif i.name == "h2" and first_h2:
        list_item.append(item)
        item = {"h2": i.text, "p": []}
        import pdb; pdb.set_trace()
    
    if i.name == "p" and first_h2:
        item["p"].append(i.text)
