with open('sales_data.txt') as f:
    sales_data = list(f.readlines())

def total_sales(data, raw_data=True):
    '''
    Data type: List of Strings
    Returns float of total sales
    '''
    result = 0
    if raw_data == True:
        for sale in data:
            split = sale.split('\t')
            result += float(split[-1][1:-1])
        return result

    for sale in data:
        result += float(sale[-1][1:-1])
    return result

def filter_month(data, month):
    '''
    Data type: List of Strings
    Month type: String
    Returns list of strings filtered by specified month
    '''
    result = []
    # month += '/'
    for entry in data:
        split = entry.split('\t')
        if month == '12' and split[1][0:2] == '12':
            result.append(split)
        elif month == '11' and split[1][0:2] == '11':
            result.append(split)
        elif month == '10' and split[1][0:2] == '10':
            result.append(split)
        elif (month + '/') == split[1][0:2]:
            result.append(split)
    return result


def filter_city_or_payment(data, filter_type, raw_data=True):
    '''
    Data type: List of strings
    Filter_type type: String
    Returns list of strings filtered by specified type
    If raw_data == False then it will not split line because raw data has been
    formatted and no longer has tabs to split
    '''
    result = []
    if raw_data == True:
        for entry in data:
            split = entry.split('\t')
            if filter_type in split:
                result.append(split)
        return result

    for entry in data:
        if filter_type in entry:
            result.append(entry)
    return result

# Question 1
# What are the total amount of sales contained in this data set?
print('Total sales:', total_sales(sales_data))

# Question 2
# Which city had the highest sales in February?
feb = filter_month(sales_data, '2')
sum_per_city = {}
for sale in feb:
    city = sale[0]
    sale_of_city = float(sale[-1][1:-1])
    if city not in sum_per_city:
        sum_per_city[city] = sale_of_city
    else:
        sum_per_city[city] += sale_of_city

name_city_highest_amount = max(sum_per_city, key=sum_per_city.get)
value_city_highest_amount = sum_per_city[name_city_highest_amount]
print('Highest sales in feb: ({0}: {1})'.format(name_city_highest_amount, value_city_highest_amount))

# Question 3
# Out of the entire data set, what is the total amount of money
# people have paid in cash?
cash = filter_city_or_payment(sales_data, 'Cash')
total = total_sales(cash, False)
print('Paid in cash:', total)

# Question 4
# What is the most popular payment type in Oakland in March?
sales_march = filter_month(sales_data, '3')

oakland_sales_march = filter_city_or_payment(sales_march, 'Oakland', False)
oakland_cash = filter_city_or_payment(oakland_sales_march, 'Cash', False)
oakland_bc = filter_city_or_payment(oakland_sales_march, 'Baseball Cards', False)
oakland_check = filter_city_or_payment(oakland_sales_march, 'Check', False)
oakland_credit = filter_city_or_payment(oakland_sales_march, 'Credit', False)

dict_payment_types = {'cash': len(oakland_cash), 'bc':len(oakland_bc), 'check':len(oakland_check), 'credit':len(oakland_credit)}

print(max(dict_payment_types, key=dict_payment_types.get))

# Question 5:
# How many sales were made on 4/20, and which city had the highest sales value?
sales_april = filter_month(sales_data, '4')
april_twenty = [sale for sale in sales_april if '4/20' in sale]
sum_per_city = {}
for sale in april_twenty:
    city = sale[0]
    sale_of_city = float(sale[-1][1:-1])
    if city not in sum_per_city:
        sum_per_city[city] = sale_of_city
    else:
        sum_per_city[city] += sale_of_city

print('Sales on 4/20:', len(april_twenty))
print('Highest sales value:', max(sum_per_city, key=sum_per_city.get))

# Question 6:
# What is the average sales amount for credit card purchases?
credit_purchases = filter_city_or_payment(sales_data, 'Credit')
total = total_sales(credit_purchases, False)
avg = total / len(credit_purchases)
print('Avg credit sale amount:', avg)

# Question 7
# How many purchases were made by bartering with baseball cards?
bc = filter_city_or_payment(sales_data, 'Baseball Cards')
print('Purchases with baseball cards:', len(bc))
