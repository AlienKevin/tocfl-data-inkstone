import csv

Row = dict[str, str]
MAX_LEVEL = 7

with open("tocfl.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    fields = next(csvreader)
    for field in fields:
        print(field)
    levels: list[list[Row]] = [[] for i in range(MAX_LEVEL)]
    export_fields = ["Simplified", "Traditional", "Pinyin", "Translation"]
    for row in csvreader:
        level = int(row["Level"]) - 1
        export_row = {"Simplified": row["Word"], "Traditional": row["Word"],
                "Pinyin": row["Pinyin"], "Translation": "/" + row["First Translation"] + "/"}
        levels[level].append(export_row)
    print(f"Read {str(csvreader.line_num)} rows")
    for i, rows in enumerate(levels, 1):
        print(f"    - {len(rows)} in level {str(i)}")
        with open(f"tocfl_level_{i}.csv", mode="w") as export_file:
            writer = csv.DictWriter(export_file, fieldnames=export_fields, delimiter="\t")
            for row in rows:
                writer.writerow(row)
