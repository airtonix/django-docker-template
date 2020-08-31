#!/bin/sh

#
# Pre Launch Runtime Tasks
#
ENTRYPOINT_TASKS_DIR=${ENTRYPOINT_TASKS_DIR:-/tasks}
echo "[ENTRYPOINT]: ${ENTRYPOINT_TASKS_DIR}"

if [ -d "$ENTRYPOINT_TASKS_DIR" ]
then
  for part in $ENTRYPOINT_TASKS_DIR/*; do
    name=$(echo $part | tr ':lower:' ':upper:')
    flag="ENTRYPOINT_TASK_$name"
    [ "${!flag}"] && . $ENTRYPOINT_TASKS_DIR/$part
  done
fi

#
# Launch CMD
#
exec "$@"
