"""
Created on Oct 24 2013

@author: ryanyu
"""

from __future__ import division

def get_month_pay(loan_amount, loan_len_year, rate):
    """
    This function is to get monthly payment
    loan_amount: how much is mortgage loan
    loan_len_year: length of the mortgage in years
    rate: annual interest rate. Assume it's compounded monthly
    """
    if rate<1:
        rate_pct=rate*100
        mr=rate/12  # convert annual rate to monthly rate
    elif rate>=1:
        rate_pct=rate
        mr=rate*0.01/12
    nm=loan_len_year*12  #get number of payments
    month_pay=(mr*loan_amount*(1+mr)**nm)/((1+mr)**nm-1)
    print("Monthly payment for loan of "+"${:,.2f}".format(loan_amount)+", "+str(loan_len_year)+
          " years, rate of "+str(rate_pct)+"%:")
    print("${:,.2f}".format(month_pay)+"\n")
    return month_pay


def get_loan_portion(loan_amount, loan_len_year, rate, paid_len_year):
    """
    Monthly payment can be divided into two portions: paying loan and
    paying interest. But how much on each portion changes over time.
    This function calculates how much loan (or percent of total loan)
    has been paid after paying for certain years.
    paid_len_year: how many years payments have been made
    """
    mp=get_month_pay(loan_amount, loan_len_year, rate)
    if rate<1:
        mr=rate/12  #get monthly rate
    elif rate>=1:
        mr=rate*0.01/12
    nm_rest=(loan_len_year-paid_len_year)*12
    nm_total=loan_len_year*12
    presentv_total=mp*((1-1/(1+mr)**nm_total)/mr) #total present value=loan
    presentv_rest=mp*((1-1/(1+mr)**nm_rest)/mr) 
    presentv=presentv_total-presentv_rest #get the true present value of last number of years payment
    int_paid=mp*12*paid_len_year-presentv
    print("After "+str(paid_len_year)+" years, your out of pocket money is:")
    print("${:,.2f}".format(mp*12*paid_len_year)+"\n")
    print("The amount you would pay on the loan:")
    print("${:,.2f}".format(presentv)+", which is "+"{0:.1f}".format(100*presentv/loan_amount)+"% of your loan.\n")
    print("The interest you would pay is: ")
    print("${:,.2f}".format(int_paid)+", which is "+"{0:.1f}".format(100*int_paid/(mp*12*loan_len_year-loan_amount))+
          "% of the total interest.")
    return presentv

# an example: 300K loan in 15 years with rate of 3.5%
get_loan_portion(300000, 15, 3.5, 7.5)

