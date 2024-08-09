# TikTok-Keywords

### SET UP

# Create virtual environment:

```sh
conda create -n tiktok python=3.11
```

# Activate tiktok environment:

```sh
conda activate tiktok
```

# Install packages:

```sh
pip install -r requirements.txt
```

# Confirm installed packages match requirements.txt file

```sh
pip list
```

# SendGrid Set Up Requirements:  
    1. Create account
    2. Activate Single Sender Verification
    3. Obtain SENDGRID_API_KEY and SENDGRID_SENDER_ADDRESS
    4. Create .env file in the root of your respository including your credentials

    ```sh
    SENDGRID_API_KEY="___________"
    SENDGRID_SENDER_ADDRESS="___________"
    ```

### USAGE

Create top trending keywords chart by running "app/chart.py" report:

```sh
python -m app.chart
```

Create email to sender of top trending keywords by running "app/email.py" report:

```sh
python -m app.email
```

### TESTING