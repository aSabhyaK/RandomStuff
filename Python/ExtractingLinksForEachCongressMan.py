from bs4 import BeautifulSoup;

url = "D:/personal/python/test/43-congress.html";
soup = BeautifulSoup (open(url));

links = soup.find_all('a');
count = 0;
for link in links:
    print(link);
    count += 1;
    
print("count", count);