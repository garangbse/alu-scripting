#!/usr/bin/env ruby

# This script extracts and outputs the sender, receiver, and flags from TextMe logs
# Format: [SENDER],[RECEIVER],[FLAGS]

ARGF.each do |line|
    if match = line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
        sender = match[1]
        receiver = match[2]
        flags = match[3]
        puts "#{sender},#{receiver},#{flags}"
    end
end