# loan_calculator.py
Two functions were defined.

<b>get_month_pay</b> is used to calculate monthly payment after input of loan_amount, loan_len_year and rate. This is pretty basic. Many
online loan calculators do exactly this.

<b>get_loan_portion</b> is used to calculate how much you have paid on the loan principal after paying a while. Over time, the proportion
of monthly payment paid on principal increases and the proportion paid on interest decreases. This function gives an idea about how fast
the change could be. The example given shows in the first half of the loan period (7.5 out of 15 years), over 72% of total interest has 
been paid. This means in the second half of loan period, you would pay much less on interest. It calls <i>get_month_pay</i> function.

