PROG_NAME=photo_port

gen:
	bash src/gen_thumbs.sh
	python3 src/gen_data.py
start: gen
	npm start
build: gen
	npm run build
deploy: build
	netlify deploy --prod
clean:
	rm src/photo_data.js
	rm -r src/assets/photos/macro/thumbnails/
	rm -r src/assets/photos/street/thumbnails/
	rm -r src/assets/photos/travel/thumbnails/
	rm -r src/assets/photos/wildlife/thumbnails/
