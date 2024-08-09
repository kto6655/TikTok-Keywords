# Welcome to the "app/email.py" file...

# Import SENDGRID_API_KEY credentials

import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDGRID_SENDER_ADDRESS = os.getenv("SENDGRID_SENDER_ADDRESS")

# Set up custom function for sending email

from sendgrid import SendGridAPIClient

from sendgrid.helpers.mail import Mail

def send_email_with_sendgrid(recipient_address=SENDGRID_SENDER_ADDRESS, 
                             subject="What's Trending on TikTok? Latest update inside!",
                             html_content= "See below for the Top 20 keywords trending on TikTok in the last 7 days in the United States!"):
    
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML CONTENT:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDGRID_SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
    
    return(response)

# Import keywords table from chart.py to place in body of email

from app.chart import email_table   # don't need this line in Colab; just locally

email_table_html = email_table.to_html(index=False)

weekly_email = f"""

    <img
        src="https://p16-cc-sg.tiktokcdn.com/tos-alisg-i-hdprqziq2y/7cbe81bcf0d3e1cce41a43f3c62e277a.png~tplv-hdprqziq2y-png.png"
        alt="tiktok creative center logo"
        height=100
    >

    <h1>Top 20 Keywords Trending in Paid Ads on TikTok in the United States (Last 7 Days)</h1>
    
    <html>
    <body>
        {email_table_html}
    <body>
    <html>

    <h3> About Trending TikTok Keywords:</h3>

    <ul>
        <li>The above table outlines the Top 20 trending keywords used in paid ad campaigns on TikTok in the United States in the Last 7 Days.
        <li>TikTok Creative Center publishes 'Keyword Insights' to showcase the performance of keywords in top-performing ads across a variety of measures of success.
        <li>Impressions are the number of times the ad has been displayed on screen. </li>
        <li>Likes, Shares, and Comments are indicators of content performance and engagement. </li>
        <li>A total of 500 keywords are extracted from voice-over, text overlay, and ad text across top-performing ads.</li>
        <li>At the link below, users can filter these keywords specifically by country, industry, objective, keyword type, and time period.</li>
    
    </ul>

    <h2>Want to learn more?</h2>
    
    <p>For more details about how trending keywords are showing up in TikTok videos in your e.g., country or industry today, click the link below:</p>
    
    <a href="https://ads.tiktok.com/business/creativecenter/keyword-insights/pc/en" target="_blank">Explore Keyword Insights at TikTok Creative Center</a>


    
    
    <p>Note: TikTok 'Keyword Insights' are approximated values, that should not be used as a benchmark for your ad campaigns. TikTok applies algorithms to keep accurate ranking order of performance while protecting business-sensitive data.</p>
"""

send_email_with_sendgrid(html_content=weekly_email)

