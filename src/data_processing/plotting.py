
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import argparse

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_file(input):
    ''' Plot the data in a single raw data csv file. '''
    file = Path(input)
    df = pd.read_csv(file, header=None)
    df = df.T
    print('Number of data points in the file:', df.shape[0])
    df.plot(subplots=True, ylim=(0,3), yticks=(0,1,2,3), legend=False, color='steelblue')
    plt.show()

def plot_dataset(input):
    ''' Analyse and plot the input dataset csv file. '''
    df = pd.read_csv(input, header=None)
    print('Input data shape:', df.shape)
    print('min is',np.min(df.iloc[:][1:].values))
    print('max is',np.max(df.iloc[:][1:].values))
    print('mean is',np.mean(df.iloc[:][1:].values))
    plt.figure(1)
    df[0].value_counts().plot(kind='bar')
    plt.suptitle('0: Negative scent sample, 1: Positive scent sample')
    plt.show()
    plt.figure(2)
    plt.suptitle('Some example time series')
    i = int(np.round(np.random.random_sample()*df.shape[0]/3))
    i = i * 3
    df.iloc[i][1:].plot(label='Sample '+str(i)+' class: '+str(df.iloc[i][0]))
    i = i+1
    df.iloc[i][1:].plot(label='Sample '+str(i)+' class: '+str(df.iloc[i][0]))
    i = i+1
    df.iloc[i][1:].plot(label='Sample '+str(i)+' class: '+str(df.iloc[i][0]))
    plt.legend()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Print information and plots that describe the input file')
    parser.add_argument('type', help='type of data file - raw or dataset', choices=['raw', 'dataset'])
    parser.add_argument('input', help='input path to a csv file')
    args = parser.parse_args()
    if args.type == 'raw':
        plot_file(args.input)
    else:
        plot_dataset(args.input)

main()