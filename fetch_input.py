import sys
import os
import requests

day_nr = sys.argv[1]

with open(f"d{day_nr}.txt", "w") as f:
    f.write(
        requests.get(
            f"https://adventofcode.com/2022/day/{day_nr}/input",
            headers={"Cookie": "crisp"},
        ).text
    )

    with open(f"d{day_nr}.py", "w") as f2:
        f2.write(f"""with open("d{day_nr}.txt", "r") as f:\n\tinp = f.read()""")

    os.system(f"reindent d{day_nr}.py")
