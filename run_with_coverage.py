import os

from coverage import Coverage

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
    api.app.run(debug=True)

