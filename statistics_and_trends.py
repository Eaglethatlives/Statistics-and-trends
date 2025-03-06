"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
"""
This code gives a graphical representation of makeup brand color 
properties using statistical and graphical methods.
It includes functions for data preprocessing, 
visualization, and analysis.
Ensure that the dataset ('data.csv') is 
present in the working directory.
"""
from corner import corner
 import matplotlib.pyplot as plt
 import numpy as np
 import pandas as pd
 import scipy.stats as ss
 import seaborn as sns


 def plot_relational_plot(df):
    """This creates scatter plots"""
   
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))  
    ax = ax.flatten()  
    plot_pairs = [('H', 'S'), ('H', 'V'), ('S', 'V')]  
    titles = ['MAC Brands Hue (H) vs. Saturation (S)', 'Fenty Brands Hue (H) vs. Value (V)', 'Revlon Brands Saturation (S) vs. Hue (H)']
    colors = ['purple', 'pink', 'yellow']
    for i, ((x_col, y_col), title, color) in enumerate(zip(plot_pairs, titles, colors)):
        sns.scatterplot(x=df[x_col], y=df[y_col], alpha=0.5, color=color, ax=ax[i])
        ax[i].set_title(title)
        ax[i].set_xlabel(x_col)
        ax[i].set_ylabel(y_col)
    fig.delaxes(ax[3])
    plt.tight_layout()
    plt.savefig('relational_plot.png')
    plt.show()
   
   
def plot_categorical_plot(df):
    """This creates count plots"""
    fig, ax = plt.subplots(figsize=(10, 12), dpi=144)
    sns.countplot(y='brand', data=df,hue='group',palette='viridis', ax=ax)
    ax.set_title("Number of MakeUp Products by Brand", fontsize=16)
    ax.set_xlabel("Count", fontsize=12)
    ax.set_ylabel("Brand", fontsize=12)
    plt.tight_layout()
    plt.show()
     
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='brand', y='L',hue='group', data=df, errorbar=None, palette=[
    "pink", "yellow", "blue", "purple", "black", "brown", "red", "orange"])
    plt.title("A Bar Plot for Average Lightness (L) for different MakeUp Brands", fontsize=16)
    plt.xlabel("Brand", fontsize=12)
    plt.ylabel("Average Lightness (L)", fontsize=12)
    plt.xticks(rotation=50, ha='right')
    plt.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')  
    plt.tight_layout()
    plt.savefig("categorical_plot.png")  
    plt.show()
    brands = [30, 25, 20, 15, 10]  
    labels = ['MAC', 'Fenty', 'bareminerals', 'Revlon', 'Dior']  # Category labels
    plt.figure(dpi=144)
    plt.pie(brands, labels=labels, autopct='%1.1f%%', startangle=140, colors=
    ['#ff0000','#66b4ff', '#99ff99', '#ffcc99', '#445bbb'])
    plt.title('Pie chart of Largest Make-Up brands ')
    plt.axis('equal')
    plt.show()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    """ This section creates histograms"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Subplots for MakeUp Products ", fontsize=16)
    
    ax1.hist(df['H'], bins=20, color='blue', edgecolor='black')
    ax1.set_title("Distribution of Hue in MAC Products ")
    ax1.set_xlabel("Hue (H)")
    ax1.set_ylabel("Frequency")
    
    ax2.hist(df['S'], bins=20, color='green', edgecolor='black')
    ax2.set_title("Distribution of Saturation in Maybelline products")
    ax2.set_xlabel("Saturation (S)")
    ax2.set_ylabel("Frequency")
    
    ax3.hist(df['S'], bins=20, color='purple', edgecolor='black')
    ax3.set_title("Distribution of Saturation in Fenty products")
    ax3.set_xlabel("Saturation (S)")
    ax3.set_ylabel("Frequency")
    
    ax4.hist(df['L'], bins=20, color='red', edgecolor='black')
    ax4.set_title("Distribution of Lightness in baremineral Products")
    ax4.set_xlabel("Lightness (L)")
    ax4.set_ylabel("Frequency")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('statistical_plot.png')
    plt.show()
    return


def statistical_analysis(df, col: str):
    """Calculates statistical moments (mean, standard 
    deviation, skewness, and kurtosis)"""
    mean = df[col].mean()
    stddev = df[col].std()
    skew = df[col].skew()
    excess_kurtosis = df[col].kurt()
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """This section is for preprocessing data """
    df.describe()
    print("Index of the DataFrame (brand):")
    print(df.index)  
    print("\nFirst few rows of the DataFrame:")
    print(df.head())  
    df = df.dropna()
    return df


def writing(moments, col):
    """Writes and interprets statistical moments in a human-readable format."""
    mean, stddev, skew, excess_kurtosis = moments
    print(f'For the attribute {col}:')
    print(f'Mean = {mean:.2f}, '
          f'Standard Deviation = {stddev:.2f}, '
          f'Skewness = {skew:.2f}, and '
          f'Excess Kurtosis = {excess_kurtosis:.2f}.')
   
    if skew > 2:
       skew = "right-skewed"
    elif skew < -2:
       skew = "left-skewed"
    else:
       skew = "not skewed"

    if excess_kurtosis > 1:
       excess_kurtosis= "leptokurtic"
    elif excess_kurtosis < -1:
      excess_kurtosis = "platykurtic"
    else:
       excess_kurtosis = "mesokurtic"
       print('The data was right/left/not skewed and platy/meso/leptokurtic.')
    return


def main():
    """Main function that executes data processing"""
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'H'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
