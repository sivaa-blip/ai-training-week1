# Task 2: Git and GitHub Workflow

## Requirements Implemented

1. **Repository Setup**:
   ```bash
   git init
   git branch -M main
   ```

2. **Add `.gitignore`**:
   Ignore sensitive and temporary files:
   ```text
   .env
   __pycache__/
   .venv/
   *.log
   ```

3. **Feature Branch & Commit**:
   ```bash
   git checkout -b feature/add-charts
   git add Task_1.py
   git commit -m "Add monthly sales chart script"
   ```

4. **Push Branch & Open Pull Request**:
   ```bash
   git push -u origin feature/add-charts
   # Open PR on GitHub and merge into main
   ```

5. **Create & Resolve Deliberate Merge Conflict**:
   - Create conflicting edits in `README.md` on two separate branches.
   - Attempt merge: `git merge <branch>`.
   - Resolve conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), save file.
   - Commit resolution: `git commit -m "Resolve README merge conflict"`.

6. **View Commit Graph**:
   ```bash
   git log --oneline --graph
   ```
