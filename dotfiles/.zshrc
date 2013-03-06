HISTFILE=~/.histfile
HISTSIZE=5000
SAVEHIST=5000

setopt hist_ignore_all_dups
bindkey -v

autoload -U compinit
compinit
zstyle ':completion:*:descriptions' format '%U%B%d%b%u'
zstyle ':completion:*:warnings' format '%BSorry, no matches for: %d%b'

# Enable color support of ls
if [[ "$TERM" != "dumb" ]]; then
    if [[ -x `which dircolors` ]]; then
	eval `dircolors -b`
	alias 'ls=ls --color=auto'
    fi
fi

setopt correctall

PROMPT="%n@%M:%~$ "
