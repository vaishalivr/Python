import pandas as pd
import matplotlib.pyplot as plt

df_tags = pd.read_csv('/Users/vaishaliverma/Documents/EDA2/RAW_recipes.csv', nrows= 10000)
df_tags = df_tags.drop(['id', 'contributor_id', 'submitted', 'steps', 'description', 'nutrition', 'n_steps', 'minutes', 'n_ingredients', 'ingredients'], axis=1)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('/Users/vaishaliverma/Documents/EDA2/RAW_recipes.csv', nrows=10000)
df['tags'] = df_tags['tags'].tolist()
nutrition = []

for index, row in df.iterrows():
    row['nutrition'] = eval(row['nutrition'])
    row['nutrition'] = row['nutrition'][:5] + row['nutrition'][6:]
    nutrition.append(row['nutrition'])
df['nutrition'] = nutrition
  

import pandas as pd
from tabulate import tabulate

df_main_dish = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_bev = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_des = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_sd = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_lun = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_br = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_soup = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_sal = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_sau = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_con = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_brd = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_app = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])
df_cu = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])

count_md = 0
count_bev = 0
count_des = 0
count_sd = 0
count_br = 0
count_soup = 0
count_sal = 0
count_sau = 0
count_con = 0
count_brd = 0
count_app = 0
count_cu = 0
count_lun = 0

