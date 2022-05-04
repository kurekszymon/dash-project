# {{Dashboard}} project 

This is the project built for `Building products based on data` classes on our master's degree. 

## Requirements 

- built with [Dash](https://dash.plotly.com/) or [Shiny](https://shiny.rstudio.com/);
- using Good Practices such as: 
  - `linting`, 
  - `formatting code`,
  - dependency management with `venv`;
- tested;
- using [GitHub Actions](https://github.com/features/actions) for CI/CD;
- using [Docker](https://www.docker.com/);

## How to run 

- Enter app destination 

### Docker

- Run `docker compose up` 
- Open [app](http://localhost:8080)

### Locally (Example with venv)

- Run `python -m venv {env name}`
  - If you are using *Bash / zsh / other linux-like* terminals run `source {env name}/bin/activate`
  - If you are using *Powershell* or *CMD* run `./{env name}/scripts/Activate.{proper extension, i.e. ps1}`
- Open [app](http://0.0.0.0:5000)
## Authors
Project was designed and developed by [Szymon Kurek](https://github.com/kurekszymon) and [Przemysław Babulski](https://github.com/pbabulski).
