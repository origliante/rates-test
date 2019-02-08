import os

from coverage import Coverage
import vcr

import api


cov = Coverage(
    data_file='.coverage_integration',
    source=['api'],
    )
cov.start()


@api.app.route('/quit', methods=['GET'])
def quit():
    global cov
    cov.stop()
    cov.save()
    os.system('kill %d' % os.getpid())


if __name__ == '__main__':
    #if you wanna see if vcr is taking from a cassette
    #import logging
    #logging.basicConfig()
    #vcr_log = logging.getLogger("vcr")
    #vcr_log.setLevel(logging.INFO)

    with vcr.use_cassette('tests/integration/get_currencies.yml'):
        api.app.run(debug=True)

