import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Text input box
    user_input = st.text_input("Enter your text here:")
    
    # Button to submit input
    if st.button("Submit"):
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()
