import app.services.cart as cart_service
import app.services.meals as meal_service
import app.services.users as user_service
from app.models import db, Order, OrderStatus
import datetime


def create_order(form):
    user = user_service.get_auth_user()
    order = Order()
    order.userId = user.get('id')
    order.status = OrderStatus.NEW
    order.date = datetime.datetime.utcnow()
    form.populate_obj(order)

    cart = cart_service.get_cart()
    order.total = cart.get('total')

    for item_id, item in cart['items'].items():
        meal = meal_service.get_by_id(int(item_id))
        order.meals.append(meal)


    db.session.add(order)
    db.session.commit()

    cart_service.clear_cart()


def get_order(user_id):
    orders_data = []

    orders = db.session.query(Order).filter(Order.userId == user_id).order_by(Order.date.desc()).all()

    for order in orders:
        order_item = {}
        order_item['date'] = '{} {}'.format(order.date.month, get_month_title(order.date.month))
        order_item['total'] = order.total
        order_item['status'] = order.status

        meals_items = []

        for meal in order.meals:
            meals_items.append({'title': meal.title, 'qty': 1, 'price': meal.price})

        order_item['meals'] = meals_items

        orders_data.append(order_item)

    return orders_data


def get_month_title(month_number):
    if month_number == 1:
        return 'Января'
    elif month_number == 2:
        return 'Февраля'
    elif month_number == 3:
        return 'Марта'
    elif month_number == 4:
        return 'Апреля'
    elif month_number == 5:
        return 'Мая'
    elif month_number == 6:
        return 'Июня'
    elif month_number == 7:
        return 'Июля'
    elif month_number == 8:
        return 'Августа'
    elif month_number == 9:
        return 'Сентября'
    elif month_number == 10:
        return 'Октября'
    elif month_number == 11:
        return 'Ноября'
    elif month_number == 11:
        return 'Декабря'
