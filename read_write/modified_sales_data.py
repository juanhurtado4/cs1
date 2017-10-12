with open('sales_data.txt') as f:
    sales_data = list(f.readlines())

testing_sales = [sales_data[0], sales_data[1], sales_data[2]]
# -------------------MANUAL TESTING ------------------
# print(testing_sales[0].split('$'))
print(testing_sales[0].split('\t'))
# print(testing_sales[1].split('\t'))
# print(testing_sales[2].split('\t'))
# money = testing_sales[0].split('$')[1]
# print(money)
 # -----------------------------------------------------

# TODO: Abstract filter month, filter value
# Question 1
def sales_transaction_number(sales_data):
    return len(sales_data)

# Question 2
def highest_in_feb(sales_data):
    feb_entries = []
    sum_per_city = {}
    for sales in sales_data:
        entry = sales.split('\t')
        if entry[1][0] == '2':
            feb_entries.append(entry)
    for sale in feb_entries:
        city = sale[0]
        sale_of_city = float(sale[-1][1:-1])
        if city not in sum_per_city:
            sum_per_city[city] = sale_of_city
        else:
            sum_per_city[city] += sale_of_city

    name_city_highest_amount = max(sum_per_city, key=sum_per_city.get)
    value_city_highest_amount = sum_per_city[name_city_highest_amount]
    return '{0}: {1}'.format(name_city_highest_amount, value_city_highest_amount)

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


# Question 4
def oakland_payment_type(sales_data):
    # TODO: Filter by march
    oakland = []
    result = {}
    for sales in sales_data:
        entry = sales.split('\t')
        if entry[0] == 'Oakland':
            oakland.append(entry)
    for sale in oakland:
        payment_type = sale[-2]
        if payment_type in result:
            result[payment_type] += 1
        else:
            result[payment_type] = 1

    print(len(oakland))
    print(result)
    return max(result, key=result.get)






# Solution for question 2 if there is only one transaction per city
# def highest_in_feb(sales_data):
#     feb_entries = []
#     sum_per_city = {}
#     for sales in sales_data:
#         entry = sales.split('\t')
#         if entry[1][0] == '2':
#             if len(feb_entries) == 0:
#                 feb_entries.append(entry)
#                 current_highest = float(feb_entries[0][-1][1:-1])
#             elif float(entry[-1][1:-1]) > current_highest:
#                 feb_entries[0] = entry
#     return feb_entries
