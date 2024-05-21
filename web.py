import streamlit as st
import functions

todos = functions.get_todos()

# adding feature for new items
def add_todo():
    todo= st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo app")
st.subheader("This is my todo app")
st.text("This app helps you organize your daily tasks")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # deleting feature for completed items
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# input box
st.text_input(label="", placeholder="Add new Todo item...",
              on_change=add_todo, key="new_todo")
