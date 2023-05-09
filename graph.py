import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
import time

#import os
#clear = lambda: os.system('cls')
#clear()

def graphDaily():
    with open('registos/diario.txt') as f:
        data = f.read()

    sales_dict = json.loads(data)
    #print(sales_dict)

    df = pd.DataFrame(sales_dict)

    df['continente'] = pd.to_numeric(df['continente'])
    df['auchan'] = pd.to_numeric(df['auchan'])
    df['aperinha'] = pd.to_numeric(df['aperinha'])
    df['minipreco'] = pd.to_numeric(df['minipreco'])

    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

    #df['data'] = pd.to_datetime(df['data'])
    df.head()

    print(df)


    time.sleep(0.2)

    #data.plot(kind='bar', x='area', y=['direct', 'telesales'], title='Sales by Area')
    #df.plot(x='data', title = 'Direct vs Tele sales', colormap = 'viridis');

    df.plot(x='data', colormap = 'viridis');
    plt.savefig('site/graph.png')

    #plt.show()



    #x = np.linspace(0, 10, 5)

    #y = [0, 1, 2, 3, 4]
    #y2 = [1, 3, 4, 6, 5]
    #y3 = [2, 2, 2, 3, 2]

    #plt.plot(x, y, label='sin(x)')
    #plt.plot(x, y2, label='cos(x)')
    #plt.plot(x, y3, label='tan(x)')
    #plt.legend()




