import json
from datetime import datetime


def main():
    name_contains = (lambda name, item_name: name.lower() in item_name.lower())
    price_greater_than = (lambda price, item_price: item_price >= int(price))
    price_less_than = (lambda price, item_price: item_price <= int(price))
    date_before = (lambda date, item_date: datetime.strptime(item_date, "%d.%m.%Y") <= datetime.strptime(date, "%d.%m.%Y"))
    date_after = (lambda date, item_date: datetime.strptime(item_date, "%d.%m.%Y") >= datetime.strptime(date, "%d.%m.%Y"))

    filters = {"NAME_CONTAINS": name_contains, "PRICE_GREATER_THAN": price_greater_than,
               "PRICE_LESS_THAN": price_less_than, "DATE_BEFORE": date_before, "DATE_AFTER": date_after}

    items = json.loads(input())

    for _ in range(5):
        for filt, value in [input().split()]:
            items = [item for item in items if filters[filt](value, item[filt.split('_')[0].lower()])]

    print(sorted(items, key=lambda x: x["id"]))


if __name__ == '__main__':
    main()
