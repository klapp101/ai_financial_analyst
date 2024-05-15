# ai_financial_analyst

This project is a web application that allows users to input a stock ticker symbol, select various stock indicators, and receive a visual representation of the stock's performance over time. The application leverages OpenAI's GPT-4o to provide detailed financial analysis based on the stock chart and additional financial metrics.

## Features

- Input a stock ticker symbol to retrieve historical data.
- Select stock indicators such as Close Price, Open Price, High Price, Low Price, and Volume.
- Generate a stock trend chart.
- Utilize GPT-4o for in-depth financial analysis of the stock and company.
- Display the analysis in a user-friendly format.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework in Python.
- **yfinance:** A Python library to fetch financial data.
- **Matplotlib:** A plotting library to create stock charts.
- **OpenAI's GPT-4o:** An advanced AI model for generating financial analysis.
- **HTML/CSS:** For structuring and styling the web application.

## Project Structure

- `app.py`: The main Flask application file that handles routing, data fetching, chart generation, and financial analysis.
- `templates/index.html`: The HTML template for the web application's user interface.
- `static/style.css`: The CSS file for styling the web application.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/klapp101/ai_financial_analyst.git
   cd ai_financial_analyst
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up OpenAI API key:**
   Create a `.env` file and have it look like the following:
   ```
   OPENAI_API_KEY='KEY_HERE'
   ```

6. **Run the Flask application:**
   ```bash
   flask run
   ```

7. **Open the application in your web browser:**
   Navigate to `http://127.0.0.1:5000` to access the web application.

## Usage

1. **Enter a Stock Ticker:**
   Input the stock ticker symbol (e.g., `META` for Meta Platforms, Inc.) in the provided text box.

2. **Select Indicators:**
   Choose the stock indicators you wish to analyze (Close Price, Open Price, High Price, Low Price, Volume).

3. **Generate Trend:**
   Click the "Get Trend" button to generate the stock trend chart and financial analysis.

4. **View Analysis:**
   The generated chart and detailed financial analysis will be displayed on the same page.

## Example

Here are some screenshots of the application in action:

### Stock Trends Form and Chart
![Stock Trends Form and Chart](https://cdn-images-1.medium.com/max/1600/1*tJdAbl5p2tMcUIRIuqiG0g.png)

### Financial Company & Chart Summary
![Financial Company & Chart Summary](https://cdn-images-1.medium.com/max/1600/1*jsan49mDWWIExqggJ3Brlg.png)

### Detailed Financial Analysis
![Detailed Financial Analysis](https://cdn-images-1.medium.com/max/1600/1*CBk-GXTRYB_kYvqhlYjovA.png)

### GPT-4o Analyst Recommendations and Insights
![GPT-4o Analyst Recommendations and Insights](https://cdn-images-1.medium.com/max/1600/1*Q6G-2AtNuirE6llzxcg5-g.png)

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Matplotlib](https://matplotlib.org/)
- [OpenAI](https://www.openai.com/)
