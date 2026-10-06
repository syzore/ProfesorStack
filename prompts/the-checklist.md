# THE SOLO FOUNDER PROJECT CHECKBOX

> The canonical checklist for every software/product project.
>
> **Rule:** Before implementation begins, every potentially applicable item must be:
>
> * `[x]` Done/planned
> * `[N/A]` Explicitly determined not applicable, with reason
> * `[DEFER]` Deliberately postponed, with trigger/date
>
> Nothing disappears silently.
>
> **Planning comes before implementation.**
>
> The checklist is a DAG: later work may depend on earlier decisions.

---

# AGENT OPERATING RULES

* Never silently skip a checklist item.
* Never mark something complete merely because code exists.
* Separate `PLANNED`, `IMPLEMENTED`, and `VERIFIED`.
* Every `[N/A]` requires a reason.
* Every `[DEFER]` requires a trigger.
* Every security/compliance requirement needs an acceptance criterion.
* Every external dependency needs an owner, failure mode, and replacement path.
* Every production dependency needs a monitoring/alerting strategy.
* Every user-data field needs a reason to exist.
* Every privileged action needs an authorization rule.
* Every background process needs retry, timeout, idempotency, and failure behavior.
* Every external API needs quota/rate-limit/error behavior.
* Every paid capability needs billing failure behavior.
* Every AI capability needs cost, abuse, privacy, reliability, and evaluation behavior.
* Never introduce a framework merely because it is popular.
* Prefer boring infrastructure unless complexity is justified.
* Implement the smallest architecture that satisfies the planned requirements.

---

# STATUS MODEL

Every item should ultimately have:

`DISCOVERED → APPLICABLE/N/A → SPECIFIED → READY → IMPLEMENTED → VERIFIED → OPERATIONAL`

---

# P0 — PROJECT DEFINITION

**Depends on:** nothing.

## Product

* [ ] Define project name
* [ ] Define one-sentence product description
* [ ] Define target user
* [ ] Define primary user problem
* [ ] Define primary user action
* [ ] Define primary value delivered
* [ ] Define explicit non-goals
* [ ] Define MVP
* [ ] Define post-MVP capabilities
* [ ] Define success criteria
* [ ] Define failure criteria
* [ ] Define kill criteria
* [ ] Define expected usage frequency
* [ ] Define expected scale
* [ ] Define expected geographic scope
* [ ] Define expected platforms
* [ ] Define expected launch date/constraint
* [ ] Define whether this is prototype, MVP, production, internal tool, or experiment

## Business

* [ ] Define business model
* [ ] Define whether product is free
* [ ] Define subscription model if applicable
* [ ] Define one-time payment model if applicable
* [ ] Define usage-based pricing if applicable
* [ ] Define advertising model if applicable
* [ ] Define affiliate model if applicable
* [ ] Define marketplace model if applicable
* [ ] Define B2B/B2C/B2B2C classification
* [ ] Define customer support expectation
* [ ] Define refund expectation
* [ ] Define economic constraints
* [ ] Define maximum acceptable infrastructure cost
* [ ] Define maximum acceptable API/LLM cost
* [ ] Define expected gross margin where relevant

## Product risks

* [ ] Identify top product risks
* [ ] Identify top technical risks
* [ ] Identify top security risks
* [ ] Identify top legal/compliance risks
* [ ] Identify top operational risks
* [ ] Identify top dependency/vendor risks
* [ ] Identify single points of failure
* [ ] Define highest-risk assumptions
* [ ] Define experiments required before significant implementation

---

# P1 — APPLICABILITY / COMPLIANCE DISCOVERY

**Depends on:** P0.

This stage does not implement compliance. It determines **which compliance obligations exist**.

## Jurisdiction

* [ ] Identify founder/company jurisdiction
* [ ] Identify target customer jurisdictions
* [ ] Identify hosting jurisdictions
* [ ] Identify data-processing jurisdictions
* [ ] Identify payment jurisdictions
* [ ] Identify employee/contractor jurisdictions where relevant
* [ ] Identify app-store jurisdictions
* [ ] Identify age restrictions
* [ ] Identify regulated-industry exposure

## Privacy

* [ ] Determine whether personal data is collected
* [ ] Determine whether sensitive personal data is collected
* [ ] Determine whether children's data is collected
* [ ] Determine whether location data is collected
* [ ] Determine whether behavioral/analytics data is collected
* [ ] Determine whether payment data is collected
* [ ] Determine whether third-party processors receive data
* [ ] Determine whether data crosses borders
* [ ] Determine retention requirements
* [ ] Determine deletion requirements
* [ ] Determine user-access/export requirements
* [ ] Determine consent requirements
* [ ] Determine cookie/tracking requirements
* [ ] Determine privacy-policy requirements

## Commercial/legal

* [ ] Determine Terms of Service requirements
* [ ] Determine Privacy Policy requirements
* [ ] Determine refund/cancellation requirements
* [ ] Determine consumer-protection requirements
* [ ] Determine tax/VAT/sales-tax requirements
* [ ] Determine invoice/receipt requirements
* [ ] Determine intellectual-property requirements
* [ ] Determine copyright/licensing exposure
* [ ] Determine trademark/name exposure
* [ ] Determine open-source license obligations
* [ ] Determine content ownership/licensing requirements

## Industry-specific

