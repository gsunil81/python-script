#!/bin/bash
DATE=$(date +%F)
PROCESS_LOG="process_log_$DATE.log"
HIGH_MEM_LOG="high_mem_processes.log"
echo "Logging running processes..."
ps aux > "$PROCESS_LOG"
echo "Checking for high memory usage..."
HIGH_MEM_PROCESSES=$(ps aux | awk '$4 > 30' | sort -k4 -nr)

if [ -n "$HIGH_MEM_PROCESSES" ]; then
    echo "Warning: High memory usage detected!"
    echo "$HIGH_MEM_PROCESSES" >> "$HIGH_MEM_LOG"
fi
echo "Checking disk usage on C: drive..."
DISK_USAGE=$(df /c | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$DISK_USAGE" -gt 80 ]; then
    echo "Warning: Disk usage on C: drive is above 80% ($DISK_USAGE%)"
fi
TOTAL_RUNNING=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM_PROCESSES" | wc -l)

echo "Summary:"
echo "Total running processes: $TOTAL_RUNNING"
echo "Processes using >30% memory: $HIGH_MEM_COUNT"
echo "Disk usage on C: drive: $DISK_USAGE%"