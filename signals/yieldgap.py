import matplotlib.pyplot as plt
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df_1 = pd.read_csv('C:/Users/Mnguyen/LGSS/Investments Team - SandPits - SandPits/data/input/vendors/fred/2021-03.csv', skiprows=[1])

    df_2 = df_1[['sasdate', 'S&P 500', 'S&P: indust', 'S&P div yield', 'S&P PE ratio', 'GS10']]

    df_2['S&P EP ratio'] = (1/df_2['S&P PE ratio'])*100

    df_2['yield gap'] = df_2['S&P EP ratio'] - df_2['GS10']

    df_3 = df_2[['sasdate', 'S&P EP ratio', 'GS10']].set_index('sasdate')

    df_3.plot()

    df_4 = df_2[['sasdate', 'yield gap']].set_index('sasdate')

    df_4.plot()
