import sys
import time
import requests
from core.config import config
from core.bot import bot


if '--updates' in sys.argv:
    print("I'm gonna read updates")
    updates = bot.get_updates(0)
    for message_item in updates:
        print(message_item)

elif '--check' in sys.argv:

    msgs = []
    prices = []
    prices_for_meter = []

    _max_floor = 25
    _from = 69
    _to = 76

    offset = 0
    c = 0

    while True:
        r = requests.get(
            url=config.apartment(),
            params={
                "offset": offset,
                "project": "michur",
                "building": "michur_1,michur_2"
            }
        )

        data = r.json()

        objects = data["results"]
        if len(objects) == 0:
            break

        for obj in objects:
            building = obj['building']
            room = obj['room']
            area = obj['area']

            price = obj['price']

            floor = obj['floor']
            number = obj['number']
            sale = obj['sale']
            white_box = obj['white_box']

            meter_price = round(price / area, 2)

            if _from < area < _to and floor <= _max_floor:
                prices.append(price)
                prices_for_meter.append(meter_price)

                msg = [
                    f"Здание: {building}, этаж: {floor}, комнат: {room}",
                    f"Площадь: {area}",
                    f"Цена: {price:,}",
                    f"За метр: {meter_price:,}",
                    f"Ссылка: https://level.ru/michur/flat/2room/{number}/",
                ]
                bot.send_message_to_chat("\n".join(msg) + "\n---\n")
                time.sleep(2)

        offset += len(objects)

    avg_price = round(sum(prices) / len(prices))
    avg_price_for_meter = round(sum(prices_for_meter) / len(prices_for_meter))
    our = round(73.3 * avg_price_for_meter)

    overall = f"Всего квартир [корпуc 1, 2], [от {_from} до {_to} метров], [этаж до {_max_floor}]: {len(prices)}"
    overall += f"\nСредняя цена: {avg_price:,}"
    overall += f"\nСредняя цена за метр: {avg_price_for_meter:,}"
    overall += f"\nНаша стоит ~ {our:,}"

    bot.send_message_to_chat(overall)
