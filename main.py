import pandas as pd
import os
import time
from datetime import datetime

from scraper import scrape_top_coins


# ==============================================
# SETTINGS
# ==============================================

MONITOR_INTERVAL = 60  # 60 seconds


# ==============================================
# FILTER SETTINGS
# ==============================================

print("==============================================")
print("        CRYPTOCURRENCY FILTER SETTINGS")
print("==============================================")

try:
    min_change = float(
        input("Enter minimum 24h change (%): ")
    )
except ValueError:
    min_change = 0

try:
    min_price = float(
        input("Enter minimum price ($): ")
    )
except ValueError:
    min_price = 0


# ==============================================
# START MONITORING
# ==============================================

print("\n==============================================")
print("     CRYPTOCURRENCY PRICE TRACKER")
print("==============================================")

print("\nAutomatic monitoring started...")
print("Update interval:", MONITOR_INTERVAL, "seconds")
print("Press Ctrl + C to stop.\n")


try:

    while True:

        print("\n==============================================")
        print("        NEW CRYPTOCURRENCY UPDATE")
        print("==============================================")


        # ------------------------------------------
        # STEP 1: SCRAPE DATA
        # ------------------------------------------

        data = scrape_top_coins()


        if not data:

            print("\nNo cryptocurrency data collected.")
            print("Trying again after 60 seconds...")

            time.sleep(MONITOR_INTERVAL)

            continue


        # ------------------------------------------
        # STEP 2: ADD TIMESTAMP
        # ------------------------------------------

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        for coin in data:

            coin["Timestamp"] = timestamp


        # ------------------------------------------
        # STEP 3: CREATE DATAFRAME
        # ------------------------------------------

        df = pd.DataFrame(data)


        print("\n--- DATAFRAME ---")

        print(df)


        # ------------------------------------------
        # STEP 4: CREATE DATA FOLDER
        # ------------------------------------------

        os.makedirs("data", exist_ok=True)


        # ------------------------------------------
        # STEP 5: SAVE LATEST CSV
        # ------------------------------------------

        latest_file = "data/crypto_data.csv"

        df.to_csv(
            latest_file,
            index=False
        )

        print("\nLatest CSV file saved successfully!")


        # ------------------------------------------
        # STEP 6: SAVE HISTORY
        # ------------------------------------------

        history_file = "data/crypto_history.csv"

        file_exists = os.path.exists(
            history_file
        )


        df.to_csv(
            history_file,
            mode="a",
            header=not file_exists,
            index=False
        )

        print("Historical data saved successfully!")


        # ------------------------------------------
        # STEP 7: CONVERT VALUES
        # ------------------------------------------

        df["Price_Value"] = (
            df["Price"]
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float)
        )


        df["Change_Value"] = (
            df["24h Change"]
            .str.replace("%", "", regex=False)
            .astype(float)
        )


        # ------------------------------------------
        # STEP 8: 24H CHANGE FILTER
        # ------------------------------------------

        print("\n==============================================")
        print("       24H CHANGE FILTER")
        print("==============================================")


        change_filtered_df = df[
            df["Change_Value"] > min_change
        ]


        print(
            f"Cryptocurrencies with "
            f"24h Change > {min_change}%:"
        )

        print("----------------------------------------------")


        if change_filtered_df.empty:

            print("No cryptocurrencies found.")

        else:

            for _, coin in change_filtered_df.iterrows():

                print(
                    f"{coin['Name']} "
                    f"({coin['Symbol']})"
                )

                print(
                    f"Price      : "
                    f"{coin['Price']}"
                )

                print(
                    f"24h Change : "
                    f"{coin['24h Change']}"
                )

                print("----------------------------------------------")


        # ------------------------------------------
        # STEP 9: PRICE FILTER
        # ------------------------------------------

        print("\n==============================================")
        print("          PRICE FILTER")
        print("==============================================")


        price_filtered_df = df[
            df["Price_Value"] > min_price
        ]


        print(
            f"Cryptocurrencies with "
            f"Price > ${min_price}:"
        )

        print("----------------------------------------------")


        if price_filtered_df.empty:

            print("No cryptocurrencies found.")

        else:

            for _, coin in price_filtered_df.iterrows():

                print(
                    f"{coin['Name']} "
                    f"({coin['Symbol']})"
                )

                print(
                    f"Price      : "
                    f"{coin['Price']}"
                )

                print(
                    f"24h Change : "
                    f"{coin['24h Change']}"
                )

                print("----------------------------------------------")


        # ------------------------------------------
        # STEP 10: REMOVE HELPER COLUMNS
        # ------------------------------------------

        df.drop(
            columns=[
                "Price_Value",
                "Change_Value"
            ],
            inplace=True
        )


        # ------------------------------------------
        # STEP 11: WAIT
        # ------------------------------------------

        print("\n==============================================")

        print(
            f"Next update in "
            f"{MONITOR_INTERVAL} seconds..."
        )

        print("Press Ctrl + C to stop.")

        print("==============================================")


        time.sleep(MONITOR_INTERVAL)


except KeyboardInterrupt:

    print("\n\n==============================================")
    print("      MONITORING STOPPED BY USER")
    print("==============================================")

    print(
        "Cryptocurrency Price Tracker stopped."
    )