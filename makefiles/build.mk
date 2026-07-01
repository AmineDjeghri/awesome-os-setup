# Build and deployment targets
# This file contains targets for building packages and deploying documentation

.PHONY: build-package deploy-doc-local deploy-doc-gh

build-package: ## Build package (wheel)
	@echo "${YELLOW}=========> Building python package and wheel...${NC}"
	@$(UV) build

deploy-doc-local: install-dev ## Deploy documentation locally
	@echo "${YELLOW}Deploying documentation locally...${NC}"
	@$(UV) run properdocs build && $(UV) run properdocs serve

# Deploy it to the gh-pages branch in your GitHub repository (you need to setup the GitHub Pages in github settings to use the gh-pages branch)
deploy-doc-gh: install-dev ## Deploy documentation to GitHub Pages
	@echo "${YELLOW}Deploying documentation in github actions..${NC}"
	@$(UV) run properdocs build && $(UV) run properdocs gh-deploy
