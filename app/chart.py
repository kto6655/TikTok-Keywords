# Welcome to the "app/chart.py" file...

# IMPORTS:  Packages required to perform this application

import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame



# IMPORT HTML DATA
# Fetch the 'keywords' HTML data from TikTok website:

tiktok_url = "https://ads.tiktok.com/business/creativecenter/keyword-insights/pc/en"

tiktok_raw_data = requests.get(tiktok_url)



# Translate the HTML data using the BeautifulSoup pacakage:

tiktok_soup = BeautifulSoup(tiktok_raw_data.text, features="html.parser")



# Parse the HTML data and then convert to JSON format:

tiktok_parse = tiktok_soup.find("script", id="__NEXT_DATA__") 

tiktok_json = json.loads(tiktok_parse.string)



# Parse JSON data further:

tiktok_keywords = tiktok_json["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["keywordList"]



# Convert JSON data into DataFrame and format data table for Email delivery:

keywords_df = DataFrame(tiktok_keywords)

keyword_summary = keywords_df[["keyword","impression","like","share","comment"]]

email_table = keyword_summary.sort_values(by=['impression'], ascending=[False])



# [OPTIONAL DATA VIZ] Create bar chart of top keywords by number of impressions:

if __name__ == "__main__":

    from plotly.express import bar

    fig = bar(x=email_table["keyword"], y=email_table["impression"], title="Top 20 Keywords Trending in Paid Ads on TikTok in the United States (Last 7 Days)",
        labels={"x":"Keyword", "y":"# of Impressions"})

    fig.show()




