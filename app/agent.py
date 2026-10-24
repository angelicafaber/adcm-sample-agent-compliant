"""Prompt agent client: keyless auth, Foundry SDK and Azure Monitor tracing."""

import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.monitor.opentelemetry import configure_azure_monitor


def main() -> None:
    configure_azure_monitor()
    client = AIProjectClient(endpoint=os.environ["PROJECT_ENDPOINT"], credential=DefaultAzureCredential())
    openai = client.get_openai_client()
    response = openai.responses.create(
        input="Which conditional access policies apply to agents?",
        extra_body={"agent": {"name": "MCPDetectionSampleAgent", "type": "agent_reference"}},
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
