Attribute VB_Name = "Module1"
Function Profit(Price, VC, Adv, FC, MarketSize)
    Profit = (Price - VC) * Demand(MarketSize, Price, Adv) - Adv - FC
End Function

Function Demand(MarketSize, Price, Adv)
    Const Alpha = 1.1
    Const Beta = 0.5
    Demand = MarketSize - WorksheetFunction.Power(Price, Alpha) + WorksheetFunction.Power(Adv, Beta)
End Function
