#!/bin/bash

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
base_path=./assets/photos/
dirs=("street/" "wildlife/" "macro/" "travel/")
thumbs_name=thumbnails/

for dir in "${dirs[@]}"; do
    photo_dir="${script_dir}/assets/photos/${dir}"    
    thumb_dir="${photo_dir}${thumbs_name}"    
    mkdir -p "${thumb_dir}"
    for file in ${photo_dir}*; do
        # next line checks the mime-type of the file
        image_type=$(file --mime-type -b "$file")
        if [[ $image_type = image/* ]]; then
            filename=$(basename "${file}")
            convert -resize 50% "${file}" "${thumb_dir}${filename}"
        fi
    done
done
