import sys
import os
import pandas as pd
from config import COLORS

"""
Class responsible for opening the file with a spreadsheet and transforming it into a Pandas Dataframe. 
"""
class Filer():
    def __init__(self):
        self.app_name = "The Filer"
        self.app_description = "The Filer is a program to open a spreadsheet"
        self.file_char = ""
    
    def __open_file(self, filename: str) -> pd.DataFrame | None:
        try:
            if filename.endswith('.csv'):
                file = self.__open_csv(filename)
            elif filename.endswith('.xlsx'):
                file = self.__open_excel(filename)
            else:
                print(COLORS['red'] + f"ERROR:\t  The file '{filename}' is not a valid CSV or Excel file."+ COLORS['reset'])
                return None
        except Exception as e:
            print(COLORS['red'] + f"ERROR:\t  An error occurred while opening the file '{filename}': {str(e)}"+ COLORS['reset'])
            return None
        print(COLORS['blue'] +f"INFO:\t  File '{filename}' opened successfully."+ COLORS['reset'])
        return file
    
    def __open_csv(self, filename: str)-> pd.DataFrame:
        return pd.read_csv(filename)
    
    def __open_excel(self, filename: str)-> pd.DataFrame:
        return pd.read_excel(filename)
    
    def __get_filename(self) -> str | None:
        params = sys.argv
        if '--file' in params:
            if params.index('--file') + 1 > len(params):
                print(COLORS['red'] + f"ERROR:\t  Missing the file name right after the '--file' flag."+ COLORS['reset'])
                return None
            filename = params[params.index('--file') + 1]
            del params[params.index('--file') + 1]
        else:
            print(COLORS['blue'] + f"CHOOSE:\t  Please, choose a {self.file_char} file in 'spreadsheets' folder:\n"+ COLORS['reset'])
            folder_list = os.listdir('./spreadsheets/')
            folder_list = [s for s in folder_list if '.xlsx' in s or '.csv' in s]
            for i in range(len(folder_list)):
                print(COLORS['white'] + f"\t{i + 1}." + COLORS['blue'] +  f" {folder_list[i]}"+ COLORS['reset'])
            
            file_index = 0
            file_index = int(input(COLORS['blue'] + "ACTION:\t  Choose a number: "+ COLORS['reset']))
            while file_index < 1 or file_index > len(folder_list):
                print(COLORS['red'] + f"ERROR:\t  You didn't specify a valid file number."+ COLORS['reset'])
                file_index = int(input(COLORS['blue'] + "ACTION:\t  Choose a valid number: "+ COLORS['reset']))
            filename = "./spreadsheets/" + folder_list[file_index - 1]
        return filename
    def run(self, filename: str = None, file_char: str = "") -> pd.DataFrame:
        self.file_char = file_char
        if filename is None:
            filename = self.__get_filename()
            if filename is None:
                return
        return self.__open_file(filename)

if __name__ == "__main__":
    Filer().run()