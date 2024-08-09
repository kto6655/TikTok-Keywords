## Welcome to the TikTok-Keywords application!
This application is sourcing public data available on the TikTok Creative Center website. It scrapes HTML data from the first page of results on the 'Keyword Insights' page, which displays the top 20 trending keywords performing in paid ads on TikTok in the United States in the Last 7 Days. This application enables users to deliver: (1) a data visualization of the top 20 keywords by number of impressions in the form of a bar chart, and (2) an HTML-formatted email via SendGrid to recipient that includes a data table of the top 20 keywords and their associated performance metrics.   

# Instructions for Local Development

## SET UP

### Create ['tiktok'] virtual environment:

```sh
conda create -n tiktok python=3.11
```

### Activate ['tiktok] virutal environment:

```sh
conda activate tiktok
```

### Install packages:

```sh
pip install -r requirements.txt
```

### Confirm installed packages match requirements.txt file:

```sh
pip list
```

### SendGrid Set Up Requirements:  
    1. Create account
    2. Activate Single Sender Verification
    3. Obtain SENDGRID_API_KEY and SENDGRID_SENDER_ADDRESS
    4. Create .env file in the root of your respository including your credentials

    ```sh
    SENDGRID_API_KEY="___________"
    SENDGRID_SENDER_ADDRESS="___________"
    ```

## USAGE

### Create top trending keywords bar chart by running "app/chart.py" report:

```sh
python -m app.chart
```

### Send email to recipient of top trending keywords by running "app/email.py" report:

```sh
python -m app.email
```

## TESTING

### Run "test/chart_test.py" report to validate imported HTML data from TikTok: 
    1. Confirm final formatted data table ("email_table") format is a DataFrame
    2. Confirm there are 20 rows (representing the top 20 keywords)
    3. Confirm the 5 columns of data are included: keyword, impression, like, share, comment

```sh
pytest
```

