# Git Operations & Large File Management Guide

This document provides a reference of the Git commands and operations used to resolve push conflicts, handle large files (>100MB), and configure Git LFS (Large File Storage) in this repository.

---

## 1. Diagnostics & Status Checks
These commands are used to check remote connections, branches, and staged commits.

### Check Remote Repository Connections
```bash
git remote -v
```
* **Function**: Displays the URLs of the connected remote repository (e.g. GitHub) for both fetching and pushing.

### Check Current Branch & Status
```bash
git branch
git status
```
* **Function**: `git branch` displays all local branches (highlighting the active branch). `git status` shows the current state of modifications (staged files, unstaged files, and untracked files).

### List Unpushed Local Commits
```bash
git log origin/main..HEAD --oneline
```
* **Function**: Lists the commits that exist locally on your computer but have not yet been pushed to the remote branch (`origin/main`). Helpful to identify commits containing unwanted large files.

---

## 2. Recovery: Undoing Heavy Commits Safely
If commits have been made locally that contain files too large for GitHub (>100MB), the push will hang. These commands reset history without deleting your code.

### Soft-Reset Local Commits
```bash
git reset --soft origin/main
```
* **Function**: Resets your local Git history back to the specified remote commit (`origin/main`). Your file modifications are kept fully safe and remain in your workspace staged for commit. No code changes are lost.

---

## 3. Untracking & Ignoring Large Files
Once a file has been tracked by Git, simply adding it to `.gitignore` will not stop Git from tracking it. It must be explicitly untracked first.

### Untrack Directory (e.g., artifacts/)
```bash
git rm -r --cached artifacts
```
* **Function**: Removes the `artifacts/` directory from Git's tracking index. The `-r` flag operates recursively on all subdirectories, and `--cached` ensures the files remain untouched on your local computer.

### Untrack Specific File (e.g., test.zip)
```bash
git rm --cached test.zip
```
* **Function**: Removes the specified file from Git tracking while leaving it intact on your hard drive.

---

## 4. Git LFS (Large File Storage) Configuration
For files larger than 100MB (like deep learning model weights `.h5`), Git LFS is used to track and store them outside the main Git repository history.

### Initialize Git LFS
```bash
git lfs install
```
* **Function**: Configures Git LFS hooks in the local repository.

### Track Files with LFS
```bash
git lfs track "model/*.h5"
```
* **Function**: Adds a tracking pattern to `.gitattributes`, instructing Git to handle any `.h5` files inside the `model/` folder using Git LFS instead of normal tracking.

### Stage and Commit LFS Settings
```bash
git add .gitattributes model/
git commit -m "add model folder tracked with Git LFS"
```
* **Function**: Prepares the updated attributes configuration and model folders, and commits them.

### Push to GitHub
```bash
git push origin main
```
* **Function**: Uploads local commits. When using Git LFS, the binary weights are uploaded to GitHub's Large File Storage servers, and the lightweight pointers are pushed to your Git repository automatically.
