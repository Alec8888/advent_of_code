import re
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


def load_robots(path):
    bots = [] # (pos), (vel)
    with open(path) as f:
        lines = [line.strip() for line in f]

        pattern = r'p=(\d+),(\d+)\s*v=(-?\d+),(-?\d+)'

        for line in lines:
            match = re.match(pattern, line)
            if match:
                bots.append([((int(match.group(1))), int(match.group(2))),(int(match.group(3)), int(match.group(4)))])
            else:
                logging.error(f"No match found for the line: '{line}'")
    return bots

path = r'.\Days\Day14\example.txt'
bots = load_robots(path)
for bot in bots:
    print(bot)