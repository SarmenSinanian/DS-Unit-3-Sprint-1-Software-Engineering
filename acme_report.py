from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Moustrap', '???']


def generate_products(num_products=30):
    products = []
    n = 0
    while n < (num_products):
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        s = (sample(ADJECTIVES, 1) + sample(NOUNS, 1))
        dic = [price, weight, flammability]
        combo = s + dic
        products.append(combo)
        n += 1
    return products


def inventory_report(products):
    prices = []
    weights = []
    flammabilities = []
    for product in products:
        prices.append(product[2])
        weights.append(product[3])
        flammabilities.append(product[4])

    uniques = len(generate_products())
    average_price = sum(prices) / len(prices)
    average_weight = sum(weights) / len(weights)
    average_flammability = sum(flammabilities) / len(flammabilities)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {uniques}')
    print(f'Average price: {average_price}')
    print(f'Average weight: {average_weight}')
    print(f'Average flammability: {average_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
