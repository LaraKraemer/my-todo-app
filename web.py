import streamlit as st
import src.functions

todos = src.functions.get_todos()

# adjust layout depending on device
st.set_page_config(layout="wide")

# adding feature for new items
def add_todo():
    todo= st.session_state["new_todo"] + "\n"
    todos.append(todo)
    src.functions.write_todos(todos)

st.title("My Todo app")
st.subheader("This is my todo app")
st.text("This app helps you organize your daily tasks.")

# input box
st.text_input(label="", placeholder="Add new Todo item...",
              on_change=add_todo, key="new_todo")

# checkbox item
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # deleting feature for completed items
    if checkbox:
        todos.pop(index)
        src.functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


