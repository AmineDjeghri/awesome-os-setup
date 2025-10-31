# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
export PATH="$HOME/.local/bin:$PATH"

# (MACOS only)
# Ensure local user binaries (uv, etc.) are found
export PATH="/opt/homebrew/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/iTerm.app/Contents/Resources/utilities:$PATH"


# Oh My Zsh
export ZSH="$HOME/.oh-my-zsh" # Path to your oh-my-zsh installation.
ZSH_THEME="powerlevel10k/powerlevel10k" # Set name of the theme to load
zstyle ':omz:update' mode auto      # update automatically without asking

ENABLE_CORRECTION="true" # enable command auto-correction.

HIST_STAMPS="mm/dd/yyyy"

# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Add wisely, as too many plugins slow down shell startup.
plugins=(git
        dirhistory
        history
        colored-man-pages
        jsontools
        zsh-autocomplete
        zsh-autosuggestions
        zsh-syntax-highlighting
        fzf-zsh-plugin
        )

source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


# Aliases. For a full list of active aliases, run `alias`.

alias zshrc="pycharm -e ~/.zshrc"
alias cat="bat"
alias ls="lsd"
alias top="btop"


# Use uv for python if available (guarded)
if command -v uv >/dev/null 2>&1; then
  alias python="uv run python"
  # Completions for uv
  eval "$(uv generate-shell-completion zsh)"
fi


# NVM (guarded)
if [ -s "$HOME/.nvm/nvm.sh" ]; then
  export NVM_DIR="$HOME/.nvm"
  . "$NVM_DIR/nvm.sh"  # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
fi


# (MACOS only)
export PATH="/Applications/PyCharm.app/Contents/MacOS:$PATH"