* [ ] Determine healthcare exposure
* [ ] Determine financial-services exposure
* [ ] Determine education/minor exposure
* [ ] Determine employment exposure
* [ ] Determine security/surveillance exposure
* [ ] Determine gambling exposure
* [ ] Determine regulated-product exposure
* [ ] Determine biometric-data exposure
* [ ] Determine accessibility/legal obligations
* [ ] Determine AI-specific regulation exposure

## Compliance deliverable

* [ ] Create jurisdiction matrix
* [ ] Create compliance applicability matrix
* [ ] Record every N/A determination
* [ ] Identify legal questions requiring professional review
* [ ] Identify requirements that affect architecture
* [ ] Identify requirements that affect UX
* [ ] Identify requirements that affect data storage
* [ ] Identify requirements that affect logging
* [ ] Identify requirements that affect marketing
* [ ] Identify requirements that affect launch

---

# P2 — USERS, TRUST & DATA MODEL

**Depends on:** P0, P1.

## Users

* [ ] Determine whether login exists
* [ ] Determine anonymous-user behavior
* [ ] Determine guest mode
* [ ] Determine account creation
* [ ] Determine account deletion
* [ ] Determine account recovery
* [ ] Determine email verification
* [ ] Determine session model
* [ ] Determine multi-device behavior
* [ ] Determine multiple accounts / organizations
* [ ] Determine roles
* [ ] Determine permissions
* [ ] Determine administrator access
* [ ] Determine support impersonation/access model

## Identity

* [ ] Choose authentication mechanism
* [ ] Choose passwordless/password/social authentication if applicable
* [ ] Define session expiration
* [ ] Define refresh-token behavior
* [ ] Define logout behavior
* [ ] Define compromised-account behavior
* [ ] Define MFA requirements
* [ ] Define OAuth/provider failure behavior
* [ ] Define email delivery failure behavior

## Data inventory

* [ ] List every stored entity
* [ ] List every stored field
* [ ] Identify data owner
* [ ] Identify data sensitivity
* [ ] Identify why each field exists
* [ ] Identify retention period
* [ ] Identify deletion behavior
* [ ] Identify export behavior
* [ ] Identify who can read it
* [ ] Identify who can modify it
* [ ] Identify who can delete it
* [ ] Identify whether it is user-generated
* [ ] Identify whether it is derived
* [ ] Identify whether it is analytics data
* [ ] Identify whether it is sent to third parties

## Data lifecycle

* [ ] Collection
* [ ] Validation
* [ ] Storage
* [ ] Processing
* [ ] Caching
* [ ] Backups
* [ ] Replication
* [ ] Export
* [ ] Deletion
* [ ] Disaster recovery
* [ ] Vendor deletion
* [ ] Log deletion

---

# P3 — SYSTEM ARCHITECTURE

**Depends on:** P0, P1, P2.

## Architecture

* [ ] Choose frontend
* [ ] Choose backend
* [ ] Choose database
* [ ] Choose cache if necessary
* [ ] Choose object/blob storage if necessary
* [ ] Choose queue if necessary
* [ ] Choose search engine if necessary
* [ ] Choose vector database if necessary
* [ ] Choose hosting
* [ ] Choose DNS
* [ ] Choose CDN
* [ ] Choose reverse proxy
* [ ] Choose email provider
* [ ] Choose authentication provider
* [ ] Choose payment provider
* [ ] Choose analytics provider
* [ ] Choose monitoring provider
* [ ] Choose logging provider

## Architecture decisions

* [ ] Define system boundaries
* [ ] Define services/modules
* [ ] Define API boundaries
* [ ] Define database boundaries
* [ ] Define trust boundaries
* [ ] Define network boundaries
* [ ] Define public/private components
* [ ] Define synchronous flows
* [ ] Define asynchronous flows
* [ ] Define background jobs
* [ ] Define event flows
* [ ] Define failure boundaries
* [ ] Define idempotency strategy
* [ ] Define transaction boundaries
* [ ] Define consistency requirements
* [ ] Define concurrency strategy
* [ ] Define rate limiting
* [ ] Define retry strategy
* [ ] Define timeout strategy
* [ ] Define circuit-breaking/fallback behavior where needed

## Scale

* [ ] Estimate users
* [ ] Estimate requests/second
* [ ] Estimate peak traffic
* [ ] Estimate storage growth
* [ ] Estimate database growth
* [ ] Estimate network bandwidth
* [ ] Estimate background workload
* [ ] Estimate third-party API volume
* [ ] Estimate LLM token volume if applicable
* [ ] Estimate worst-case cost
* [ ] Identify expected bottlenecks
* [ ] Define scaling threshold

## Architecture documentation

* [ ] Create architecture diagram
* [ ] Create data-flow diagram
* [ ] Create sequence diagrams for critical flows
* [ ] Create dependency map
* [ ] Create ADRs for meaningful architecture decisions
* [ ] Record rejected alternatives

---

# P4 — UX, UI, ACCESSIBILITY & INTERNATIONALIZATION

**Depends on:** P0, P2, P3.

## UX

* [ ] Define primary user journey
* [ ] Define onboarding
* [ ] Define empty states
* [ ] Define loading states
* [ ] Define success states
* [ ] Define failure states
* [ ] Define offline behavior
* [ ] Define slow-network behavior
* [ ] Define destructive-action confirmation
* [ ] Define undo behavior
* [ ] Define navigation
* [ ] Define back behavior
* [ ] Define deep links
* [ ] Define browser refresh behavior
* [ ] Define mobile behavior
* [ ] Define responsive behavior

## Accessibility

