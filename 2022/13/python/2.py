import functools

def get_number_as_list_item(i):
    return f"[{i}]"


def get_item(i):
    idx = 0 
    if len(i) < 1:
        return None, "NONE"
    if i[idx] == '[':
        cnt = 0
        while cnt > 0 or idx == 0:
            if i[idx] == ']':
                cnt -= 1
            if i[idx] == '[':
                cnt += 1
            idx+=1
        return i[0:idx], "LIST"
    return int(i.split(',')[0].replace(']', '')), "NUMBER"


def get_items_of_list(list):
    items = []
    start = 0
    cnt = 0
    for idx in range(len(list)):
        if list[idx] == "[":
            cnt+=1
        if list[idx] == "]":
            cnt-=1
        if list[idx] == "," and cnt == 0:
            items.append(list[start:idx])
            start=idx+1
    items.append(list[start:])
    return items


def check(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return 1
    if len(b) == 0:
        return -1
    item_b, type_b= get_item(b)
    item_a, type_a = get_item(a)
    if item_a == None and item_b == None:
        return 0
    if item_a == None:
        return 1
    if item_b == None:
        return -1
    if type_a == "LIST" and type_b == "NUMBER":
        item_b = get_number_as_list_item(item_b)
        type_b = "LIST"
    if type_b == "LIST" and type_a == "NUMBER":
        item_a = get_number_as_list_item(item_a)
        type_a = "LIST"
    if type_a == "NUMBER" and type_b == "NUMBER":
        if int(item_b) > int(item_a):
            return 1
        elif int(item_b) == int(item_a):
            return 0
        else: return -1
    if type_a == "LIST" and type_b == "LIST":
        items_a = get_items_of_list(str(item_a)[1:-1])
        items_b = get_items_of_list(str(item_b)[1:-1])
        if len(items_b) < 1 and len(items_a) > 0:
            return -1
        for idx in range(max(len(items_b), len(items_a))):
            if idx >= len(items_b):
                return -1
            if idx >= len(items_a):
                break
            res = check(items_a[idx], items_b[idx])
            if res == -1:
                return -1
            if res == 1:
                return 1
        return 1
    return -1

with open('../input/input') as data:
    packets = []
    for packet in data.read().replace('\n\n', '\n').split('\n'):
        packets.append(packet)
    packets.append('[[2]]')
    packets.append('[[6]]')
    print(packets)
    packets.sort(key=functools.cmp_to_key(check), reverse=True)
    keys=1
    for i in range(len(packets)):
        print(packets[i])
        if packets[i] == '[[2]]' or packets[i] == '[[6]]':
            keys*=(i)
    print(keys)
