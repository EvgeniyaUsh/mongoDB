from pymongo import MongoClient


def create_matches_collection(accrual_list, payment):
    """
    Функция создает новую коллекцию matches, которая содержит поля:
    accrual__id: id долга
    accrual_date: дата долга
    accrual_month: месяц долга
    payment__id: id платежа
    payment_date: дата платежа
    payment_month: месяц платежа
    :param accrual_list: список долгов
    :param payment: соответсвующий списку долгов платеж
    """
    accrual_for_payment = accrual_list[0]
    accrual_collection.delete_one(accrual_for_payment)
    for i in accrual_for_payment:
        accrual_for_payment[f'accrual_{i}'] = accrual_for_payment.pop(i)
        payment[f'payment_{i}'] = payment.pop(i)
    matches_dict = {**accrual_for_payment, **payment}
    client.test_database.matches.insert_one(matches_dict).inserted_id


def request_for_payments_and_accrual(payment_collect, accrual_collect):
    """
    :param payment_collect: коллекция платежей
    :param accrual_collect: коллекция долгов
    :return: список платежей, которые не нашли себе долг
    """
    for i in payment_collect.find().sort('date'):
        date = i['date']

        accrual_with_same_month = []
        accrual_with_other_month = []

        try:
            for j in accrual_collect.find({'date': {'$lt': date}}).sort('date'):
                accrual_with_same_month.append(j) if i['month'] == j['month'] else accrual_with_other_month.append(j)

            if accrual_with_same_month:
                create_matches_collection(accrual_with_same_month, i)
            else:
                create_matches_collection(accrual_with_other_month, i)

        except IndexError:
            payment_without_accrual.append(i)

    return payment_without_accrual


if __name__ == '__main__':
    client = MongoClient()

    payment_collection = client.test_database.payment
    accrual_collection = client.test_database.accrual

    payment_without_accrual = []
    request_for_payments_and_accrual(payment_collection, accrual_collection)
