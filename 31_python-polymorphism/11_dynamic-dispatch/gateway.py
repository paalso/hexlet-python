KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75

PRICE_NORMALIZERS = {
    'kostrovok': lambda price: round(price * (1 + KOSTROVOK_FEE)),
    'book-king': lambda price: round(price * BOOKKING_CONVERT_RATE),
    'airdnb': lambda price: price
}


def find_all_matching(data, limits={}):
    default_limits = {'min': -float('inf'), 'max': float('inf')}
    limits = default_limits | limits

    all_hotels = _extract_all_hotels(data)

    matched_hotels = filter(
        lambda e: limits['min'] <= e['hotel']['cost'] <= limits['max'],
        all_hotels)
    return list(matched_hotels)


def _extract_all_hotels(data):
    all_hotels = []
    for entry in data:
        service = entry['service']
        for hotel_record in entry['hotels']:
            all_hotels.append(_normalize_record(service, hotel_record))
    return all_hotels


def _normalize_price(service, price):
    return PRICE_NORMALIZERS[service](price)


def _normalize_record(service, record):
    normalized_record = {**record}
    price = record['cost']
    normalized_record['cost'] = _normalize_price(service, price)
    return {'hotel': normalized_record, 'service': service}


def main():
    import json

    with open('data.json') as f:
        data = json.loads(f.read())

    predicates = {}
    predicates = {'min': 650, 'max': 700}

    result = find_all_matching(data, predicates)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
