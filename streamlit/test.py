"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import ast
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

counter = 0

with open("file.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

with open("file_card.txt", 'r') as f_card:
    cards = str(f_card.readline()).split(',')
    st.write('11111', cards)
    cards = all_card if cards == "" else cards


if st.button("next card"):
    a += 1  
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        st.write(f"counter is now: {a}")
        st.write(f"[{cards[a].split('_')[-1]}]", punishment[cards[a].split('_')[-1]])

if st.button("init card"):
    a = 0
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        st.write(f"counter is now: {a}")

    with open("file_card.txt", 'w') as f_card:
        for number_patter in number_patters:
            all_card.extend([card_pattern + f'_{number_patter}' for card_pattern in card_patterns])

        random.shuffle(all_card)

        for ele in all_card:
            f_card.write(ele)
            f_card.write(',')
        st.write('cards are ready')

# p1 = st.text_input('input player1')
# p2 = st.text_input('input player2')
# p3 = st.text_input('input player3')
# p4 = st.text_input('input player4')
st.write('2222', cards)
for i in cards:
    # _ = input('抽卡請按enter !')
    number = i.split('_')[-1]
    if number == 'K':
        k_counter += 1
    if k_counter == 4:
        st.write('~~~')
        st.write(i, '第四次K，請清空公杯')
        st.write('~~~')
        k_counter = 0
    else:
        st.write(i, [number], punishment[number])
    