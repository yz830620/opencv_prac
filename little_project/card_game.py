import random
import time

def shuffle_cardset():
    all_card = []
    number_patters = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_patterns = ['黑桃', '方塊', '紅心', '梅花']
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
    function_stack={i:{'小姐':0,'照相機':0,'摸鼻子':0, '廁所牌':0} for i in name_list}
    return function_stack

def ask_skill_card(function_stack):
    skill_card_stage = True
    while skill_card_stage: 
        pretty_skill_print(function_stack)
        ask_reset = input('請問要重置卡片嗎？ y or n  ')
        if ask_reset.lower() in ['y', 'yes']:
            names = list(function_stack.keys())
            person_to_activate = int(input(f'請問要重置誰呢?{str({i:j for i,j in enumerate(names)})}'))
            cards = ['小姐','照相機','摸鼻子', '廁所牌']
            card_to_activate = int(input(f"請問發動哪張牌呢?{str({i:j for i,j in enumerate(cards)})}"))
            card_qty = function_stack[names[person_to_activate]][cards[card_to_activate]]
            if card_qty > 0:
                function_stack[names[person_to_activate]][cards[card_to_activate]] -= 1
                print(names[person_to_activate], '發動了技能卡', cards[card_to_activate])
            else:
                print('！！！lier, you have no card')
                time.sleep(0.5)
        else:
            print('結束使用技能卡階段')
            skill_card_stage = False
    return function_stack

def pretty_skill_print(function_stack):
    for user in function_stack:
        for skill in function_stack[user]:
            if function_stack[user][skill] != 0:
                print(f'{user} 現在有 {skill} {function_stack[user][skill]}張')


def consume_card(all_card, function_stack, punishment, name_list):
    k_counter = 0
    user_qty = len(name_list)
    for idx, card in enumerate(all_card):
        current_user = name_list[idx%user_qty]
        print('-'*20)
        skill = input(f'{current_user}, 抽卡請按enter，發動技能請輸入skill !')
        if skill:
            function_stack = ask_skill_card(function_stack)
            _ = input(f'{current_user}, 抽卡請按enter，發動技能請輸入skill !')
        number = card.split('_')[-1]
        if number == 'K':
            k_counter += 1
        if k_counter == 4:
            print('~'*20)
            print(card, '第四次K，請清空公杯')
            print('~'*20)
            k_counter = 0
        else:
            skill_card_set = {'2':'小姐', '5':'照相機', '6':'摸鼻子', '8':'廁所牌'}
            if number in skill_card_set:
                function_stack[current_user][skill_card_set[number]] += 1
            print(current_user, '抽到', card, [number], punishment[number])
            
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
