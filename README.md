# deal_or_no_deal
Quick text based deal or no deal game made in Python. The idea to make this came about after researching the formula for calculating the offer of the bank after every round. The formula I found online and thus first used looked something like this:

                                                          2            2
12275.30  +  0.748E  -  2714.71C  -  0.04M  + 0.000006986E   +  32.623C 

Which seemed to work in "normal" performances, where the player would not experience extreme luck or be extremely unlucky. However, in the extreme cases the proposed sums would not make any sense, as in some cases the amount would be negavtive.
