import pytest
import pandas as pd

@pytest.fixture
def sample_income_df():
    """Fixture for sample income DataFrame."""
    data = {
        'date': ['01-01-2023', '15-01-2023'],
        'description': ['Salary', 'Freelance'],
        'amount': [2000.0, 500.0]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_expense_df():
    """Fixture for sample expense DataFrame."""
    data = {
        'date': ['05-01-2023', '20-01-2023'],
        'description': ['Rent', 'Groceries'],
        'amount': [800.0, 150.0]
    }
    return pd.DataFrame(data)

def test_calculate_balance_no_expenses(sample_income_df):
    """Test balance calculation with income only and no expenses."""
    empty_expense_df = pd.DataFrame(columns=['date', 'description', 'amount'])
    result = calculate_and_display_balance(sample_income_df, empty_expense_df)
    assert result["total_income"] == 2500.0
    assert result["total_expenses"] == 0.0
    assert result["balance"] == 2500.0

def test_calculate_balance_no_income(sample_expense_df):
    """Test balance calculation with expenses only and no income."""
    empty_income_df = pd.DataFrame(columns=['date', 'description', 'amount'])
    result = calculate_and_display_balance(empty_income_df, sample_expense_df)
    assert result["total_income"] == 0.0
    assert result["total_expenses"] == 950.0
    assert result["balance"] == -950.0

def test_calculate_balance_with_income_and_expenses(sample_income_df, sample_expense_df):
    """Test balance calculation with both income and expenses."""
    result = calculate_and_display_balance(sample_income_df, sample_expense_df)
    assert result["total_income"] == 2500.0
    assert result["total_expenses"] == 950.0
    assert result["balance"] == 1550.0
