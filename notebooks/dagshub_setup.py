import dagshub
import mlflow
mlflow.set_tracking_uri('https://dagshub.com/pandeyshivam8765/MLops_mini_project.mlflow')

dagshub.init(repo_owner='pandeyshivam8765', repo_name='MLops_mini_project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)