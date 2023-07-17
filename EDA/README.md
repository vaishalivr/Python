# Python
Exploratory Data Analysis Code
As past of my MS coursework, I was supposed to perform an Exploratory Data Analysis on a dataset of our choice. I choose one from kaggle about food.com.
Considered first 10000 rows of 2 datasets and combined them together.

We relocated from India to US recently and I am making an attempt to find ways to get closer to food outside the Indian cooking format (apart from spending time studying US history). Most recipes are completely new, others not so much. The more I work with this dataset, I am realizing that the few recipes I know, are also localized as per convenience :)

Questions to ask:
1.How does the nutrition of a random sample of 50 main dishes and 50 side dishes compare to the required daily nutrition
2.List of ingredients that I need to buy to be able to cook more recipes
3.Check if there is a relation between cooking time and number of ingredients.
4. Summary statistics

Overview of steps taken:
1.Split the dataset based on tags such as main dish, side dish, desserts and many more. Also make a table with the total count.
2.On a weeknight, we have 60 minutes to cook dinner for a family of 3. So I found the most frequest recipes by time and made a subset.
3.Made an assumption that we always wished to cook one main dish and one side dish. So took a random of 50 main dishes and 50 side dishes.
4.Created a hypothetical menu for 50 working nights along with the nutrition.
5.Split the nutrition array and normalized everything to 700 calories (the daily intake is recommended to be 2000 calories, for simplicity I considered 700*3 for breakfast, lunch, dinner)
6.Check for correlation - if the increase or decrease in calories affects the fats, sugar, carbs, salt and protein levels (normalization)
7.Plotted normalized calories as box plot to look for outliers
8. Performed a chi-square test (goodness of fit) for exhaustive dataset to check if all butrition in sample dataset is in accordnace with that recommended by WHO. IT WAS NOT!!
9.Cleaned ingredients array and compared it with what I currently have in the kitchen to see how many recipes I can cook.
10. Found out lisst of missing ingredients and their frequency in the dataset. Now there is a list of ingredients I may need to buy.
11.Finally, checked if there is any relation between ingredients and cooking time. THERE WAS NONE!
