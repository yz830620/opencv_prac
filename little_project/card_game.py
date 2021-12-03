import random

def shuffle_cardset():
    all_card = []
    number_patters = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_patterns = ['clubs', 'diamonds', 'hearts', 'spades']
    for number_patter in number_patters:
        all_card.extend([card_pattern + f'_{number_patter}' for card_pattern in card_patterns])

    random.shuffle(all_card)
    return all_card

def init_user():
    name_list = []
    naming_stage = True
    while naming_stage:
        name = input('輸入使用者或{""}跳出：')
        if name == '':
            naming_stage = False
            print('結束命名階段')
        else:
            name_list.append(name)
            print(f"hi, {name}, 歡迎來玩小姐遊戲，目前玩家有{name_list}")
    random.shuffle(name_list)
    return name_list

def init_user_card(name_list):
    function_stack={i:{'小':0,'照':0,'鼻':0, '廁':0} for i in name_list}
    return function_stack

def ask_skill_card(function_stack):
    pretty_skill_print(function_stack)
    names = list(function_stack.keys())
    person_to_activate = int(input(f'請問要重置誰呢?{str({i:j for i,j in enumerate(names)})}'))
    cards = ['小','照','鼻', '廁']
    card_to_activate = int(input(f"請問發動哪張牌呢?{str({i:j for i,j in enumerate(cards)})}"))
    card_qty = function_stack[names[person_to_activate]][cards[card_to_activate]]
    print(names[person_to_activate], cards[card_to_activate])
    if card_qty > 0:
        function_stack[names[person_to_activate]][cards[card_to_activate]] -= 1
        return function_stack
    else:
        print('lier, you have no card')
    return function_stack

def pretty_skill_print(function_stack):
    for user in function_stack:
        for skill in function_stack[user]:
            if function_stack[user][skill] != 0:
                print(f'{user} 現在有 {skill}卡 {function_stack[user][skill]}張')


def consume_card(all_card, function_stack, punishment, name_list):
    k_counter = 0
    user_qty = len(name_list)
    for idx, card in enumerate(all_card):
        current_user = name_list[idx%user_qty]
        skill = input(f'{current_user}, 抽卡請按enter，發動技能請輸入skill !')
        if skill:
            function_stack = ask_skill_card(function_stack)
        number = card.split('_')[-1]
        if number == 'K':
            k_counter += 1
        if k_counter == 4:
            print('~~~')
            print(card, '第四次K，請清空公杯')
            print('~~~')
            k_counter = 0
        else:
            skill_card_set = {'2':'小', '5':'照', '6':'鼻', '8':'廁'}
            if number in skill_card_set:
                function_stack[current_user][skill_card_set[number]] += 1
            print(card, [number], punishment[number])
    else:
        print('gameover')
        re = input('reset_game?')
        if re.lower() in ['y', 'yes']:
            reset(name_list)

def game(punishment):
    all_card = shuffle_cardset()
    name_list = init_user()
    function_stack = init_user_card(name_list)
    consume_card(all_card, function_stack, punishment, name_list)

def reset(name_list):
    all_card = shuffle_cardset()
    function_stack = init_user_card(name_list)
    consume_card(all_card, function_stack, punishment, name_list)




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

def main():
    game(punishment)


if __name__ == "__main__":
    main()

# unit test...
# name_list = [input(f"輸入第i個使用者姓名:") for i in range(1,5)]
# function_stack={i:{'小':0,'照':0,'鼻':0, '廁':0} for i in name_list}

# current_users = name_list[0], name_list[2], name_list[3], name_list[0], name_list[1],name_list[0], name_list[3],
# cards = '小', '照', '鼻', '廁', '小', '照'

# for current_user, card in zip(current_users, cards):
#     if card in['小','照','鼻','廁']:
#         function_stack[current_user][card] += 1