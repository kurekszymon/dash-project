# {{Dashboard}} project 

This is the project built for `Building products based on data` classes on our master's degree. 

<center> [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=kurekszymon_dash-project&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=kurekszymon_dash-project) </center>


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

### On the web 

[Open app](https://data-lectures.herokuapp.com/)

### Docker

- Enter app destination 
- Run `docker compose up` 
- [Open app](http://localhost:8080)

### Locally (Example with venv)

- Enter app destination 
- Run `python -m venv {env name}`
  - If you are using *Bash / zsh / other linux-like* terminals run `source {env name}/bin/activate`
  - If you are using *Powershell* or *CMD* run `./{env name}/scripts/Activate.{proper extension, i.e. ps1}`
- [Open app](http://0.0.0.0:5000)

## Authors
Project was designed and developed by [Szymon Kurek](https://github.com/kurekszymon) and [Przemysław Babulski](https://github.com/pbabulski).
