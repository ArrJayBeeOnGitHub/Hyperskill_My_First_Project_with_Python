import dbm

earned_amounts = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250,
                  'Milk chocolate': 1680, 'Doughnut': 1075, 'Pancake': 80}
pre_expenses_profit = sum(earned_amounts.values())

# The following was messing with me.
# It's used as an example in the project description, but is not a part of the expected solution.
# I've left it in to remember how long it took me to notice the issue... Almost a whole goddamn hour...
"""print("What's your name?")
username = input()
print("Hello,", username, end='!')
print()
print()"""

print('Earned amount:')
for k, v in earned_amounts.items():
    print(k, v, sep=': $')
print()
print('Income: $', str(sum(earned_amounts.values())), sep='')
print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())
print('Net income: $', (pre_expenses_profit - staff_expenses - other_expenses), sep='')
