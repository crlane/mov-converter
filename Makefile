.PHONY: build run deploy

build:
	docker build -t crlane/mov-converter .

run:
	docker run --rm -it -p 5000:5000 crlane/mov-converter

deploy:
	heroku container:push web
