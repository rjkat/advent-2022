#!/usr/bin/env bash

FAKE_DIR=day07-temp

sed 's/\$ ls//g' \
| sed '/^$/d' \
| sed -E 's/^([0-9]+) (.*)/dd if=\/dev\/zero bs=\1 count=1 of=\2/g' \
| sed -E 's/^dir (.*)/mkdir -p \1/' \
| sed 's/^\$ cd/cd/' \
| sed "s/cd \//mkdir -p ${FAKE_DIR} \&\& cd ${FAKE_DIR}/" \
| bash

tree=`find ${FAKE_DIR} -type f | xargs wc -c | sed '$d'`
max_depth=`echo "$tree" | tr -c -d '/\n' | awk '{ print length }' | sort -rn | head -n 1`

sizes=""
for i in `seq $max_depth`; do
    tree=`echo "$tree" | sed -E 's/(.*) (.*)\/(.*)/\1 \2/' | grep "/"`
    sizes+="$tree"
    sizes+=$'\n'
done
echo -n "$sizes" | sed '/^$/d' | perl -e '$\ = "\n"; %sizes=(); while (<>) { @toks = split; $sizes{@toks[1]} += @toks[0] }; $total = 0; foreach (values %sizes) { $total += $_ unless $_ > 100000; }; print $total'