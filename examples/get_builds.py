import buildkite
import os

api = buildkite.Buildkite()
api.auth().access_token(os.environ["BUILDKITE_API_TOKEN"])
api.organization().set_organization("saymedia")
builds = api.builds().list(organization=True)
for build in builds:
    print build

