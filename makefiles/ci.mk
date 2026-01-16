# CI/CD targets
# This file contains targets for local CI/CD testing with GitHub Actions

.PHONY: install-act act clear_ci_cache

install-act: ## Install GitHub Actions act for local testing
	@echo "${YELLOW}=========> Installing github actions act to test locally${NC}"
	curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
	@echo -e "${YELLOW}Github act version is :"
	@./bin/act --version

act: install-act ## Run Github Actions locally
	@echo "${YELLOW}Running Github Actions locally...${NC}"
	@./bin/act --env-file .env

clear_ci_cache: ## Clear GitHub local caches
	@echo "${YELLOW}Clearing CI cache...${NC}"
	@echo "${YELLOW}Clearing Github ACT local cache...${NC}"
	rm -rf ~/.cache/act ~/.cache/actcache
