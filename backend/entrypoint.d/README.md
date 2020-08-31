## Container PreLaunch Tasks

These shell scripts will execute:
- after container launch
- before app launch
- if they are enabled:

```

# in container
$ ls -al ./entrypoint.d/

migrate.sh
fixtures.sh
smoke-test.sh


# outside container

$ docker run --rm \
    -e ENTRYPOINT_TASK_MIGRATE=1 \
    -e ENTRYPOINT_TASK_FIXTURES=1 \
    -e ENTRYPOINT_TASK_SMOKE-TEST=1 \
    this-container-name
```