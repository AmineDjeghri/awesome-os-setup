# Testing targets
# This file contains all testing-related targets

.PHONY: test-installation test

test-installation: ## Test installation
	@echo "${YELLOW}=========> Testing installation...${NC}"
	@$(UV) run --directory . hello

test: ## Run tests with pytest
	@echo "${YELLOW}Running tests...${NC}"
	@$(UV) run pytest tests
