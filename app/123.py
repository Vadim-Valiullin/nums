shop = [1, 1, 2, 2, 2, 1]
customer_money = [1, 1, 2, 5, 5, 5]
product_dict = {'bread': 1, 'milk': 2, 'potato': 3}
customer_product = []

while True:
    print('На полке магазина:')
    for product, price in product_dict.items():
        print(f' {product} -  {price} руб')
    ask = input('Что желаете: ')
    if ask in product_dict:
        price = product_dict[ask]
        print(f'Цена товара: {price}')
    else:
        print('Такого товара нет.')
        continue
    if price in customer_money:
        print('Успешно')
        customer_money.remove(price)
        customer_product.append(ask)
        del product_dict[ask]
        print(f'В кошельке осталось: {customer_money}')
        print(f'В магазине осталось: {product_dict}')
        print(f'В корзине покупателя: {customer_product}')
    else:
        del product_dict[ask]
        for i in customer_money:
            if i > price:
                change = i - price
                customer_money.remove(i)
                customer_product.append(ask)
                customer_money.append(change)
        print(customer_money)
        print(product_dict)
        print(f'В корзине покупателя: {customer_product}')
    if product_dict == {}:
        print('Все товары проданы')
        break
