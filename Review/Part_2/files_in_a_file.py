def conv_to_bytes(units):
    num, volume = units
    if volume == "B":
        return num
    elif volume == "KB":
        return num * 1024
    elif volume == "MB":
        return num * (1024 ** 2)
    elif volume == "GB":
        return num * (1024 ** 3)
    else:
        raise Exception


def conv_to_max(num):
    volumes = ["B", "KB", "MB", "GB"]
    i = 0
    while num > 1024:
        num /= 1024
        i += 1
    return f"{round(num)} {volumes[i]}"


with (open("files.txt", 'r', encoding='utf-8') as file):
    entries = dict([f.strip().split(".") for f in file.readlines()])

    name_dict = {}
    summ_dict = {}

    for key, value in entries.items():
        extension, num, volume = value.split(" ")
        names = name_dict.setdefault(extension, [])
        names.append(f"{key}.{extension}")

        converted_num = conv_to_bytes([int(num), volume])
        summ_dict[extension] = summ_dict.get(extension, 0) + converted_num

    for ext, names in sorted(name_dict.items()):
        print(*sorted(names), sep="\n")
        print(f"----------")
        print(f"Summary: {conv_to_max(summ_dict[ext])}")
        print()