#Nattesferd Theme for zsh 

![](https://raw.githubusercontent.com/diegovicen/nattesferd-zsh/master/nattesferd.png)

## Installation

### Theme

The theme is a fork from [Honukai](https://github.com/oskarkrawczyk/honukai-iterm-zsh), based on the wonderfully made [ys](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/ys.zsh-theme) theme from the official [oh-my-zsh repo](https://github.com/robbyrussell/oh-my-zsh). Its main features are the ability to change the hostname displayed to custom aliases (as well as the username), as well as the intelligent path shortener that uses to display your actual directory and a subtle Vi-mode visual indicator. Nattesferd is possible thanks to the help of [mcornella](https://github.com/mcornella).

### Installation

1. Clone the repo anywhere in your computer using `git clone https://github.com/DiegoVicen/nattesferd-zsh.git`
2. Go to the folder with `cd nattesferd-zsh` and then run `cp nattesferd.zsh-theme $ZSH/custom/themes/nattesferd.zsh-theme` to move the file to the themes folder.
3. Change the theme variable name to `ZSH_THEME="nattesferd"` in your `~/.zshrc`.
4. Reload ZSH with `source ~/.zshrc` to make the changes.

## Enjoying Nattesferd

### Changing names

1. Open the file `$ZSH/custom/themes/nattesferd.zsh-theme` with your favourite text editor.
2. Inside, you can see two dictionary called `host_repr` and `user_repr`, where you can add new aliases for hostnames and usernames, respectively. The format to follow is explained in the theme file.
3. Once you have added the alias, run `source ~/.zshrc` to make the changes effective.

If no alias is found, the prompt will display the default value of `$HOST` or `$USER`.

### Path shortener

The path displayed in Nattesferd is not the complete path of the actual directory. Instead, Nattesferd displays the complete name of the current directory and the shortest meaningful prefix for any parent directory. That means that the part of the name displayed is the minimum necessary to uniquely identify the directory. As a nmemonic, you can also think that the name displayed is the minimum necessary for tab-completion to work instantly (only one possible completion). This feature is completely implemented in shell script and is inspired by [this answer in StackOverfow](http://stackoverflow.com/a/2951707).

### Vi-mode indicator

Vi-mode is a capability that zsh offers, and it enables modal editing (vi-like) in the shell: press `esc` to exit the normal mode and use all vi commands to move and edit text inserted. For vi/vim users, this can be comfortable, but there is no actual mode indicator. Nattesferd includes a subtle solution to this problem: The prompt character changes color to inform the user if it is insert mode (blue) or in command mode (green). To correctly use vi-mode and enable the indicator, copy this to your `.zshrc`.

```shell
# Enable vi-mode
bindkey -v
# Reduce the lag in vi-mode
export KEYTIMEOUT=1

# Vi-mode indicator for Nattesferd
export NORMAL_IND="%{$terminfo[bold]$fg[green]%}☉%{$reset_color%}"
export INSERT_IND="%{$terminfo[bold]$fg[blue]%}☉%{$reset_color%}"
export VIM_PROMPT="$INSERT_IND"

function zle-line-init zle-keymap-select {
    VIM_PROMPT="${${KEYMAP/vicmd/$(echo $NORMAL_IND)}/(main|viins)/$(echo $INSERT_IND)}"
    zle reset-prompt
}

zle -N zle-line-init
zle -N zle-keymap-select
```


### Eyecandy

In case you care, the screenshot of my terminal features Nattesferd with the color scheme [Tomorrow Night Eighties](https://github.com/chriskempson/tomorrow-theme/blob/master/iTerm2/Tomorrow%20Night%20Eighties.itermcolors) and the typography [Input Mono](http://input.fontbureau.com).

### Genius Annotation

Nattesferd means *night traveller* in Norwegian, and it's inspired by an incredible song by the Norwegian band Kvelertak. You can listen to it [here](https://www.youtube.com/watch?v=I189nD_yeQs).

**NOTE**: Nattesferd has been done in 90 minutes while procastinating a Sunday afternoon. This has not been thoroughly tested anywhere apart from my own computer running Mac OS and iTerm. Feel free to install it or fork it, and if anything goes wrong, open an issue and let me know.


