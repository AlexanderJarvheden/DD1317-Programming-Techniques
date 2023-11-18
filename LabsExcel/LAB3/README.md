## Introduction
A once profitable toy store has over the past ten years come into a gradual decline due to steep competition from the internet. The company sits on a lot of sales data, which has never been fully analyzed. The managers need to get a basic feel for how the company is doing, preferably visualized in a month-by-month diagram. They also want a prediction on how much they will sell this year in December, which is the most important month of the year for the store. Lastly, they suspect this can’t go on forever, and they need your best estimate for when they will stop making a profit.

#### Products
This file contains the product catalogue, as a list of all the products on offer in the store, the selling price as well as the cost of acquiring each individual item. Each product has a product_id which uniquely identifies each product.

#### Receipts
This file contains a list of all the receipts from the cash register over the last ten years. Each receipt has a unique receipt_id as well as a timestamp indicating when the transaction was made. The file also contains payment method (Either Visa, Mastercard or American Express) and finally a customer_id to identify who has made the purchase.

#### Receipt Items
This file indicates all the bought products on a receipt. Each row has a unique receipt_item_id. The receipt column tells you which receipt the item is included in, quantity the number of items sold, and the product id indicate which product this row refers to.
You need to load all of these files into Excel. It is probably a good idea to add each into its own sheet and name the sheet something that gives you a clue what it contains.
     
## Step 1a, using the import wizard
The following steps help you load a file into the Excel. Repeat for each file. This section may look slightly different depending on platform and version of Excel, but the basic functionality should be available and the same regardless of version. Alternative methods are also welcome, this should be seen one of many ways of importing data into Excel.
1) Make sure you are on a new and blank sheet, select cell A1, so that the data will be placed into the upper left corner once imported.
2) Select the data tab, and press “From Text”
3) Select delimited and pick a suitable delimiter.
4) The product file contains decimal numbers, and the file uses . (Dot) as decimal
separator. When importing the product file, in the last step, press “Advanced..” and change decimal separator to .
  
## Step 1b – copy paste, then split data into columns
Alternatively, you could open each file in a text editor, such as Notepad (PC) or TextEdit (Mac) and simply copy the content over to Excel. After which you need to split the data up into columns.
This is easily done using the “Text to Columns” feature under the data tab. Select Delimited, press next and choose a suitable delimiter.

## Step 2 - Restructuring
To quickly be able to manipulate data in Excel, you need to get it into a pivot table. But to get the data into a format that is easily fed into a pivot table, it will need to be restructured a bit. Start with the Receipt Items table and use VLookUp to include the created_at column from the Receipt table.

Again, starting in the ReceiptItems, now use XLookUp to include the price and cost columns from the product table.
Make a new column named profit, defined as (price – costs) * quantity for each individual row in the table. You may find it convenient to transform the import data into an Excel table (CMD + T / CTRL + T [MAC/PC]). Naming the tables something meaningful makes working with VLookUp a lot easier!

![image](https://github.com/AlexanderJarvheden/DD1317-Programming-Techniques/assets/131161901/8cb0ee9f-f5b6-4451-8c0f-f91079692aa4)

Example of the receipt items table when relevant columns have been joined in.

## Step 3 - Visualization
Now that all the relevant data is in one single table, it is time to get some insights. Create a Pivot Table and put in a new sheet. Name the sheet something meaningful, perhaps “Profit per year”. Use the pivot table to calculate the profit for each year since the beginning of the dataset. Add a line graph to visualize the development over time. For later sanity check, add a trend line (Right click on the actual plot line and click add trend line). Also tick in the option to display equation on chart. You may find it useful to right click on the dates in the pivot table and select “Group...”, select Year or Year and Month depending on how you wish to visualize it.

### Predicting the future
As stated in the beginning, two predictions are needed. One simple forecast for the profit this upcoming December, and a second one to determine which year the company will stop making a profit. Making good predictions is notoriously tricky and a science that lies well outside the scope of this course. In this assignment we will be content with a very blunt estimate, using some of Excel’s built-in functions.

When looking at dates in a pivot table, you may find it useful to group them together. When a date column has been dragged into e.g. the rows axis box, right click on one of the dates and press click “group”, select both year and month. This makes it easier to plot an overview of sales per time period.
 
## Step 4 - Predicting next December
Create a new Pivot Table off our constructed dataset. Put the pivot table on a new sheet and name it something meaningful. Maybe “December forecast”. In the pivot table, once again calculate the sum of profits per year, but this time filter to only look at the December month each year. To predict the profit for next December, a simple linear regression through the 10 or so last Decembers, should provide a good enough estimate. Start by using the formula for a simple linear function:

𝑓(𝑥) = 𝑘𝑥 + 𝑚

The Slope function calculates the derivative, or in this case the k value for a linear regression line through the data points. It takes two arguments as input, a range of y-values and a range of x-values. Make sure that the year column is actually treated as numbers. If the numbers are left aligned by default, it means Excel is treating them as text, in which case they cannot be used in the function. The function “Value” can be used to translate something that is interpreted as a string into a number.
The m value can be calculated using the intercept function. Like the Slope function it takes a list of known y’s and known x’s. Now that you have your k and m values, you can just insert your x, in this case the current year, and you have yourself a reasonable prediction.

Use this to calculate make a prediction for December’s profit.

## Step 5, Predicting break even
Finally, predict when the company is expected to stop being profitable. Assuming the company has fixed costs of 6 000 annually, which must be accounted for when measuring the overall profit (not needed in previous graphs and predictions). Go back to the “Profit per year” sheet. Copy out total profits per year from the pivot table and deduct the annual fixed costs every year.
Now we are going to try the built-in forecast function. To make a forecast by linear regression, use the FORECAST.LINEAR function. Older versions have it named FORECAST, so if you are on an old excel version, you can use the old FORECAST function which works the same way.

FORECAST.LINEAR takes 3 arguments
• X – The point in time to predict, in this case the current year
• Known Y’s, in this case all the sums of profit
• Known X’s, in this case the years
We can use the FORECAST.LINEAR function to estimate a profit for a given time in the future. Combine this with GOAL SEEK to estimate a time for when the company stops making a profit.
As a sanity check, you can optionally right click on the trend line in the graph, click format and increase the “Forecast” option from 0 to the number of years into the future that you want to extend it.
