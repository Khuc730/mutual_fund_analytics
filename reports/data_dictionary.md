## Table : dim_fund ##

Column Name         Data Type       Description

amfi_code           INTEGER         Unique AMFI scheme code 
scheme_code         TEXT            Name of the mutual fund scheme
fund_house          TEXT            Asset Management Company(AMC)
category            TEXT            Fund category
sub_category        TEXT            Fund sub-category
risk Category       TEXT            Risk classification of the fund 

## Table: fact_nav ##

Column Name         Data Type       Description

amfi_code           INTEGER         AMFI scheme code
date                DATE            NAV date
nav                 REAL            Net Asset Value

## Table: fact_transactions ##

Column Name         Data Type       Description

investor_id         TEXT            Unique investor identifier
transaction_date    DATE            Transaction date
amfi_code           INTEGER         Fund scheme code
transaction_type    TEXT            SIP, Lumpsum, or Redemption
amount_inr          REAL            Transaction amount in INR
state               TEXT            Investor state
city	            TEXT	        Investor city
city_tier	        TEXT	        Tier classification of city
age_group	        TEXT	        Investor age category
gender	            TEXT	        Investor gender
annual_income_lakh	REAL	        Annual income in lakhs
payment_mode	    TEXT	        Mode of payment
kyc_status	        TEXT	        KYC verification status

## Table: fact_benchmark ##

Column Name         Data Type       Description

date	            DATE	        Benchmark date
index_name	        TEXT	        Benchmark index name
index_value	        REAL	        Benchmark index value