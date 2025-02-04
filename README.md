# Speelvoorzieningen Kosten Dashboard

An interactive dashboard for visualizing playground equipment costs and maintenance data.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Deploy directly from your GitHub repository

### Option 2: Heroku

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Deploy:
```bash
git push heroku main
```

## Data

The dashboard uses data from `playground_costs.csv` which contains information about:
- Asset types and quantities
- Inspection costs
- Maintenance costs
- Technical lifespan
- Exploitation budgets