* [ ] Keyboard navigation
* [ ] Visible focus
* [ ] Logical focus order
* [ ] Screen-reader semantics
* [ ] Accessible names
* [ ] Form labels
* [ ] Error association
* [ ] Color contrast
* [ ] Do not use color alone
* [ ] Text resizing
* [ ] Zoom behavior
* [ ] Reduced motion
* [ ] Touch target sizing
* [ ] Keyboard-only critical journeys
* [ ] Accessible dialogs/modals
* [ ] Accessible notifications/toasts
* [ ] Accessible charts/data visualizations
* [ ] Accessible media
* [ ] Accessibility automated tests where appropriate
* [ ] Accessibility manual verification

## Internationalization

* [ ] Determine supported languages
* [ ] Externalize strings
* [ ] Handle pluralization
* [ ] Handle date formatting
* [ ] Handle time formatting
* [ ] Handle number formatting
* [ ] Handle currency formatting
* [ ] Handle timezone
* [ ] Handle RTL if relevant
* [ ] Handle text expansion
* [ ] Handle translated error messages
* [ ] Handle locale-specific validation
* [ ] Determine translation workflow

---

# P5 — ENGINEERING FOUNDATION

**Depends on:** P3.

## Repository

* [ ] Create repository
* [ ] Define branch strategy
* [ ] Define commit conventions if needed
* [ ] Define directory structure
* [ ] Define environment strategy
* [ ] Define configuration strategy
* [ ] Define secrets strategy
* [ ] Define development setup
* [ ] Define local database setup
* [ ] Define seed/test data strategy

## Code quality

* [ ] Language/toolchain versions pinned
* [ ] Package/dependency manager chosen
* [ ] Dependency versions controlled
* [ ] Formatter configured
* [ ] Linter configured
* [ ] Type checking configured
* [ ] Static analysis configured
* [ ] Pre-commit checks where useful
* [ ] Dead-code strategy
* [ ] Error-handling conventions
* [ ] Logging conventions
* [ ] Naming conventions
* [ ] API conventions
* [ ] Database conventions
* [ ] Migration conventions
* [ ] Testing conventions

## Configuration

* [ ] Development configuration
* [ ] Test configuration
* [ ] Staging configuration
* [ ] Production configuration
* [ ] Secret injection
* [ ] Environment validation
* [ ] Missing-config failure behavior
* [ ] Configuration documentation

---

# P6 — SECURITY FOUNDATION

**Depends on:** P2, P3, P5.

Use a security verification framework such as OWASP ASVS as the detailed verification layer.

## Application security

* [ ] Threat model
* [ ] Attack surface inventory
* [ ] Trust-boundary review
* [ ] Authentication security
* [ ] Authorization model
* [ ] Object-level authorization
* [ ] Privilege escalation protection
* [ ] Input validation
* [ ] Output encoding
* [ ] Injection protection
* [ ] SQL/NoSQL injection protection
* [ ] XSS protection
* [ ] CSRF protection where applicable
* [ ] SSRF protection
* [ ] Path traversal protection
* [ ] File-upload security
* [ ] Command/code execution protection
* [ ] Open redirect protection
* [ ] CORS policy
* [ ] Security headers
* [ ] Content Security Policy where appropriate
* [ ] Secure cookie configuration
* [ ] TLS configuration
* [ ] Cryptographic requirements
* [ ] Password handling
* [ ] Token security
* [ ] Session fixation protection
* [ ] Brute-force protection
* [ ] Rate limiting
* [ ] Abuse detection
* [ ] Account enumeration review

## Data security

* [ ] Encryption in transit
* [ ] Encryption at rest where appropriate
* [ ] Secret storage
* [ ] Key management
* [ ] Database permissions
* [ ] Object-storage permissions
* [ ] Backup security
* [ ] Log security
* [ ] Sensitive-data redaction
* [ ] PII exposure review
* [ ] Production-data access review

## Supply chain

* [ ] Dependency inventory
* [ ] Lock files
* [ ] Vulnerability scanning
* [ ] Dependency update strategy
* [ ] License scanning
* [ ] Third-party package review
* [ ] CI/CD permission review
* [ ] CI secret review
* [ ] Container image scanning if applicable
* [ ] Build provenance/integrity where appropriate

## Operational security

* [ ] Admin accounts protected
* [ ] Production access restricted
* [ ] Least privilege
* [ ] SSH/access strategy
* [ ] Emergency access
* [ ] Access revocation
* [ ] Audit logging
* [ ] Security alerts
* [ ] Incident response procedure
* [ ] Vulnerability reporting mechanism

OWASP's current 2025 Top 10 explicitly elevates supply-chain failures, insecure design, authentication failures, logging/alerting failures, and exceptional-condition handling alongside traditional issues.

---

# P7 — PRIVACY & DATA GOVERNANCE

**Depends on:** P1, P2, P3, P6.

* [ ] Privacy policy
* [ ] Terms of service
* [ ] Cookie/tracking policy where needed
* [ ] Consent flows where needed
* [ ] Consent storage
* [ ] Consent withdrawal
* [ ] Data-access request process
* [ ] Data-export process
* [ ] Data-deletion process
* [ ] Account-deletion process
* [ ] Retention enforcement
* [ ] Backup-deletion policy
* [ ] Processor/vendor inventory
* [ ] Data-processing agreements where needed
* [ ] Cross-border transfer review
* [ ] Subprocessor review
* [ ] Privacy-safe analytics
* [ ] PII log scrubbing
* [ ] Support-data access controls
* [ ] Internal-data access policy
* [ ] Data breach response process

