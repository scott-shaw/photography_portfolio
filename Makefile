PROG_NAME=photo_port

start:
	python3 src/gen_data.py
	npm start
build:
	python3 src/gen_data.py
	npm run build
deploy: build
	netlify deploy --prod
clean:
	rm src/photo_data.js
