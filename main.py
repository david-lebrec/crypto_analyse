import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 21000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
pd.options.display.float_format = '{:,.0f}'.format


def read_csv():
    dataset = pd.read_csv('consolidated_coin_data_prepared.csv')
    return dataset


def obtenir_type_crypto(dataset):
    return dataset['Currency'].unique()


def convertir_time(dataset):
    dataset['format_date'] = pd.to_datetime(dataset['Date'])
    return dataset


def graphs_crypto_evolution(dataset):
    tab_crypto = obtenir_type_crypto(dataset)
    for nom_crypto in tab_crypto:
        dataset_crypto = dataset[dataset['Currency'] == nom_crypto].sort_values(['format_date'])
        plt.plot(dataset_crypto['format_date'], dataset_crypto['Close'])
        plt.title('evolution du prix de ' + nom_crypto)
        plt.show()


def transform_string_int(dataset):
    dataset['Volume'] = dataset['Volume'].str.replace(',', '')
    dataset['Volume'] = pd.to_numeric(dataset['Volume'], errors='coerce')
    return dataset


def trouver_max_vol_tezos(dataset):
    dataset_tezos = dataset[dataset['Currency'] == 'tezos']
    return dataset_tezos['Volume'].max()


def graphs_volume_evolution(dataset):
    tab_crypto = obtenir_type_crypto(dataset)
    for nom_crypto in tab_crypto:
        dataset_crypto = dataset[dataset['Currency'] == nom_crypto].sort_values(['format_date'])
        print(dataset_crypto['Volume'])
        plt.plot(dataset_crypto['format_date'], dataset_crypto['Volume'])
        plt.title('evolution du Volume de ' + nom_crypto)
        plt.savefig(nom_crypto + '_volume.png')
        plt.show()


if __name__ == '__main__':
    dataset = read_csv()
    dataset2 = convertir_time(dataset)
    dataset2.to_csv('consolidated_coin_data_prepared2.csv', index=False)
    print(obtenir_type_crypto(dataset2))
    graphs_crypto_evolution(dataset2)
    dataset3 = transform_string_int(dataset2)
    graphs_volume_evolution(dataset3)
    print(trouver_max_vol_tezos(dataset3))
