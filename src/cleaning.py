import pandas as pd


def clean_data(df):
    print("Original shape:", df.shape)

    # duplicates
    df = df.drop_duplicates()

    # convert dates
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    # remove fully empty rows
    df = df.dropna(how="all")

    print("Cleaned shape:", df.shape)

    print("\nMissing values:")
    print(df.isnull().sum().sort_values(ascending=False).head(10))

    return df


def main():
    df = pd.read_csv("data/processed/master_data.csv")

    cleaned = clean_data(df)

    cleaned.to_csv(
        "data/processed/cleaned_data.csv",
        index=False
    )

    print("\nSaved → data/processed/cleaned_data.csv")


if __name__ == "__main__":
    main()