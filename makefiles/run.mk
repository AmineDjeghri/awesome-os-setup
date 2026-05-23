# Run targets
# This file contains targets for running the application

.PHONY: run

run: ## Run the Application
	@echo "Starting server..."
	@$(UV) run python src/awesome_os/frontend/main.py
