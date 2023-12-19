build:
	docker build -t imm-mlops

run:
	docker run -d -p 8000:8000 imm-mlops

install:
	pip install -r requirements.txt

lint:
	black --check .
