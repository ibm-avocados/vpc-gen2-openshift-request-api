# vpc-gen2-openshift-request-api

## Scope
A simple `flask` based API that when you send a `json` blob to it it will put in the correct numbers and kick off the `code-engine` job
to request the clusters. 


## Usage

**Example:**
Create a request:
```
curl -X POST localhost:8080/create -H 'Content-Type: application/json' -d '{"APIKEY": "BLAH", "WORKSPACE": "BLAH2", "GHEKEY": "FakeKEY", "COUNTNUMBER": 10}'
```

Delete a request:
```
curl -X DELETE localhost:8080/delete -H 'Content-Type: application/json' -d '{"APIKEY": "BLAH", "WORKSPACE": "BLAH2"}']
```

## License & Authors

If you would like to see the detailed LICENSE click [here](https://raw.githubusercontent.com/jjasghar/COBOL-on-k8s/master/LICENCE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2021- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