---

# P8 — CORE PRODUCT IMPLEMENTATION

**Depends on:** P3, P4, P5, P6, P7.

## Domain

* [ ] Define domain entities
* [ ] Define domain invariants
* [ ] Define validation rules
* [ ] Define state machines
* [ ] Define lifecycle transitions
* [ ] Define permissions
* [ ] Define error cases
* [ ] Define edge cases
* [ ] Define concurrency cases
* [ ] Define idempotency behavior

## API

* [ ] API contract
* [ ] Authentication
* [ ] Authorization
* [ ] Request validation
* [ ] Response schemas
* [ ] Error schemas
* [ ] Pagination
* [ ] Filtering
* [ ] Sorting
* [ ] Rate limiting
* [ ] Versioning strategy
* [ ] API documentation

## Database

* [ ] Schema
* [ ] Primary keys
* [ ] Foreign keys/relationships
* [ ] Constraints
* [ ] Indexes
* [ ] Unique constraints
* [ ] Query patterns
* [ ] Transaction boundaries
* [ ] Migration strategy
* [ ] Seed strategy
* [ ] Backup strategy
* [ ] Restore strategy

---

# P9 — CONDITIONAL MODULE: AI / LLM

**Only applicable when using generative AI, LLM APIs, agents, RAG, embeddings, or model inference.**

**Depends on:** P2, P3, P6, P7.

Do not automatically interpret this as "install LangChain."

## Model layer

* [ ] Identify all model calls
* [ ] Identify model providers
* [ ] Define provider abstraction where useful
* [ ] Define model selection
* [ ] Define fallback model
* [ ] Define timeout
* [ ] Define retry
* [ ] Define token limits
* [ ] Define maximum generation size
* [ ] Define cost limits
* [ ] Define per-user limits
* [ ] Define global limits
* [ ] Define caching strategy
* [ ] Define streaming behavior
* [ ] Define structured-output strategy

## Framework

* [ ] Determine whether an orchestration framework is necessary
* [ ] Evaluate LangChain/LangGraph/etc. only if needed
* [ ] Avoid framework dependency for trivial calls
* [ ] Define abstraction boundaries around framework-specific code
* [ ] Define framework upgrade strategy

## Prompting

* [ ] System-prompt architecture
* [ ] Prompt versioning
* [ ] Prompt testing
* [ ] Prompt rollback
* [ ] Prompt injection strategy
* [ ] User-input isolation
* [ ] Retrieved-content isolation
* [ ] Secret isolation
* [ ] System-prompt leakage review

## Output safety

* [ ] Validate model output
* [ ] Schema-validate structured output
* [ ] Sanitize output
* [ ] Prevent executable-output abuse
* [ ] Prevent generated-link abuse
* [ ] Prevent unsafe tool arguments
* [ ] Define refusal behavior
* [ ] Define hallucination handling
* [ ] Define human-review path where required

## RAG

* [ ] Data-source inventory
* [ ] Source authorization
* [ ] Document ingestion
* [ ] Chunking strategy
* [ ] Embedding strategy
* [ ] Vector storage
* [ ] Metadata security
* [ ] Tenant isolation
* [ ] Retrieval authorization
* [ ] Retrieval quality evaluation
* [ ] Citation/provenance where required
* [ ] Document deletion propagation
* [ ] Embedding deletion propagation

## Agents/tools

* [ ] Tool inventory
* [ ] Tool permissions
* [ ] Least-privilege tool access
* [ ] Tool argument validation
* [ ] Tool result validation
* [ ] Maximum action count
* [ ] Budget limit
* [ ] Timeout
* [ ] Human approval for dangerous actions
* [ ] External-side-effect protection
* [ ] Agent loop detection
* [ ] Prompt injection defenses
* [ ] Excessive-agency review
* [ ] Audit log for agent actions

## Evaluation

* [ ] Golden test set
* [ ] Regression tests
* [ ] Quality metrics
* [ ] Safety tests
* [ ] Cost tests
* [ ] Latency tests
* [ ] Model-change evaluation
* [ ] Prompt-change evaluation
* [ ] Fallback evaluation

OWASP's 2025 LLM guidance specifically calls out prompt injection, insecure output handling, sensitive-information disclosure, supply-chain vulnerabilities, unbounded consumption, excessive agency, and model misuse patterns.

---

# P10 — CONDITIONAL MODULE: PAYMENTS

**Only applicable if money changes hands.**

**Depends on:** P2, P3, P6, P7, P8.

* [ ] Payment provider
* [ ] Merchant account
* [ ] Currency model
* [ ] Product/price model
* [ ] Subscription model
* [ ] Trials
* [ ] Coupons
* [ ] Taxes
* [ ] Invoices/receipts
* [ ] Checkout
* [ ] Payment success
* [ ] Payment failure
* [ ] Card declined behavior
* [ ] Webhooks
* [ ] Webhook authentication
* [ ] Webhook idempotency
* [ ] Refunds
* [ ] Partial refunds
* [ ] Cancellations
* [ ] Upgrades
* [ ] Downgrades
* [ ] Proration
* [ ] Failed renewal
* [ ] Chargeback behavior
* [ ] Customer portal
* [ ] Entitlement model
* [ ] Entitlement revocation
* [ ] Payment reconciliation
* [ ] Finance/admin reporting
* [ ] Tax/accounting workflow

