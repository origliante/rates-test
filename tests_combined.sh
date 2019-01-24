
# run test_*
COVERAGE_FILE=.coverage_unit PYTHONPATH=`pwd` python -m pytest --cov api tests/unit
# run tavern
#COVERAGE_FILE=.coverage_integration PYTHONPATH=`pwd` python -m pytest --tavern-http-backend=flask --tavern-global-cfg=tests/stories/tavern.conf.yaml --cov api tests/stories

COVERAGE_FILE=.coverage_integration PYTHONPATH=`pwd` coverage run run.py &
pid=$!
#COVERAGE_FILE=.coverage_integration PYTHONPATH=`pwd` python -m pytest --tavern-http-backend=flask --cov api tests/stories
#COVERAGE_FILE=.coverage_integration
PYTHONPATH=`pwd` python -m pytest tests/stories
kill $pid

#python -m coverage combine .coverage_unit .coverage_integration
#python -m coverage html



