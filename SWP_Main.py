import pandas as pd
import re
import matplotlib.pyplot as plt

from babel.numbers import format_currency

class SWPCalculator:
    
    def __init__(self, swp_amount, investment, investment_period, RoR, inflation):
        self.swp_amount = int(swp_amount)
        self.investment = int(investment)
        self.investment_period = int(investment_period)
        self.RoR = int(RoR)
        self.inflation = int(inflation)
    

    def calculate_interest_earned(self, current_balance, current_swp_amount):
        return round(((current_balance-current_swp_amount) * self.RoR/100) / 12)
    
    def inflation_adjusted_withdrawal(self, current_swp_amount):
        return round((current_swp_amount*self.inflation/100)/12) + current_swp_amount
      
    def remove_decimals(self, currency):
        return re.sub(r'\.[0-9]+','',currency)

    def convert_to_currency(self, number):
        currency = format_currency(number, 'INR', locale='en_IN', currency_digits =False)
        return self.remove_decimals(currency)
        
    def calculate_swp(self):
        try:
            # Pre conditions
            current_balance = self.investment
            current_swp_amount = self.swp_amount
            data_list = []
            money_does_not_end = True
            for year in range(1, self.investment_period+1):
                for month in range(1,13):
                    data_dict = {}
                    data_dict['Year'] = year-1
                    data_dict['Month'] = month
                    data_dict['Balance at Begin'] = current_balance
                    data_dict['Withdrawal'] = current_swp_amount
                    current_interest_per_month = self.calculate_interest_earned(current_balance, current_swp_amount)
                    data_dict['Interest Earned'] = current_interest_per_month
                    data_dict['Balance at End'] = current_balance-current_swp_amount+current_interest_per_month
                    
                    data_list.append(data_dict)
                    
                    current_balance = data_dict['Balance at End']
                    current_swp_amount = self.inflation_adjusted_withdrawal(current_swp_amount)
             
            data_df = pd.DataFrame(data_list)
            
            for position, balance in enumerate(data_df['Balance at End']):
                if balance <=0:
                    money_does_not_end = False
                    ending_year = data_df.loc[position,('Year')]
                    ending_month = data_df.loc[position,('Month')]
                    break
                    
            data = data_df.copy()
            data[data < 0] = 0
            
            data_df['Balance at Begin'] = data_df['Balance at Begin'].apply(self.convert_to_currency)
            data_df['Withdrawal'] = data_df['Withdrawal'].apply(self.convert_to_currency)
            data_df['Interest Earned'] = data_df['Interest Earned'].apply(self.convert_to_currency)
            data_df['Balance at End'] = data_df['Balance at End'].apply(self.convert_to_currency)
            
            if money_does_not_end:
                ending_year = self.investment_period
                ending_month = 12
                
            # return {'data':data,'data_df':data_df,'ending year':ending_year,'ending month':ending_month}
            return {'data':data.to_json(orient="records", double_precision=1),
                    'data_df':data_df.to_json(orient="records", double_precision=1),
                    'ending year':str(ending_year),
                    'ending month':str(ending_month)}
                        
        except:
            return {"Error":"Error in execution"}


# =============================================================================
# Testing Section
# =============================================================================
# swp_amount = 80000
# investment = 30000000
# investment_period = 60
# RoR = 12
# inflation = 7

# swp = SWPCalculator(swp_amount, investment,investment_period, RoR, inflation)
# output_data = swp.calculate_swp()
# data = output_data['data']
# data_df = output_data['data_df']

# plt.plot(data['Year'], data['Balance at Begin'])

# =============================================================================
# 
# =============================================================================

# df = pd.DataFrame(swp_list)

# import re

# currency = '₹54,33,422.00'
# def remove_decimals(curreny):
#     return re.sub(r'\.[0-9]+','',currency)

# def convert_to_currency(number):
#     currency = format_currency(number, 'INR', locale='en_IN', currency_digits =False)
#     return remove_decimals(currency)

# converted_currency = remove_decimals(currency)
# print(converted_currency)


# df['Balance at End'].apply(convert_to_currency)     

# invest_p = 5

# for month in range(1,13):
#     print(month)

# previous_withdrawal = SWP_Amount
# current_withdrawal = SWP_Amount

# print(inflation_adjusted_withdrawal())


# json_list = [{'Year':1,
#               'Month':12,
#               'Balance at Begin': 1200},
#              {'Year':2,
#               'Month':25,
#               'Balance at Begin': 1400}]
