import buildkite
import os

api = buildkite.Buildkite()
api.auth().access_token(os.environ["BUILDKITE_API_TOKEN"])
pipelines = api.organization().set_organization("saymedia").pipelines().list()
for pipeline in pipelines:
    print pipeline

