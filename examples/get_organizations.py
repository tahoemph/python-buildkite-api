import buildkite
import os

api = buildkite.Buildkite()
api.auth().access_token(os.environ["BUILDKITE_API_TOKEN"])
organizations = api.organization().list()
for organization in organizations:
    print organization

