# Lint as: python3
"""Stub API calls used in logs.py for testing.

Instead of doing real API calls, we return test JSON data.
"""

# pylint: disable=unused-argument
# pylint: disable=invalid-name

import json
import pathlib

PREFIX_GKE1 = pathlib.Path(__file__).parents[2] / 'test-data/gke1/json-dumps'

logging_body = None


class LoggingApiStub:
  """Mock object to simulate container api calls."""
  body: str

  def entries(self):
    return self

  def list(self, body):
    global logging_body
    logging_body = body
    return self

  def list_next(self, req, res):
    del req, res

  def execute(self, num_retries=0):
    with open(PREFIX_GKE1 / 'logging-entries-1.json') as json_file:
      return json.load(json_file)


def get_api_stub(service_name: str, version: str):
  return LoggingApiStub()