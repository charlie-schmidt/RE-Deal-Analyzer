import streamlit as st
import pandas as pd
import math

# Streamlit Setup

st.write("""

# Rental Property Calculator


	""")

# Column layout
# col1, col2, col3, col4 = st.beta_columns((1,1,1,1))

# # Specific to House Hacking
# if col1.button("House Hack"): 
# 	rent_savings = st.number_input("Rent Savings")

# col2.button("Short Term Rental")
# col3.button("Traditional LTR")
# col4.button("BRRRR")

col1, col2, col3, col4, col5 = st.beta_columns((2,0.35,2,0.35,2))

col1.write("""

### Rental Income

	""")
 
rent_income = col1.number_input("Expected Rent Income") 

# One Time Expenses
col3.write("""

### One Time Expenses

	""")

closing_costs = col3.number_input("Closing Costs")
repair_costs = col3.number_input("Rehab Costs") 

# Recurring Expenses
col5.write("""

### Recurring Expenses

	""")

with col5.beta_expander("Taxes & Insurance"):
	annual_property_taxes = st.number_input("Annual Property Taxes")
	annual_insurance = st.number_input("Annual Insurance")

# Reserves/CapEx
with col5.beta_expander("Reserves/Management (% of Income)"):

	maintenance = st.number_input("Maintenance", .00)
	vacancy = st.number_input("Vacancy", .00)
	capEx = st.number_input("CapEx", .00)
	management = st.number_input("Management", 0.00)

with col5.beta_expander("Other"):
	HOA = st.number_input("HOA")
	utilities = st.number_input("Utilities")




# Loan details
st.sidebar.header("Loan Details")
purchase_price = st.sidebar.number_input("Purchase Price", 1000)
loan_term = st.sidebar.slider("Loan Term",15, 30, value = 30)
down_payment = st.sidebar.number_input("% Down Payment", 3.0)
down_payment_percent = down_payment/100
rate = st.sidebar.number_input("Interest Rate", 3.00, 5.00)/100
mortgage_insurance = st.sidebar.number_input("PMI", 0.000, 1.500)


# PITI Calculations
monthly_property_taxes = annual_property_taxes/12
monthly_insurance = annual_insurance/12

num_pmts = loan_term * 12
down_payment = down_payment_percent * purchase_price
cash2close = down_payment + closing_costs + repair_costs
loan_amount = purchase_price - down_payment
monthly_interest_rate = rate/12
mortgage_payment = (loan_amount*monthly_interest_rate*math.pow(1+monthly_interest_rate, num_pmts))/(math.pow(1+monthly_interest_rate, num_pmts)-1)

PITI = mortgage_payment + monthly_property_taxes + monthly_insurance
reserves = (maintenance*rent_income) + (vacancy*rent_income) + (capEx*rent_income)
management_cost = rent_income * management
total_monthly_expenses = PITI + reserves +  utilities + HOA + management_cost

# Performance Metrics
cash_flow = rent_income - total_monthly_expenses
CoC = ((cash_flow * 12)/cash2close)*100
NOI = (rent_income*12)-(total_monthly_expenses*12)
cap_rate = NOI/purchase_price



# Monthly Expenses Overview 

# st.write("""## Monthly Expenses Overview""")
st.write("""### Total Monthly Expenses""", round(total_monthly_expenses,2))
st.write("""### Cash Flow""", round(cash_flow,2))
with st.beta_expander("Expense Breakdown"):
	col_v, col_w, col_x, col_y, col_z = st.beta_columns(5)

	col_v.write("""PITI""")
	col_v.write(round(PITI, 2))

	col_w.write("""Reserves""")
	col_w.write(round(reserves,2))

	col_x.write("""Utilities""")
	col_x.write(round(utilities,2))

	col_y.write("""HOA""")
	col_y.write(round(HOA,2))

	col_z.write("""Management""")
	col_z.write(round(management_cost,2))
	

# col_y.write("""PITI""", round(PITI,2))
# col_y.write("""Principal + Interest:""", round(mortgage_payment,2))
# col_y.write("""Taxes""", round(monthly_property_taxes,2))
# col_y.write("""Insurance""", round(monthly_insurance,2))



# Returns 
st.write("""

	## Returns

	""")

col_a, col_b, col_c, col_d, col_e = st.beta_columns(5)

col_a.write("""Cash Flow""")
col_a.write(round(cash_flow,2))

col_b.write("""Cash Flow w/o Reserves""")
col_b.write(round(cash_flow + reserves,2))

col_c.write("""CoC Return (%)""")
col_c.write(round(CoC,2))

# col_d.write("""NOI""")
# col_d.write(round(NOI, 2))

# col_e.write("""Cap Rate""")
# col_e.write(round(cap_rate,2))


# Specific to STR
avg_nightly_rate = 0
expected_occupancy = 0
cleaning_expense = 0

# Specific to BRRRR
ARV = 0


# Property Income
st.sidebar.write("""Principal + Interest:""", round(mortgage_payment,2))




