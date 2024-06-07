import streamlit as st
def nijou(n):
    return n+2
input_num = st.number_input('Input a number', value=0)

result = nijou(input_num)
st.write('Result: ', result)


