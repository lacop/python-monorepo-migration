# Python monorepo migration testing

Working on services:

```shell
$ cd production/<service>
$ poetry install # poetry lock if needed
$ potry shell
(someservice) $ python -m someservice
```