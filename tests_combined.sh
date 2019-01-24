
rm -f .coverage_*

# run test_*
COVERAGE_FILE=.coverage_unit PYTHONPATH=`pwd` python -m pytest --cov="api" --cov-report="" tests/unit
# run tavern
#COVERAGE_FILE=.coverage_integration PYTHONPATH=`pwd` python -m pytest --tavern-http-backend=flask --tavern-global-cfg=tests/stories/tavern.conf.yaml --cov api tests/stories

PYTHONPATH=`pwd` python run_with_coverage.py 2>/dev/null 1>/dev/null &
PYTHONPATH=`pwd` python -m pytest tests/stories
# hack
curl http://localhost:5000/quit

echo -e "\nIntegration tests coverage:"
COVERAGE_FILE=.coverage_integration coverage report -m

echo -e "\nUnit tests coverage:"
COVERAGE_FILE=.coverage_unit coverage report -m

python -m coverage combine .coverage_unit .coverage_integration
echo -e "\nCombined coverage:"
coverage report -m
echo -e "\n"

