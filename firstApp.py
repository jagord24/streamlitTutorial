"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

dataframe = pd.DataFrame(
    np.random.randn(20,3),
    columns = ('col %d' % i for i in range(3))
)

map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50] + [37.76, -122.4],
    columns = ('lat', 'lon')
)


st.sidebar.text_input("Your name", key="name")

option = st.sidebar.selectbox(
    'Which number do you like best?',
     dataframe['col 0'])


st.session_state.name
'You selected ', option

x = st.sidebar.slider('x')

st.write(x, 'squared is', x*x)
st.map(map_data)
st.line_chart(dataframe)

if st.checkbox('Show dataframe'):
    
    st.table(dataframe)

left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")