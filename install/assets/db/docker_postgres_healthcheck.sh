#!/bin/bash
if [ ! -f /tmp/container_healthy ]; then
    export PGPASSWORD=${POSTGRES_PASSWORD}
    psql -d ${POSTGRES_DB} -U ${POSTGRES_USER} -c "SELECT PostGIS_version();" || exit 1;
    touch /tmp/container_healthy
fi
exit 0

