# AI agent
Project focused on learning agent architectures, LLM orchestration, and system design

---

⚠️ Security Warning

Use this tool with extreme caution. This agent has the capability to read, write, and execute code on your local filesystem.

    Prompt Injection Risk: LLMs can be manipulated by malicious input. If the agent reads a file containing "malicious instructions," it may attempt to execute harmful shell commands or delete data.
    No Sandbox: By default, this agent runs with the same permissions as your user account. It is not running in a container or a virtual machine.
    Internet Access: If the agent has access to tools that can make network requests, it could theoretically exfiltrate local data.

Best Practices for Usage:

    Version Control: Always run this agent on a clean Git branch. Review all changes using git diff before committing.
    Isolated Environments: Run the agent inside a dedicated virtual environment or, ideally, a Docker container.
    Sensitive Data: Ensure no .env files, API keys, or sensitive credentials are in the directories the agent can read.
---
