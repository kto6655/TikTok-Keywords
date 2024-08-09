# Welcome to the "app/chart.py" file...

# Import the HTML data
import requests

tiktok_url = "https://ads.tiktok.com/business/creativecenter/keyword-insights/pc/en"

tiktok_raw_data = requests.get(tiktok_url)

tiktok_raw_data

# Translate the HTML data
from bs4 import BeautifulSoup

tiktok_soup = BeautifulSoup(tiktok_raw_data.text)

tiktok_soup

# Parse the HTML data

tiktok_parse = tiktok_soup.find("script", id="__NEXT_DATA__") 

# Convert to JSON format

import json

tiktok_json = json.loads(tiktok_parse.string)

# Parse JSON data

tiktok_keywords = tiktok_json["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["keywordList"]

# Convert JSON data into DataFrame

from pandas import DataFrame

keywords_df = DataFrame(tiktok_keywords)

keyword_summary = keywords_df[["keyword","impression","like","share","comment"]]

# Organize table for chart and email 

email_table = keyword_summary.sort_values(by=['impression'], ascending=[False])

# Create bar chart

from plotly.express import bar

bar(x=email_table["keyword"], y=email_table["impression"], title="Top 20 Keywords Trending on TikTok in the United States (Last 7 Days)",
    labels={"x":"Keyword", "y":"# of Impressions"})

