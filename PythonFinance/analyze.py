import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
import pandas as pd

import numpy as np
import pickle

#Machine learning modules
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

style.use('ggplot')

def visualize_data():
    df = pd.read_csv('sp500_joined_close.csv')
    """
    df['BA'].plot()
    plt.tight_layout()
    plt.show()
    """
    df_corr = df.corr()
    print(df_corr.head())

    sns.heatmap(df_corr,annot=True)
    plt.show()


def process_data_for_labels():
    #df = pd.read_csv('stock_dfs/%s.csv' % ticker)
    df = pd.read_csv('sp500_joined_close.csv', index_col=0)
    tickers= df.columns.values.tolist()
    df.fillna(0,inplace=True)

    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = .03
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0

def extract_featuresets():
    df = pd.read_csv('sp500_joined_close.csv', index_col=0)
    tickers = df.columns
    hm_days=7
    df_change = pd.DataFrame()
    for i in range(1,hm_days+1):
        for ticker in tickers: 
            df_change['{}_{}d'.format(ticker,i)] = df[ticker].pct_change(periods=hm_days)
    df_change.fillna(0,inplace=True)

    df_reco = pd.DataFrame()
    for ticker in tickers:
        df_reco['{}_7'.format(ticker)] = df_change['{}_{}d'.format(ticker,7)].apply(buy_sell_hold)
    df_reco.fillna(0,inplace=True)

    return df_change, df_reco

def do_ml(df_change, df_reco,ticker):
    """
    1. Get X, y     #y is the target (-1,0,1), X is the pct_change values
    2. Train_test_split
    3. Classifer (KNN,RFC)
    """
    list = []
    for i in range(1,8):
        list.append('{}_{}d'.format(ticker,i))
    X = df_change[list][:-1]
    y = df_reco['{}_7'.format(ticker)][1:]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    clf = VotingClassifier([('svc', SVC()), 
    ('rfc',RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy:', confidence)
    predictions = clf.predict(X_test)

    print(confusion_matrix(y_test,predictions))
    print('\n')
    print(classification_report(y_test, predictions))



if __name__=='__main__':
    df_change, df_reco = extract_featuresets()
    do_ml(df_change, df_reco,'MMM')