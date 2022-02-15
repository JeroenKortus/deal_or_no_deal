# deal_or_no_deal
In this repository you find a quickly made text based deal or no deal game made in Python. The idea to make this came about after I became interested in what the Deal or no deal bank formula might be. After researching the formula I found one on a blog[1] and wanted to test it out. The formula I found online and the first formula I used looked something like this:

<img src="https://latex.codecogs.com/svg.image?12275.30&space;&space;&plus;&space;&space;0.748E&space;&space;-&space;&space;2714.71C&space;&space;-&space;&space;0.04M&space;&space;&plus;&space;0.000006986E^2&space;&space;&space;&plus;&space;&space;32.623C^2" title="12275.30 + 0.748E - 2714.71C - 0.04M + 0.000006986E^2 + 32.623C^2" />

Which seemed to work in "normal" performances, where the player would not experience extreme luck or be extremely unlucky. However, in the extreme cases the proposed sums would not make any sense, as in some cases the amount would be negative. Later I opted for I more simple approach. Where a portion of the average would be proposed based on how far into the game the player is.

[1] http://commcognition.blogspot.com/2007/06/deal-or-no-deal-bankers-formula.html