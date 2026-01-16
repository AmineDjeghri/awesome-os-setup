# Build and deployment targets
# This file contains targets for building packages and deploying documentation

.PHONY: build-package deploy-doc-local deploy-doc-gh

build-package: ## Build package (wheel)
	@echo "${YELLOW}=========> Building python package and wheel...${NC}"
	@$(UV) build

deploy-doc-local: ## Deploy documentation locally
	@echo "${YELLOW}Deploying documentation locally...${NC}"
	@$(UV) run mkdocs build && $(UV) run mkdocs serve

deploy-doc-gh: ## Deploy documentation to GitHub Pages
	@echo "${YELLOW}Deploying documentation in github actions..${NC}"
	@$(UV) run mkdocs build && $(UV) run mkdocs gh-deploy
