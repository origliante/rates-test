from api import rates, app

def test_sum():
    ret = rates.sum(1, 1)
    assert ret == 2

def test_build_resp():
    with app.app_context():
        ret = rates._build_resp(None)
        print(ret)
        ret = rates._build_resp({'test': 1})
        print(ret)

