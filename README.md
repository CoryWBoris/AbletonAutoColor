<div style="text-align:center; border: 2px solid black; padding: 5px;">
  <img src="AbletonColorPalette_Crop2.jpg" style="width:35%;" />
</div>



# AbletonAutoColor
![Stability Badge](https://img.shields.io/badge/-stable-blue)  
By: Cory Boris  
© 2023 MIT License

## Automatic Color Assignment Based On Midi or Audio Track Name In Ableton Live WITHOUT PLUGINS ;)

\*\*for Mac or Windows\*\*

### 5 Steps to setup:
1. Mac users:  
   Go to `/Users/{your_username}/Music/Ableton/User Library`  
   Windows users:  
   Go to `\Users\[username]\Documents\Ableton\User Library`
2. Create a folder 'Remote Scripts' if it's not already created.
3. Create a folder titled 'ColorChanger' inside the 'Remote Scripts' folder.
4. Download **both** .py files, "Colorchanger.py" and "\_\_init\_\_.py", and place them in the 'Remote Scripts/ColorChanger' folder.
5. In Ableton, select ColorChanger in the "Link|Tempo|Midi" tab, and make sure the input and output are set to 'None'.  

**Note**: You can add the downloadable files from here to their respective folders as shown by my tutorial while Ableton is open or quit, but if Ableton is open, then you *will* have to restart Ableton for the selected control surface to go into effect. This is something that you won't have to deal with when I release the full version with a gui, which is finished at this point in time, just waiting to release it.

### Instructions for use:
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

To add a new color and name combo to the above structure in the code, you just have to follow the pattern of your desired track name in quotes "name" followed by a colon and then a number. As long as the last item in this dictionary (called a dictionary in python, json object in other languages) doesn't have a comma, then it should work.  
**Repeat of Note:** you will have to restart Ableton whenever you make changes to the files downloaded here, such as intalling or updating. But with the new gui version, it will be possible to change a layout while ableton is open.

<div style="text-align:center; border: 2px solid black; padding: 5px;">
  <img src="AbletonColorPalette_Indexed.jpg" style="width:29%;" />
</div>

If you look at the picture above, the colors start at '0' and go to '69' from top left to right. You can add as many names and colors as you want, as long as you only use numbers 0 - 69.

Only tested and working on Ableton 11, but this could work for older versions if the python script were backwards compatible for python 2.

**Past Fixes:**

I fixed the inability to change colors of previously named tracks on load. It now does that, yeah.

I fixed the inability to change all variations of nested group tracks. It also that does.

**Future Updates:**

I have officially released <a href="https://coryboris.gumroad.com/l/TrueAutoColor">TrueAutoColor</a>, hosted by gumroad.com. I highly encourage you to try it out! I think you will like the clips coloring automatically; the ability to create custom color layouts from the ableton color palette with a **beautifully designed user interface**;  as well as the ability to load a layout without restarting ableton.

But by all means keep enjoying this free version!
However, if you purchase the full version, make sure to deselect the Control Surface named ColorChanger in Ableton's preferences before selecting the new version, named TrueAutoColor, as the free version and pro version can't run at the same time.


**Coffees Welcome!**
- Paypal: tromboris@gmail.com
- Venmo: @Cory-Boris
- Ethereum Address: `0x3f6af994201c17eF1E86ff057AB2a2F6CB0D1f6a`

Thank you! 🔥🥰✌🏻🙏🏻

**Happy Music Making,**  
-C

