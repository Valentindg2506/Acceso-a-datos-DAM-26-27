#!/bin/bash

echo "=== SISTEMA ==="
cat /etc/os-release | grep -E '^(NAME|VERSION|VERSION_ID)='
echo
echo "Kernel:"
uname -r

echo
echo "=== NODE.JS ==="
node -v

echo
echo "=== NPM ==="
npm -v

echo
echo "=== MONGOSH ==="
mongosh --version

echo
echo "=== MONGODB ==="
mongosh --quiet --eval 'db.version()'
