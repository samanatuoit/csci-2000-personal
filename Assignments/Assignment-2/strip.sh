#!/bin/bash

cat $3 | tail -n +$1 | head -n -$2
