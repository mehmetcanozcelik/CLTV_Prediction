import pandas as pd

from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter


def cltv_prediction(df):
    df = df[(df['net_order_count'] > 1)]  # Only regular customers (more than 1 order) are included in the analysis.

    df['recency'] = df['order_date_diff'] / 7   # Calculations should be weekly. Order Date Diff means date difference in days between customers first and last order.
    df['T'] = df['days_since_first_order'] / 7


    # BG/NBD Model for Expected Number of Transaction #

    bgf = BetaGeoFitter(penalizer_coef=0.001)


    # Fit the BGF model with "Net Order Count", "Recency" and "T (Time since the customer's first order [Customer Age]) values.
    bgf.fit(df['net_order_count'],
            df['recency'],
            df['T'])

    # Predict these values for next 1 week or 1 month.
    df["expected_purchase_1_week"] = bgf.predict(1,
                                                 df['net_order_count'],
                                                 df['recency'],
                                                 df['T'])

    df["expected_purchase_1_month"] = bgf.predict(4,
                                                  df['net_order_count'],
                                                  df['recency'],
                                                  df['T'])

    # Gamma&Gamma Sub Model for Expected Revenue #
    ggf = GammaGammaFitter(penalizer_coef=0.01)

    # Fit the GGF model with "Net Order Count", and "Net AVG Revenue" values.
    ggf.fit(df['net_order_count'], df['net_avg_revenue'])

    # Predict these values for next 1 week or 1 month.
    df["expected_avg_revenue"] = ggf.conditional_expected_average_profit(df['net_order_count'], df['net_avg_revenue'])

    # Predict CLTV value for next 1 week or 1 month.

    df["predicted_cltv"] = ggf.customer_lifetime_value(bgf,
                                                       df['net_order_count'],
                                                       df['recency'],
                                                       df['T'],
                                                       df['net_avg_revenue'],
                                                       time=1,
                                                       freq="W")

    df = df.sort_values("predicted_cltv", ascending=False)
    df.to_excel("NEW_DATASET_predicted_cltv.xlsx")


def cltv_prediction_main ():
    df_ = pd.read_excel("customers_YOUR_DATASET.xlsx")
    df = df_.copy()
    pd.set_option('display.max_columns', None)
    cltv_prediction(df)
