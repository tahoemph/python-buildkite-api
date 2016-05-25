import buildkite
import os

api = buildkite.Buildkite()
api.auth().access_token(os.environ["BUILDKITE_API_TOKEN"])
builds = api.builds().list()
for build in builds:
    print build

