<div style="text-align:center; border: 2px solid black; padding: 5px;">
  <img src="AbletonColorPalette.jpg" style="width:28%;" />
</div>


# AbletonAutoColor

# by Cory Boris  
### Automatic Color Assignment Based On Midi or Audio Track Name In Ableton Live

for Mac or Windows (not tested on Ableton linux yet)

### 5 Steps to setup:
1. Mac users:  
  Go To /Users/{your_username}/Music/Ableton/User Library  
  Windows users:  
  Go To \Users\[username]\Documents\Ableton\User Library
2. create folder 'Remote Scripts' if not already created
3. create a folder in 'Remote Scripts' titled ColorChanger
4. download files to this folder
5. select ColorChanger in Link|Tempo|Midi tab in Ableton, and make sure input and output are set to 'None'

### Instructions for use:
Rename a Midi or Audio Track and then the color is changed instantaneously afterwards. Also colors are applied when loading a set as well. Names are not case sensitive, but they must have the same letters in the same order.

The Default color choices I wrote are as follows:

`track_colors = {
    "drums": 1,
    "bass": 2,
    "guitar": 3,
    "vocals": 4,
    "synth": 5
}`

To add a new color and name combo to the above structure in the code, you just have to follow the pattern of your desired track name in quotes "name" followed by a colon and then a number. As long as the last item in this dictionary (called a dictionary in python, json object in other languages) doesn't have a comma, then it should work. Note: you will have to restart ableton for any changes to be reflected in this script.   

If you look at the picture at the top of this, the colors start at '0' and go to '69' from top left to right. You can add as many names and colors as you want, as long as you only use numbers 0 - 69.

Only tested on Ableton 11, but should work for any version of Ableton if they have python3 natively and can use control surfaces
Enjoy the python functionality native to Ableton Live which makes this possible!



### future updates:
I'd like to make a gui for choosing the colors you want automatically applied. For now with just a tiny tiny little bit of typing you can add the colors to the dictionary in this script.


Donations Welcome!  
Paypal: tromboris@gmail.com  
or  
Ethereum Address: 0x3f6af994201c17eF1E86ff057AB2a2F6CB0D1f6a
thank you 🔥🥰✌🏻🙏🏻.

Happy Music Making  
-C
