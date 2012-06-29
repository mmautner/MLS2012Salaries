#!/usr/bin/python

"""
mls.csv - a simple script for analyzing MLS player base salaries

By: Max Mautner, max.mautner@gmail.com
Edited: June 28, 2012
"""

def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i # assume first-line headers

if __name__=="__main__":
    import csv, pdb
    import matplotlib.pyplot as plt
    import numpy as np

    filename = 'mls.csv'
    num_of_rows = file_len(filename)
    num_of_cols = 5
    str_cols = [0,1,2]
    salary_cols = [3,4]
    str_data = np.array([['' for h in xrange(len(str_cols))] \
                        for i in xrange(num_of_rows)], dtype='|S25')
    salary_data = np.zeros((num_of_rows, len(salary_cols)), dtype=float)
    with open('mls.csv','r') as f:
        # read first line into 'headers'
        headers = f.readline()
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            str_data[i,:] = [row[c] for c in str_cols]
            salary_data[i,:] = [float(row[c]) for c in salary_cols]

    team_names = np.unique(str_data[:,0])
    #position_names = np.unique(str_data[:,2])
    position_names = np.array(['GK','D','M','F'])

    # by team: 
    fig = plt.figure(figsize=(10,6))
    fig.canvas.set_window_title('Team Salaries')
    ax1 = fig.add_subplot(111)
    bp = plt.boxplot([salary_data[str_data[:,0]==team, 0] for team \
                in team_names], 0, '')
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', 
                alpha=0.5)
    ax1.set_axisbelow(True)
    ax1.set_title('MLS Base Salaries by Team (2012)')
    ax1.set_xlabel('Teams')
    ax1.set_ylabel('Base Salary')
    xtickNames = plt.setp(ax1, xticklabels=team_names)
    plt.setp(xtickNames, rotation=45, fontsize=8)

    # by position:
    fig = plt.figure(figsize=(10,6))
    fig.canvas.set_window_title('Position Salaries')
    ax1 = fig.add_subplot(111)
    bp = plt.boxplot([salary_data[str_data[:,2]==position, 0] for position \
                in position_names], 0, '')
    ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', 
                alpha=0.5)
    ax1.set_axisbelow(True)
    ax1.set_title('MLS Base Salaries by Position (2012)')
    ax1.set_xlabel('Positions')
    ax1.set_ylabel('Base Salary')
    xtickNames = plt.setp(ax1, xticklabels=['Keeper','Defender','Middie','Forward'])
    plt.setp(xtickNames, fontsize=10)

    plt.show()
