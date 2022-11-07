# ci-cd-for-prefect2-with-github-actions
Repo with the details for 11/7 Prefect stream about using Github Actions to deploy your Prefect flows

## How to use

1. Add PREFECT_API_KEY and PREFECT_API_URL as secrets to your GitHub repo for use by the GitHub Action (Settings > Secrets > Actions). _NOTE: You can see your api key and your api url for a given workspace after logging in to your cli (`prefect cloud login`) with `prefect config view`.)_
2. Create a GitHub Block in Prefect Cloud referencing your repo and the target branch.
3. Copy `.github/workflows/cloud-deployment.yaml` to your repo and update it to reference your flow. Set the storage block (`--sb`) to the slug of your Github Block from step 2. Change the other flags like the tags and work queue to your preference.
4. Create a `requirements.txt` in your repo's root directory; make sure to update `requirements.txt` if your flow needs access to more python packages.
