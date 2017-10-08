# Wings.ai Forecast Data

This is source code I used to collect wings.ai forecast data and calculated weighted median
forecast value for for each project. For quick start copy `data/forecast_snapshot` dir to
`data/forecast`.

If you want to get actual data run `run fetch_forecast_data all` command, it will save result into `data/forecast`
directory. To get forecast data for only specific project use `run fetch_forecast_data <id>`command.
You can find project IDs in `data/project.json` file.

# Rich data
Here http://bit.ly/2jA1LHg is spreadsheet with basic parameters of ICOs listed on wings.ai

## How to prepare environment

Clone repo and run `make build` command. Then activate virtualenv with command:
`activate .env/bin/activate`.

## Feedback

Create github issue or contact me in telegram: @madspectator
