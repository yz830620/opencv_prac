import random

all_card = []
number_patters = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_patterns = ['clubs', 'diamonds', 'hearts', 'spades']

k_counter = 0

punishment = {
    'A' : '指定',
    '2' : '小姐',
    '3' : '菜園果園動物園',
    '4' : 'pass一次',
    '5' : '照相機',
    '6' : '摸鼻子',
    '7' : '玩倍數遊戲',
    '8' : '廁所牌',
    '9' : '自己喝',
    '10': '神經病',
    'J' : '左喝',
    'Q' : '右喝',
    'K' : '大怒神公杯'
}

for number_patter in number_patters:
    all_card.extend([card_pattern + f'_{number_patter}' for card_pattern in card_patterns])

random.shuffle(all_card)

# print(all_card)

for i in all_card:
    _ = input('抽卡請按enter !')
    number = i.split('_')[-1]
    if number == 'K':
        k_counter += 1
    if k_counter == 4:
        print('~~~')
        print(i, '第四次K，請清空公杯')
        print('~~~')
        k_counter = 0
    else:
        print(i, [number], punishment[number])
    