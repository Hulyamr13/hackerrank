def mostActive(customers):
    n = len(customers)
    counts = {}
    for customer in customers:
        counts[customer] = counts.get(customer, 0) + 1
    result = []
    for customer, count in counts.items():
        if count / n >= 0.05:
            result.append(customer)
    result.sort()
    return result


if __name__ == '__main__':
    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    print('\n'.join(result))
