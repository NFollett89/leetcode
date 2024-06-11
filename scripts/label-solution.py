#!/usr/bin/env bash

usage() {
  echo "USAGE: $0 SOLUTION_PATH LABEL_1 [LABEL_2 ... LABEL_n]"
  echo "Example: $0 solutions/numbered/1904/full_rounds_played.py math"
  exit $1
}

[[ "$#" -lt 2 ]] && usage 1

file_path="$1"
if [ ! -e "${file_path}" ]; then
  echo "Error: File '${file_path}' does not exist."
  exit 1
fi

shift
script_dir="$(dirname "$(realpath "${BASH_SOURCE}")")"
for label in "$@"; do
  link_path="$(echo "${file_path}" | sed -E "s|solutions/numbered/([0-9]+)/.*|solutions/symlinks-by-category/${label}/\1|")"
  mkdir -p $(dirname "${link_path}")
  ln -s "${file_path}" "${link_path}"
  echo "Created symlink '${file_path}' <-- '${link_path}'"
done
