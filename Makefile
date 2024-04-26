requirements:
	pip install -r requirements.txt

run:
	uvicorn main:app --host 127.0.0.1 --port 8000

dev:
	uvicorn main:app --reload --host 127.0.0.1 --port 8000

tailwind:
	npx tailwindcss -i ./src/input.css -o ./static/tailwind.css --watch