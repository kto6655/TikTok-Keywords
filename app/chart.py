# Welcome to the "app/chart.py" file...

# IMPORT PACKAGES

import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame
from plotly.express import bar

# FETCH DATA

def fetch_tiktok_data():
    
    # import HTML data
    tiktok_url = "https://ads.tiktok.com/business/creativecenter/keyword-insights/pc/en"
    tiktok_raw_data = requests.get(tiktok_url)

    # translate HTML data
    tiktok_soup = BeautifulSoup(tiktok_raw_data.text)

    # parse the HTML data
    tiktok_parse = tiktok_soup.find("script", id="__NEXT_DATA__") 

    # convert HTML data to JSON format
    tiktok_json = json.loads(tiktok_parse.string)

    # parse JSON data
    tiktok_keywords = tiktok_json["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["keywordList"]

    # convert JSON data into DataFrame
    keywords_df = DataFrame(tiktok_keywords)
    keyword_summary = keywords_df[["keyword","impression","like","share","comment"]]

    # sort table by impressions
    email_table = keyword_summary.sort_values(by=['impression'], ascending=[False])

fetch_tiktok_data

# CHART DATA

keyword_chart = bar(x=email_table["keyword"], y=email_table["impression"], 
    title="Top 20 Keywords Trending on TikTok in the United States (Last 7 Days)",
    labels={"x":"Keyword", "y":"# of Impressions"})

keyword_chart





