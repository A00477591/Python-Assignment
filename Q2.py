import pandas as pd

def main():
    df = pd.read_csv("titles.csv",)            
    result = df.head(100).apply(getVowelsCount, axis=1)
    df['Vowels'] = result
    print(df.head(100))

def getVowelsCount(columns):
        return sum(1 for letter in columns["title"] if letter in "aeiouAEIOU")

if __name__ == "__main__":
    main()