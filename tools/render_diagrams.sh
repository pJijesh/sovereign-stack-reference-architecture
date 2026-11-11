#!/usr/bin/env bash
# Render every docs/diagrams/*.mmd to PNG with Mermaid CLI (mmdc).
#
#   tools/render_diagrams.sh          write PNGs next to the sources
#   tools/render_diagrams.sh --check  render into a temporary folder and fail on
#                                     any syntax or rendering error (no files changed)
#
# Requires: mmdc (npm install -g @mermaid-js/mermaid-cli). The puppeteer config
# disables the browser sandbox, which is needed in most containers and CI runners.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
src="$root/docs/diagrams"
cfg="$root/tools/puppeteer-config.json"

if ! command -v mmdc >/dev/null 2>&1; then
  echo "mmdc not found. Install with: npm install -g @mermaid-js/mermaid-cli" >&2
  exit 127
fi

out="$src"
if [[ "${1:-}" == "--check" ]]; then
  out="$(mktemp -d)"
  trap 'rm -rf "$out"' EXIT
fi

status=0
shopt -s nullglob
files=("$src"/*.mmd)
if [[ ${#files[@]} -eq 0 ]]; then
  echo "no .mmd files found" >&2
  exit 1
fi
for f in "${files[@]}"; do
  name="$(basename "$f" .mmd)"
  if mmdc -p "$cfg" -i "$f" -o "$out/$name.png" -b white -s 2 >/dev/null 2>&1 && [[ -s "$out/$name.png" ]]; then
    echo "ok    $name"
  else
    echo "FAIL  $name" >&2
    status=1
  fi
done
exit $status