---

# P11 — CONDITIONAL MODULE: ADS / MONETIZATION

**Only applicable if advertising or tracking-supported monetization exists.**

**Depends on:** P1, P2, P4, P7, P8.

* [ ] Define advertising model
* [ ] Define ad providers
* [ ] Define ad placements
* [ ] Define ad frequency
* [ ] Define ad loading behavior
* [ ] Define ad failure behavior
* [ ] Define ad-blocker behavior
* [ ] Define consent requirements
* [ ] Define tracking requirements
* [ ] Define personalization requirements
* [ ] Define non-personalized fallback
* [ ] Define minors/age restrictions
* [ ] Define prohibited-content rules
* [ ] Define UX restrictions
* [ ] Define performance impact
* [ ] Define revenue attribution
* [ ] Define ad-event analytics
* [ ] Review privacy impact
* [ ] Review accessibility impact

---

# P12 — CONDITIONAL MODULE: EMAIL / NOTIFICATIONS

**Depends on:** P2, P7, P8.

* [ ] Email provider
* [ ] Domain authentication
* [ ] SPF
* [ ] DKIM
* [ ] DMARC
* [ ] Transactional emails
* [ ] Marketing emails
* [ ] User preferences
* [ ] Unsubscribe
* [ ] Bounce handling
* [ ] Complaint handling
* [ ] Rate limits
* [ ] Retry strategy
* [ ] Template versioning
* [ ] Localization
* [ ] Delivery monitoring
* [ ] Notification deduplication

---

# P13 — CONDITIONAL MODULE: FILES / MEDIA

**Depends on:** P2, P3, P6, P8.

* [ ] Upload limits
* [ ] File-type validation
* [ ] Content-type validation
* [ ] File-name sanitization
* [ ] Malware scanning where required
* [ ] Image-processing limits
* [ ] Archive-bomb protection
* [ ] Storage isolation
* [ ] Signed URLs
* [ ] Access-control checks
* [ ] Expiration
* [ ] CDN behavior
* [ ] Thumbnail generation
* [ ] Metadata stripping where appropriate
* [ ] Deletion
* [ ] Backup handling
* [ ] Abuse/rate limits

---

# P14 — CONDITIONAL MODULE: SEARCH / RAG / INDEXING

**Depends on:** P2, P3, P6, P8.

* [ ] Search engine selection
* [ ] Index model
* [ ] Query model
* [ ] Ranking strategy
* [ ] Filtering
* [ ] Pagination
* [ ] Tenant isolation
* [ ] Access-control enforcement
* [ ] Index update strategy
* [ ] Delete propagation
* [ ] Reindexing
* [ ] Failure recovery
* [ ] Search analytics
* [ ] Query abuse protection

---

# P15 — CONDITIONAL MODULE: REALTIME / WEBSOCKETS

**Depends on:** P3, P6, P8.

* [ ] Connection authentication
* [ ] Authorization
* [ ] Connection limits
* [ ] Message validation
* [ ] Message size limits
* [ ] Rate limits
* [ ] Heartbeats
* [ ] Reconnect behavior
* [ ] Duplicate-message behavior
* [ ] Ordering requirements
* [ ] Backpressure
* [ ] Disconnect handling
* [ ] Presence model
* [ ] Horizontal scaling strategy

---

# P16 — CONDITIONAL MODULE: BACKGROUND JOBS / CRON / AGENTS

**Depends on:** P3, P5, P8.

* [ ] Job inventory
* [ ] Scheduling
* [ ] Worker model
* [ ] Retry strategy
* [ ] Timeout
* [ ] Idempotency
* [ ] Deduplication
* [ ] Dead-letter handling
* [ ] Concurrency limits
* [ ] Resource limits
* [ ] Failure alerts
* [ ] Job observability
* [ ] Manual replay
* [ ] Manual cancellation
* [ ] Graceful shutdown
* [ ] Recovery after deployment
* [ ] Recovery after database outage
* [ ] Recovery after provider outage

---

# P17 — TESTING

**Depends on:** P8 and every relevant conditional module.

## Unit

* [ ] Domain logic
* [ ] Validation
* [ ] State transitions
* [ ] Permission logic
* [ ] Utility functions

## Integration

* [ ] Database
* [ ] Authentication
* [ ] External APIs
* [ ] Payments
* [ ] Email
* [ ] Storage
* [ ] Queue/jobs
* [ ] AI provider
* [ ] Search/vector infrastructure

## API

* [ ] Happy paths
* [ ] Invalid input
* [ ] Unauthorized access
* [ ] Forbidden access
* [ ] Missing resources
* [ ] Duplicate requests
* [ ] Rate limiting
* [ ] Timeouts
* [ ] Provider failures

## End-to-end

* [ ] New user
* [ ] Returning user
* [ ] Core product journey
* [ ] Account recovery
* [ ] Account deletion
* [ ] Payment journey if applicable
* [ ] Error journey
* [ ] Mobile journey
* [ ] Critical accessibility journey

## Security testing

* [ ] Authentication testing
* [ ] Authorization testing
* [ ] Injection testing
* [ ] XSS testing
* [ ] CSRF testing
* [ ] SSRF testing
* [ ] File-upload testing
* [ ] Rate-limit testing
* [ ] Abuse testing
* [ ] Secret-leak scanning
* [ ] Dependency scanning
* [ ] Security regression tests

## AI testing

