import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def cltv_calc(dataframe):

    # Purchase Frequency Calculation : TOTAL TRANSACTION / TOTAL NUMBER OF CUSTOMERS (Row number of dataset)
    dataframe["purchase_frequency"] = dataframe["net_order_count"] / dataframe.shape[0]

    # Repeat Rate Calculation : TOTAL NUM of CUSTOMERS who has more than 1 Order / TOTAL NUMBER OF CUSTOMERS
    repeat_rate = dataframe[dataframe.net_order_count > 1].shape[0] / dataframe.shape[0]

    # Churn Rate Calculation :
    churn_rate = 1 - repeat_rate

    # Customer Value Calculation : AVERAGE ORDER VALUE x PURCHASE FREQUENCY
    dataframe["customer_value"] = (dataframe["net_avg_revenue"] * dataframe["purchase_frequency"])

    # CLTV Calculation : (CUSTOMER VALUE / CHURN RATE) x PROFIT MARGIN (In this case profit margin ignored.)
    dataframe["cltv"] = (dataframe["customer_value"] / churn_rate)

    # Segment distribution by CLTV :
    dataframe["segment"] = pd.qcut(dataframe["cltv"].rank(method="first"),4, labels=["D", "C", "B", "A"])

    cltv_dataframe = dataframe.sort_values(by="cltv", ascending=False)
    cltv_dataframe.to_excel("NEW_CLTV_SEGMENTS.xlsx")


def cltv_main():
    pd.set_option('display.max_columns', None)

    df_ = pd.read_excel("YOUR_customer_datamart.xlsx")
    df = df_.copy()
    cltv_calc(df)
