#!/bin/bash
response=$(curl -s "$1")
echo -n "$response" | wc -c
