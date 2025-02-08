ENV_FILE_PATH := .env
-include $(ENV_FILE_PATH) # keep the '-' to ignore this file if it doesn't exist.(Used in gitlab ci)

# Colors
GREEN=\033[0;32m
YELLOW=\033[0;33m
NC=\033[0m

NVM_USE := export NVM_DIR="$$HOME/.nvm" && . "$$NVM_DIR/nvm.sh" && nvm use
UV := "$$HOME/.local/bin/uv" # keep the quotes incase the path contains spaces

# installation
install-uv:
	@echo "${YELLOW}=========> installing uv ${NC}"
	@if [ -f $(UV) ]; then \
		echo "${GREEN}uv exists at $(UV) ${NC}"; \
		$(UV) self update; \
	else \
	     echo "${YELLOW}Installing uv${NC}"; \
		 curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="$$HOME/.local/bin" sh ; \
	fi

install:install-uv
	@echo "${YELLOW}=========> Installing dependencies...${NC}"
	@$(UV) sync
	@echo "${GREEN}Dependencies installed.${NC}"

pre-commit:
	@echo "${YELLOW}=========> Running pre-commit...${NC}"
	$(UV) run pre-commit install
	$(UV) run pre-commit run --all-files

# This build the documentation based on current code 'src/' and 'docs/' directories
# This is to run the documentation locally to see how it looks
deploy-doc-local:
	@echo "${YELLOW}Deploying documentation locally...${NC}"
	@$(UV) run mkdocs build && $(UV) run mkdocs serve

# Deploy it to the gh-pages branch in your GitHub repository (you need to setup the GitHub Pages in github settings to use the gh-pages branch)
deploy-doc-gh:
	@echo "${YELLOW}Deploying documentation in github actions..${NC}"
	@$(UV) run mkdocs build && $(UV) run mkdocs gh-deploy

init:
	@echo "${YELLOW}Initializing chezmoi...${NC}"
	@chezmoi init --config-path .