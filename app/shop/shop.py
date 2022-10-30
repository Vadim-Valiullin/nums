shop = [1, 1, 2, 2, 2, 1]
customer_money = [1, 1, 2, 5, 5, 5]
product_dict = {'bread': 1, 'milk': 2, 'potato': 3}
customer_product = []
change = 0

while True:
    print('На полке магазина:')
    for product, price in product_dict.items():
        print(f' {product} -  {price} руб')
    ask = input('Что желаете: ')
    if ask == 'stop':
        print(f'Покупки закончены!\nВ корзине покупателя:{customer_product}')
        break
    elif ask in product_dict:
        price = product_dict[ask]
        print(f'Цена товара: {price}')
    elif product_dict == {}:
        print('Все товары проданы')
        break
    else:
        print('Такого товара нет.')
        continue
    for i in customer_money:
        change = i - price
        if i == price:
            print('Успешно')
            customer_money.remove(price)
            customer_product.append(ask)
            del product_dict[ask]
            print(f'В кошельке осталось: {customer_money}')
            print(f'В магазине осталось: {product_dict}')
            print(f'В корзине покупателя: {customer_product}')
            break
        elif sum(customer_money) < price:
            print('У вас недостаточно денег. Выберите товар по карману.')
        elif i > price and change in shop:
            customer_money.remove(i)
            customer_product.append(ask)
            customer_money.append(change)
            shop.remove(change)
            del product_dict[ask]
            print(f'В кошельке осталось: {customer_money}')
            print(f'В магазине осталось: {product_dict}')
            print(f'В корзине покупателя: {customer_product}')
            break
        elif i < price:
            continue
        else:
            print('Продажа товара приостановлена из-за отстутствия сдачи')
            break
    if len(customer_money) == 0:
        print('Без оплаты мы не можем вам продать товар.\nНайдите деньги и приходите снова.')
        break


