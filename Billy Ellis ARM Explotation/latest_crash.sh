#!/bin/bash
cat $(ls /var/mobile/Library/Logs/CrashReporter/*.ips -t | head -n 1)