# Nattesferd Theme for zsh 

![](https://raw.githubusercontent.com/diegovicen/nattesferd-zsh/master/nattesferd.png)

## Installation

### Theme

The theme is a fork from [Honukai](https://github.com/oskarkrawczyk/honukai-iterm-zsh), based on the wonderfully made [ys](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/ys.zsh-theme) theme from the official [oh-my-zsh repo](https://github.com/robbyrussell/oh-my-zsh). It's main feature is the ability to change the hostname displayed to custom aliases, without changin any global variables or other configuration files.

### Installation

1. Clone the repo anywhere in your computer using `git clone https://github.com/DiegoVicen/nattesferd-zsh.git`
2. Go to the folder with `cd nattesferd-zsh` and then run `sh setup.sh`
3. Change the theme variable name to `ZSH_THEME="nattesferd"` in `~/.zshrc`
4. Reload ZSH with `source ~/.zshrc`

### Changing names

1. Open the file `~/.host-alias.py` with your favourite text editor.
2. Inside, you can see a dictionary called `alias`. Following the same format in the example, write each of the aliases you want to use for your hostnames. 
3. If no alias is found, the prompt will display the default value of `hostname`.

### Eyecandy

In case you care, the screenshot of my terminal features Nattesferd with the color scheme [Tomorrow Night Eighties](https://github.com/chriskempson/tomorrow-theme/blob/master/iTerm2/Tomorrow%20Night%20Eighties.itermcolors) and the typography [Input Mono](http://input.fontbureau.com).

**NOTE**: Nattesferd has been done in 90 minutes while procastinating a Sunday afternoon. This has not been thoroughly tested anywhere apart from my own computer running Mac OS and iTerm. Feel free to install it or fork it, and if anything goes wrong, open an issue and let me know.

