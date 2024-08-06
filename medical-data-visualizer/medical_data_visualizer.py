import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv("medical_examination.csv")

# 2 Create the overweight column in the df variable
# To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
# If that value is > 25 then the person is overweight. 
# Use the value 0 for NOT overweight and the value 1 for overweight. 
df['overweight'] = np.where((df['weight']/(df['height']*df['height'])*10000) > 25,1,0)

# 3 Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0.
# If the value is more than 1, set the value to 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1).astype(int)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1).astype(int)

# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot with values from cholesterol, gluc, smoke, alco, active, and overweight.
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # 6 Group and reformat the data in df_cat to split it by cardio.
    # Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio','variable','value']).size().reset_index(name="total"))

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features 
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        order=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )

    fig.savefig('catplot.png') 
    return fig


# 8 Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 9 Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data
    df_heat = df.loc[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 10 Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr()

    # 11 Generate a mask for the upper triangle and store it in the mask variable
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 12 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # 13 Plot the correlation matrix
    ax = sns.heatmap(
        corr,
        mask=mask,
        vmax=0.4,
        square=True,
        fmt=".1f",
        annot=True,
    )

    fig.savefig('heatmap.png') 
    return fig