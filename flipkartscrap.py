from bs4 import BeautifulSoup
import requests
import os

url = "https://www.flipkart.com/"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

# print(soup)

title = soup.select("title")
# print("title:-", title[0].text)

# *****Link Tag Links*****
link_tag = soup.find_all('link');

# print(len(link_tag))

link_tag_list = []

for link in link_tag:
    link_tag_list.append(link)

# print("link_tag_list:- ", link_tag_list)

path = r"C:\Users\acer\PycharmProjects\webScraping\flipkart_scrap_data"
filename = "links.txt"

str_list = []

with open(os.path.join(path, filename), "w") as f:
    for link in link_tag_list:
        s = str(link)
        f.write("".join(s) + "\n")
    f.close()


# *****Meta tag*****
meta = soup.find_all("meta")
# print("meta:-", meta)
meta_tag_list = []


for m in meta:
    meta_tag_list.append(m)
# print(meta_tag_list)


# ***** writing meta tags to "meta.txt" file *****
with open("flipkart_scrap_data/meta.txt", "w") as meta_txt:
    for m in meta_tag_list:
        s = str(m)
        # print(m)
        meta_txt.write(s)
    meta_txt.close()


# *****select using CSS*****
select_div = soup.select("div", class_="_2JQgSY")
# print(select_div)

# *****select heading text of h2*****
h2 = soup.find_all("h2", class_="_2cAig-")
h2_set = set()
for heading in h2:
    h2_set.add(heading.text)

# print(h2_set)
# ***** writing h2 tags text to h2.txt file *****
with open("flipkart_scrap_data/h2.txt", "w") as h2_txt:
    for h2 in h2_set:
        s = str(h2)
        h2_txt.write("".join(s)+"\n");
        # print(s)
    h2_txt.close()


anchor = soup.find_all("a", class_='_3CuAg8')

anchor_tag_links = set()
for a in anchor:
    if a.text != "Homeopathy":
        link = "https://www.flipkart.com" + a.get("href")
        anchor_tag_links.add(link);
    if a.text == "Homeopathy":
        anchor_tag_links.add(a.get("href"))
# print(anchor_tag_links)

# ***** writing h2 tags text to h2.txt file *****
with open("flipkart_scrap_data/anchor.txt","w") as anchor_txt:
    for a in anchor_tag_links:
        s = str(a)
        anchor_txt.write("".join(s)+"\n")
        # print(s)
    anchor_txt.close()

image = soup.select("img", class_="_396cs4")
image_tag_src = set()
for i in image:
    image_tag_src.add(i.get("src"))

# for i in image_tag_src:
#     print(i)

# print(len(image))

if not os.path.isdir("flipkart_scrap_data"):
    os.mkdir("flipkart_scrap_data")

i = 1
for index, img_link in enumerate(image_tag_src):
    if i <= 10:
        img_data  = requests.get(img_link).content
        with open("flipkart_scrap_data/"+str(index+1)+".jpg", "wb+") as f:
            f.write(img_data)
            i+=1
        print(img_data)
    else:
        f.close()
        break
