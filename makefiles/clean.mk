# Cleaning targets
# This file contains all cleanup-related targets

.PHONY: prune-uv clean-uv-cache clean

prune-uv: ## Removes all unused cache entries
	@echo "${YELLOW}=========> Prune uv cache...${NC}"
	@$(UV) cache prune

clean-uv-cache: ## Removes all cache entries from the cache directory,
	@echo "${YELLOW}=========> Cleaning uv cache...${NC}"
	@$(UV) cache clean

clean: clean-uv-cache ## Clean up cache and temp files
	@echo "Cleaning up..."
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
