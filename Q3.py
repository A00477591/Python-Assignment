
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Python Assignment Question 3")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if len(df.columns) != 2:
            st.error("Please upload a file with exactly 2 columns including an age column")
        elif 'age' not in map(str.lower, df.columns):
            st.error("No age data in the CSV")
        else:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write("CSV file uploaded:")
            st.write(df)
            st.title('Age Histogram')
            plt.xlabel("Age")
            plt.ylabel("Frequency")
            plt.hist(df["Age"], bins=10, color='lightgreen', edgecolor="black")
            st.pyplot()

if __name__ == "__main__":
    main()
