import pandas as pd
import matplotlib.pyplot as plt


HISTORY_FILE = "data/crypto_history.csv"


# ==============================================
# LOAD HISTORICAL DATA
# ==============================================

df = pd.read_csv(HISTORY_FILE)

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"]
)

df["Price_Value"] = (
    df["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)


print("Historical data loaded successfully!")


# ==============================================
# SELECT CRYPTOCURRENCY
# ==============================================

print("\nAvailable cryptocurrencies:")

crypto_list = df["Name"].unique()

for i, crypto in enumerate(crypto_list, start=1):

    print(f"{i}. {crypto}")


choice = int(
    input(
        "\nEnter cryptocurrency number: "
    )
)


selected_crypto = crypto_list[choice - 1]


# ==============================================
# FILTER SELECTED CRYPTOCURRENCY
# ==============================================

crypto_df = df[
    df["Name"] == selected_crypto
].copy()


crypto_df = crypto_df.sort_values(
    "Timestamp"
)


# ==============================================
# DISPLAY DATA
# ==============================================

print(
    f"\nPrice history for "
    f"{selected_crypto}:"
)

print("----------------------------------------------")

print(
    crypto_df[
        [
            "Timestamp",
            "Price"
        ]
    ].to_string(index=False)
)


# ==============================================
# TREND ANALYSIS
# ==============================================

first_price = crypto_df.iloc[0]["Price_Value"]

latest_price = crypto_df.iloc[-1]["Price_Value"]

price_change = latest_price - first_price

percentage_change = (
    price_change / first_price
) * 100


print("\n==============================================")
print("          TREND ANALYSIS")
print("==============================================")

print(f"Cryptocurrency : {selected_crypto}")

print(f"First Price    : ${first_price:,.2f}")

print(f"Latest Price   : ${latest_price:,.2f}")

print(f"Price Change   : ${price_change:,.2f}")

print(
    f"Percentage     : {percentage_change:.2f}%"
)


if price_change > 0:

    print("Trend          : UP 📈")

elif price_change < 0:

    print("Trend          : DOWN 📉")

else:

    print("Trend          : NO CHANGE ➡️")

print("==============================================")



# ==============================================
# CREATE PRICE TREND GRAPH
# ==============================================

plt.figure(figsize=(10, 5))

plt.plot(
    crypto_df["Timestamp"],
    crypto_df["Price_Value"],
    marker="o"
)

plt.title(
    f"{selected_crypto} Price Trend"
)

plt.xlabel("Time")

plt.ylabel("Price ($)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()