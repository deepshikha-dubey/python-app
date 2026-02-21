Step 1: Project Setup
* Create a folder python app in your local
* Initialize git (init git)
  
Step 2: Version Control
* Make your first commit:
* git add .
* git commit -m "Initial commit: Todo app"
* Push to github
* git remote add origin <your-repo-url>
* git push -u origin main

Step 3: Containerization
* Write a Dockerfile:
* Build & run locally:
* docker build -t todo-app .
* docker run -p 5000:5000 todo-app

Step 4: Multi-Container Setup
 * Create docker-compose.yml:
 * Run CMD:
 * docker-compose up

Step 4: CI/CD with GitHub Actions
  * Create .github/workflows/ci.yml:
  * Push changes and watch the pipeline run on GitHub.

What This Pipeline Does

Starts when you push or open a pull request to main.
Spins up a clean Ubuntu VM.
Downloads your repo.
Installs Python + dependencies.
Runs your tests.
Reports success/failure in the GitHub Actions tab.


