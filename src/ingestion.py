import pandas as pd
import os


RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


def load_csv(filename):
    path = os.path.join(RAW_PATH, filename)
    df = pd.read_csv(path)
    print(f"{filename} loaded → {df.shape}")
    return df


def main():
    # Load datasets
    customers = load_csv("olist_customers_dataset.csv")
    orders = load_csv("olist_orders_dataset.csv")
    items = load_csv("olist_order_items_dataset.csv")
    payments = load_csv("olist_order_payments_dataset.csv")

    print("\nMerging datasets...")

    # Merge customers + orders
    df = pd.merge(
        orders,
        customers,
        on="customer_id",
        how="left"
    )

    # Merge items
    df = pd.merge(
        df,
        items,
        on="order_id",
        how="left"
    )

    # Merge payments
    df = pd.merge(
        df,
        payments,
        on="order_id",
        how="left"
    )

    print("Final merged shape:", df.shape)

    # Save master dataset
    output_path = os.path.join(
        PROCESSED_PATH,
        "master_data.csv"
    )

    df.to_csv(output_path, index=False)

    print(f"Saved → {output_path}")


if __name__ == "__main__":
    main()