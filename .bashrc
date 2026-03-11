#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

#PS1='[\u@\h \W]\$ '
#eval "$(starship init bash)"


if [ "$TERM" = "linux" ]; then
    # Мы в TTY (виртуальной консоли) - используем простой промпт
    PS1='[\u@\h \W]\$ '
else
    # Мы в графическом терминале (Alacritty/Kitty) - включаем Starship
    eval "$(starship init bash)"
fi
