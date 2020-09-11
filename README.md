# feel_good_mobile_app

#### The app suggest users quots based on their feelings. This app has been written using Kivy library in python

#### This is a mobile app  that can be run on the following devices:

- Andriod
- iOS
- Windows
- macOS
- Linux


### Installing the Library
We will use the kivy library to build a mobile app in Python. Below you will find the instructions on how to install kivy.


Important note: Do not simply use pip install kivy to install kivy because even though the command may run without errors, you may get a [CRITICAL] [App] Unable to get a Window, abort error later on when you run a kivy app. Instead, see the instructions below in order to install kivy correctly.


#### Mac and Linux users
Kivy currently only works with Python 3.7 or earlier on Mac and Linux. You might want to install Python 3.7 first, and then install kivy for your Python 3.7 with:

python3.7 -m pip install kivy

Tip: If you just installed Python 3.7, make sure to configure your IDE to use Python 3.7, otherwise your IDE may be still using the other version of Python.



#### Windows users
##### Python 3.7 or earlier

If you are using Python 3.7 or earlier, run all three following commands one by one:

     pip install kivy

     pip install kivy.deps.glew

     pip install docutils pygments pypiwin32 kivy.deps.sdl2

##### Python 3.8

If you are using Python 3.8, run all four following commands one by one:

     pip install --upgrade pip setuptools wheel

     pip install https://github.com/kivy/kivy/archive/master.zip

     pip install kivy.deps.glew

     pip install docutils pygments pypiwin32 kivy.deps.sdl2

Some users may get installation errors or they might get a [CRITICAL] [App] Unable to get a Window, abort error later on when they run a Kivy app. If that's the case, run the following commands:

     python -m pip install --upgrade pip setuptools wheel
     python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
     python -m pip install kivy==1.11.1

If you still get errors, see the FAQs further below.


#### FAQs
1. I get an error message Microsoft Visual C++ should be installed after running the pip commands.

Solution: Download the Microsoft C++ Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/, install them, restart your computer, and then run again the three pip commands.
