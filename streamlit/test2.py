import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with open("file.txt", "r") as f:
    a = f.readline()  # starts as a string
    a = 0 if a == "" else int(a)  # check if its an empty string, otherwise should be able to cast using int()

if st.button("Click me"):
    a += 1  
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        st.write(f"counter is now: {a}")

if st.button("init card"):
    a = 0
    with open("file.txt", "w") as f:
        f.truncate()
        f.write(f"{a}")
        st.write(f"counter is now: {a}")