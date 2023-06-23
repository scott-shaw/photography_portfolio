PROG_NAME=photo_port

gen:
	python3 src/gen_data.py
start: gen
	npm start
build: gen
	npm run build
deploy: build
	netlify deploy --prod
clean:
	rm src/photo_data.js

