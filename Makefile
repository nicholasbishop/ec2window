format:
	yapf -ir .

lint:
	pylint *.py ec2window

.PHONY: format lint
