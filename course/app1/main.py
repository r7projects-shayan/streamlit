import streamlit as st

st.title("This is the first streamlit app")

st.subheader("this is a subheader")

st.text("this is a text which is normal")

st.header("This is the header")

# Markdown
st.markdown(
    "**bold text in markdown**"
)

#json 

jsonobject = {
    "a":"1",
    "b":"2",
    "c":"3"
}

st.json(jsonobject)

#code 

codevar = '''

def func1(param1, param2):
  print("hello world")

'''

st.code(codevar)

#Add stylings to all these

st.write('''# this is h1 tag
        
         ''')

#matrix

st.metric(label = "wind speed", value = "170", delta="1.4ms")

#here delta means the change in wind speed


#chatbox

hello = st.chat_input("enter something")

st.write(hello)