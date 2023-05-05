import math
import argparse
import sys


def check_input(data):
    if data.count(None) > 1:  # not enough parameters
        return False
    if not (args.type == "annuity" or args.type == "diff"):  # invalid type of loan
        return False
    if data[0] == 'diff' and data[1] is not None:  # differentiated payments and static payment ammount
        return False
    if data[4] is None:  # must have interest
        return False
    for i in range(1, 5):
        if data[i] is not None:
            if float(data[i]) < 0:
                return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

data = [args.type, args.payment, args.principal, args.periods, args.interest]
if not check_input(data):  # checking data and returning error and exiting if it isn't correct
    print('Incorrect parameters')
    sys.exit()

for i in range(1, 5):
    if data[i] is not None:
        data[i] = float(data[i])

# changing to these variables to use the old code and match equations from hyperskill
A = data[1]  # annuity payment, monthly payment
P = data[2]  # loan principal
i = data[4] / 1200  # monthly interest rate converted from yearly percent to monthly float
n = data[3]  # number of months to pay off the loa

if args.type == 'annuity':
    if args.periods is None:
        n = math.ceil(math.log(A / (A - i * P), 1 + i))
        years = n // 12
        months = n % 12
        years_str = '' if years == 0 else '1 year' if years == 1 else f'{years} years'
        _and = '' if years == 0 or months == 0 else ' and'
        months_str = '' if months == 0 else '1 month' if months == 1 else f'{months} months'
        print(f'It will take {years_str}{_and} {months_str} to repay this loan!')
    elif args.payment is None:
        A = math.ceil((P * i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print(f'Your monthly payment = {A}!')
    elif args.principal is None:
        P = round((A * ((1 + i) ** n - 1)) / (i * (1 + i) ** n))
        print(f'Your loan principal = {P}!')
    print('\n' + 'Overpayment =', A * n - P)
else:
    sum_of_payments = 0
    for m in range(1, int(n) + 1):
        Dm = math.ceil(P / n + i * (P - (P * (m - 1) / n)))  # m-th differentiated payment
        print(f'Month {m}: payment is {Dm}')
        sum_of_payments += Dm
    print('Overpayment =', sum_of_payments - P)
