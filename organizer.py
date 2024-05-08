import pandas as pd
from filer import Filer
from config import COLORS

class Organizer:
    def __init__(self):
        self.app_name = "The Organizer"
        self.app_description = "The Organizer is a program to organize a spreadsheet"

    def __separator(self, df: pd.DataFrame, separator: str = ';')-> pd.DataFrame:
        columns = df.columns.tolist()[0].split(separator)
        new_df = pd.DataFrame(columns=columns)
        for i in range(len(df)):
            new_df.loc[i] = df.iloc[i, 0].split(separator)
        print(COLORS['blue'] + "INFO:\t  Separated the dataframe from one column to several."+ COLORS['reset'])
        return new_df

    def __turn_NA(self, df: pd.DataFrame) -> pd.DataFrame:
        df[df == ""] = pd.NA
        print(COLORS['blue'] + "INFO:\t  Changed DataFrame values from '' to NaN."+ COLORS['reset'])
        return df

    def __remove_null_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        null_per_col = df.isnull().sum()
        col_null = null_per_col[null_per_col == len(df)].index.tolist()
        new_df = df.drop(columns=col_null)
        print(COLORS['blue'] + "INFO:\t  Removed null columns from DataFrame."+ COLORS['reset'])
        return new_df

    def __filter_df(self, df: pd.DataFrame, columns_not: list[str]) -> pd.DataFrame:
        new_df = df.drop(columns=columns_not)
        print(COLORS['blue'] + f"INFO:\t  Filtered DataFrame removing specific columns."+ COLORS['reset'])
        return new_df

    def save_df(self, df: pd.DataFrame, name: str) -> bool:
        df.to_excel(name,index=False)
        print(COLORS['blue'] + f"INFO:\t  Saved DataFrame in {name}."+ COLORS['reset'])
        return True
    
    def run(self, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        #transforma os dados de csv de coluna unica em um excel.
        df = self.__separator(df)

        #faz com que todos os dados vazios (strings vazias) sejam NaN
        df = self.__turn_NA(df)

        #remove as colunas que não possuem dados
        df = self.__remove_null_columns(df)

        #separa os dados de fornecedores e destinatários das notas ficais
        columns_not = [
            col for col in df.columns if 'Fornecedor' not in col and col != 'Número da NF-e'
        ]
        df_fornecedores = self.__filter_df(df, columns_not)

        columns_not = [
            col for col in df.columns if 'Destinatário' not in col and col != 'Número da NF-e'
        ]
        df_destinatarios = self.__filter_df(df, columns_not)

        columns_not = [
            col for col in df.columns if 'Destinatário' in col or 'Fornecedor' in col
        ]
        df_nfe = self.__filter_df(df, columns_not)

        return df_destinatarios, df_fornecedores, df_nfe

if __name__ == '__main__':
    df = Filer().run()
    Organizer().run(df)