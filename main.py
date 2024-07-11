import json
import sys
from openbb import obb
from indicators_config import indicators
from datetime import datetime
import warnings

# Suppressing a specific deprecation warning from the pandas library used within 'openbb'
warnings.filterwarnings("ignore", message="Series.__getitem__ treating keys as positions is deprecated", category=FutureWarning)

def get_stock_data(stock_symbol, start_date, end_date=None):
    """Retrieve historical stock data for a given symbol between start_date and end_date.
    If end_date is not provided, defaults to the current date.
    """
    if end_date is None:
        end_date = datetime.today().strftime('%Y-%m-%d')  # Set end_date to today if not specified
    try:
        # Fetch historical price data using the OpenBB library with yfinance as the provider
        return obb.equity.price.historical(
            symbol=stock_symbol,
            start_date=start_date,
            end_date=end_date,
            provider='yfinance'
        )
    except Exception as e:
        # Handle exceptions by logging error messages to stderr
        print(f"Error retrieving stock data: {e}", file=sys.stderr)
        return None

def calculate_indicator(stock_data, indicator):
    """Calculate the specified indicator using data from stock_data.
    Uses dynamic attribute access to call the appropriate function from 'openbb.technical'.
    """
    try:
        indicator_func = getattr(obb.technical, indicator['name'])
        indicator_data = indicator_func(data=stock_data.results, **indicator['params'])
        return indicator_data.results[-1:]
    except Exception as e:
        # Log any exceptions raised during the calculation
        print(f"Error calculating {indicator['name'].upper()}: {e}", file=sys.stderr)
        return []

def format_indicator_data(indicator_name, indicator_data, indicator):
    """Format the indicator data for output, extracting relevant keys from the raw data."""
    if not indicator_data:
        return []

    keys = indicator.get('keys', [indicator.get('value_key')])
    formatted_data = []
    current_date = datetime.today().strftime('%Y-%m-%d')

    for data in indicator_data:
        entry = {'date': getattr(data, 'date', current_date)}
        for key in keys:
            value = getattr(data, key, None)
            if value is not None and isinstance(value, str):
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep the value as string if it can't be converted to float
            entry[key] = value
        formatted_data.append(entry)

    return formatted_data



def get_last_10_days_data(stock_data, indicators):
    """Retrieve and format the last 10 days of indicator data for each indicator."""
    last_10_days_data = {}
    for indicator in indicators:
        try:
            indicator_data = calculate_indicator(stock_data, indicator)
            formatted_data = format_indicator_data(indicator['name'].upper(), indicator_data, indicator)
            last_10_days_data[indicator['name'].upper()] = formatted_data
        except Exception as e:
            # Log processing errors for each indicator
            print(f"Error processing indicator {indicator['name'].upper()}: {e}", file=sys.stderr)
            last_10_days_data[indicator['name'].upper()] = []
    return last_10_days_data

def save_pretty_json(data, filename):
    """Save data to a JSON file with pretty formatting. Useful for human-readable output."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Use indent=4 for pretty formatting
    except Exception as e:
        # Handle file I/O errors
        print(f"Error saving JSON data to file: {e}", file=sys.stderr)
        sys.exit(1)

def save_json_data(data, filename):
    """Save data to a JSON file in a compact format. Efficient for storage and transmission."""
    try:
        with open(filename, 'w') as file:
            file.write(json.dumps(data, separators=(',', ':')))
    except Exception as e:
        # Handle file I/O errors
        print(f"Error saving JSON data to file: {e}", file=sys.stderr)
        sys.exit(1)

def filter_indicators(data, indicators_to_include):
    """Filter the indicator data to only include specified indicators."""
    filtered_data = {k: v for k, v in data.items() if k in indicators_to_include}
    return filtered_data

if __name__ == "__main__":
    # Main execution block to run the script
    try:
        if len(sys.argv) < 2:
            # Ensure there is at least one command-line argument
            print("Please provide stock symbol as a command-line argument.", file=sys.stderr)
            sys.exit(1)

        stock_symbol = sys.argv[1]
        start_date = '2023-01-01'
        
        stock_data = get_stock_data(stock_symbol, start_date)
        if not stock_data:
            # Exit if no data could be retrieved
            sys.exit(1)

        last_10_days_data = get_last_10_days_data(stock_data, indicators)
        save_json_data(last_10_days_data, 'output.json')
        #save_pretty_json(last_10_days_data, 'output_pretty.json')
        # Filter and save the specific indicators
        # indicators_to_include = ['ADOSC', 'STOCH', 'RSI', 'MACD']  
        # filtered_data = filter_indicators(last_10_days_data, indicators_to_include)
        # save_json_data(filtered_data, 'aidata.json')
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
