# deal_or_no_deal
In this repository you find a quickly made text based deal or no deal game made in Python. The idea to make this came about after I became interested in the Deal or no deal show and wanted to know if there was a formula for the banker offers. After some quick researching (googling), I found a formula on a blog[1] and wanted to test it out. The formula I found online and the first formula I used looked something like this:

<img src="https://render.githubusercontent.com/render/math?math=12275.30 + 0.748E - 2714.71C - 0.04M + 0.000006986E^2 + 32.623C^2">

Which seemed to work in "normal" performances, where the player would not experience extreme luck or be extremely unlucky. However, in the extreme cases the offer would not make any sense, as in there cases the amount would be negative or extremely high. Later I opted for I more simple approach. Where a portion of the average or expected value(EV) would be offered based on how far into the game the player is. A fully played game would consist of 9 offers. The portion of the expected value would be given as followed:

$[0.30, 0.30, 0.30, 0.30, 0.30, 0.40, 0.50, 0.60, 0.70]$

Where the portion for the round is the item in the list. This would mean in the starting rounds the offer would be only 30% of the EV, and in the last round it would be 70%. This, however, would make for quite a boring game. As this would mean the offer would always be less than the EV, so in a game like this, where no real money is at stake, one would always be best of rejecting the offer. It would be more fun trying to estimate if the deal is actually good and maybe even have the deals push the player to take the money or keep playing after a switch in their luck.

[1] http://commcognition.blogspot.com/2007/06/deal-or-no-deal-bankers-formula.html