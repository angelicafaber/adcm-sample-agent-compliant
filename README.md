# MCP detection helper (compliant sample)

Sample agent repository that matches the ADCM agent golden baseline v1.1.0. The manifest
declares the Foundry prompt agent `MCPDetectionSampleAgent`, so ADCM also compares the
deployed agent's model and tools with what is declared here. Tool calls use the on-behalf-of
flow, so the user's identity carries through to the MCP server's logs.

Synthetic sample for ADCM guardrails testing. Identifiers in the manifest are illustrative.
