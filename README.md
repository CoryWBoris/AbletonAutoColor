<div style="text-align:center; border: 2px solid black; padding: 5px;">
  <img src="AbletonColorPalette_Crop2.jpg" style="width:35%;" />
</div>



# AbletonAutoColor
![Stability Badge](https://img.shields.io/badge/-stable-blue)  
By: Cory Boris  
© 2023, 2024 MIT License

## Automatic Color Assignment Based On Midi or Audio Track Name In Ableton Live 11+ WITHOUT PLUGINS ;)

\*\*for Mac or Windows\*\*

### 6 Steps to setup. -note-, this assumes you are using the default user library folder. If you have moved this folder externally or otherwise, make a Remote Scripts folder inside of whatever user library folder you have pointed Ableton to, and start from step 2:
1. Mac users:  
   Go to `/Users/{your_username}/Music/Ableton/User Library`  
   Windows users:  
   Go to `\Users\[username]\Documents\Ableton\User Library`
2. Create a folder 'Remote Scripts' if it's not already created.
3. Create a folder titled 'ColorChanger' inside the 'Remote Scripts' folder.
4. Download **both** .py files, "Colorchanger.py" and "\_\_init\_\_.py", and place them in the 'Remote Scripts/ColorChanger' folder.
5. Restart or Open Ableton Live
6. In Ableton, select ColorChanger in the "Link|Tempo|Midi" tab, and make sure the input and output are set to 'None'.

**Note**: You can add the 2 mentioned files from here to their respective folders as shown by my tutorial while Ableton is open or quit, but if Ableton is open, then you *will* have to restart Ableton for the selected control surface to go into effect. The reason being is that Ableton compiles python and loads python code into memory when Ableton starts, but not after it loads up. This means for you using the software that in order to change a color layout and have the changes go into effect, you will have the restart Ableton. While I can't change the nature of how Ableton loads control surfaces, I circumvented this inconvenience with the full version of this program called 'TrueAutoColor'. The release details are at the bottom but with the full version you can change the layout without restarting Ableton.

## Instructions for use:
Rename a Midi or Audio Track and then the color is instantaneously changed afterwards. Also colors are applied when loading a set as well. Names are not case sensitive. But, you have to use your defined spelling.

The Default color choices I wrote are as follows:

`track_colors = {
    "drums": 69,
    "bass": 14,
    "guitar": 63,
    "vocals": 13,
    "synth": 19,
    "hats": 15,
    "quarternote": 7,
    "sixteenthnote": 17,
    "openhat": 21,
    "kick": 29,
    "snare": 64
}`

To add a new color and name combo to the above structure in the code, just locate the above dictionary in my script, and you simply have to follow the pattern of your desired track name in quotes "name" followed by a colon and then a number. As long as the last item in this dictionary (called a dictionary in python, json object in other languages) doesn't have a comma, then it should work. You can have different strings assigned to the same color, and as many as you want, as long as the format is: one string in quotes, colon, number, comma.  
**Repeat of Note:** Just a reminder, you will have to restart Ableton whenever you make changes to the files downloaded here, such as intalling or updating. But with the new gui version, it will be possible to change a layout while ableton is open.

### Ableton Color Palette
<div style="text-align:center; border: 2px solid black; padding: 5px;">
  <img src="AbletonColorPalette_Indexed.jpg" style="width:29%;" />
</div>

If you look at the picture above, the colors start at '0' and go to '69' from top left to right. You can add as many names and colors as you want, as long as you only use numbers 0 - 69.

Tested and working on Ableton 11+, but this could work for older versions if the python script were written to be backwards compatible for python 2.

**Past Fixes:**

I fixed the inability to change colors of previously named tracks on load. It now does that, yeah.

I fixed the inability to change all variations of nested group tracks. It also that does.

Also I fixed the code preventing a user from entering a string into the dictionary containing caps without it breaking the name recognition. By default the code is not sensitive to caps. I think this makes sense because I genuinely believe the last thing someone should be concerned with when naming a track is a capital letter making the diference between a color change. That feeling at first glance feels like it wouldn't be conducive to the in the moment flow necessary when creating art.

**Future Updates:**

I have officially released <a href="https://coryboris.gumroad.com/l/TrueAutoColor">TrueAutoColor</a> for both Mac AND Windows, hosted by gumroad.com - check it out!  
I think you will like the additional features it brings, such as:  
-clips coloring automatically based on track color  
-custom layout creating software with a simple and easy to use interface accurate to the colors of Ableton Live. In other words, bijection color selection!  
-light cpu usage and, like AbletonAutoColor, **doesn't need to run in the background to change track and clip colors**  
-a NEW 'Contains Mode' which allows you to use a keyword rather than an explicit name to change track and clip colors  
-unlimited rows for unlimited keywords (a lot easier than typing into a dictionary within a python script)  
-as well as the ability to load a layout without restarting ableton  
...and more  
  
But by all means keep enjoying this free version!
However, if you purchase the full version, make sure to deselect the Control Surface named ColorChanger in Ableton's preferences before selecting the new version, named TrueAutoColor, as the free version and full version can't run at the same time.


**Coffees Welcome!**
- Paypal: tromboris@gmail.com
- Venmo: @Cory-Boris
- Ethereum Address: `0x3f6af994201c17eF1E86ff057AB2a2F6CB0D1f6a`

Thank you! 🔥🥰✌🏻🙏🏻

**Happy Music Making,**  
-C

