import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df['temp'].tolist()
dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_dev = statistics.stdev(dataset)
print('mean of sample', mean)
print('standard deviation of sample',std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['temp'],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(40)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

population_mean = statistics.mean(data)
print("population mean is equal to", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(40)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("standard deviation", std_deviation)

standard_deviation()

