#!/bin/bash

# EJERCICIO 1 - Comprueba que todo está listo

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
