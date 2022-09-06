## Use this program to calculate the pay of an employee before/after State Taxes.

def print_pay():

    print("Your pay before tax is:   ", int(xpay_no_tax))
    print("Your pay after tax is:    ", int(xpay_after_tax))
    print("Ammount in taxes:         ", int(xpaid_tax))

state_tax = input("Enter state tax rate: ")
xhours = input("Enter Number of Hours: ")
xrate = input("Enter Hourly Pay: ")
tax_rate = float(state_tax) / 100

try:

## Claculates the yearly pay
    if float(xhours) == (2080):
        xpay_no_tax = float(xhours) * float(xrate)
        xpaid_tax = float(xpay_no_tax) * tax_rate
        xpay_after_tax = float(xpay_no_tax) - float(xpaid_tax)
        print_pay()

## Calculates the pay if there is no overtime
    elif float(xhours) <= 80:
        xpay_no_tax = float(xhours) * float(xrate)
        xpaid_tax = float(xpay_no_tax) * tax_rate
        xpay_after_tax = float(xpay_no_tax) - float(xpaid_tax)
        print_pay()

## Calculates the pay if there is overtime
    else:
        xover_time = (float(xhours) - 80) * (float(xrate) * 1.5)
        xpay_no_tax = (float(xhours) * float(xrate)) + float(xover_time)
        xpaid_tax = float(xpay_no_tax) * tax_rate
        xpay_after_tax = float(xpay_no_tax) - float(xpaid_tax)
        print_pay()

except:
        print("Invalid Input")


