import pandas as pd


class Optimiser:

    @staticmethod
    def compute_optimal_consumption(
            appliance_df: pd.DataFrame, 
            category_df: pd.DataFrame, 
            total_expected_consumption: float):

        cons_appliance_df = None
        total_consumption = None
        
        return cons_appliance_df, total_consumption