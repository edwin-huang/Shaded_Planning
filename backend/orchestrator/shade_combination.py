import json
from dijkstra_shade import main
import sys

if __name__ == "__main__":
    # Convert the string arguments back into lists of floats
    origin = list(map(float, sys.argv[1].split(',')))
    destination = list(map(float, sys.argv[2].split(',')))
    hour = int(sys.argv[3]) if len(sys.argv) > 3 else None

# Initialize a dictionary to hold all path types and their data

paths_data = {
    "Shortest": main(1, 0, origin, destination, hour),
    "Shaded": main(0, 1, origin, destination, hour),
    "50-50": main(0.5, 0.5, origin, destination, hour),
    "70-30": main(0.7, 0.3, origin, destination, hour),
    "30-70": main(0.3, 0.7, origin, destination, hour)
}

# Convert the dictionary to a JSON string and print
print(json.dumps(paths_data))
