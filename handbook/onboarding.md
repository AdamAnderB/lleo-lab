# Welcome to LLEO
## Your first week
1. Create your own GitHub account and enable two-factor authentication. Never share passwords. Send the lead your username privately so they can arrange appropriate access.
2. Read [public/private boundaries](public-private.md). Agree with the project lead where study data and documents belong.
3. Read the project README and ask which small task would help. Establish communication, meeting expectations, and a realistic milestone together.
4. Practice a correction to public documentation. Open a pull request and ask the lead to review it.
5. Choose your [profile visibility](members.md). A public profile is optional.

## Git in plain language
A repository is a project with a history. A commit is a named checkpoint. A branch is a parallel line of work. A pull request proposes merging that work and provides a place to review it. Git runs locally; GitHub hosts repositories and collaboration.

## Your first change — browser route
Open the file on GitHub, choose Edit, make a small change, and propose it on a new branch. Explain what changed and why. Review the diff, then open a pull request. A maintainer reviews before merging. Outside contributors can fork the public repository and propose changes from their fork.

## Your first change — local route
Install Git from https://git-scm.com/downloads or use GitHub Desktop. Authenticate using the supported GitHub sign-in flow; never paste tokens into tracked files.

```sh
git clone https://github.com/AdamAnderB/lleo-lab.git
cd lleo-lab
git switch -c docs/my-first-change
# Make your edit. For site content, regenerate and validate:
python3 build.py
python3 check.py
git status
git diff
# Stage only the intended files, not everything in the folder.
git add handbook/onboarding.md
git commit -m "Clarify first contribution instructions"
git push -u origin docs/my-first-change
```
If you do not have push permission, use your fork as the clone destination. Open the pull-request link GitHub provides and describe your change. For generated site edits, also stage the changed source and generated HTML after reviewing them.

## Stay in sync
Start a fresh task from main with `git switch main` and `git pull --ff-only`, then create a new branch. If conflicts appear, stop and compare both versions with the lead; do not discard another person's work or force-push shared branches.

## Done means reviewed
The change is understandable, checks pass, authors get credit, and no sensitive material appears in the diff. Ask for help early; a small clear contribution is a useful first step.

Reference: https://docs.github.com/en/get-started/start-your-journey/hello-world
