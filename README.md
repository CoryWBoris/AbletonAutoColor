# AbletonAutoColor
### by Cory Boris
Automatic Color Assignment Based On Name In Ableton Live

for Mac or Windows (not tested on Ableton linux yet)

4 Steps:
1. go to /Users/{your_username}/Music/Ableton/User Library/Remote Scripts/
2. create folder titled ColorChanger
3. download files to this folder
4. select ColorChanger in Link|Tempo|Midi tab in Ableton, and make sure input and output are set to 'None'

Only tested on Ableton 11, but should work for any Abletons if they have python3 natively and can use control surfaces
Enjoy the python functionality native to Ableton Live which makes this possible!

limitations:
name change event is only registered when a new track is made or a new device is opened (i.e., max for live device, instrument, but not an audio or midi effect)
this means, the color only changes when you do something as defined above. Updates to follow!

one (so far) runtime error:
If you are using ableton beta, you will see that the first name change will result in a NoneType object is not callable, but that only happens the first time you name something in a newly loaded set, which I'm still trying to figure out. Open to any suggestions! I'm so close to having this work when you leave the renaming field or press the return or enter key.

donations welcome!  
paypal tromboris@gmail.com  
or  
ethereum address: 0x3f6af994201c17eF1E86ff057AB2a2F6CB0D1f6a
thank you 🥰🔥✌🏻🙏🏻.

Happy Music Making
-C
