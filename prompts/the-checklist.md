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
>
> Each step has a guide in `the-checklist/` (`P<NN>-<slug>.md`). Basic drafts, pending Aviv's review.

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

Guide: [P00-product](the-checklist/P00-product.md)

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

Guide: [P00-business](the-checklist/P00-business.md)

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

Guide: [P00-product-risks](the-checklist/P00-product-risks.md)

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

Guide: [P01-jurisdiction](the-checklist/P01-jurisdiction.md)

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

Guide: [P01-privacy](the-checklist/P01-privacy.md)

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

Guide: [P01-commercial-legal](the-checklist/P01-commercial-legal.md)

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

Guide: [P01-industry-specific](the-checklist/P01-industry-specific.md)

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

Guide: [P01-compliance-deliverable](the-checklist/P01-compliance-deliverable.md)

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

Guide: [P02-users](the-checklist/P02-users.md)

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

Guide: [P02-identity](the-checklist/P02-identity.md)

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

Guide: [P02-data-inventory](the-checklist/P02-data-inventory.md)

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

Guide: [P02-data-lifecycle](the-checklist/P02-data-lifecycle.md)

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

## Non-functional requirements

Guide: [P03-non-functional-requirements](the-checklist/P03-non-functional-requirements.md)

* [ ] Choose CAP/PACELC behavior for each data domain: what it gives up during a partition, and what it trades for latency when healthy
* [ ] Set the consistency model for each data domain (strong, read-your-writes, eventual)
* [ ] Set the availability SLO and monthly error budget for each user-facing path
* [ ] Name the scalability axis: what grows (users, data volume, writes, reads, tenants) and by how much, e.g. 10x in 12 months
* [ ] Set p50 and p99 latency targets for each key path
* [ ] Set peak read and write throughput, e.g. requests/second at the busiest hour
* [ ] Set durability: RPO, write acknowledgement semantics, and replication needed to meet it
* [ ] Set fault tolerance: RTO, blast radius of one failure, and the DR approach
* [ ] Set security requirements: authentication, authorization, encryption, audit
* [ ] Set privacy and compliance requirements: regimes in scope, data residency, retention
* [ ] Record environment constraints: budget, team size, cloud limits, legacy systems
* [ ] Set observability requirements: what must be measurable and alertable per path
* [ ] Set a cost ceiling per month and per user
* [ ] Set maintainability requirements: who operates this, on-call load, upgrade cadence
* [ ] Give every requirement a number or a test, not an adjective

## Architecture

Guide: [P03-architecture](the-checklist/P03-architecture.md)

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

Guide: [P03-architecture-decisions](the-checklist/P03-architecture-decisions.md)

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

## Trade-offs and options

Guide: [P03-trade-offs-and-options](the-checklist/P03-trade-offs-and-options.md)

For each item: name the options considered, record the choice, and record why.

* [ ] Decide SQL vs NoSQL per data domain
* [ ] Decide sync vs async (queue) per flow
* [ ] Decide push vs pull, and fan-out on write vs fan-out on read
* [ ] Decide cache strategy (cache-aside, write-through, write-behind) and the invalidation rule
* [ ] Decide the sharding/partition key, and what queries it makes expensive
* [ ] Decide replication model (leader-follower, multi-leader, leaderless/quorum)
* [ ] Decide batch vs stream vs micro-batch for each pipeline
* [ ] Decide strong vs eventual consistency per domain
* [ ] Decide build vs managed for each component, e.g. self-run Kafka vs a managed queue
* [ ] Decide monolith vs services
* [ ] Decide polling vs WebSockets vs SSE for each live update
* [ ] Decide which indexes to add, weighing read speed against write cost and storage
* [ ] Decide where idempotency keys are required, and their scope and expiry
* [ ] Decide backpressure and load-shedding behavior: what is dropped, delayed, or rejected first
* [ ] Decide how to mitigate hot partitions (key salting, caching, splitting hot keys)

## Scale

Guide: [P03-scale](the-checklist/P03-scale.md)

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

## Escalations

Guide: [P03-escalations](the-checklist/P03-escalations.md)

Do not decide these alone. Bring them to the human with the options and a recommendation.

* [ ] Escalate before choosing AP over CP for money or identity data: stale or divergent reads could cost money or grant wrong access
* [ ] Escalate before accepting an RPO above zero for customer data: data loss becomes possible
* [ ] Escalate before any irreversible data migration: no tested way back
* [ ] Escalate before adding a new paid or managed vendor: new cost, dependency, and data-sharing
* [ ] Escalate before cross-region deployment or data residency choices: legal and cost impact
* [ ] Record the cost threshold above which an estimate needs human approval
* [ ] Escalate before accepting a cost estimate above that threshold
* [ ] Escalate before weakening any security control
* [ ] Escalate before any compliance scope change (SOC 2, GDPR, HIPAA, CCPA)
* [ ] Escalate before any one-way-door architecture choice: hard or costly to reverse

