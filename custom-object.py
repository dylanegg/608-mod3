#custom-object.py
"""Create a tax and tip calculator"""

#define functions
def calculateTax(bill, tax_percent):
    return bill * tax_percent/100
def calculateTip(bill, tip_percent):
    return bill * tip_percent/100
def total_bill(bill, tax_percent, tip_percent):
    return bill * (1 + tip_percent/100 + tax_percent/100)


#set bill, tax and tip percent
bill = 100
tax_percent = 7.5
tip_percent = 20.0

#calculate tax and tip
tax = calculateTax(bill,tax_percent)
tip = calculateTip(bill,tip_percent)

#Display Tax Amount, Tip Amount, and Total Bill
print('Tax:', tax)
print('Tip:', tip)
print('Total Bill:',total_bill(bill, tax_percent, tip_percent))