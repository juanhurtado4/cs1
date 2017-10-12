with open('sales_data.txt') as f:
    sales_data = list(f.readlines())

testing_sales = [sales_data[0], sales_data[1], sales_data[2]]
print(testing_sales[0].split('$'))
money = testing_sales[0].split('$')[1]
print(money)
# for index, test in enumerate(sales_data[0]):
#     # print('char:', test)
#     # print('ordinal char:', ord(test))
#     print('test', chr(9))
#     # print(test[0:test.index(str(ord(9)))])
#     # print('index:', index)
#     # print(sales_data[3].find(' '))
#     # print(sales_data[3].index(' '))

# Question 1
def sales_transaction_number(sales_data):
    return len(sales_data)

# Question 2
def highest_in_feb(sales_data):
    feb_entries = []
    cities = {}
    for sales in sales_data:
        slash_index = sale.index('/')
        if sales[slash_index - 2] == '1':
            continue
        else:
            if sales[slash_index -1] == '2':
                feb_entries.append(sales)

    for entry in feb_entries:
        index_dollar = sale.index('$')
        sale_amount = float(entry[index_dollar + 1:-1])
        city_last_index = city.index(chr(9)) # First tab in the entry
        cities[city[0:city_last_index]] += sale_amount


# Question 3
def sales(sales_data, payment_type=None):
    num = 0
    if payment_type == None:
        for sale in sales_data:
            index_dollar = sale.index('$')
            sale_amount = float(sale[index_dollar + 1:-1])
            num = num + sale_amount
        return num
    else:
        for sale in sales_data:
            if payment_type in sale:
                index_dollar = sale.index('$')
                sale_amount = float(sale[index_dollar + 1:-1])
                # print(type(sale_amount))
                num = num + sale_amount

        return num


def total_sales_in_cash(sales_data):
    return sales(sales_data, 'Cash')
