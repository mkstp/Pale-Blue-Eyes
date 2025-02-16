This is a flask app for generating OSC commands to send to the Data Feel dots

Positive statements will turn the colors on the dots blue
Negative statements -> red
Neutral statements -> purple

### HOW TO
- run `python src/app.py` in terminal 
- plug in data feel dots
- insert `Program.cs` into [DataFeelSDK sample project](https://github.com/DataFeel/devkit-samples) folder
- in the webpage, enter any text and press submit
- the colours should now be changing  

### Generating new mapping behaviour

- [link to specialized Data Feel GPT](https://chatgpt.com/g/g-67b0884b6e108191a52b319df18ea680-datafeel-c-creator)

Prompt used for Pale-Blue-Eyes C# component:

```
Now write me a program that takes the following OSC signals:
/affect STRING FLOAT

where STRING is "positive", "negative" or "neutral"
and FLOAT is between 0 and 1

if STRING is "positive" use red, if "negative" use blue, and use FLOAT to set the intensity of colour on all dots.

Let's have it also output any received OSC signal to screen.
```
