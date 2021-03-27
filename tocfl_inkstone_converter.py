import csv
import re
import zhon.pinyin

Row = dict[str, str]
MAX_LEVEL = 7

with open("tocfl_with_simplified_numbered_pinyin.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    fields = next(csvreader)
    for field in fields:
        print(field)
    levels: list[list[Row]] = [[] for i in range(MAX_LEVEL)]
    export_fields = ["Simplified", "Traditional", "Pinyin", "Translation"]
    for row in csvreader:
        level = int(row["Level"]) - 1
        pinyin = row["Pinyin"]
        pinyin = " ".join(map(lambda p: p if p[-1].isdigit() else p + "5",
            re.findall(zhon.pinyin.num_syl, pinyin, re.IGNORECASE)))
        translation = row["Meaning"].replace("\"", "'")
        export_row = {"Simplified": row["Simplified"], "Traditional": row["Traditional"],
                "Pinyin": pinyin, "Translation": translation}
        levels[level].append(export_row)
    print(f"Read {str(csvreader.line_num)} rows")
    for i, rows in enumerate(levels, 1):
        print(f"    - {len(rows)} in level {str(i)}")
        with open(f"tocfl_level_{i}.list", mode="w") as export_file:
            writer = csv.DictWriter(export_file, fieldnames=export_fields, delimiter="\t")
            for row in rows:
                writer.writerow(row)

