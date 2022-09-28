## CSV
import pandas as pd

url='https://raw.githubusercontent.com/mariolpantunes/powerbi/main/datasets/stock_prices.csv'
df = pd.read_csv(url)

## JSON
import pandas as pd

url='https://raw.githubusercontent.com/mariolpantunes/powerbi/main/datasets/stock_prices.json'
df = pd.read_json(url)

## XLSX
import pandas as pd

url='https://raw.githubusercontent.com/mariolpantunes/powerbi/main/datasets/stock_prices.xlsx'
df = pd.read_excel(url)

## Custom dataframe
import pandas as pd
  
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

## Web Scrapping
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)'
simpsons = pd.read_html(url)
df = simpsons[0]