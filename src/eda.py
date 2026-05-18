import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv(
        "data/processed/cleaned_data.csv"
    )

    print("Dataset shape:", df.shape)

    # total revenue
    revenue = df["payment_value"].sum()
    print("\nTotal Revenue:", round(revenue, 2))

    # avg order value
    avg = df["payment_value"].mean()
    print("Average Order Value:", round(avg, 2))

    # top states
    print("\nTop 10 States:")
    print(
        df["customer_state"]
        .value_counts()
        .head(10)
    )

    # payment types
    print("\nPayment Types:")
    print(
        df["payment_type"]
        .value_counts()
    )

    # monthly sales
    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )

    monthly_sales = (
        df.groupby(
            df["order_purchase_timestamp"].dt.to_period("M")
        )["payment_value"]
        .sum()
    )

    monthly_sales.plot(figsize=(12, 5))
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()


if __name__ == "__main__":
    main()