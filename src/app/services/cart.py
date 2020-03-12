from flask import session
import app.services.meals as meals_service
import plural_ru


def get_cart():
    if session.get('cart') is None:
        session['cart'] = create_empty_cart()

    return session['cart']


def add_to_cart(meal_id):
    meal = meals_service.get_by_id(meal_id)

    cart = get_cart()

    total = cart.get('total')
    qty = cart.get('qty')
    items = cart.get('items')

    if items.get(str(meal.id)) is None:
        total += float(meal.price)
        qty = int(qty) + 1
        items[str(meal.id)] = {'title': meal.title, 'qty': 1, 'price': meal.price}
        set_data_to_cart(qty, total, items)


def delete_from_cart(meal_id):
    cart = get_cart()

    total = cart.get('total')
    qty = cart.get('qty')
    items = cart.get('items')
    item_key = str(meal_id)

    if items.get(item_key) is not None:
        item = items.get(item_key)
        total -= float(item.get('price'))
        qty = int(qty) - 1
        items.pop(item_key)
        set_data_to_cart(qty, total, items)


def clear_cart():
    session['cart'] = create_empty_cart()


def create_empty_cart():
    return {'total': 0, 'qty': 0, 'items': {}, 'qty_title': ''}


def set_data_to_cart(qty, total, items):
    qty_title = '{} {}'.format(qty, plural_ru.ru(qty, ['блюдо', 'блюда', 'блюд']))
    session['cart'] = {'total': total, 'qty': qty, 'items': items, 'qty_title': qty_title}
