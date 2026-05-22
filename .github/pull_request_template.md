## 📝 Description

<!-- Describe your PR here. -->
<!-- Include a summary of the change and which feature is added or issue is fixed. -->
<!-- If the PR is still a work in progress, publish it as DRAFT. -->

## 🔗 Related Issues

- Relates to #
- Closes #

## 🔄 Type of Change
- [ ] 🐛 Bug fix (`fix:`) — patch bump
- [ ] ✨ New feature (`feat:`) — minor bump
- [ ] 💥 Breaking change (`feat!:`) — major bump
- [ ] 📝 Documentation (`docs:`) — no release
- [ ] ♻️ Refactor (`refactor:`) — no release
- [ ] 🧪 Tests (`test:`) — no release
- [ ] 🔧 Chore / CI (`chore:`, `ci:`, `build:`) — no release

## ✅ PR Checklist

- [ ] I have read and follow the [Contributing Guide](../CONTRIBUTING.md)
- [ ] My **PR title** follows [conventional commits](../CONTRIBUTING.md#commit-convention) (`feat:`, `fix:`, etc.) — it becomes the squash commit message
- [ ] I ran `make pre-commit` locally — no errors
- [ ] I ran `make test` locally — all tests pass
- [ ] I have added or updated tests and documentation where needed
- [ ] This PR targets the correct branch:
  - `feature/*` or `bugfix/*` → **`dev`**
  - `dev` → **`main`** (stable production release)

## 💬 Further Comments

<!-- If this is a large or complex change, explain why you chose this solution and what alternatives you considered. -->

---

> ⚠️ **Merge reminder**: always use **Squash merge** — it keeps history clean and ensures semantic-release reads the PR title as the commit message for version bumping.
