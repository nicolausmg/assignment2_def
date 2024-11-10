import pandas as pd

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

    description = input("Enter a description for the income: ").strip()
    amount = float(input("Enter the income amount (Negative if it is an expense): ").strip())
    category = input("Enter the category for the income: ").strip()

    new_income = pd.DataFrame({'date': [date], 'description': [description], 'amount': [amount], 'category': 
[category]})
    return pd.concat([income_df, new_income], ignore_index=True)
