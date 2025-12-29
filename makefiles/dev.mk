# Development targets
# This file contains targets for running and developing the application

.PHONY: run pre-commit-install pre-commit lint format

run: ## Run the Stremio Addon (Dev Mode)
	@echo "Starting server..."
	uv run python -m awesome_os

pre-commit-install:
	@echo "${YELLOW}=========> Installing pre-commit...${NC}"
	$(UV) run pre-commit install

pre-commit: pre-commit-install ## Run pre-commit
	@echo "${YELLOW}=========> Running pre-commit...${NC}"
	$(UV) run pre-commit run --all-files

lint: ## Lint code with Ruff
	@echo "Linting code..."
	uv run ruff check .

format: ## Format code with Ruff
	@echo "Formatting code..."
	uv run ruff format .
