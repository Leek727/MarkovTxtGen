# Markov Chain Text Generator
## How to run
```
python3 assemble.py # assemble the kaggle dataset - stored on github in small pieces since too large
python3 csv_format.py # get csv body data only
python3 markov_chain.py # inference
```
The Kaggle Reddit dataset takes ~4.7gb of memory to load with 2-grams and a 50 word text length.

## Principle
An n-gram is a phrase of n words.
For example:
2-gram
    - youre stupid
3-gram
    - no i'm not

A program can generate somewhat coherent text by strining together a lot of n-grams, with the next based on the previous. Higher n values cause more coherent text, but less creativity.

## Results
### 1-gram
```
Seed (Type three exclamation marks to exit) : cock
Finding keys...
Generating...
--------------------------------------------------------------------------------
Cock, folks. They are malicious. It’s not like 00:40 Have you assumed you Maybe you reform effectively doing so. But on PUBG 6 players view. Thanks for understanding!

#NOTE: **Do not where/ when JPow are white walking tutorial stuff(achievement farming), and there’s probably just sick and by the back again? Because I
```

### 2-gram
```
Seed (Type three exclamation marks to exit) : how are
Finding keys...
Generating...
--------------------------------------------------------------------------------
=/
How are you holding your breath.
From the way it was..
The lady I helped who was on my phone because "he wasn't born yet."
No, he meant all the mexicans locked out so they get to this point though.
If Thor had magically become in recent years

Human culture was taught in school but the shooting 
```

```
Seed (Type three exclamation marks to exit) : musk
Finding keys...
Generating...
--------------------------------------------------------------------------------
musk updated his pfp, bio and cover photo after endgame because I hated softball and nobody will read the title (or a teammate) would come after this don't come out as bisexual to people he could to accusing a person moving their thumb off the joystick works for them, among many other
```

### 3-gram
```
Seed (Type three exclamation marks to exit) : how to
Finding keys...
Generating...
--------------------------------------------------------------------------------
than how to tell what robert frost meant when he wrote about someone who sounded like me but reverse, i was skinny and work but now im fat and never does something
I feel like older hot ones episodes weren’t always about this though. Like some of the guests in seasons 1-5 didn’t even plug anything lol
I find the fixation on labels bizarre and counter productive.
```

### Conclusion
Markov Chain text gen does not produce good results without using massive amounts of data.