* [ ] Prompt-injection tests
* [ ] Output-validation tests
* [ ] Data-leakage tests
* [ ] Tool-abuse tests
* [ ] Cost-abuse tests
* [ ] Hallucination/quality tests
* [ ] Regression suite
* [ ] Model replacement tests

---

# P18 — PERFORMANCE

**Depends on:** functional implementation.

* [ ] Define performance budgets
* [ ] Define page-load target
* [ ] Define API latency target
* [ ] Define database latency target
* [ ] Define background-job target
* [ ] Measure frontend performance
* [ ] Measure API performance
* [ ] Measure database performance
* [ ] Measure cache behavior
* [ ] Measure asset sizes
* [ ] Measure mobile performance
* [ ] Identify N+1 queries
* [ ] Identify expensive operations
* [ ] Add caching where justified
* [ ] Add pagination where necessary
* [ ] Add asynchronous processing where justified
* [ ] Load test critical paths
* [ ] Test peak behavior
* [ ] Test degraded dependency behavior

---

# P19 — OBSERVABILITY

**Depends on:** P3, P5, P8.

## Logging

* [ ] Structured logs
* [ ] Correlation/request ID
* [ ] User/session correlation where safe
* [ ] Error classification
* [ ] Security-event logging
* [ ] Admin-action logging
* [ ] Sensitive-data redaction
* [ ] Log retention
* [ ] Log access controls

## Metrics

* [ ] Request count
* [ ] Error rate
* [ ] Latency
* [ ] Traffic
* [ ] Database health
* [ ] Queue depth
* [ ] Job failures
* [ ] External API failures
* [ ] Cost
* [ ] Authentication failures
* [ ] Core business metric

## Tracing

* [ ] Critical request tracing
* [ ] Background-job tracing
* [ ] External-call tracing
* [ ] Database tracing where useful

## Alerts

* [ ] Service unavailable
* [ ] Error spike
* [ ] Latency spike
* [ ] Database failure
* [ ] Disk/storage exhaustion
* [ ] Queue failure
* [ ] Provider failure
* [ ] Security anomaly
* [ ] Cost anomaly
* [ ] Certificate/domain expiry
* [ ] Backup failure

---

# P20 — ANALYTICS & EXPERIMENTATION

**Depends on:** P2, P4, P7, P8.

* [ ] Define product events
* [ ] Define conversion events
* [ ] Define retention events
* [ ] Define activation event
* [ ] Define funnel
* [ ] Define analytics naming convention
* [ ] Define anonymous identity
* [ ] Define authenticated identity
* [ ] Define event properties
* [ ] Avoid unnecessary PII
* [ ] Define retention
* [ ] Define dashboards
* [ ] Define founder-level KPIs
* [ ] Define error/product event separation
* [ ] Define experiment tracking
* [ ] Verify analytics accuracy
* [ ] Define experiment framework
* [ ] Define feature-flag strategy
* [ ] Define experiment goals/objectives
* [ ] Define primary metric
* [ ] Define guardrail metrics
* [ ] Define population segmentation
* [ ] Define randomization/assignment strategy
* [ ] Define sample-size and confidence approach
* [ ] Define holdout/control design
* [ ] Define experiment duration
* [ ] Define ramp plan
* [ ] Define decision thresholds
* [ ] Define rollback/kill criteria
* [ ] Define analysis workflow
* [ ] Define experiment data retention
* [ ] Define feature-flag cleanup/expiry policy

---

# P21 — SEO / DISCOVERABILITY

**Only applicable to public web products.**

**Depends on:** P4, P8.

* [ ] Domain
* [ ] HTTPS
* [ ] Canonical URLs
* [ ] Metadata
* [ ] Title tags
* [ ] Descriptions
* [ ] Open Graph
* [ ] Twitter/X metadata where relevant
* [ ] Sitemap
* [ ] Robots configuration
* [ ] Structured data where useful
* [ ] 404 page
* [ ] Redirect strategy
* [ ] Indexing strategy
* [ ] Duplicate-content strategy
* [ ] Public/private page distinction
* [ ] Search-console setup
* [ ] Social sharing preview

---

# P22 — DEPLOYMENT / CI/CD

**Depends on:** P5, P6, P17.

* [ ] CI
* [ ] Build
* [ ] Test
* [ ] Lint
* [ ] Type check
* [ ] Security scan
* [ ] Dependency scan
* [ ] Build artifact
* [ ] Environment separation
* [ ] Secret injection
* [ ] Deployment strategy
* [ ] Migration strategy
* [ ] Rollback strategy
* [ ] Health check
* [ ] Readiness check
* [ ] Liveness check
* [ ] Zero/minimal-downtime strategy where needed
* [ ] Deployment lock/concurrency protection
* [ ] Post-deploy verification

---

# P23 — INFRASTRUCTURE / RELIABILITY

**Depends on:** P3, P19, P22.

* [ ] Production infrastructure
* [ ] Staging infrastructure where justified
* [ ] DNS
* [ ] TLS certificate
* [ ] Domain renewal
* [ ] Server monitoring
* [ ] Storage monitoring
* [ ] CPU monitoring
* [ ] Memory monitoring
* [ ] Database monitoring
* [ ] Backup monitoring
* [ ] Provider status monitoring
* [ ] Resource limits
* [ ] Autoscaling where justified
* [ ] Disaster-recovery plan
* [ ] Recovery procedure
* [ ] Recovery-time objective
* [ ] Recovery-point objective
* [ ] Restore test
* [ ] Single-point-of-failure review

---

