import pandas as pd
from ast import literal_eval


class Optimiser:

    CATEGORIES = ["A", "F", "L"]

    @staticmethod
    def compute_optimal_consumption(
            app_df: pd.DataFrame,
            cat_df: pd.DataFrame,
            total_expected_consumption: float):
        """
        Determine the time each appliance should be on and the associated energy so the total consumption 
        is as close as possible from the targeted energy without overpassing it. 

        Args:
            app_df (pd.DataFrame): dataframe of appliances (colums "category", "power", "name")
            app_df (pd.DataFrame): dataframe of categories with at least column "id", "possible_durations", "power"
            total_expected_consumption (float): target energy that appliances should be consuming but not overpassing 

        Returns:
            pd.DataFrame, float: dataframe of appliances with two new columns "energy", "time"
        """
        # unserialized possible_duration #TODO: pass to specific data management
        cat_df = Optimiser.unserialize_list_column(cat_df, "possible_duration")
        # get power and napps for each category
        cat_power_napp_df = Optimiser.get_category_power_num_app(app_df)
        # get all the possible combinations of duration
        duration_combinations_df = Optimiser.get_duration_combinations(cat_df)
        # extract power values (vector (3, 1)) and possible duration (matrix (n, 3)) 
        power = cat_power_napp_df.loc[Optimiser.CATEGORIES, "power"].values
        duration = duration_combinations_df[Optimiser.CATEGORIES].values
        # compute energy for each duration combination (sum product = matmul)à
        energy = duration @ power
        duration_combinations_df["energy"] = energy

        # determine duration combination with highest energy which is bellow expected
        bellow_expected_consumption_filter = energy<=total_expected_consumption
        optim_idx = duration_combinations_df[bellow_expected_consumption_filter]["energy"].idxmax()
        optim_combination = duration_combinations_df.loc[optim_idx]
        optim_energy = optim_combination["energy"]

        # compute how much time should an appliance of each category be on
        cat_to_num_app = cat_power_napp_df["num_app"].to_dict()
        cat_to_optim_duration = optim_combination[Optimiser.CATEGORIES].to_dict()
        cat_to_appliance_duration = (
            cat_df
            # create column duration and colum num_app
            .assign(duration=cat_df["id"].map(cat_to_optim_duration),
                    num_app=cat_df["id"].map(cat_to_num_app))
            # compute time per appliance of each category$
            .assign(time_appliance=lambda df_: df_["duration"] / df_["num_app"])
            # extract `time_appliance` as dictionary category -> time
            .set_index('id')["time_appliance"].to_dict()
        )
        
        # update appliance dataframe with value of time that it should 
        # be on and corresponding energy consumed
        app_df["time"] = app_df["category"].map(cat_to_appliance_duration)
        app_df["consumption"] = app_df["power"] * app_df["time"]

        return app_df, optim_energy
    
    @staticmethod
    def unserialize_list_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
        """
        Parse the column of a dataframe which is a serialized as list 

        Args:
            df (pd.DataFrame): Dataframe
            column (str): column to unserialize

        Returns:
            pd.DataFrame: Dataframe with updated column
        """
        df[col] = df[col].apply(literal_eval)
        return df
    
    
    @staticmethod
    def get_category_power_num_app(app_df: pd.DataFrame) -> pd.DataFrame:
        """
        Determine the equivalent power per category (sum of power of each appliance) and the number of appliances per category
        
        Args:
            app_df (pd.DataFrame): dataframe of appliances

        Returns:
            pd.DataFrame: DataFrame with index being category and two columns: "power" (float) and "num_app" (int)
        """
        df = (
            app_df
            .groupby("category", as_index=False)
            .agg({"power":"sum", "name": "count"})
            .set_index("category")
            .rename(columns={"name": "num_app"})
        )
        return df

    @staticmethod
    def get_duration_combinations(cat_df: pd.DataFrame) -> pd.DataFrame:
        """
        Determine all the possible combinations of duration possible of the categories

        Args:
            app_df (pd.DataFrame): dataframe of categories with at least column "id", "possible_duration"

        Returns:
            pd.DataFrame: DataFrame with a column for each category. Values are durations and the rows are the combination of durations.
        """
        duration_combinations_df = (
            cat_df
            # set category ids as column and there is one row with the list of possible duration
            .set_index('id')[["possible_duration"]].transpose()
            # perform cartesian product by exploding each category column
            .explode("F").explode("A").explode("L")
            # index is useless, reset it
            .reset_index()
        )
        return duration_combinations_df