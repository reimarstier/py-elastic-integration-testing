
default:
	docker-compose -f docker-compose/testenv.yml up -d
	docker-compose -f docker-compose/unittest.yml up

run:
	docker-compose -f docker-compose/unittest.yml up

envs:
	$(CONDA_EXE) env list

activate: 
	echo conda activate py-elastic-int

tests:
	#pyb run_unit_tests
	#PYTHONPATH=src/main/python pytest -v
	python -m pytest -c pytest.ini src/test/python/ -v

# show coverage
coverage:
	firefox target/reports/coverage_html/index.html

clean:
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete
	rm -rf .coverage
	rm -rf target/
	rm -rf .cache/
