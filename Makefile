.PHONY: install run fetch docker-build docker-run

install:
	pip install -r requirements.txt

fetch:
	python main.py

run:
	streamlit run app.py

docker-build:
	docker build -t ai-job-aggregator .

docker-run:
	docker run -p 8501:8501 ai-job-aggregator
