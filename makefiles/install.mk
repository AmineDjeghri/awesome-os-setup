# Installation targets
# This file contains all installation-related targets

.PHONY: install-uv install install-dev

install-uv: ## Install uv
	@echo "${YELLOW}=========> installing uv ${NC}"
ifeq ($(OS),Windows_NT)
	@powershell -NoProfile -ExecutionPolicy Bypass -Command "\
		$$ErrorActionPreference = 'Stop'; \
		$$uv = Get-Command uv -ErrorAction SilentlyContinue; \
		if ($$uv) { \
		  Write-Host 'uv exists at' $$uv.Source -ForegroundColor Green; \
		  uv self update; \
		} else { \
		  Write-Host 'Installing uv' -ForegroundColor Yellow; \
		  irm https://astral.sh/uv/install.ps1 | iex; \
		}"
else
	@if command -v uv >/dev/null 2>&1; then \
		echo "${GREEN}uv exists at $$(command -v uv) ${NC}"; \
		$(UV) self update; \
	else \
		echo "${YELLOW}Installing uv${NC}"; \
		curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="$$HOME/.local/bin" sh; \
	fi
endif

install: install-uv ## Install dependencies using uv
	@echo "Installing dependencies (required and docs)..."
	@$(UV) sync
	@echo "${GREEN}Dependencies installed.${NC}"

install-dev: install-uv ## Install dev dependencies using uv
	@echo "${YELLOW}=========> Installing dev dependencies (required, dev and docs)...${NC}"
	@$(UV) sync --dev
	@echo "${GREEN}Dev dependencies installed.${NC}"
