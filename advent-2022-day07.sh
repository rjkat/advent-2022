#!/usr/bin/env bash

FAKE_DIR=day07-temp

cat day07.txt \
| sed 's/\$ ls//g' \
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

echo "Part 1"
echo -n "$sizes" \
    | sed '/^$/d' \
    | perl -e '%sizes=(); while (<>) { @toks = split; $sizes{@toks[1]} += @toks[0] }; $total = 0; foreach (values %sizes) { $total += $_ unless $_ > 100000; }; print $total, "\n"'

echo "Part 2"

toplevel=`echo -n "$sizes" | sed 's/.*\/.*\/.*//g' | sed '/^$/d'`
toplevel+=$'\n'
toplevel+=`find ${FAKE_DIR} -type f -depth 1 | xargs wc -c`

needed=`echo "$toplevel" \
    | perl -e '$used = 0; while (<>) { @toks = split; $used += @toks[0]; }; $needed = 30000000 - (70000000 - $used); print $needed'`

echo -n "$sizes" \
    | sed '/^$/d' \
    | perl -e "%sizes=(); while (<>) { @toks = split; \$sizes{@toks[1]} += @toks[0] }; foreach (keys %sizes) { \$sizes{\$_} >= $needed && print \$_, \" \", \$sizes{\$_}, \"\\n\"  }" \
    | sort -n -k 2 \
    | head -n 1