## Architecture documentation

Guide: [P03-architecture-documentation](the-checklist/P03-architecture-documentation.md)

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

Guide: [P04-ux](the-checklist/P04-ux.md)

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

Guide: [P04-accessibility](the-checklist/P04-accessibility.md)

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

Guide: [P04-internationalization](the-checklist/P04-internationalization.md)

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

Guide: [P05-repository](the-checklist/P05-repository.md)

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

Guide: [P05-code-quality](the-checklist/P05-code-quality.md)

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

Guide: [P05-configuration](the-checklist/P05-configuration.md)

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

Guide: [P06-application-security](the-checklist/P06-application-security.md)

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
* [ ] Edge proxy in front of the app: WAF, DDoS protection, per-IP rate limits
* [ ] Abuse detection
* [ ] Account enumeration review

## Data security

Guide: [P06-data-security](the-checklist/P06-data-security.md)

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

Guide: [P06-supply-chain](the-checklist/P06-supply-chain.md)

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

Guide: [P06-operational-security](the-checklist/P06-operational-security.md)

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

Guide: [P07-privacy-and-data-governance](the-checklist/P07-privacy-and-data-governance.md)

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

Guide: [P08-domain](the-checklist/P08-domain.md)

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

Guide: [P08-api](the-checklist/P08-api.md)

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
* [ ] Per-user rate limits on endpoints that cost money or reach a person (LLM calls, paid APIs, feedback, email)
* [ ] Versioning strategy
* [ ] API documentation

## Database

Guide: [P08-database](the-checklist/P08-database.md)

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

