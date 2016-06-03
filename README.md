Python wrapper for Buildkite API
================================

The intent of this library is to provide a wrapper for the
[buildkite API](https://buildkite.com/docs/api).

Initially it will only support read information for buildkite.
This is useful for building tools to query what is happeing in
various pipelines.

As a quick summary of the API it is built around the following
objects.  Only the first four are supported in the wrapper at
this time.

* auth
* organizations
* pipelines
* builds
* jobs (not implemented)
* agents (not implemented)
* artifacts (not implemented)
* emojis (not implemented)


The API looks like

```
api = Buildkite()
api.auth().access_token(os.environ["BUILDKITE_API_TOKEN"])
builds = api.builds().list()
for build in builds:
    ...
```

See the examples directory for more.

Todo
----

* Tests
* Other nouns
* CLI
* More example programs
* Documentation
* Python wrappers for returned objects
