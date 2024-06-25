sales_data = [
    ('product1', [100, 120, 130, 140, 110]),
    ('product2', [80, 90, 95, 85, 100]),     
    ('product3', [200, 190, 210, 205, 195])
]
def calculate_mean(data):
    return sum(data) / len(data)

sales_product1 = sales_data[0][1]
mean_product1 = calculate_mean(sales_product1)
print(f"Среднее значение продаж товара 1: {mean_product1}")

def calculate_max_min(data):
    max_value = max(data)
    min_value = min(data)
    return max_value, min_value

sales_product2 = sales_data[1][1]
max_product2, min_product2 = calculate_max_min(sales_product2)
print(f"Максимальные продажи товара 2: {max_product2}")
print(f"Минимальные продажи товара 2: {min_product2}")
