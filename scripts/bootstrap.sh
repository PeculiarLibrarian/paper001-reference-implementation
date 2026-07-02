#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo "[BOOTSTRAP v2] Semantic Environment Init"
echo "======================================"

# -----------------------------
# CONFIGURATION
# -----------------------------
export JENA_HOME="$HOME/peculiarlibrarian/apache-jena-6.1.0"
export PROJECT_ROOT="$HOME/peculiarlibrarian"

# -----------------------------
# VALIDATE JENA INSTALL
# -----------------------------
if [ ! -d "$JENA_HOME" ]; then
  echo "[FATAL] JENA_HOME not found: $JENA_HOME"
  exit 1
fi

# -----------------------------
# PATH INJECTION (IDEMPOTENT)
# -----------------------------
case ":$PATH:" in
  *"$JENA_HOME/bin"*) ;;
  *) export PATH="$JENA_HOME/bin:$PATH" ;;
esac

# -----------------------------
# TOOLCHAIN VALIDATION
# -----------------------------
echo "[CHECK] RIOT availability..."

if ! command -v riot >/dev/null 2>&1; then
  echo "[FATAL] RIOT not available in PATH"
  exit 1
fi

echo "[OK] RIOT detected"

echo "[INFO] RIOT version:"
riot --version

# -----------------------------
# OPTIONAL: PM2 STATE INSPECTION
# -----------------------------
if command -v pm2 >/dev/null 2>&1; then
  echo "[INFO] PM2 state snapshot:"
  pm2 list || true
else
  echo "[INFO] PM2 not active in this environment"
fi

# -----------------------------
# RDF SANITY GATE (CRITICAL)
# -----------------------------
echo "[CHECK] RDF syntax validation gate..."

ORG_FILE="$PROJECT_ROOT/schemas/organization.ttl"

if [ ! -f "$ORG_FILE" ]; then
  echo "[FATAL] Missing required ontology: organization.ttl"
  exit 1
fi

if ! riot --syntax=TURTLE "$ORG_FILE" > /dev/null; then
  echo "[FATAL] RDF syntax validation failed for organization.ttl"
  exit 1
fi

echo "[OK] RDF syntax validation passed"

# -----------------------------
# PHASE READINESS SIGNAL
# -----------------------------
echo "======================================"
echo "[READY] Phase 5 environment is VALID"
echo "======================================"
