import requests
import pandas as pd
import streamlit as st

FMP_BASE_URL = "https://financialmodelingprep.com/api/"

def get_quarterly_income_statements(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/income-statement/{symbol.upper()}?period=quarter&limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df

def get_annual_income_statements(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/income-statement/{symbol.upper()}?limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df

def get_quarterly_balance_sheets(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/balance-sheet-statement/{symbol.upper()}?period=quarter&limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df

def get_annual_balance_sheets(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/balance-sheet-statement/{symbol.upper()}?limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df

def get_quarterly_cash_flows(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/cash-flow-statement/{symbol.upper()}?period=quarter&limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df

def get_annual_cash_flows(symbol, last, return_df):
    req_url = FMP_BASE_URL + f"/v3/cash-flow-statement/{symbol.upper()}?limit={last}&apikey={st.secrets['FMP_TOKEN']}"
    req = requests.get(req_url).json()

    if return_df == True:
        df = pd.DataFrame(req)
    else:
        df = req
    return df