Harpsichord
=================================================

A Python and Piano mashup to create unique music out of a computer-code file (JS, C#, C++, Python, CSS, etc.)

[![License](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Latest release](https://img.shields.io/badge/Release-Latest-orange.svg?style=flat-square)](https://github.com/flancast90/harpsichord/releases)


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)


Introduction
------------

Harpsichord is a python implementation of a music-generator that is mathematically-based. The program takes as input a computer-code file of any language (eg C, C#, JS, Python, Html, CSS, etc.), and maps common symbols within them to a randomly-generated note that fits the bounds of the song's random octave. 

The below function maps the symbols:
```python
def map_keys(code):
    symbols = ['+', '-', '%', '&', '*', '/', ';', '?', '"', '\'', '!', '$', '{', '}', '=', '_', '(', ')', '[', ']', ',', '.', '#', '`', '\\']
    for item in symbols:
        if item in code:
            play_sound((len(code)/8000)*80)
```

which then are played with the following code:
```python
def play_sound(length):
    C1 = 32.7032
    note = pick_random_note("note")
    motion = pick_random_note("motion")
    if motion == "up":
        note_loc = (octave*12)+note+4
    elif motion == "down":  
        note_loc = (octave*12)-note+4
    OCTAVE = math.floor((note_loc+8)/12)
    SURPLUS = note_loc - globals()["OCTAVEINT"+str(OCTAVE)]
    sine(frequency=(C1*(2**(OCTAVE-1))*(1.05946371509**(SURPLUS))), duration=length)
```
**NOTE:** Harpsichord uses [pysine](https://pypi.org/project/pysine/) to output the generated notes over computer speakers.


Installation
------------

The non-native dependencies of Harpsichord are [PySine](https://pypi.org/project/pysine/). For any speaker or sound-output-related errors, refer to the PySine documentation [here](https://github.com/lneuhaus/pysine)

1. To get started with Harpsichord, first make sure Python is downloaded as per https://www.python.org/downloads/, and then download PIP [here](https://pip.pypa.io/en/stable/cli/pip_download/)
2. Next, make sure that the necessary libraries are installed using Pip
```bash
pip install pysine
```
3. Once PySine is downloaded, start Harpsichord as follows:
```bash
cd path/to/Harpsichord-main
cd src
python harpsichord.py
```
4. That's it! Refer to the [Usage Section](#usage) for the quick-start guide


Usage
-----

Once harpsichord starts, you should see an output similar to the following:
[![Harpsichord Start Img](https://i.imgur.com/LsQm3VK.png)]

In the ```Enter File Path:``` prompt, enter the path to your code file. **Note that your current directory is listed above this input by the program, and defaults to the src folder of Harpsichord.**

Assuming your program file were located on your desktop, and that the Harpsichord-main folder was also on your desktop, then, a path similar to the following would work:
```
Enter File Path: ../../code-file.fileType
```

If everything works, you can expect to see a visual output similar to the following, and if your **computer volume is up**, then you should hear some soft music playing!:
[![Harpsichord output img](https://i.imgur.com/Xm1beEa.png)]


Getting help
------------

Hopefully you don't need this section, but in case something goes wrong, feel free to drop me an email at ```flancast90@gmail.com```, or [open a new issue on this GitHub Repo](https://github.com/flancast90/Harpsichord/issues/new). I will do my best to respond ASAP to these problems!


Contributing
------------

Contributions to this file can be done as a [Pull Request](https://github.com/flancast90/Harpsichord/compare), or by shooting an email to ```flancast90@gmail.com```. If any Python or Music-Savvy person would like to be added as a Collaborator to this repo, please send an email to the same address given above. 


License
-------

This README file is distributed under the terms of the [MIT License](https://opensource.org/licenses/MIT). The license applies to this file and other files in the [GitHub repository](http://github.com/flancast90/harpsichord) hosting this file.


Acknowledgments
---------------

Thanks to everyone in the list below! Each of them helped me on my journey to create Harpsichord, and their knowledge and expertise in the subject of music, music-theory, or programming, respectively, taught me something new that is now implemented in Harpsichord. You all are awesome!

* https://music.stackexchange.com/questions/115906/determine-octave-number-given-only-key-num/115919
* http://www.sengpielaudio.com/calculator-notenames.htm
* https://github.com/mhucka/readmine/
* https://github.com/badges/shields
