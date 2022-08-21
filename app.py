import streamlit as st

from src import financials, charts

st.header("Visualize Financial Statements")

col1, col2, col3, col4 = st.columns(4)
with col1:
    ticker = st.text_input("Ticker: ", value="AAPL")
with col2:
    statement = st.selectbox("Statement: ", ["Income Statement", "Balance Sheet", "Cash Flow"])
with col3:
    reporting_type = st.selectbox("Reporting Type: ", ["Quarter", "Annual"])
with col4:
    last = st.number_input("Last ___ reports", min_value=4, max_value=40, step=1)

if ticker and statement and reporting_type and last:
    if statement == "Income Statement":
        st.header("Income Statements")
        if reporting_type == "Quarter":
            quarterly_is = financials.get_quarterly_income_statements(ticker, last, return_df=True)

            quarterly_is_names = quarterly_is.columns[8:]
            quarterly_included_data = st.multiselect("Ratios to include in chart: ", quarterly_is_names, default=quarterly_is_names[0])
            
            charts.plot_statements(quarterly_is, quarterly_included_data)
        else:
            annual_is = financials.get_annual_income_statements(ticker, last, return_df=True)

            annual_is_names = annual_is.columns[8:]
            annual_included_data = st.multiselect("Ratios to include in chart: ", annual_is_names, default=annual_is_names[0])

            charts.plot_statements(annual_is, annual_included_data)
    elif statement == "Balance Sheet":
        st.header("Balance Sheets")
        if reporting_type == "Quarter":
            quarterly_bs = financials.get_quarterly_balance_sheets(ticker, last, return_df=True)

            quarterly_bs_names = quarterly_bs.columns[8:]
            quarterly_included_data = st.multiselect("Ratios to include in chart: ", quarterly_bs_names, default=quarterly_bs_names[0])
            
            charts.plot_statements(quarterly_bs, quarterly_included_data)
        else:
            annual_bs = financials.get_annual_balance_sheets(ticker, last, return_df=True)

            annual_bs_names = annual_bs.columns[8:]
            annual_included_data = st.multiselect("Ratios to include in chart: ", annual_bs_names, default=annual_bs_names[0])

            charts.plot_statements(annual_bs, annual_included_data)
    else:
        st.header("Cash Flows")
        if reporting_type == "Quarter":
            quarterly_cf = financials.get_quarterly_cash_flows(ticker, last, return_df=True)

            quarterly_cf_names = quarterly_cf.columns[8:]
            quarterly_included_data = st.multiselect("Ratios to include in chart: ", quarterly_cf_names, default=quarterly_cf_names[0])
            
            charts.plot_statements(quarterly_cf, quarterly_included_data)
        else:
            annual_cf = financials.get_annual_cash_flows(ticker, last, return_df=True)

            annual_cf_names = annual_cf.columns[8:]
            annual_included_data = st.multiselect("Ratios to include in chart: ", annual_cf_names, default=annual_cf_names[0])

            charts.plot_statements(annual_cf, annual_included_data)