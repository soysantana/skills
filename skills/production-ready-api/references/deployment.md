# Deployment and Configuration

## Configuration
Separate configuration from code. Validate required production configuration
at startup. Avoid unsafe defaults for security-sensitive settings.

## Secrets
Use the deployment platform's secret mechanism where available. Never bake
production secrets into images or repositories.

## Containers
When applicable:
- use reproducible builds
- minimize runtime contents
- avoid running as root where practical
- use an appropriate init/signal strategy
- define health behavior intentionally
- exclude unnecessary files from build context

## Proxies
When behind a reverse proxy/load balancer, configure trusted proxy behavior
carefully because it affects client IPs, HTTPS detection, secure cookies, and
rate limiting.

## Shutdown
Support graceful termination within the platform's termination window.

## Migrations
Define when and how migrations run. Avoid uncontrolled concurrent migration
execution from many application replicas.

## Rollout
Consider backward compatibility between old/new application versions and the
database during rolling deployments.
