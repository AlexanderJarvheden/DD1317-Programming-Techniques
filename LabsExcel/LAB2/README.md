## Introduction
Now it is time to optimize company profits. In this not so realistic example, we will assume you only have one kind of product. The demand for the product depends on the price set and the money spent on advertising. The higher the price, the fewer the people who are interested in buying but the more money we make on each individual sale. Money spent on advertising will to an extent boost demand but too much is likely to be a suboptimal use of company resources.

The formulas below are not realistic and constructed solely for the purpose of the assignment. Do not panic if the mathematics appear opaque. In this case you do not need to understand the inner workings of the formula to be able to optimize it. That is the beauty of letting the computer do the work for you.

We will assume here that the demand for our product depends on the market size minus the price to the power of a coefficient (𝛼), plus money put on advertising (Adv) to the power of a coefficient (𝛽)n.

𝐷𝑒𝑚𝑎𝑛𝑑(𝑀𝑎𝑟𝑘𝑒𝑡𝑆𝑖𝑧𝑒, 𝑃𝑟𝑖𝑐𝑒, 𝐴𝑑𝑣) = 𝑀𝑎𝑟𝑘𝑒𝑡𝑆𝑖𝑧𝑒 − 𝑃𝑟𝑖𝑐𝑒𝛼 + 𝐴𝑑𝑣𝛽

We will assume that 𝛼 and 𝛽 are constants, fixed at 𝛼 = 1,1 and 𝛽 = 0,5

The total profit for a company is expressed as the profit per sold item (Price – Variable Cost) multiplied by the number of items sold (Demand), minus money put on advertising and other Fixed Costs.

𝑃𝑟𝑜𝑓𝑖𝑡(Price, VC, Adv, FC, MarketSize) = (𝑃𝑟𝑖𝑐𝑒 − 𝑉𝐶) ∗ 𝐷𝑒𝑚𝑎𝑛𝑑(𝑀𝑎𝑟𝑘𝑒𝑡𝑆𝑖𝑧𝑒, 𝑃𝑟𝑖𝑐𝑒, 𝐴𝑑𝑣) − 𝐴𝑑𝑣 − 𝐹𝐶

The company has fixed costs of 20 000 per month and variable costs on 180 per sold item. The total market size (the total potential costumers) is estimated to 1100.

We can now make a strategy table to visualize how different prices and money spent on advertising affect profits (See template). Fill in the table and add conditional formatting, in a suitable color so that a viewer can quickly decipher what is going on.

### Step 1A) - If you are using pure Excel formulas
Create a formula to calculate the profit and apply it to each cell in the table. For the very first cell in the table where price = 330 and advertising = 5000 the number should be something like the following: 
𝑃𝑟𝑜𝑓𝑖𝑡(Price, VC, Adv, FC, MarketSize) = (𝑃𝑟𝑖𝑐𝑒 − 𝑉𝐶) ∗ 𝐷𝑒𝑚𝑎𝑛𝑑(𝑀𝑎𝑟𝑘𝑒𝑡𝑆𝑖𝑧𝑒, 𝑃𝑟𝑖𝑐𝑒, 𝐴𝑑𝑣) − 𝐴𝑑𝑣 − 𝐹𝐶
𝑃𝑟𝑜𝑓𝑖𝑡(330, 180, 5000,1100) = (330 − 180) ∗ (1100 − 3301.1 + 50000,5 ) − 5000 − 20000

Make sure you are using references so that numbers outside of the table can be updated and the model recalculated.

### Step 1B) If you are using VBA
The demand function (see above) can in VBA be expressed as follows.
Function Demand(MarketSize, Price, Advertising) Const Alpha = 1.1 Const Beta = 0.5
Demand = MarketSize - WorksheetFunction.Power(Price, Alpha) + WorksheetFunction.Power(Advertising, Beta) End Function

Note the decimal separator is always a period, regardless of settings in Excel or on your computer in general. This function takes three arguments, MarketSize, Price and Advertising. The WorksheetFunction.Power function is just a different way of writing the power operator ^, which for some reason has a tendency to not work on Excel for Mac.

Create a new function ”Profit” that takes the following arguments (Price, Cost, Adv, FixedCost, MarketSize). Preferably, this function should internally use the given demand function to calculate total profit. Apply the function to each cell in the table.

### Step 2 – Calculating optimality

Now we would like to calculate what values on price and advertising that maximizes our profit. These have to be optimized together, as they both influence each other. More money spent on advertising will increase what price to charge for optimal profits. Start by using solver to calculate optimal values for price and advertising.

### Step 3 – A look at sensitivity
Now we wish to examine how sensitive our optimal price and advertising are to changes in the market size. Assuming the market size is 90% or 110% of our initial estimate, how would the optimal price and money spent on advertising be affected? Fill in table 1 below. To be able to compare advertising and price in the same graph, we have to normalize this to a change in percentage (Since they are of different orders of magnitude). Reduce the market size by 10% and calculate a new optimal price and money spent on advertising. Fill in the values in the table, divided by the original optimal values to see changes in percent.

![image](https://github.com/AlexanderJarvheden/DD1317-Programming-Techniques/assets/131161901/9770b713-a6fc-4654-9790-4225b5b5d2eb)

Increase the market size by 10% and again fill in the new normalized optimal advertising and optimal price. Plot a line graph on the table to illustrate how small changes in market size willaffect pricing and money spent on advertising accordingly. Prepare to present your work; align headlines, adjust number of decimals shown and make sure the assignment as a whole look reasonably professional and aesthetically pleasing.

![image](https://github.com/AlexanderJarvheden/DD1317-Programming-Techniques/assets/131161901/c108d05d-fee8-4dc5-982f-3bf34d701efd)
