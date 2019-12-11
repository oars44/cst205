# cst205
"""
This depository holds the files for a program that uses OpenCV to recognize playing cards in a game of Blackjack and
advise the player on the best possible move to make

It is heavily adapted from pre-existing code by tech blogger Evan Juras, who provided the framework for the detection of playing cards
at https://github.com/EdjeElectronics/OpenCV-Playing-Card-Detector. His code provided a working example of OpenCV able to identifiy cards
against a dark background and determine their rank and suit by isolating the symbols in the top corner of each card and comparing them
to a series of custom made training images. On his youtube channel he expresses a desire to use this code to develop his own Blackjack
program, but at the current date of writing has not made any such program publicily avaliable

Only four of the .py files in the main directory are required to run the program. The fifth, Rank_Suit_Isolator.py, is used to create
custom training images for the program to identify cards with. Although the cards in a deck of playing cards is extremely standardized
the font and style in which the card numbers and symbols are depicted can vary wildly from deck to deck. As such it may be necisary 
to creat your own training images depending on what kind of deck you are using. Despite this I have still included the training images
that I personally created from a deck of retro Bicycle no. 808 playing cards. Note that for this specific implimentation, the 
images of card suits are not used as suit has no bearing in the game of blackjack. 

CardDetector.py is the main file from which the program is launched and acts as the bridge between the other files. It uses 
VideoStream.py to find and open an external webcam and identifies any playing cards in view using the functions and structures outlined
in Cards.py. Finally it uses the logic functions contained in Hands.py (the only file that I personally wrote in its entirety) to determine
the best move for the player to take and displays that move to the screen.

Detection of the playing cards can be somewhat tempermental depending on the cameras position and current lighting, as well as the fact
that the origional program was written for a Picam, rather than an actual webcam. To accomidate for this I made several changes in
VideoStream.py including drastically lowering the frame rate and exposure. Even so, I've found that the program requires a dark background,
indirect lighting, and as close to a top down perspective as possible to reliably work.

Around line 49 of VideoStream.py you will notice the use of cv2.VideoCapture() to access the webcamera for the program. This function
takes in a video index that tells it where to look to find the camera for the program to use. Typically if a computer has a built in 
webcam it will be designated as index 0, and external web cams will start at index 1. Unfortunately I have been running into an issue
where the index of my external cam changes seemingly at random. To get around this a while loop cycles through all available indexes until a valid camera is found. For some reason the index of my computers built in cam is at 1, therefore this loop starts at 2 and goes up. If the video index of your camera is 0 or 1 you will need to change this code to more quickly find it. In its current state the code
will eventually loop back around to the beginning of the index but it could take several minutes for this to happen.

Concerning the logic of playing blackjack, the program follows a simplified table of blackjack hands that assumes the dealer standing at
a soft 17 and only using a single deck. The program also does not support splitting, as getting it to recognize two different player 
hands at once would require splitting the screen vertically as well as horizontally which would reduce the amount of space avaliable
to place the cards extremely tight. Traditionally the two player hands are seperated by layering the cards ontop of each other but 
this program requires the entirety of each card to be in full view at all times, making the game take up more space that usual. Due to
the omission of splitting this program is technically not optimal and as such may encounter a much larger loss rate that is statistically
possible.

"""