for index, row in df.iterrows():
    if 'main-dish' in eval(row['tags']):
        df_main_dish.loc[len(df_main_dish.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_md += 1
    elif 'beverages' in row['tags']:
        df_bev.loc[len(df_bev.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_bev += 1
    elif 'desserts' in row['tags']:
        df_des.loc[len(df_des.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_des += 1
    elif 'side-dishes' in row['tags']:
        df_sd.loc[len(df_sd.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_sd += 1
    elif 'lunch' in row['tags']:
        df_lun.loc[len(df_lun.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_lun += 1
    elif 'breakfast' in row['tags']:
        df_br.loc[len(df_br.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_br += 1 
    elif 'soups-stews' in row['tags']:
        df_soup.loc[len(df_soup.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_soup += 1
    elif 'salads' in row['tags']:
        df_sal.loc[len(df_sal.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_sal += 1
    elif 'sauces' in row['tags']:
        df_sau.loc[len(df_sau.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_sau += 1
    elif 'condiments-etc' in row['tags']:
        df_con.loc[len(df_con.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_con += 1
    elif 'breads' in row['tags']:
        df_brd.loc[len(df_brd.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_brd += 1
    elif 'appetizers' in row['tags']:
        df_app.loc[len(df_app.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_app += 1
    elif 'cuisine' in row['tags']:
        df_cu.loc[len(df_cu.index)] = [row['name'], row['nutrition'], row['tags']] 
        count_cu += 1

total = count_md + count_bev + count_des + count_sd + count_br + count_soup + count_sal + count_sau + count_con + count_brd + count_app + count_cu

headers = ['Type', 'Count']
data = [
    ["main-dish", count_md],
    ['beverage', count_bev],
    ['desserts', count_des],
    ['side-dish', count_sd],
    ['breakfast', count_br],
    ['soup', count_soup],
    ['salads', count_sal],
    ['sauces', count_sau],
    ['condiments', count_con],
    ['breads', count_brd],
    ['appetizers', count_app],
    ['cuisine', count_cu],
    ['TOTAL', total]
]

table = tabulate(data, headers, tablefmt="pretty")

df_upto_60mins = pd.DataFrame(columns = ['name', 'nutrition', 'minutes', 'n_ingredients', 'tags'])
for index, row in df.iterrows():
    if '15-minutes-or-less' in eval(row['tags']) or '30-minutes-or-less' in eval(row['tags']) or '60-minutes-or-less' in eval(row['tags']):
        df_upto_60mins.loc[len(df_upto_60mins.index)] = [row['name'], row['nutrition'], row['minutes'], row['n_ingredients'], row['tags']] 

df_md_upto_60mins = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])

for index, row in df_main_dish.iterrows():
    if '15-minutes-or-less' in eval(row['tags']) or '30-minutes-or-less' in eval(row['tags']) or '60-minutes-or-less' in eval(row['tags']):
        df_md_upto_60mins.loc[len(df_md_upto_60mins.index)] = [row['name'], row['nutrition'], row['tags']] 

#df_md_random = df_md_upto_60mins.sample(n=50, replace=False)
df_md_random = df_md_upto_60mins.head(50)
df_app_upto_60mins = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])

for index, row in df_app.iterrows():
    if '15-minutes-or-less' in eval(row['tags']) or '30-minutes-or-less' in eval(row['tags']) or '60-minutes-or-less' in eval(row['tags']):
        df_app_upto_60mins.loc[len(df_app_upto_60mins.index)] = [row['name'], row['nutrition'], row['tags']] 

df_sd_upto_60mins = pd.DataFrame(columns = ['name', 'nutrition', 'tags'])

for index, row in df_sd.iterrows():
    if '15-minutes-or-less' in eval(row['tags']) or '30-minutes-or-less' in eval(row['tags']) or '60-minutes-or-less' in eval(row['tags']):
        df_sd_upto_60mins.loc[len(df_sd_upto_60mins.index)] = [row['name'], row['nutrition'], row['tags']] 

#df_sd_random = df_sd_upto_60mins.sample(n=50, replace=False)
df_sd_random = df_sd_upto_60mins.head(50)

menu_df = df_md_random.copy()
menu_df = menu_df.drop('tags', axis=1)
sd_column_name = df_sd_random['name'].tolist()
sd_column_nutrition = df_sd_random['nutrition'].tolist()

menu_df['other_dish'] = sd_column_name
menu_df['other_dish_nutrition'] = sd_column_nutrition
menu_df.columns = ['main_dish', 'main_dish_nutrition', 'other_dish', 'other_dish_nutrition']
combined_nutrition = []

for index,row in menu_df.iterrows():
    cn = [x + y for x, y in zip(row['main_dish_nutrition'], row['other_dish_nutrition'])]
    cn_round = []
    for num in cn:
        num = round(num,2)
        cn_round.append(num)
    combined_nutrition.append(cn_round)
menu_df['combined_nutrition'] = combined_nutrition

import ast
calories = []
total_fat = []
normalized_total_fat = []
sugar = []
normalized_sugar = []
sodium = []
normalized_sodium = []
protein = []
normalized_protein = []
carbs = []
normalized_carbs = []
normalization_factor = []

for index, row in menu_df.iterrows():
    nutrition = row['combined_nutrition']
    current_normalization_factor = 1
    if nutrition[0] > 0:
        current_normalization_factor = 700/nutrition[0]
    calories.append(nutrition[0])
    total_fat.append(nutrition[1])
    normalized_total_fat.append(nutrition[1] * current_normalization_factor)
    sugar.append(nutrition[2])
    normalized_sugar.append(nutrition[2] * current_normalization_factor)
    sodium.append(nutrition[3])
    normalized_sodium.append(nutrition[3] * current_normalization_factor)
    protein.append(nutrition[4])
    normalized_protein.append(nutrition[4] * current_normalization_factor)
    carbs.append(nutrition[5])
    normalized_carbs.append(nutrition[5] * current_normalization_factor)
    normalization_factor.append(current_normalization_factor)
       
#print(calories)
menu_df['calories'] = calories
menu_df['calorie_normal'] = 700
menu_df['normalization_factor'] = normalization_factor
menu_df['total_fat'] = total_fat
menu_df['normalized_total_fat'] = normalized_total_fat
menu_df['sugar'] = sugar
menu_df['normalized_sugar'] = normalized_sugar
menu_df['sodium'] = sodium
menu_df['normalized_sodium'] = normalized_sodium
menu_df['protein'] = protein
menu_df['normalized_protein'] = normalized_protein
menu_df['carbs'] = carbs
menu_df['normalized_carbs'] = normalized_carbs
pd.set_option('display.max_rows', None)

import matplotlib.pyplot as plt
from itertools import chain

xaxis = []
xaxis.append(['fat' for _ in range(50)])
xaxis.append(['sugar' for _ in range(50)])
xaxis.append(['sodium' for _ in range(50)])
xaxis.append(['protein' for _ in range(50)])
xaxis.append(['carbs' for _ in range(50)])

def flatten_list(nested_list):
    return list(chain.from_iterable(nested_list))
xaxis_flat = flatten_list(xaxis)

yaxis = []
fat = menu_df['normalized_total_fat'].tolist()
sugar = menu_df['normalized_sugar'].tolist()
salt = menu_df['normalized_sodium'].tolist()
protein = menu_df['normalized_protein'].tolist()
carbs = menu_df['normalized_carbs'].tolist()
yaxis.append(fat)
yaxis.append(sugar)
yaxis.append(salt)
yaxis.append(protein)
yaxis.append(carbs)
yaxis_flat = flatten_list(yaxis)

main_recipe_names = menu_df['main_dish'].tolist() * 5
side_recipe_names = menu_df['other_dish'].tolist() * 5

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
sc = plt.scatter(xaxis_flat, yaxis_flat, alpha = 0.3, s=10)

annotations = []
for i in range(0,5):
    annotations.append(ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->")))
    annotations[i].set_visible(False)

number_of_recipes = len(menu_df.index)

def update_annot(ind):
    start_pos = ind["ind"][0] % number_of_recipes

    text = "{}\n{}".format(": ".join(["Main dish", main_recipe_names[ind["ind"][0]]]), 
                              ": ".join(["Side dish", side_recipe_names[ind["ind"][0]]]))
    
    for i in range(0,5): 
        pos = sc.get_offsets()[start_pos + i * number_of_recipes]
        annotations[i].xy = pos
        annotations[i].set_text(text)
    
def hover(event):
    vis = annotations[0].get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            for annot in annotations:
                annot.set_visible(True) 
            fig.canvas.draw_idle()
        else:
            if vis:
                for annot in annotations:
                    annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.ylim(0)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

plt.show()
