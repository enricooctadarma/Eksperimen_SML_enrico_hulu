import pandas as pd


def preprocess_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)

    # Drop unnecessary columns
    df = df.drop(columns=["Cabin", "Name", "Ticket"])

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Encode categorical variables
    df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

    # Save processed data
    df.to_csv(output_path, index=False)

    print("Preprocessing selesai. File disimpan di:", output_path)


if __name__ == "__main__":
    input_file = "../namadataset_raw/titanic.csv"
    output_file = "namadataset_preprocessing.csv"

    preprocess_data(input_file, output_file)