# P24 — LAUNCH READINESS

**Depends on all required prior gates.**

## Product

* [ ] Critical journey works
* [ ] Empty states work
* [ ] Errors are understandable
* [ ] Mobile works
* [ ] Accessibility critical path verified
* [ ] Analytics verified
* [ ] Onboarding verified

## Security

* [ ] Critical vulnerabilities resolved
* [ ] Authentication verified
* [ ] Authorization verified
* [ ] Secrets checked
* [ ] Production access checked
* [ ] Dependency vulnerabilities reviewed

## Data

* [ ] Backups running
* [ ] Restore tested
* [ ] Deletion tested
* [ ] Export tested if required
* [ ] Privacy controls tested

## Operations

* [ ] Monitoring works
* [ ] Alerts work
* [ ] Logs work
* [ ] Founder receives critical alerts
* [ ] Deployment rollback tested
* [ ] Incident procedure exists
* [ ] Provider outage procedures exist

## Legal/business

* [ ] Required legal documents published
* [ ] Required disclosures published
* [ ] Pricing correct
* [ ] Taxes configured
* [ ] Payment flow verified
* [ ] Refund/cancellation behavior verified
* [ ] Support contact exists
* [ ] Domain/email infrastructure ready

## Launch

* [ ] Production smoke test
* [ ] Analytics smoke test
* [ ] Critical API smoke test
* [ ] Critical user flow smoke test
* [ ] Backup verification
* [ ] Launch checklist signed off
* [ ] Rollback decision prepared

---

# P25 — POST-LAUNCH OPERATIONS

**Depends on:** P24.

## Daily/continuous

* [ ] Service health
* [ ] Error health
* [ ] Security alerts
* [ ] Cost
* [ ] Infrastructure capacity
* [ ] User-reported issues
* [ ] Failed background jobs
* [ ] Payment failures
* [ ] Third-party provider failures

## Weekly

* [ ] Dependency updates
* [ ] Security review
* [ ] Product analytics review
* [ ] Cost review
* [ ] Error review
* [ ] Dead-code review
* [ ] Backup verification
* [ ] Performance review
* [ ] User feedback review

## Monthly/periodic

* [ ] Access review
* [ ] Secret/credential review
* [ ] Vendor review
* [ ] Compliance review
* [ ] Privacy review
* [ ] Disaster-recovery review
* [ ] Dependency/license review
* [ ] Domain/certificate review
* [ ] Architecture review
* [ ] Delete stale data
* [ ] Delete unused infrastructure
* [ ] Remove unused accounts

---

# P26 — GROWTH

**Only after the product is operational.**

* [ ] Landing page
* [ ] Positioning
* [ ] SEO
* [ ] Social accounts
* [ ] Email capture
* [ ] Referral mechanism
* [ ] Share mechanism
* [ ] Viral loop
* [ ] Community strategy
* [ ] Launch channels
* [ ] Content strategy
* [ ] Founder/public voice
* [ ] Customer interview loop
* [ ] Feedback collection
* [ ] Feature-request pipeline
* [ ] Experiment pipeline
* [ ] Conversion funnel
* [ ] Retention funnel
* [ ] Churn analysis

---

# P27 — PROJECT MAINTENANCE / AGENT HYGIENE

**Continuous.**

* [ ] Detect dead code
* [ ] Detect dead dependencies
* [ ] Detect unused configuration
* [ ] Detect stale feature flags
* [ ] Detect stale migrations
* [ ] Detect stale documentation
* [ ] Detect duplicated logic
* [ ] Detect architectural drift
* [ ] Detect security drift
* [ ] Detect dependency drift
* [ ] Detect undocumented behavior
* [ ] Detect orphaned database fields
* [ ] Detect orphaned API endpoints
* [ ] Detect orphaned background jobs
* [ ] Detect unused environment variables
* [ ] Detect stale tests
* [ ] Detect flaky tests
* [ ] Detect monitoring gaps
* [ ] Detect unowned alerts
* [ ] Detect excessive complexity

---

# P28 — RETIREMENT / EXIT

**Depends on:** whenever the project is killed, replaced, sold, or archived.

* [ ] Announce shutdown if necessary
* [ ] Define final user-access date
* [ ] Export user data if required
* [ ] Delete user data if required
* [ ] Disable new registrations
* [ ] Disable payments
* [ ] Cancel subscriptions
* [ ] Disable integrations
* [ ] Revoke secrets
* [ ] Revoke API keys
* [ ] Remove production access
* [ ] Archive source
* [ ] Archive required records
* [ ] Shut down infrastructure
* [ ] Remove DNS
* [ ] Cancel vendors
* [ ] Cancel domains if appropriate
* [ ] Confirm backups/retention obligations
* [ ] Record final architecture/state
* [ ] Record lessons learned

---

# MASTER CONDITIONAL MODULE TRIGGERS

An agent should automatically activate modules according to these predicates:

