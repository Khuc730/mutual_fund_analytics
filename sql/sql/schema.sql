CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT    
);

CREATE TABLE fact_nav(
    amfi code TEXT FK,
    nav_date DATE 
    nav REAL,
    daily_return REAL
);

CREATE TABLE fact_transactions(
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    kyc_status TEXT
);

CREATE TABLE fact_performance(
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL
);

CREATE TABLE fact_benchmark(
    date DATE,
    index_name TEXT,
    index_value REAL
);

