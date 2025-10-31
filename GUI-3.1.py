import streamlit as st
from PIL import Image

col1,col2=st.columns((4,5))

with col1:
    st.title("My Resume")
    st.header("Jaxon Davis")
with col2:
    image = Image.open('Dog.jpg')
    st.image(image, width=200)

st.markdown("**About Me**")
st.text("I am a human being that requires dioxide and dihydrogen monoxide to survive.")
st.text("This is just a picture of a dog I found on Google. It is not actually related to me whatsoever. I'd like to think that he is a good boy, but I don't actually know.")
st.divider()
st.markdown("**Education:**")
st.text("The most educated")
st.divider()
st.markdown("**Experience:** (in order of importance)")
st.text("Dungeon Master")
st.text("Eagle Scout")
st.text("Marketing Assistant")
st.divider()
st.markdown("**Hobbies:**")
st.text("All of them")
st.divider()
st.markdown("**Contact**")
st.text_input("Your Name: ")
st.text_input("Email: ")
message = st.text_area("Message")
st.button("Send")