from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
import markdown2

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    
    info = stock.info if 'info' in dir(stock) else {}
    actions = stock.actions if 'actions' in dir(stock) else {}
    dividends = stock.dividends if 'dividends' in dir(stock) else {}
    splits = stock.splits if 'splits' in dir(stock) else {}
    
    income_stmt = stock.income_stmt if 'income_stmt' in dir(stock) else {}
    balance_sheet = stock.balance_sheet if 'balance_sheet' in dir(stock) else {}
    cashflow = stock.cashflow if 'cashflow' in dir(stock) else {}
    
    major_holders = stock.major_holders if 'major_holders' in dir(stock) else {}
    institutional_holders = stock.institutional_holders if 'institutional_holders' in dir(stock) else {}
    insider_transactions = stock.insider_transactions if 'insider_transactions' in dir(stock) else {}

    financials = {
        "hist": hist,
        "info": info,
        "actions": actions,
        "dividends": dividends,
        "splits": splits,
        "income_stmt": income_stmt,
        "balance_sheet": balance_sheet,
        "cashflow": cashflow,
        "major_holders": major_holders,
        "institutional_holders": institutional_holders,
        "insider_transactions": insider_transactions
    }
    
    return financials

def save_image(image_data, filename):
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(image_data))

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def plot_stock_data(hist, ticker, indicators):
    plt.switch_backend('Agg')  # Use the 'Agg' backend for non-GUI environments
    plt.figure(figsize=(10, 5))
    
    for indicator in indicators:
        plt.plot(hist[indicator], label=indicator)
    
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    save_image(plot_url, f'images/{ticker}_stock_plot.png')
    
    plt.close()
    return plot_url

def analyze_stock_image(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are a helpful financial stock analyst who provides insights on stock data."},
            {"role": "user", "content": [
                {"type": "text", "text": "Can you describe the chart below?"},
                {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
                }
            ]}
        ],
        temperature=0.0,
    )

    return response.choices[0].message.content

def generate_financial_analysis(chart_summary, financials):
    messages = [
        {"role": "system", "content": "You are a helpful financial analyst. Provide a detailed financial analysis based on the given chart summary and financial data. Make sure to give insights on the company's financial performance and to output using markdown format."},
        {"role": "user", "content": f"Chart Summary:\n{chart_summary}\n\nFinancial Data:\nInfo: {financials['info']}\nActions: {financials['actions']}\nDividends: {financials['dividends']}\nSplits: {financials['splits']}\nIncome Statement: {financials['income_stmt']}\nBalance Sheet: {financials['balance_sheet']}\nCash Flow: {financials['cashflow']}\nMajor Holders: {financials['major_holders']}\nInstitutional Holders: {financials['institutional_holders']}\nInsider Transactions: {financials['insider_transactions']}"}
    ]
    
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        temperature=0.0,
    )
    
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker = None
    indicators = ['Close']
    plot_url = None
    stock_data = {}
    analysis = None

    if request.method == 'POST':
        ticker = request.form['ticker']
        indicators = request.form.getlist('indicators') or ['Close']
        stock_data = fetch_stock_data(ticker)
        plot_url = plot_stock_data(stock_data['hist'], ticker, indicators)
        
        image_path = f'images/{ticker}_stock_plot.png'
        chart_summary = analyze_stock_image(image_path)
        raw_analysis = generate_financial_analysis(chart_summary, stock_data)
        analysis = markdown2.markdown(raw_analysis)

    return render_template('index.html', plot_url=plot_url, ticker=ticker, indicators=indicators, stock_data=stock_data, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
