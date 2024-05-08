from filer import Filer
import pandas as pd
from organizer import Organizer
import sys
from config import COLORS

FILE1 = None
FILE2 = None
# FILE1 = './spreadsheets/dados.xlsx'
# FILE2 = './spreadsheets/Codigos_de_cancelamento.xlsx'

if __name__ == "__main__":
    # abre o excel
    filer = Filer()
    organizer = Organizer()

    df = filer.run(FILE1)
    df_cancel = filer.run(FILE2)
    
    #organiza o excel em três planilhas diferentes
    df_destinatarios, df_fornecedores, df_nfe = organizer.run(df)

    # faz um merge com a planilha com motivos de cancelamento
    df_nfe['Código de Cancelamento'] = df_nfe['Código de Cancelamento'].fillna(0).astype(int)
    df_resultado = pd.merge(df_nfe, df_cancel,left_on='Código de Cancelamento', right_on='Código', how='left')
    df_resultado = df_resultado.drop(columns=['Código de Cancelamento'])

    if '--save' in sys.argv:
        organizer.save_df(df_destinatarios, './spreadsheets/nfe-destinatarios.xlsx')
        organizer.save_df(df_fornecedores, './spreadsheets/nfe-fornecedores.xlsx')
        organizer.save_df(df_resultado, './spreadsheets/nfe.xlsx')
    else:
        print(COLORS['blue'] + "CHOOSE:\t  Do you want to save the organization result?:\n" + COLORS['reset'])
        print(COLORS['blue'] + "\t 1." + COLORS['blue'] + " Yes"+ COLORS['reset'])
        print(COLORS['blue'] + "\t 2." + COLORS['blue'] + " No"+ COLORS['reset'])
        val = int(input(COLORS['blue'] + "ACTION:\t  Choose a number: "+ COLORS['reset']))
        while val < 1 or val > 2:
            print(COLORS['red'] + f"ERROR:\t  You didn't specify a valid file number."+ COLORS['reset'])
            val = int(input(COLORS['blue'] + "ACTION:\t  Choose a valid number: "+ COLORS['reset']))
        if val == 1:
            organizer.save_df(df_destinatarios, './spreadsheets/nfe-destinatarios.xlsx')
            organizer.save_df(df_fornecedores, './spreadsheets/nfe-fornecedores.xlsx')
            organizer.save_df(df_resultado, './spreadsheets/nfe.xlsx')
    print("Destinatários: ")
    print(df_destinatarios)
    print("Fornecedores: ")
    print(df_fornecedores)
    print("Notas Fiscais: ")
    print(df_resultado)



