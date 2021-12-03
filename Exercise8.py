import sys
with open(sys.argv[1]) as data: data_dict, dataList = {}, [x.split(":") for x in data.read().splitlines()]
for archive in dataList: data_dict[archive[0]] = str(archive[1])
for inpt in sys.argv[2].split(","):
    try: print(f"{inpt},University: {data_dict[inpt]}")
    except: print(f"No record '{inpt}' was found")