```text
LOGIN
  → user accounts OR authenticated state

PAYMENTS
  → money changes hands

ADS
  → advertisements OR advertising identifiers

EMAIL
  → email is collected OR email is sent

NOTIFICATIONS
  → push/SMS/email/in-app notification exists

EXPERIMENTS
  → A/B tests, feature flags, controlled rollouts, or personalization experiments

LLM
  → any generative/model inference call

LLM_AGENT
  → model can invoke tools, APIs, code, or external actions

RAG
  → embeddings/vector search/retrieval-augmented generation

FILES
  → users or systems upload/download files

MEDIA
  → images/audio/video processing/storage

SEARCH
  → full-text/search experience

REALTIME
  → WebSocket/SSE/live updates/presence

CRON
  → scheduled work

BACKGROUND_JOBS
  → asynchronous processing

MULTI_TENANT
  → organizations/workspaces/customers have isolated data

PUBLIC_WEB
  → unauthenticated public pages exist

MOBILE
  → native/mobile application

IOT
  → physical devices/sensors

SOCIAL
  → user-generated public content/interactions

MARKETPLACE
  → multiple independent buyers/sellers/providers

CHILDREN
  → minors are expected users

HEALTH
  → health-related information/functionality

FINANCE
  → financial products/data/functionality

EDUCATION
  → schools/students/education-specific data or workflows

AI_DECISION
  → AI materially influences decisions affecting users

HIGH_RISK
  → failure could cause significant physical, financial,
     legal, safety, or other real-world harm
```

---

# THE PRE-CODE GATE

Before the first production implementation task, the agent must produce:

* [ ] Product specification
* [ ] Scope/non-goals
* [ ] Applicability matrix
* [ ] Compliance matrix
* [ ] Data inventory
* [ ] Threat model
* [ ] Architecture
* [ ] Data model
* [ ] API contracts
* [ ] UX flows
* [ ] Accessibility requirements
* [ ] Error-state requirements
* [ ] External-dependency inventory
* [ ] Cost model
* [ ] Observability plan
* [ ] Experimentation plan
* [ ] Feature-flag strategy
* [ ] Testing strategy
* [ ] Deployment strategy
* [ ] Backup/recovery strategy
* [ ] Launch acceptance criteria
* [ ] Conditional modules activated
* [ ] All N/A decisions recorded
* [ ] All deferred items recorded
* [ ] Dependency DAG generated
* [ ] Implementation tasks generated from DAG

Only then:

**CODE MAY BEGIN.**

---

# AGENT EXECUTION MODEL

The agent should not receive:

> "Build the app."

It should receive:

```text
PROJECT
   ↓
DISCOVERY
   ↓
APPLICABILITY ANALYSIS
   ↓
REQUIREMENTS
   ↓
RISK / COMPLIANCE
   ↓
DATA + TRUST MODEL
   ↓
ARCHITECTURE
   ↓
UX / A11Y / I18N
   ↓
ENGINEERING FOUNDATION
   ↓
SECURITY FOUNDATION
   ↓
CORE IMPLEMENTATION
   ↓
CONDITIONAL MODULES
   ↓
TESTING
   ↓
PERFORMANCE
   ↓
OBSERVABILITY
   ↓
CI/CD
   ↓
RELIABILITY
   ↓
LAUNCH
   ↓
OPERATIONS
   ↓
GROWTH
   ↓
CONTINUOUS REVIEW
```

The orchestration layer should convert each checkbox into a graph node:

```yaml
id: SEC.AUTH.04
name: Session expiration
phase: security
applies_when:
  - authentication.enabled == true

depends_on:
  - DATA.IDENTITY.01
  - ARCH.AUTH.02
  - SEC.THREAT.01

artifacts:
  - security-spec.md

acceptance:
  - sessions expire according to defined policy
  - refresh behavior is explicitly tested
  - revoked sessions cannot access protected resources

status: specified
```

An agent is allowed to work only on nodes whose dependencies are `VERIFIED`.

---

# THE MOST IMPORTANT META-RULE

Do **not** turn this into:

> "Every project must implement 500 things."

Turn it into:

> **Every project must make 500 decisions about whether those things apply.**

A two-hour toy project might end with:

```text
145 applicable
73 N/A
8 deferred
64 implemented
```

A serious SaaS product might activate most of the tree.

An AI agent product might additionally activate:

```text
LLM
RAG
AGENT
BACKGROUND_JOBS
SEARCH
FILES
EMAIL
PAYMENTS
ANALYTICS
MULTI_TENANT
PUBLIC_WEB
```

The important property is that **the agent cannot accidentally forget one of them**.

---

# RECOMMENDED PROJECT FILE STRUCTURE

Every project generated by your factory could therefore begin with:

```text
/spec
    product.md
    requirements.md
    architecture.md
    data-model.md
    security.md
    privacy.md
    ux.md
    accessibility.md
    integrations.md
    ai.md
    testing.md
    operations.md

/project
    checklist.yaml
    applicability.yaml
    decisions.yaml
    risks.yaml
    dependencies.yaml
    launch-gate.yaml

/agents
    planner.md
    architect.md
    security-reviewer.md
    accessibility-reviewer.md
    implementation-agent.md
    test-agent.md
    operations-agent.md
    adversarial-reviewer.md
```

And the factory's **first agent** should not write code.

Its job is:

```text
SCAN PROJECT
      ↓
ACTIVATE MODULES
      ↓
BUILD DAG
      ↓
IDENTIFY MISSING REQUIREMENTS
      ↓
GENERATE SPECS
      ↓
GENERATE IMPLEMENTATION PLAN
      ↓
ONLY THEN RELEASE CODING AGENTS
```

This is much more powerful than a conventional "project checklist": it becomes a **project compiler**. The founder gives the machine an idea; the machine expands that idea into the applicable engineering requirements, compliance, and data model before writing code.

NIST's current SSDF material is particularly compatible with this philosophy: it emphasizes applicability, risk, cost, feasibility, and automation rather than treating security as a static checklist.
