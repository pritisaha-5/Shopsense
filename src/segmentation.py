import pandas as pd
import datetime as dt


def segment_customer(row):
    score = int(row["R_score"]) + int(row["F_score"])

    if score >= 8:
        return "Champion"
    elif score >= 6:
        return "Loyal"
    elif score >= 4:
        return "Potential"
    elif score >= 3:
        return "At Risk"
    else:
        return "Lost"


def main():
    df = pd.read_csv("data/processed/cleaned_data.csv")

    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )

    snapshot_date = (
        df["order_purchase_timestamp"].max()
        + dt.timedelta(days=1)
    )

    rfm = df.groupby("customer_unique_id").agg({
        "order_purchase_timestamp":
            lambda x: (snapshot_date - x.max()).days,
        "order_id": "nunique",
        "payment_value": "sum"
    })

    rfm.columns = [
        "Recency",
        "Frequency",
        "Monetary"
    ]

    rfm["R_score"] = pd.qcut(
        rfm["Recency"],
        5,
        labels=[5,4,3,2,1]
    )

    rfm["F_score"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        5,
        labels=[1,2,3,4,5]
    )

    rfm["M_score"] = pd.qcut(
        rfm["Monetary"],
        5,
        labels=[1,2,3,4,5]
    )

    rfm["Segment"] = rfm.apply(
        segment_customer,
        axis=1
    )

    print("\nSegment Count:")
    print(
        rfm["Segment"].value_counts()
    )

    rfm.to_csv(
        "data/processed/rfm_data.csv"
    )

    print("\nSaved → data/processed/rfm_data.csv")


if __name__ == "__main__":
    main()