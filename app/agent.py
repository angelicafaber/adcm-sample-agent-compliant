"""Prompt agent client: keyless auth, Foundry SDK and Azure Monitor tracing."""

import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential, OnBehalfOfCredential
from azure.monitor.opentelemetry import configure_azure_monitor


def user_credential(user_assertion: str) -> OnBehalfOfCredential:
    """Tool calls run on behalf of the signed-in user, so downstream logs show who asked.

    The agent identity proves itself with a managed identity federated credential: no secret."""
    federated = ManagedIdentityCredential()
    return OnBehalfOfCredential(
        tenant_id=os.environ["AZURE_TENANT_ID"],
        client_id=os.environ["AGENT_CLIENT_ID"],
        client_assertion_func=lambda: federated.get_token("api://AzureADTokenExchange/.default").token,
        user_assertion=user_assertion,
    )


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
