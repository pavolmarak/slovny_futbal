import sys

def print_progress(percent, bar_length=40):
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"\r[{bar}] {percent:3d}%", end="", flush=True)

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# spočítaj riadky
with open(input_file, "r", encoding="utf-8") as f:
    total_lines = sum(1 for _ in f)

processed = 0
last_percent = -1

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    
    for line in infile:
        parts = line.strip().split()  # split by any whitespace
        if len(parts) == 3:
            tag = parts[2]
            if tag.startswith("S") and (tag.endswith("s1") or tag.endswith("p1")):
                # write only 2nd column
                outfile.write(f"{parts[1]}\n")
        
        processed += 1
        percent = int(processed * 100 / total_lines)
        if percent != last_percent:
            print_progress(percent)
            last_percent = percent

print("\nDone ✅")
