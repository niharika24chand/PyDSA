#operations using list and tuple
"""
my_list=[10,20,30,40,50]
my_tuple=(5,10,15,20,25)
list_slice=my_list[1:3]
tuple_slice=my_tuple[:2]
print("First element of the list: ", my_list[0])
print("Last element of the tuple: ",my_tuple[-1])
print(type(my_list))
print(type(my_tuple))
print("sliced list: ",list_slice)
print("sliced tuple: ",tuple_slice)
"""

#basic application
"""
import pandas as pd
data ={
    'Name':['Niharika', 'Khushi', 'Robin', 'Colt', 'Charlie'],
    'Age':[21, 21, 31, 27, 29],
    'Salary':[180000, 170000, 80000, 59000, 72000]
}
df = pd.DataFrame(data)  #DataFrame is used for tabular representation
high_earners = df[df['Salary'] > 75000]
# Reset the index and start it from 1
high_earners = high_earners.reset_index(drop=True)
high_earners.index += 1
print(high_earners)
"""

#Example of scraping a web page and retrieving for the headlines
import requests
from bs4 import BeautifulSoup

url = 'https://google.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h2')
 
for headline in headlines:
    print(headline.text)


"""Code Breakdown:
import requests: This line loads the requests library into your program. The requests library is used to fetch (download) the content of web pages from the internet.
from bs4 import BeautifulSoup: This imports the BeautifulSoup class from the bs4 library. BeautifulSoup helps you understand and work with the HTML content of a webpage.
url = 'https://google.com': This line stores the URL (web address) of the Google homepage in a variable called url.
response = requests.get(url): This sends a request to the server at the URL (https://google.com) and gets back the HTML content of the webpage. The response is saved in a variable called response.
soup = BeautifulSoup(response.text, 'html.parser'): The .text part of response gives the raw HTML of the webpage. This raw HTML is passed to BeautifulSoup, which processes and organizes it into a structured format (called a "parse tree").
'html.parser' tells BeautifulSoup to use Python's built-in HTML parser to read and understand the HTML.
headlines = soup.find_all('h2'): The find_all() method searches the structured HTML for all <h2> tags. These <h2> tags usually represent headings or subheadings on a webpage. The method collects all the <h2> tags into a list and saves it in the variable headlines.
for headline in headlines: This starts a loop to go through each <h2> tag in the headlines list, one at a time. The current <h2> tag in each loop is saved in the variable headline.
print(headline.text): The .text part extracts only the text content of the <h2> tag (removing any HTML formatting). This text is then printed to the screen.

What the Code Does (Simplified):
Fetches the content of the Google homepage. Uses BeautifulSoup to organize the HTML of the page into a structure you can work with. Searches for all the <h2> tags (headings) in the page. Prints the text of each heading (if any exist).
"""

