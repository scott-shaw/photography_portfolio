import subprocess

# Reduce file sizes of images
subprocess.run(["python", "reduce_size.py", "./assets/photos/featured", "2048"])
subprocess.run(["python", "reduce_size.py", "./assets/photos/macro", "2048"])
subprocess.run(["python", "reduce_size.py", "./assets/photos/street", "2048"])
subprocess.run(["python", "reduce_size.py", "./assets/photos/travel", "2048"])
subprocess.run(["python", "reduce_size.py", "./assets/photos/wildlife", "2048"])

# Generate thumbnails (smaller file sizes)
print("Generating thumbnails...")
subprocess.run(["./gen_thumbs.sh"])

# Generate photo_data.js file
print("Generating `gen_data.py`...")
subprocess.run(["python", "gen_data.py"])
