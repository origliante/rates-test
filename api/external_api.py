
_rates = [
    {
        'id': 1,
        'currency': u'USD',
        'rate': 1.0,
    },
    {
        'id': 2,
        'currency': u'EUR',
        'rate': 1.14,
    }
]


def _get_rates(currency=None):
    if currency:
        for r in _rates:
            if currency == r['currency']:
                return r
        return {}
    return _rates



