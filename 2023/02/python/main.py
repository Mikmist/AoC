def parse_game(game):
    red = 0; green = 0; blue = 0
    colors = game.split(',')
    for i in colors:
        parts = i.strip().split(' ')
        if 'green' in parts[1]:
            green = int(parts[0])
        if 'red' in parts[1]:
            red = int(parts[0])
        if 'blue' in parts[1]:
            blue = int(parts[0])
    return red, green, blue


with open('../input/input') as data:
    game_id = 1
    sum = 0
    power_sum = 0
    for line in data:
        print(line.strip())
        games = line.strip().split(':')[1]
        print('games', games)
        faulty = False
        min_red = 0
        min_blue = 0
        min_green = 0
        for i in games.split(';'):
            red, green, blue = parse_game(i)
            if red > 12 or blue > 14 or green > 13:
                faulty = True
            print(red, green, blue)
            min_red = max(min_red, red)
            min_blue = max(min_blue, green)
            min_green = max(min_green, blue)
        if not faulty:
            sum += game_id
        print(min_red,min_blue,min_green)
        power_sum += (min_red*min_blue*min_green)
        game_id += 1
    print(sum)
    print(power_sum)

