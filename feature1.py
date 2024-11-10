import pandas as pd
import datetime

def initialize_df():
    """
    Initializes an empty DataFrame for tracking financial entries.
    """
    finance_log = pd.DataFrame(columns=['date', 'description', 'amount', 'category'])
    return finance_log

def add_income_entry(income_df):
    """
    Adds an income entry to the income DataFrame.

    Parameters:
    - income_df (pd.DataFrame): The DataFrame containing income records.

    Returns:
    - pd.DataFrame: Updated income DataFrame with the new entry added.
    """
    date = input("Enter the income date (DD-MM-YYYY): ").strip()
    try:
      datetime.datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
      print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
      return income_df

    description = input("Enter a description for the income: ").strip()
    if not description:
      raise ValueError("Invalid description. Description cannot be empty or just whitespace.")
      return income_df

    amount = float(input("Enter the income amount (Negative if it is an expense): ").strip())
    if not isinstance(amount, (int, float)):
      raise ValueError("Invalid amount. Income amount must be a positive number.")
      return income_df

    category = input("Enter the category for the income: ").strip()



    new_income = pd.DataFrame({'date': [date], 'description': [description], 'amount': [amount], 'category': [category]})
    return pd.concat([income_df, new_income], ignore_index=True)