Guide: [P09-model-layer](the-checklist/P09-model-layer.md)

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
* [ ] Censor PII in-process before any text reaches a model SDK or API
* [ ] Define the PII types this product must catch
* [ ] Restore originals only in process memory, after the response
* [ ] Keep the censor token map out of logs, storage, and the outbound request
* [ ] Block the model call when the censor fails
* [ ] Choose the censor: [PrivacyScrubber](https://privacyscrubber.com/) (`@privacyscrubber/sdk`, local `sanitize` / `restore`) or the same behavior built in-house. Record owner, failure mode, and replacement path

## Framework

Guide: [P09-framework](the-checklist/P09-framework.md)

* [ ] Determine whether an orchestration framework is necessary
* [ ] Evaluate LangChain/LangGraph/etc. only if needed
* [ ] Avoid framework dependency for trivial calls
* [ ] Define abstraction boundaries around framework-specific code
* [ ] Define framework upgrade strategy

## Prompting

Guide: [P09-prompting](the-checklist/P09-prompting.md)

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

Guide: [P09-output-safety](the-checklist/P09-output-safety.md)

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

Guide: [P09-rag](the-checklist/P09-rag.md)

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

Guide: [P09-agents-tools](the-checklist/P09-agents-tools.md)

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

Guide: [P09-evaluation](the-checklist/P09-evaluation.md)

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

Guide: [P10-payments](the-checklist/P10-payments.md)

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

Guide: [P11-ads-monetization](the-checklist/P11-ads-monetization.md)

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

Guide: [P12-email-notifications](the-checklist/P12-email-notifications.md)

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

Guide: [P13-files-media](the-checklist/P13-files-media.md)

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

Guide: [P14-search-rag-indexing](the-checklist/P14-search-rag-indexing.md)

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

Guide: [P15-realtime-websockets](the-checklist/P15-realtime-websockets.md)

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

Guide: [P16-background-jobs-cron-agents](the-checklist/P16-background-jobs-cron-agents.md)

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

Guide: [P17-unit](the-checklist/P17-unit.md)

* [ ] Domain logic
* [ ] Validation
* [ ] State transitions
* [ ] Permission logic
* [ ] Utility functions

## Integration

Guide: [P17-integration](the-checklist/P17-integration.md)

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

Guide: [P17-api](the-checklist/P17-api.md)

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

Guide: [P17-end-to-end](the-checklist/P17-end-to-end.md)

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

Guide: [P17-security-testing](the-checklist/P17-security-testing.md)

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

Guide: [P17-ai-testing](the-checklist/P17-ai-testing.md)

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

Guide: [P18-performance](the-checklist/P18-performance.md)

**Depends on:** functional implementation.

* [ ] Define performance budgets
* [ ] Define page-load target
* [ ] Define API latency target
* [ ] Check measured p50/p99 against the latency target of each key path from P3
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
* [ ] Find the capacity ceiling on a production-like copy, and record what saturates first
* [ ] Load test at the P3 peak throughput target, not only at current traffic
* [ ] Check for hot partitions or hot keys under skewed load
* [ ] Set a cache hit-rate target and measure it
* [ ] Test peak behavior
* [ ] Test degraded dependency behavior

---

# P19 — OBSERVABILITY

**Depends on:** P3, P5, P8.

## Logging

Guide: [P19-logging](the-checklist/P19-logging.md)

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

Guide: [P19-metrics](the-checklist/P19-metrics.md)

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

Guide: [P19-tracing](the-checklist/P19-tracing.md)

* [ ] Critical request tracing
* [ ] Background-job tracing
* [ ] External-call tracing
* [ ] Database tracing where useful

## Alerts

Guide: [P19-alerts](the-checklist/P19-alerts.md)

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

Guide: [P20-analytics-and-experimentation](the-checklist/P20-analytics-and-experimentation.md)

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

Guide: [P21-seo-discoverability](the-checklist/P21-seo-discoverability.md)

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

Guide: [P22-deployment-ci-cd](the-checklist/P22-deployment-ci-cd.md)

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
* [ ] One-off startup work (schema, migrations, seed, recompute) runs once per deploy in a release step, not in every app process
* [ ] Rollback strategy
* [ ] Health check
* [ ] Readiness check
* [ ] Liveness check
* [ ] Zero/minimal-downtime strategy where needed
* [ ] Deployment lock/concurrency protection
* [ ] Post-deploy verification

---

# P23 — INFRASTRUCTURE / RELIABILITY

Guide: [P23-infrastructure-reliability](the-checklist/P23-infrastructure-reliability.md)

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
* [ ] More than one app process (workers or replicas)
* [ ] App processes times connection-pool size stays under the database's connection limit
* [ ] Scale the database up before adding read replicas
* [ ] Autoscaling where justified
* [ ] Disaster-recovery plan
* [ ] Recovery procedure
* [ ] Recovery-time objective
* [ ] Recovery-point objective
* [ ] Restore test, timed against the RTO and checked against the RPO
* [ ] Failover drill for each component with a standby or replica
* [ ] Test backpressure and load-shedding behavior under overload
* [ ] Define the error-budget policy: what stops or slows when the budget is spent
* [ ] Single-point-of-failure review

---

# P24 — LAUNCH READINESS

**Depends on all required prior gates.**

## Product

Guide: [P24-product](the-checklist/P24-product.md)

* [ ] Critical journey works
* [ ] Empty states work
* [ ] Errors are understandable
* [ ] Mobile works
* [ ] Accessibility critical path verified
* [ ] Analytics verified
* [ ] Onboarding verified

## Security

Guide: [P24-security](the-checklist/P24-security.md)

* [ ] Critical vulnerabilities resolved
* [ ] Authentication verified
* [ ] Authorization verified
* [ ] Secrets checked
* [ ] Production access checked
* [ ] Dependency vulnerabilities reviewed

## Data

Guide: [P24-data](the-checklist/P24-data.md)

* [ ] Backups running
* [ ] Restore tested
* [ ] Deletion tested
* [ ] Export tested if required
* [ ] Privacy controls tested

## Operations

Guide: [P24-operations](the-checklist/P24-operations.md)

* [ ] Monitoring works
* [ ] Alerts work
* [ ] Logs work
* [ ] Founder receives critical alerts
* [ ] Deployment rollback tested
* [ ] Incident procedure exists
* [ ] Provider outage procedures exist

## Legal/business

Guide: [P24-legal-business](the-checklist/P24-legal-business.md)

* [ ] Required legal documents published
* [ ] Required disclosures published
* [ ] Pricing correct
* [ ] Taxes configured
* [ ] Payment flow verified
* [ ] Refund/cancellation behavior verified
* [ ] Support contact exists
* [ ] Domain/email infrastructure ready

## Launch

Guide: [P24-launch](the-checklist/P24-launch.md)

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

Guide: [P25-daily-continuous](the-checklist/P25-daily-continuous.md)

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

Guide: [P25-weekly](the-checklist/P25-weekly.md)

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

Guide: [P25-monthly-periodic](the-checklist/P25-monthly-periodic.md)

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

Guide: [P26-growth](the-checklist/P26-growth.md)

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

Guide: [P27-project-maintenance-agent-hygiene](the-checklist/P27-project-maintenance-agent-hygiene.md)

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

Guide: [P28-retirement-exit](the-checklist/P28-retirement-exit.md)

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
