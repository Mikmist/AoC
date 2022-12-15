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
    print(a, b)
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    item_b, type_b= get_item(b)
    item_a, type_a = get_item(a)
    if item_a == None:
        return True
    if item_b == None:
        return False
    if type_a == "LIST" and type_b == "NUMBER":
        item_b = get_number_as_list_item(item_b)
        type_b = "LIST"
    if type_b == "LIST" and type_a == "NUMBER":
        item_a = get_number_as_list_item(item_a)
        type_a = "LIST"
    if type_a == "NUMBER" and type_b == "NUMBER":
        if int(item_b) > int(item_a):
            return True
        elif int(item_b) == int(item_a):
            return None
        else: return False
    if type_a == "LIST" and type_b == "LIST":
        items_a = get_items_of_list(str(item_a)[1:-1])
        items_b = get_items_of_list(str(item_b)[1:-1])
        print("a:", items_a)
        print("b:", items_b)
        if len(items_b) < 1 and len(items_a) > 0:
            print("Right side ran out of items, so inputs are not in the right order")
            return False
        for idx in range(max(len(items_b), len(items_a))):
            if idx >= len(items_b):
                print("Right side ran out of items, so inputs are not in the right order")
                return False
            if idx >= len(items_a):
                break
            res = check(items_a[idx], items_b[idx])
            if res == False:
                print("Right side is smaller, so inputs are not in the right order")
                return False
            if res == True:
                return True
        return True
    print(item_a, item_b)
    return False

def check_values(a, b):
    print(a, b)
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    if a[0] == '[' and b[0] == '[':
        return check_values(a[1:], b[1:])
    elif a[0] == '[' and b[0] != '[':
        if b[0] == ']':
            print("Right side ran out of items, so inputs are not in the right order")
            return False
        return check_values(a[1:], b)
    elif a[0] != '[' and b[0] == '[':
        return check_values(a, b[1:])
    elif a[0] == ']' and b[0] != ']':
        return True
    elif a[0] == ']' and b[0] == ']':
        if len(a) == 1:
            return True
        if len(b) == 1:
            print("Right side is smaller, so inputs are not in the right order")
            return False
        return check_values(a[2:], b[2:])
    elif a[0] != ']' and b[0] == ']':
        return False
    num_a = a.split(',')[0].replace(']', '')
    num_b = b.split(',')[0].replace(']', '')
    print(num_a, num_b)
    if int(num_a) <= int(num_b):
        print('True')
        if a[len(num_a)] != ']':
            cor = len(b.split(',')[0])
            print(cor)
            return check_values(a[len(num_a)+1:], b[cor+1:])
        return True
    return False


with open('../input/input') as data:
    idx = 1; sum = 0
    for pair in data.read().split('\n\n'):
        pairs = pair.split('\n')
        print(f"\n== Pair {idx} ==")
        if check(pairs[0], pairs[1]) != False:
            sum += idx
            print("Added")
        idx += 1
    print(sum)
