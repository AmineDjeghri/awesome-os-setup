# Unified .zshrc for macOS and Linux (with/without CUDA)

# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# ============================================================================
# OS Detection
# ============================================================================
if [[ "$OSTYPE" == "darwin"* ]]; then
  export IS_MACOS=true
  export IS_LINUX=false
else
  export IS_MACOS=false
  export IS_LINUX=true
fi

# Ensure local user binaries are found
export PATH="$HOME/.local/bin:$PATH"




# Oh My Zsh
export ZSH="$HOME/.oh-my-zsh" # Path to your oh-my-zsh installation.
ZSH_THEME="powerlevel10k/powerlevel10k" # Set name of the theme to load
zstyle ':omz:update' mode auto      # update automatically without asking


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

# Aliases for both MacOS and Linux. For a full list of active aliases, run `alias`.
alias zshrc="pycharm -e ~/.zshrc"
alias cat="bat"
alias ls="lsd"
alias top="btop"

# Aliases for Linux.
if [ "$IS_LINUX" = true ]; then
  alias bat="batcat"
fi


# ============================================================================
# PATH Configuration
# ============================================================================

# Paths for MacOS
if [ "$IS_MACOS" = true ]; then
  # macOS-specific paths (Homebrew, Cryptexes)
  export PATH="/opt/homebrew/bin:/System/Cryptexes/App/usr/bin:$PATH"
  # PyCharm - Only if installed
  if [ -d "/Applications/PyCharm.app/Contents/MacOS" ]; then
    export PATH="/Applications/PyCharm.app/Contents/MacOS:$PATH"
  fi
  # PostgreSQL - Only if installed (Homebrew)
  if [ -d "/usr/local/opt/postgresql@17/bin" ]; then
    export PATH="/usr/local/opt/postgresql@17/bin:$PATH"
  elif [ -d "/opt/homebrew/opt/postgresql@17/bin" ]; then
    export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"
  fi
fi

# ============================================================================
# NVM (Node Version Manager) - Only if installed
# ============================================================================
if [ -s "$HOME/.nvm/nvm.sh" ]; then
  export NVM_DIR="$HOME/.nvm"
  . "$NVM_DIR/nvm.sh"  # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
fi

# ============================================================================
# Rust/Cargo - Only if installed
# ============================================================================
if [ -f "$HOME/.cargo/env" ]; then
  . "$HOME/.cargo/env"
fi

# ============================================================================
# CUDA - Only if installed (typically Linux only)
# ============================================================================
if [ -d "/usr/local/cuda/bin" ]; then
  export PATH=/usr/local/cuda/bin:$PATH
fi

if [ -d "/usr/local/cuda/lib64" ]; then
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
fi

if [ "$IS_LINUX" = true ]; then
  # Check for NVIDIA GPU (CUDA availability indicator)
  if command -v nvidia-smi &> /dev/null; then
    export HAS_CUDA=true
  else
    export HAS_CUDA=false
  fi
fi

# ============================================================================
# UV - Only if installed
# ============================================================================
if command -v uv >/dev/null 2>&1; then
  alias python="uv run python"
  # Completions for uv
  eval "$(uv generate-shell-completion zsh)"
fi

# ============================================================================
# Auto-activate Python venv - Only if .venv exists in current directory
# ============================================================================
autoload -U add-zsh-hook

_auto_activate_venv() {
  # Only check current directory for .venv
  if [[ -f ".venv/bin/activate" ]]; then
    # Only activate if not already in this venv
    if [[ "$VIRTUAL_ENV" != "$PWD/.venv" ]]; then
      source .venv/bin/activate
    fi
  fi
  # Note: We don't deactivate if no .venv is found
  # This allows you to keep your venv active when navigating
}

add-zsh-hook chpwd _auto_activate_venv
_auto_activate_venv  # Run once on shell startup
