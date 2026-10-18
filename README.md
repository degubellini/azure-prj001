## Requirements

The following tools are required to run the project locally:

- Docker
- kubectl
- kind
- Task
- Python 3

You can verify the main container and Kubernetes tooling with:

```bash
docker --version
kubectl version --client
kind version
task --version
python3 --version
```

### Tested Environment

The project has been tested using:

- Windows Subsystem for Linux (WSL)
- Linux-based development environment
- Docker accessible from WSL
- kind `v0.33.0`

The project is designed to be run as a **non-root user**.

The user running the project must therefore have permission to access the Docker daemon without using `sudo`.

For example, the following should work:

```bash
docker ps
```

without requiring:

```bash
sudo docker ps
```

This is important because project automation such as:

```bash
task build
task container:run
task kind:create
```

runs Docker commands as the current user.

If Docker requires root privileges, configure Docker so that your normal development user can access the Docker daemon before running the project.

### Kubernetes Development Environment

Local Kubernetes development uses [kind](https://kind.sigs.k8s.io/), which creates Kubernetes nodes as Docker containers.

The expected local architecture is therefore:

```text
WSL
 |
 +-- Docker
      |
      +-- azure-prj001 application containers
      |
      +-- kind Kubernetes node
           |
           +-- Kubernetes Pods
```

AKS will be introduced later for the Azure-hosted environment, while kind provides a lightweight local Kubernetes environment for development and testing.

