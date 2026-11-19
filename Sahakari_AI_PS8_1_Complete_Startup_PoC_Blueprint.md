# SAHAKARI AI — THE COOPERATIVE PRODUCTION TRUST OS

> **PS 8.1 | Tech4Bharat 2026 / JanAI Mass Entrepreneurship Challenge | Theme 08 — Youth & Women Empowerment**  
> **Official problem:** “Women's self-help groups lose orders and members' trust because fulfilment and pay are chaotic.”  
> **Product vision:** Turn a loosely coordinated group of home-based producers into a reliable, transparent, buyer-ready micro-manufacturing network — without taking decisions or earnings away from its members.  
> **Primary beachhead:** Women's self-help groups producing standardized school uniforms and other stitched items.  
> **Product category:** Offline-first, voice-accessible, agent-assisted cooperative production and earnings platform.  
> **Document status:** Complete **build-and-validation blueprint**, not a claim that all software has been implemented.  
> **Version:** 2.0 — 18 November 2026.

---

## 0. The one-minute decision

**Build this, not a generic SHG marketplace or chatbot:**

**Sahakari AI is an operating system for one bulk order shared among many women.** It turns buyer requirements into a feasible production plan; lets members privately accept or decline assignments; records stage-wise work, quality and corrections; recalculates deadline risk; and produces member-understandable earnings plus a buyer-facing **Order Passport** backed by traceable events.

### The unmistakable differentiator: **Cooperative Proof Layer (CPL)**

Each important action creates an attributable, revisable-with-history **evidence event**:

**Order requirement → agreed costing → approved assignment → member work confirmation → quality decision → dispute/correction → approved earnings → payout status → buyer delivery evidence.**

Other products may manage product listings, orders or SHG profiles. **Our specific hypothesis** is that a connected, member-verifiable *production-to-earnings evidence chain* can make small groups more reliable and trustworthy to buyers. This is a product thesis to validate in the field, **not an unsupported claim that no competitor has such features**.

### Five non-negotiable proofs for the jury

1. **A real algorithm** produces feasible assignments using skills, stages, availability and capacity — not hardcoded numbers.
2. **A real offline operation** is entered on a phone in airplane mode and then synchronizes without duplication.
3. **A real late-work incident** is detected and replanned with member consent; no hidden forced reassignment.
4. **A real dispute** is raised and resolved with immutable *history*, not by overwriting an earlier earning.
5. **A real Order Passport** is generated from stored events, separating verified facts from simulated payment states and unverified assumptions.

**A complete successful 5-minute demonstration of those proofs matters more than twenty decorative features.** No project can guarantee a hackathon win, but these proofs offer substantial differentiation.

---

## 1. Problem-to-product fit: exactly what PS 8.1 asks

### The problem from the supplied brief

When an SHG takes a bulk order across roughly 10–15 members, splitting work, maintaining quality, consolidating output and sharing pay are chaotic. Manual accounting erodes trust; groups may underprice by 30–40% when material, labour and margin are not properly calculated. The challenge also highlights that some members have low literacy and that **allocation and payout must be fair**. The group must approve every payout; each member must be able to access and understand her own record.

### Four measurable pains

| Current pain | Root cause to test | Specific product response | Observable outcome |
|---|---|---|---|
| Bulk orders are missed or delayed | Verbal allocation, no capacity accounting, slow escalation | Stage-aware plan + deadline-risk alerts + consent-based reassignment | On-time order completion and earlier warning |
| Members cannot verify how work was allocated | No shared assignment record | Member-visible task agreement and revision history | Fewer unidentified assignment changes |
| Quality rejection causes arguments | Checks happen late; reasons are undocumented | Photo/notes plus a documented accept/rework/reject decision | Faster traceable quality resolution |
| Pay is split by guesswork or unclear deductions | Mixed records, opaque rules, no audit trail | Deterministic earnings ledger, member audio summary, group payout gate | Reconciled ledgers and fewer unresolved disputes |

### Explicit boundaries

- **The SHG owns the work.** A recommendation never becomes binding without its required human consent.
- **The group controls pay rules** under its applicable obligations and approved bylaws; AI cannot invent a wage rate.
- **A quality reviewer decides acceptance.** Computer vision provides assistance, not a final verdict.
- **Payments in the hackathon are simulated.** Never imply that money moved or a bank verified a transfer.
- **A buyer report states only what the stored records support.** It is not an independent certification of labour practices.

---

## 2. Why now? Market and competitor reality

India's DAY-NRLM ecosystem is large: a Ministry of Rural Development update dated **2 September 2026** describes **more than 10 crore women in over 93 lakh SHGs**. This is context for potential reach, **not an addressable market forecast**. Source: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2305947&lang=1&reg=3

Existing government efforts already cover enterprise profiles, product marketing, catalogue management and e-commerce. In particular, **eSaras** provides online marketplace, inventory, order, logistics and payment-related functions. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2283704 and https://www.esaras.in/marketplace

**Do not pitch Sahakari AI as the world's first SHG app.** Pitch it as the **production-execution and member-trust layer** usable *before, during and after* a marketplace order.

### Strategic positioning

| Common category | Typical focus | Sahakari's narrow wedge |
|---|---|---|
| Online SHG storefront | Discovery, listings, buyer checkout | Can the SHG *deliver a shared order reliably?* |
| Spreadsheet / basic bookkeeping | Totals and balances | Can *each member* understand and challenge the events behind the total? |
| Generic ERP | Purchase orders and inventory | Can an offline home-based producer with a basic phone actually participate? |
| Generic AI chatbot | Advice and summaries | Does every suggested action produce a checked, attributable operational event? |
| Sahakari AI | **Cooperative production execution** | **Feasible production + proof of contribution + explainable earnings + dispute workflow** |

**Defensible advantage to develop over time:** validated cooperative workflows, multilingual usability data, stage-time estimates, trust/audit design, relationships with producer groups and verified supplier performance — **not** an unsubstantiated claim that AI alone is a proprietary moat.

---

## 3. Product identity and pitch

**Name:** Sahakari AI  
**Positioning:** *From Bulk Order to Every Member's Verified Earnings.*  
**One-line jury pitch:** “A women's producer group can receive a 500-piece order, share it fairly, recover from delays and prove exactly how each member's earnings were calculated — even when phones go offline.”  
**Longer pitch:** “Most solutions help SHGs find customers. Sahakari helps them earn and retain customers by delivering orders reliably and keeping the group informed. Our agent coordinates the workflow, our optimizer checks feasibility, and our Cooperative Proof Layer makes production and payouts explainable and contestable.”

### Ideal first users

- **Operational customer:** 10–15-member women-run stitching collective taking repeat bulk uniform or garment orders.
- **Everyday user:** member producing at home, sometimes on low connectivity and with limited time for data entry.
- **Supervisor:** elected group leader and designated quality checker.
- **External observer:** school/bulk procurement buyer wanting delivery commitments and traceability.
- **Potential payer:** a producer enterprise, SHG federation, established procurement partner or livelihood-support organization. Avoid charging members a large fee before willingness-to-pay research.

### What NOT to build for the first PoC

No public marketplace, no direct lending, no live bank transfers, no compulsory biometric attendance, no blockchain token, no unvalidated wage-law certification, no overpromised image-quality grading, and no machine-learning “fairness score” presented as proof of social fairness.

---

## 4. Four flagship innovations that must work together

### 4.1 Cooperative Production Digital Twin (CPDT)

One order is not simply “500 pieces assigned to 12 women.” It is a **stage graph** with dependencies:

`Buyer order → cutting & kits → sewing/assembly → finishing & quality → packed/ready → dispatched → accepted`.

The twin tracks **requested**, **in progress**, **stage completed**, **quality accepted**, **rework**, **rejected** and **delivered** quantities *without double counting*. It continuously recomputes outstanding work, machine/skill constraints, potential bottlenecks and schedule feasibility.

**Differentiator:** It recognizes that a buttonholer, cutter or quality checker cannot automatically be allocated the same complete-garment quota as a sewing artisan. It also knows that completing sewing is not the same as delivering an accepted uniform.

### 4.2 Consent-aware scheduling and recovery

Use **Google OR-Tools CP-SAT** or a simpler deterministic feasible allocator as the first implementation. Inputs: member skills, machine compatibility, voluntarily declared hours, task duration, existing allocations, deadlines, production stage and group-approved protections. **AI explains the recommendation; a constraint solver decides whether it is mathematically feasible.**

When a member is delayed, generate options such as: move four sewing tasks to an eligible volunteer, extend a noncritical internal milestone, or warn that the deadline cannot safely be promised. Display the tradeoffs and require the receiving member to accept.

**Differentiator:** The agent cannot force assignment, use undisclosed private circumstances, or silently overload a helper.

### 4.3 Cooperative Proof Layer / Order Passport

An **Order Passport** is a buyer-facing digest that references:

- Purchase order ID and agreed specifications.
- Approved material-cost and production assumptions with source classes.
- Versioned assignment and completion events.
- Quality sampling and review outcomes, including rework.
- Delay alerts, proposed recovery and accepted revisions.
- Final accepted quantities and documented dispatch/receipt.
- Attested group-level payout **approval** status; **never individual private bank details**.

Each event has `event_id`, `actor_id`, `role`, `order_id`, `action`, `entity_id`, `revision`, `event_time`, `server_received_at`, `device_id`, `source`, and `previous_event_hash`. Preserve the sequence and corrections in an append-only log. A hash chain helps reveal later alteration of an exported log, but **does not independently prove that the underlying real-world event happened**. Seek member and reviewer attestations.

**Differentiator:** Buyers can inspect a *production trail*, not just see a “quality assured” sticker.

### 4.4 Member-readable earnings and challenge rights

Every member gets a **private, simple ledger**, in Tamil first:

> “You completed 18 accepted sewing operations at the group's approved rate of ₹45 each. Gross earnings: ₹810. Recorded advance: ₹200. Proposed net payable: ₹610. This payment is awaiting the group's approval.”

The member can press **“Agree”**, **“Something is wrong”**, or **“Hear again.”** A dispute freezes the **affected proposed line or payout for review**; it does not imply real escrow or block unrelated members' approved payments. Approved corrections are new adjustment events.

**Differentiator:** Trust is created by understandable evidence and the ability to challenge errors, not by a claim of automatic fairness.

---

## 5. Complete system architecture

```text
                           [BUYER WEB PORTAL]
                              Create / track order
                                      |
           [LEADER WEB APP]           |          [MEMBER ANDROID PWA]
        Costing, quality, votes       |       Tamil/audio, accept, check-in
                     \                |               /
                      \         HTTPS API           /
                       +--------------+-------------+
                                      |
                            [FastAPI BACKEND]
                                      |
             +------------------------+-------------------------+
             |                        |                         |
       [WORKFLOW ENGINE]        [TOOLS + AGENT]          [TRUST / RULES]
    Orders, stages, status     Explain / recommend       Auth, consent,
        state machines          bounded actions          payout quorum
             |                        |                         |
   +---------+---------+      +-------+-------+         +-------+-------+
   | Deterministic      |      | Document      |         | Costing and   |
   | OR-Tools scheduler |      | interpretation |         | payroll engine|
   | and risk scorer    |      | and Tamil help |         | (no LLM math) |
   +---------+---------+      +-------+-------+         +-------+-------+
             \                        |                         /
              +-----------------------+------------------------+
                                      |
                          [POSTGRESQL + EVENT LOG]
                              [OBJECT STORAGE]
                                      |
                     [ORDER PASSPORT / PDF GENERATOR]
                                      |
                        [BUYER / MEMBER / GROUP REPORTS]

  OFFLINE MEMBER DEVICE:
  Cached PWA shell + IndexedDB local outbox + local UUIDs + queued events
             -> reconnect -> authenticated sync -> validation -> receipt
             -> conflict review if needed -> update visible device state
```

### Architecture choices and reasons

| Concern | Chosen approach | Why it is credible |
|---|---|---|
| Interface | React + TypeScript PWA; responsive leader/buyer views | Familiar web stack, phone-friendly, demoable |
| Offline state | Service worker (cached app shell) + IndexedDB outbox | Reliable structure for offline data, not fragile `localStorage` alone |
| APIs | FastAPI + Pydantic request validation | Explicit contracts and testable business logic |
| Database | PostgreSQL | Transactional assignments, payroll and event consistency |
| File evidence | S3-compatible object storage or local demo storage | Supports photos, receipts and export PDFs |
| Scheduler | OR-Tools CP-SAT; fallback greedy feasible allocator | Formal constraints and clear infeasible states |
| Agent | Tool-using orchestrator with bounded permissions | Interprets, summarizes and proposes; never auto-pays |
| Cost and pay | Decimal/integer paise, versioned rules | Prevents floating-point and silent payout drift |
| Audit | Append-only events, transactionally enforced revisions, hash-chain on export | Supports reproducibility and later corrections |
| Audio | Tamil text + approved local TTS or pre-recorded offline clips | Avoid assuming browser Tamil speech is available offline everywhere |
| Vision | Optional photo quality pre-screening | Keeps human decision on actual garment quality |
| CI/tests | pytest, Playwright, API integration tests | Real verification, including failure modes |

**Primary references:** OR-Tools: https://developers.google.com/optimization/cp ; PWA offline data: https://web.dev/learn/pwa/offline-data ; MDN speech: https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

### Agent tools: explicit, permission-bounded

1. `parse_buyer_order()` — extracts structured requirements with source spans and missing fields.
2. `price_quote()` — calls deterministic costing, reports assumptions and risk.
3. `check_capacity()` — evaluates constrained schedule and bottleneck.
4. `propose_rebalance()` — generates *uncommitted* alternative assignments.
5. `explain_earnings()` — retrieves checked ledger lines and translates explanation.
6. `draft_dispute_resolution()` — proposes adjustment for humans to decide.
7. `prepare_order_passport()` — generates a draft with provenance warnings.

**Not available to an LLM:** `release_money`, `change_group_bylaws`, `accept_quality_on_behalf_of_member`, `override_votes`, `edit_verified_event`. Agents are for decision support, **not sole financial authority**.

---

## 6. End-to-end product: who sees which screens?

### Role A — Buyer

1. **Create order:** product variant, quantity, required date, quality specification, requested evidence.
2. **See quote:** price, lead time and terms, *approved by group*, not generated arbitrarily.
3. **Track milestones:** accepted stages, exception notices, order readiness.
4. **Receive Order Passport:** item count, quality records, dispatch evidence and approved aggregate assurance fields.

### Role B — Group leader

1. **Command Center:** revenue at risk, stage throughput, current orders, late tasks, pending disputes.
2. **Quote Builder:** materials, wage rules, delivery cost, wastage assumptions, group reserve.
3. **Schedule Studio:** members, skills, time limits, stage queues, bottleneck warnings.
4. **Approval Queue:** accept recommended assignments or request edits.
5. **Quality Desk:** sampled images, checklists, accept/rework/reject with reasons.
6. **Consensus Desk:** member earnings preview, quorum state, objections, approval release.
7. **Export Center:** customer documents, operational records, group accounting statements.

### Role C — Member

1. **My Work Today:** clear Tamil label, quantity, pay rate, deadline, accept/decline.
2. **I Completed:** quantity input, optional photo, simple confirmation.
3. **Need More Time:** private voluntary status change, not an AI-inferred reason.
4. **My Earnings:** gross, deductions, adjustments, pending vs approved vs simulated-paid.
5. **Hear My Earnings:** audio where device supports the configured offline voice; text and icon fallback.
6. **Challenge an Entry:** raise correction, attach explanation, see decision history.
7. **Sync Status:** pending on device, accepted by server, needs review, or rejected with reason.

### Role D — Quality checker / accountant / group approver

Capabilities are role-specific, with the smallest necessary access. A checker cannot change bank details or wage rules. A finance approver cannot rewrite past production quantities.

---

## 7. End-to-end PoC scenario: a realistic, testable single order

**DEMO DATA — SYNTHETIC, NOT A CLAIM OF COMPLETED FIELD PILOT**

- **Order:** `PO-2026-SHIRT-001` — 500 standardized school-uniform sets over 10 workdays.
- **Group:** 12 simulated members; role assignments and machine capacities intentionally model distinct stages.
- **Product scope:** One standardized size/specification for the PoC. Add size variants only after the core workflow passes tests.
- **Acceptance:** Defined visual checks plus approved human QC; no automatic pass based on one photo.
- **Each set has three production stages:** (A) cutting/kitting → (B) sewing/assembly → (C) finishing/QC/packing.
- **Input rates below are scenario assumptions, not asserted regional wage or machine-performance standards.**

### 7.1 Stage-aware capacity model — resolves the original README's mixed-role problem

| Stage | Members (of 12) | Hours per member/day | Assumed minutes of work per set | Nominal capacity/day |
|---|---:|---:|---:|---:|
| A. Cutting and kitting | 2 | 4 | 8 | `2 × 4 × 60 / 8 = 60` |
| B. Sewing and assembly | 8 | 5.5 | 45 | `8 × 5.5 × 60 / 45 = 58.67` |
| C. Finishing, QC and packing | 2 | 6 | 12 | `2 × 6 × 60 / 12 = 60` |
| **Bottleneck** | **12 total** | — | — | **58.67 gross sets/day** |

**Required pace:** `500 / 10 = 50 accepted sets/day` on average.  
**Gross theoretical buffer:** `58.67 − 50 = 8.67 sets/day` at the bottleneck, **before** pauses, rejected items, learning curves, stage-to-stage queues and delivery arrangements.  
**Productivity interpretation:** This is a **capacity upper-bound check**, not a proof that 500 sets will be delivered on time. A feasible day-by-day schedule and handling of rework must be separately verified.

**Avoid a misleading single score:** A perfectly equal utilization ratio among members does not by itself establish fair earnings. Show whether assignments respect *voluntary hours, eligibility, previously agreed pay rates and group priorities*.

### 7.2 Order simulation sequence for the jury

| Demo moment | Actor | Real user action | Expected visible result |
|---|---|---|---|
| 1 | Buyer | Upload 500-set RFQ | Structured fields with cited source and unknowns |
| 2 | Leader | Review costing and send quote | Traceable cost breakdown, explicit buyer-price warning |
| 3 | Leader | Press **Generate feasible plan** | Solver status, stage bottleneck, candidate allocations |
| 4 | 2 members | Accept work; one declines extra work | Consent recorded; solver revises or marks infeasible |
| 5 | Member A | Go offline and mark 6 units sewn | Local outbox shows `Pending sync` |
| 6 | Another device | Enter an overlapping quantity update | Conflict surfaced; no silent extra credited output |
| 7 | Member A | Reconnect | Exactly one accepted event, with receipt and correct quantities |
| 8 | Group leader | Simulate Day 4 work shortfall | **7 sewing-stage operations behind plan**; delay risk detected |
| 9 | Members / leader | Accept a feasible 4+3 redistribution | Updated task assignments, consent and revision history |
| 10 | Quality checker | Reject 3 pieces for rework | Accepted and rework quantities change, but total conservation holds |
| 11 | Member | Dispute one earning entry | Pending disputed amount and reason visible |
| 12 | Group | Correct line, reach configured approval quorum | Versioned payroll and clear approved status |
| 13 | Buyer | Open Order Passport | Approved quantity, exceptions and source-backed evidence only |

### 7.3 Why the Day 4 recovery is feasible (illustrative check)

A sewing-stage member was due to complete **seven** assignments on Day 4 but completed zero. Rather than saying an arbitrary member can absorb seven jobs, choose **two eligible volunteers** and check their remaining capacity.

- For each sewing member: `5.5 × 60 / 45 = 7.333... sets/day` gross rate.
- Six subsequent working days provide approximately `6 × 7.333 = 44` gross sewing operations per person.
- Volunteer A already has **36** remaining operations: spare gross capacity `44 − 36 = 8`; recommend transferring **4**.
- Volunteer B already has **38** remaining operations: spare gross capacity `44 − 38 = 6`; recommend transferring **3**.
- Using the *optional, group-approved 75% spare-buffer rule*: A's transfer `4 ≤ 0.75 × 8 = 6`; B's transfer `3 ≤ 0.75 × 6 = 4.5`.
- Both must accept. Task competencies and downstream stage capacity must still be satisfied. If neither accepts, raise a *cannot safely commit* warning.

**Do not show a falsely precise completion probability.** Instead show deterministic schedule feasibility under stated assumptions, plus tested scenarios for absenteeism, quality rework, and slow material arrival.

### 7.4 Costing that balances exactly

The original README models a **₹260.55 operational cost per set** and a **12% group savings allocation**. Keep its useful economics, but clearly label unverified rates as **demo assumptions** until original supplier quotations and meeting records are available.

| Cost component | Per set (₹) | Demo provenance |
|---|---:|---|
| Fabric, 2.2 m | 143.00 | Illustrative supplier rate — replace with uploaded quotation |
| Trims and accessories | 22.00 | Illustrative supplier rate — replace with uploaded quotation |
| Cutting wastage allowance, 7% of materials (`165 × 0.07`) | 11.55 | Model assumption |
| Direct production labour | 70.00 | Proposed group-agreed labour budget, not a legal wage claim |
| Packing and local transport | 14.00 | Model assumption |
| **Operating cost** | **260.55** | Exact sum of preceding rows |
| Group savings allocation, 12% of cost | 31.27 | Illustrative bylaw target, not an external expense |
| **Recommended minimum target quote** | **291.82** | Rounded `(260.55 × 1.12)` |

If the buyer offers ₹160, the shortfall from the **modeled operating cost** is **₹100.55 per set**, or about **38.6%** of the cost. This does **not** establish actual wage theft; it shows that the offer does not cover the assumed costs. Check wage requirements separately with qualified local expertise.

At 500 sets, **modeled production labour** is `500 × ₹70 = ₹35,000` before individual deductions, corrections and group policies. A coherent sample group-approved **stage pay allocation** is:

| Stage completed and human-accepted | Member piece-rate portion |
|---|---:|
| A: cutting/kitting | ₹8 per set |
| B: sewing/assembly | ₹45 per set |
| C: finishing/QC/packing | ₹17 per set |
| **Total group labour budget** | **₹70 per set** |

The ₹70 budget is a *per-set labour allocation*, not a claim that every worker earns ₹70 for each sewing operation. Example: a sewing member completes 18 **accepted sewing-stage operations** at **₹45** each, giving `18 × 45 = ₹810` gross. An **approved** ₹200 advance deduction results in **₹610 proposed payable**, pending member/group review. If a different group chooses another rule, version the rule and recalculate explicitly.

### 7.5 Invariant: no imaginary garments or money

For each order and stage, enforce conservation:

`incoming − completed − scrapped − pending = 0` (with recorded transfers and explicit definitions).  
`accepted + rework_pending + rejected = inspected` (for the same inspection batch, no overlap).  
`sum(approved_member_gross_pay) = sum(accepted_stage_units × approved_stage_rate)` (plus explicit line adjustments).  
`net_payable = gross − approved_deductions + approved_adjustments`, never silently clamp a negative figure; flag it for review.

**Important:** One garment can generate separate valid paid operations at A, B and C, but it must not be counted as three *finished products*.

---

## 8. Scheduling model: constraints, objective, explainability

Let `x[i,s,d]` be the **integer** number of stage `s` operations assigned to member `i` on day `d`.

**Inputs:** member stage skills, available minutes, consent, accessible machine type, estimated minutes per operation, work-in-progress, deadline, quality/rework allowance and approved maximum workload. Capacities are recalibrated from actual accepted records; initial rates remain tagged assumptions.

### Hard constraints (never optimized away)

1. `x[i,s,d] ≥ 0` and integer.
2. Unqualified member → `x[i,s,d] = 0`.
3. Member not available or declining → no new unaccepted assignment.
4. `sum_s(x[i,s,d] × t[i,s]) ≤ volunteered_minutes[i,d]`.
5. Downstream stage cannot complete units that are not available from its predecessor (accounting for valid opening WIP).
6. Final accepted order quantity cannot exceed eligible completed quantities.
7. No unapproved change to piece rates, pay rules or governing quorum.
8. Existing committed tasks are protected unless the owner and affected member authorize a change.
9. Schedule respects order deadline or reports `INFEASIBLE`; never quietly change the date.

### Soft objective (configurable priorities)

Optimize weighted terms for late units, overload, concentration of opportunity, excess reassignment, idle time and estimated cost **subject to** the hard constraints. Report the trade-off, not one opaque “fairness score.” Jain's fairness index may be shown as a **secondary diagnostic** for comparable normalized utilization; it is not ethical certification.

### Required solver responses

- `FEASIBLE` with assumptions and alternatives.
- `INFEASIBLE` with an explanation of limiting stage, capacity or date.
- `UNKNOWN/TIMEOUT` with a *not proven feasible* warning, not fabricated optimum.
- `NEEDS_MEMBER_CONSENT` when a plan is mathematically possible but not approved.

See OR-Tools constraint/job-shop guides: https://developers.google.com/optimization/scheduling/job_shop

---

## 9. The Cooperative Proof Layer: trust, offline sync and disputes

### 9.1 Minimum domain model

```text
Group -> Membership -> MemberSkills / MemberAvailability
Buyer -> Order -> OrderLine -> ProductSpec -> ProductionStage
Order -> WorkBatch -> Assignment -> WorkEvent -> QualityEvent
Order -> PriceBookVersion -> ApprovedQuote
Order -> LedgerEntry -> PayrollRun -> ApprovalVote -> PaymentStatus
Order -> Dispute -> ResolutionEvent
Order -> OrderPassportExport
Device -> OfflineOutboxEvent -> SyncReceipt
```

### 9.2 The event envelope

```json
{
  "event_id": "f9f2c28a-3dea-4ec2-8b37-1441f947813d",
  "idempotency_key": "android-A91:seq-00053",
  "order_id": "PO-2026-SHIRT-001",
  "entity_id": "assignment-A-017",
  "event_type": "WORK_QUANTITY_REPORTED",
  "actor_id": "MEMBER-07",
  "actor_role": "member",
  "device_id": "android-A91",
  "base_revision": 4,
  "client_time": "2026-11-18T09:30:00+05:30",
  "quantity": 6,
  "stage": "SEWING",
  "status": "PENDING_SERVER_VALIDATION",
  "evidence_source": "MANUAL_MEMBER_ENTRY"
}
```

**Never treat the client timestamp as authority.** Use the server's monotonic revision/sequence after authenticated validation. Client time can be recorded as a hint, together with clock-skew warnings.

### 9.3 Correct offline synchronization: no last-write-wins on pay

- The local app shell loads from the service-worker cache; pending events live in **IndexedDB**, protected by the device's normal app-access safeguards and minimized sensitive content.
- When offline, a member can capture an *unverified draft work event*; label it `Pending sync`.
- On reconnect, send events with unique idempotency keys; the server validates identity, role, quantities, current revision and business state.
- Repeated event → return the **same receipt**, **do not** increment production twice.
- Out-of-date base revision → return `409 CONFLICT`; prompt review or offer a safe derived merge where the operations are provably independent.
- **Never** automatically choose the latest timestamp for a conflicting payout, work correction, vote, QC status or advance deduction.
- If offline edit conflicts with approved pay, create a **correction request**, not a rewritten approved ledger.
- Display a human-readable sync receipt and an unsynced-item count. Allow members to verify server acceptance.

### 9.4 Dispute and quorum protocol

1. Member opens a specific ledger or QC line and raises a reason-coded dispute.
2. Existing record remains visible; the affected line becomes `DISPUTED`.
3. Checker/leader examines evidence and proposes a signed adjustment or rejection explanation.
4. Member sees the resolution in Tamil and can accept or escalate under group rules.
5. New approved adjustment event is appended. The prior line is never erased.
6. Group reviews the payout snapshot **version**; approvals refer to that snapshot's hash.
7. A changed snapshot invalidates stale approvals and requires re-approval.
8. The group-configured quorum is checked transactionally. **For demo only**, use 2/3 of eligible members plus leader signature *if this rule is explicitly adopted for the simulated group*; do not claim this is universally required of all SHGs.
9. `APPROVED_FOR_EXTERNAL_PAYMENT` is **not** `PAID`. Mock UPI reference IDs are labelled `DEMO ONLY`.

### 9.5 Security, privacy and audit protections

- HTTPS, secure server sessions, strong PIN/password or suitable auth, and per-group tenant isolation.
- Row-level access checks; a member views only her private wage details, while group aggregate reporting is permissioned.
- No government ID, biometric, full bank account or minors' data required for the PoC; use synthetic accounts.
- Minimum permissions for camera/microphone; don't record audio by default.
- Optional-photo evidence has retention/deletion rules and access limitations.
- No secrets or API keys in the PWA; never include private account information in public Order Passports.
- Hash-chained append-only *application* event trail + privileged audit; explain the limitations of application-controlled hashes.
- Perform authorization **server side**, not merely by hiding buttons.

---

## 10. Tamil-first UX — accessibility without false claims

### Member interaction: 3-button default

**என் வேலை** (My work) → **முடித்தேன்** (I completed it) → **என் வருமானம்** (My earnings).

Use clear numbers, icons, confirmation and accessible audio. Voice is an **assistive interface**, not a prerequisite for completing work. A person must be able to cancel or correct misrecognized speech before it becomes an event.

### Audio implementation reality

- Speech *recognition* may use a cloud service; browsers vary, and on-device Tamil support **must be tested** on target devices.
- Speech *synthesis* depends on installed/browser voices; do not promise zero latency or automatic offline Tamil support on every phone.
- **Reliable PoC fallback:** pre-record approved Tamil prompts for core actions + offline cached numeric/amount display + large buttons; use live TTS only after device capability checks.
- Do not announce “money transferred” until an actual verified payment webhook/confirmation exists. Say “approved” or “proposed” as appropriate.

References: https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition and https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API

---

## 11. Optional assistive computer vision (after the core workflow)

**Target only a specific standardized garment and photo protocol.** The system may reject unusable photos, crop garments, highlight obvious shape/seam deviations and route uncertain items for human QC. **It must not** infer material strength, stitch integrity, dimensions or overall acceptance solely from a single unconstrained photograph.

| Task | PoC method | Safeguard |
|---|---|---|
| Image readability | Laplacian blur measurement + exposure checks | Calibrate thresholds on captured phone images |
| Garment framing | Simple segmentation/cropping; capture guide | Permit manual retake |
| Placket or visible seam alignment | Edge/line measurements with uncertainty | Only flag, never auto-reject |
| Final item quality | Human checklist, optional sample measurements | Human signature and reason codes |

**High-value demo:** A blurry image is rejected as **insufficient evidence**, not as a defective garment. A clearly visible defect is marked **needs human review**. That separation is technically and ethically stronger than a fabricated 99% inspection-accuracy claim.

---

## 12. API contracts and backend state machines

### Key API endpoints

| Method | Path | Behavior |
|---|---|---|
| `POST` | `/v1/orders` | Buyer/leader creates draft order |
| `POST` | `/v1/orders/{id}/quote/calculate` | Deterministic costs with source tags |
| `POST` | `/v1/orders/{id}/quote/approve` | Group-authorized quote transition |
| `POST` | `/v1/orders/{id}/plans/generate` | Create uncommitted feasible proposals |
| `POST` | `/v1/assignments/{id}/accept` | Member accepts/declines with revision |
| `POST` | `/v1/sync/events` | Batch offline idempotent event submission |
| `POST` | `/v1/quality/events` | Qualified reviewer signs accept/rework/reject |
| `GET` | `/v1/members/me/earnings` | Permissioned member ledger |
| `POST` | `/v1/disputes` | Raise a line-specific challenge |
| `POST` | `/v1/payroll/{id}/submit` | Freeze draft snapshot for approval |
| `POST` | `/v1/payroll/{id}/vote` | Record eligible vote against snapshot revision |
| `POST` | `/v1/payroll/{id}/finalize` | Validate quorum and lock approved statement |
| `GET` | `/v1/orders/{id}/passport.pdf` | Generate provenance-tagged export |
| `GET` | `/v1/audit/orders/{id}` | Permissioned event trail |

### Example state machines

```text
ORDER: DRAFT -> QUOTED -> GROUP_APPROVED -> ACCEPTED
       -> IN_PRODUCTION -> QC_COMPLETE -> DISPATCHED -> BUYER_RECEIVED -> CLOSED
       [ON_HOLD or CANCELLED through controlled, auditable transitions]

ASSIGNMENT: PROPOSED -> MEMBER_ACCEPTED -> IN_PROGRESS
            -> REPORTED_COMPLETE -> QC_ACCEPTED | REWORK | REJECTED
            [DECLINED or REASSIGN_REQUESTED, with consent]

PAYROLL: DRAFT -> SNAPSHOT_LOCKED -> VOTING -> GROUP_APPROVED
         -> PAYMENT_EXPORT_READY -> EXTERNALLY_CONFIRMED_PAID
         [DISPUTED / SUPERSEDED / EXPIRED approvals]
```

**No fake transitions:** a `SIMULATED_PAID` status is a distinct demo state and must never share a UI indicator with real external confirmation.

### Invariants to encode in database transactions

- One business event per idempotency key, enforced by a unique constraint.
- One applicable latest *approved* price-book version for each operation at its effective date.
- An assignment accepted by one member cannot be reassigned without the necessary documented approvals.
- No payroll finalization if approvals refer to an older snapshot version.
- No negative assigned quantity, accepted production, or duplicate credited output.
- Financial calculations use integer paise and well-defined half-up rounding at documented boundaries.

---

## 13. Hardware requirements — exact answers for the jury

### Short answer

**Mandatory industrial hardware: NONE.** PS 8.1 is primarily a **software/agentic AI** product. No Raspberry Pi, ESP32, PLC, microcontroller, camera module, sensors or custom PCB is required to prove the central workflow.

### 13.1 Minimum demo hardware (use equipment the team already owns)

| Item | Minimum practical specification | Why | Required? |
|---|---|---|---|
| Development laptop | Modern 4-core CPU, **8 GB RAM**, SSD with **10 GB free**, Windows/Linux/macOS | Run development server, DB, browser and tests | **Yes** (one) |
| Android phone A | Android device with modern Chromium browser, ~**3–4 GB RAM**, microphone/speaker | Offline member workflow and Tamil prompts | **Yes** (one) |
| Android phone B | Second phone or browser device | Demonstrate different actor / sync conflict | **Recommended**, can emulate |
| Wi-Fi / hotspot | Local network or phone hotspot | Initial app loading and controlled reconnect | **Yes** for multi-device local demo |
| Charging and backup | Phone chargers; optional power bank | Stable 5-minute demo | **Strongly recommended** |
| Camera | Built-in Android camera | Optional image evidence | Already in typical phone |
| Cloud account | Small backend instance, or host locally on laptop | Stores transactions and reports | Optional if using local demo server |

**More comfortable setup:** one laptop with **16 GB RAM** if running multiple containers, an LLM locally, emulator and development tools simultaneously. Cloud-based LLM inference does not require a local GPU. An offline-first *member* interaction should remain usable if the LLM is unreachable.

### 13.2 Optional physical props that make the demo memorable

| Optional item | Purpose | Necessary? |
|---|---|---|
| **10–20 sewn sample garments or fabric pieces** | Show a believable work/QC handoff | No |
| Printed batch cards with QR codes | Scan to open the specific work batch and its Order Passport | No; useful differentiator |
| Phone tripod + small LED light | Reproducible optional QC photos | No |
| Bluetooth thermal printer | Print batch/receipt slips after approval | No; can add failure modes |
| Local mini-PC or Raspberry Pi | Offline gateway at federation office | **Not necessary** for this PoC |
| Barcode/QR scanner | Faster scanning than phone camera | No |

**QR rule:** A QR code is a pointer to a batch ID with access-controlled validation, *not* a public link containing a member's earnings, phone number or bank information.

### 13.3 Production deployment hardware

- **Member:** existing affordable Android smartphone, no new industrial sensors.
- **Group leader:** Android tablet or smartphone; laptop helpful but not mandatory.
- **Federation:** regular desktop/laptop plus reliable data connection for periodic synchronization.
- **Server:** managed hosting and database; start with modest resources and right-size after load tests.
- **Optional:** shared device with QR cards or paper-backed workflow for members without personal smartphones; no requirement that everyone owns a phone.

**Hardware procurement priority:** 1) reliable phones with tested offline UI, 2) demonstration networking/power, 3) optional QR props, 4) optional camera rig. Don't spend limited hackathon time on ESP32 unless the event explicitly adds a hardware requirement.

---

## 14. Full live-demo script — 5 minutes, no hidden handwaving

| Time | On stage | Visible proof | What the judge should learn |
|---|---|---|---|
| 0:00–0:30 | Introduce buyer order and 12-member group | Real order dashboard with demo-data disclaimer | Real user, real problem |
| 0:30–1:00 | Input ₹160 buyer offer | Cost tool computes ₹260.55 operating cost and warns | AI does not invent finances |
| 1:00–1:35 | Generate production plan | Three-stage capacities, solver status, plan approval | Actual scheduling logic |
| 1:35–2:10 | Turn member phone offline; submit 6 operations | `Pending sync` appears without server request | Offline-first product |
| 2:10–2:35 | Reconnect and replay same event twice | One accepted event, identical receipt, unchanged total | Idempotency and integrity |
| 2:35–3:10 | Trigger Day 4 seven-operation shortfall | 4+3 proposed to two volunteers; members accept | Feasible recovery, not forced labour |
| 3:10–3:40 | Quality checker flags 3 units | Rework is separate from accepted quantity | Evidence-based QC |
| 3:40–4:20 | Show sewing member's ₹810/₹200/₹610 ledger, then dispute | Correction event visible, prior entry remains | Member trust and accountability |
| 4:20–4:45 | Group votes on revised payroll snapshot | Reached configured quorum or correctly blocked | Cooperative governance |
| 4:45–5:00 | Export buyer Order Passport | Source-backed timeline and simulated payment label | End-to-end product, not chatbot |

### Demo insurance: three backup modes

- **Plan A:** Two phones + laptop backend, internet initially enabled then intentionally disabled on member phone.
- **Plan B:** Laptop local network + seeded data, with screen recording of the offline/reconnect test.
- **Plan C:** Fully recorded non-edited scenario plus reproducible tests and stored logs if venue connectivity fails.

**Never switch a hardcoded video to the live UI and represent it as live inference.** Label recordings and seeded demo events clearly.

---

## 15. What code and tests must exist for a serious end-to-end PoC?

### Suggested repository structure

```text
sahakari-ai/
├─ README.md
├─ docs/
│  ├─ architecture.md
│  ├─ hardware.md
│  ├─ evaluation_protocol.md
│  ├─ privacy_and_governance.md
│  └─ field_interview_template.md
├─ frontend/
│  ├─ src/pages/{buyer,leader,member,qc,finance}/
│  ├─ src/features/{orders,assignments,offline,quality,earnings,disputes}/
│  ├─ src/locales/{en,ta}/
│  ├─ src/offline/{outbox,sync,conflictResolution}.ts
│  └─ public/{manifest.json,audio/}
├─ backend/
│  ├─ app/api/
│  ├─ app/domain/{orders,stages,work,quality,ledger,governance}.py
│  ├─ app/services/{scheduler,costing,passport,agent}.py
│  ├─ app/db/{models,migrations}/
│  └─ app/security/
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  ├─ property/
│  ├─ offline/
│  └─ e2e/
├─ demo/
│  ├─ seed_500_uniform_sets.py
│  ├─ demo_scenario.json
│  ├─ output_example_order_passport.pdf
│  └─ expected_metrics.json
├─ .github/workflows/ci.yml
├─ docker-compose.yml
└─ LICENSE
```

**Do not describe these paths as existing until implemented.** The uploaded original README references `app.py` and `tests/test_sahakari.py`; these files were *not* provided with this request. The blueprint's proposed structure is an upgrade path, not evidence that those files currently pass.

### 15.1 Critical automated test gates (minimum 30, expand as time allows)

**Costing and finance**

1. Exact quote arithmetic with integer paise.
2. Source tags for each cost line; missing supplier evidence is marked estimated.
3. A ₹160 offer triggers cost-floor warning without labelling it legal wage theft.
4. Rate version changes apply only to approved effective periods.
5. Accepted stage operations reconcile exactly to approved gross wage lines.
6. Deductions require recorded authorization and never silently generate a negative net.
7. An updated payout snapshot invalidates all stale votes.
8. No duplicate payroll entry after repeated API submissions.

**Scheduling and workflow**

9. Sewing worker is never assigned QC-only work without required skill.
10. Zero availability yields zero assigned work.
11. Infeasible order returns `INFEASIBLE`, not a fabricated plan.
12. Precedence: finishing cannot exceed eligible sewn work plus valid opening WIP.
13. Two helpers may accept a 4+3 redistribution within their capacities.
14. Helper rejection prevents a forced reassignment.
15. A single-member absence triggers evidence-based recalculation.
16. Two absences and upstream material shortage produce honest deadline-risk warnings.
17. Assignment revisions preserve previous assignments.
18. Accepted completed work cannot be unilaterally moved to a different member.

**Offline, sync, integrity**

19. Member records work with network disconnected.
20. Same event uploaded three times results in one ledger/business mutation.
21. Out-of-date revision returns explicit `409 CONFLICT` and does not overwrite.
22. Offline update cannot modify a payroll item already approved.
23. Device clock set ahead cannot win a conflict.
24. Device sync resumes after interruption without losing pending events.
25. Server restart retains committed order and event history.

**Governance, access, usability**

26. A member cannot view another member's private wage information.
27. QC reviewer cannot alter group pay rules.
28. Quorum failure blocks approval, including leader-only unauthorized attempts.
29. A challenged item remains in the audit history after correction.
30. Tamil member summary shows the same ledger numbers as the backend.
31. Audio unavailable → readable text/buttons remain usable.
32. Buyer Passport omits private account/contact information.
33. Simulated settlement can never be mistaken for externally confirmed payment.
34. QC blurry photo returns `INSUFFICIENT_EVIDENCE`, not `DEFECTIVE`.
35. PWA loads cached shell on the selected test phone while offline.

### 15.2 Validation hierarchy — be explicit

| Evidence type | What it proves | What it **does not** prove |
|---|---|---|
| Unit tests | Functions match specifications | Field adoption |
| API + E2E tests | Connected workflow works | Real customer value |
| Offline on two real phones | Selected connectivity scenarios work | All handset/browser combinations |
| Simulated 500-set order | Scheduling/accounting invariants | Actual factory-grade production rate |
| One SHG walkthrough | Local usability and pain points | Broad product-market fit |
| Real pilot order | Real operational usefulness | Guaranteed scalable ROI |

### 15.3 Metrics to show beside baselines

- **Schedule feasibility accuracy:** does the system correctly say feasible/infeasible on constructed known cases?
- **Late-work detection lead time:** hours/days before buyer deadline, measured against manual workflow.
- **Work-entry time:** median seconds for a member to log a completed batch.
- **Sync success:** percentage of offline events delivered exactly once after reconnection in test scenarios.
- **Ledger reconciliation:** all accepted piece counts and approved rates match aggregate gross, with **zero unexplained variance**.
- **Correction transparency:** each member can locate the original, disputed and revised entry.
- **Usability:** percentage of test participants able to complete tasks without facilitator assistance.
- **Pilot business outcome:** late units, rejected lots, reconciliation time and buyer renewals — report only if measured.

**Do not invent KPIs such as 99% accuracy, 40% income increase or guaranteed 100% fair pay.** Set targets, record observed values, and publish limitations.

---

## 16. Security and engineering quality gates before a demo

| Gate | Pass condition | Fail behavior |
|---|---|---|
| Authentication | Correct roles and tenant membership | API returns 401/403 |
| Cost confidence | Every quote line traceable or clearly assumed | `NEEDS_EVIDENCE` banner |
| Solver validity | Hard constraints satisfied and status disclosed | `INFEASIBLE` / `UNKNOWN` with explanation |
| Consent | Every new assignment requires appropriate member acceptance | `AWAITING_CONSENT` |
| Offline integrity | Idempotent event receipt and conflict handling | Safe retry or review queue |
| QC integrity | No evidence-free automatic acceptance | `HUMAN_REVIEW_REQUIRED` |
| Payroll integrity | Totals reconcile; group rules and snapshot votes valid | Freeze finalization |
| Payout integrity | No unverified transfer shown as actual | `DEMO_SIMULATION` clearly visible |
| Audit | Corrections append new events; no silent overwrite | Reject edit and record attempt |
| Privacy | Buyer export excludes member-sensitive fields | Export blocked/test fails |
| Accessibility | Essential task works without speech recognition | Buttons/text fallback |

**Architecture principle:** Fail *safe and explainably*, not *confidently and invisibly*.

---

## 17. Build priority: what's essential and what is optional?

### P0 — Must genuinely work

- Buyer order creation and a versioned accepted quote.
- Stage graph and solver-backed assignment proposals.
- Member acceptance, work entry and QC state changes.
- Offline PWA outbox, reconnection and idempotency demonstration.
- Deterministic member ledger, dispute correction and quorum gate.
- Buyer Order Passport and basic audit log.
- 30+ automated tests, with visible real results.

### P1 — Strong differentiators if P0 is stable

- Tamil audio passbook with device-tested offline fallback.
- QR batch cards and evidence scan.
- AI order-document extraction with user confirmation.
- Agent-generated natural-language explanations of scheduling alternatives.
- Comparative metrics versus manual notebook/spreadsheet procedure.

### P2 — Post-hackathon

- Vision-assisted QC with field image validation.
- Real buyer/marketplace integrations with permission.
- Real payout integration only after security, compliance and reconciliation review.
- Supplier/catalogue/credit features only if validated customer demand warrants them.
- Multi-product planning and federation-level production pooling.

**Avoid ten half-built tabs.** A trustworthy seven-screen product is more compelling than an inaccurate feature list.

---

## 18. Implementation plan by available time

### If only 48 hours remain

**0–8 h:** freeze one garment/order case; define data schema, auth/roles, seed script; build basic leader/member screens.  
**8–18 h:** build deterministic cost, stage capacity, simple constrained allocation, real backend records.  
**18–28 h:** add offline outbox, resync/idempotency and two-device test.  
**28–36 h:** earnings, dispute, quorum checks, auditable changes.  
**36–42 h:** Order Passport, staged demo, 15–20 critical tests.  
**42–48 h:** fix actual bugs, record fallback demonstration, sharpen user story.

This is a **stretch scope** for a small team. If time is insufficient, cut optional vision and voice recognition first — **never** cut correctness of pay or sync to preserve demo appearance.

### If 7–14 days remain

1. **Days 1–2 — Discovery:** three SHG member interviews, leader interview, buyer/NGO interview; document wage and stage rules.
2. **Days 3–4 — Domain + P0:** role-specific screens, API, schema, costing, stage-aware plan.
3. **Days 5–6 — Offline/consent:** PWA outbox, idempotency, concurrency tests.
4. **Days 7–8 — Trust:** quality, member earnings, dispute, quorum, PDF.
5. **Days 9–10 — Tamil/agent:** translation proofread by fluent speaker, audio capability checks, bounded agent tools.
6. **Days 11–12 — Verification:** devices, poor connection, security, invalid data, baseline metrics.
7. **Days 13–14 — Pilot and pitch:** stakeholder walkthrough, demo freeze, backup recording, honest report.

### Suggested team split (four people)

| Role | Deliverables |
|---|---|
| Systems/backend | State machines, APIs, PostgreSQL, auth, audit, transaction rules |
| Optimization/AI | Capacity solver, scenario simulator, source-grounded agent tools |
| Mobile/frontend | PWA, offline UX, Tamil accessibility, buyer/member views |
| QA/product/business | Financial correctness, automated/E2E tests, interviews, demonstration, pitch |

If team is smaller, combine roles but retain one person accountable for **verification**.

---

## 19. How to answer “Is this a real startup?”

### Beachhead business model — hypotheses to validate

1. **Pilot:** free short-term trial with one producer group and a buyer willing to review workflow evidence.
2. **Paid customer:** federation, procurement agency or producer enterprise pays for multi-group coordination and verified order reporting.
3. **Potential pricing experiments:** a modest organization subscription or an enterprise service fee per managed group/order, **not a percentage of a woman's earnings by default**.
4. **Key value metric:** fewer missed orders / less administrative reconciliation time / fewer disputed payouts, confirmed by customer records.
5. **Sales channel:** federation partnerships, SHG livelihood organizations, schools/uniform procurement partners; avoid claiming endorsement from them before one exists.

### Pilot acceptance gates

- One real producer group agrees to a demo using *consented*, non-sensitive order records.
- At least three members independently understand their pay statements and can challenge an entry.
- A group leader can create and close one order without developer intervention.
- At least one buyer says the Order Passport is useful, with documented objections.
- Savings/adoption claims are backed by before/after measurements, not synthetic scenario outputs.

### Defensible go-to-market sequence

`One garment type → One producer group → One repeat buyer → Two more groups → Federation deployment → Adjacent craft/food categories (after workflow adaptation).`

**Important:** Food requires materially different compliance and traceability processes; do not imply that a garment-quality workflow automatically certifies food safety.

---

## 20. Differentiation scoreboard for judges

| Dimension | Weak/common demo | Sahakari proof to show |
|---|---|---|
| AI | Chatbot says “assign fairly” | Verified constraint solver with infeasible/consent states |
| Business realism | “Women earn more” | Measured base costs, explicit assumptions, testable unit economics |
| Production | Assigns 500 finished units directly | Stage graph, quality state and conserved quantities |
| Accessibility | “Tamil support” label | Tested Tamil text/audio plus true offline fallback |
| Offline | Browser localStorage only | IndexedDB outbox, idempotency, conflict review, sync receipt |
| Trust | “Blockchain transparency” buzzword | Readable events, versioned approvals, disputes and corrections |
| Payments | Fake UPI success animation | Exact ledger, quorum, exported simulated payment request |
| Buyer | Generic PDF certificate | Evidence-backed, privacy-safe Order Passport with limitations |
| Originality | Adds many features | Solves *trust and recoverability* as one auditable workflow |

**Core jury claim:** “We don't just tell a self-help group how to organize. We give every member a voice in the production record and make every business-critical decision inspectable.”

---

## 21. Hard questions the jury will ask — defensible answers

**Q1. Why not WhatsApp + Excel?**  
They are valid baselines and should be tested. Sahakari's proposition is a governed, synchronized workflow: stage dependency checking, consent, duplicate protection, member-specific access, dispute versions and buyer provenance reports. Present *measured task time/error* comparisons rather than claiming Excel cannot perform arithmetic or automation.

**Q2. Why is this Agentic AI instead of ordinary software?**  
A bounded agent coordinates interpretation, risk explanation, candidate plans and exception-resolution proposals across independent tools. Hard constraints and financial outcomes remain deterministic; the group approves impactful actions. The agent adds value in exceptions and unstructured buyer requests, not by overriding the business process.

**Q3. Is the allocation fair?**  
We respect declared availability, approved pay rules, skills and member choice; we show distribution metrics and reasons. Jain's index is supplementary, not proof of fairness. Members can decline/review tasks and challenge their records.

**Q4. Who pays and why?**  
Potential buyers are federations or procurement partners seeking reliable fulfilment and lower reconciliation burden; user interviews must determine willingness to pay. We do not claim a validated price before pilots.

**Q5. Does your AI certify wages or ethical sourcing?**  
No. We expose evidence and group-attested decisions. Independent auditing and applicable legal verification remain separate processes.

**Q6. Can a leader cheat or alter records?**  
Application permissions, append-only corrections, member-visible sync receipts, versioned votes and exports make certain manipulation detectable. No digital design can prove every off-platform action; audits and social governance remain necessary.

**Q7. What if the internet disappears?**  
Installed PWA shell and IndexedDB event outbox permit member entry. We test a reconnect flow on a real device. Live AI, new remote data and some speech services may remain unavailable offline, with explicit fallbacks.

**Q8. Why is a ₹160 offer problematic?**  
Our illustrative operating cost is ₹260.55; the offer would fall ₹100.55 short of the modeled cost per set. These figures require evidence from an actual group's suppliers and labour arrangements before any real quotation.

**Q9. Do you need Raspberry Pi, ESP32 or sensors?**  
No. This is a software-led distributed production and trust problem. Phone + laptop + backend are sufficient; optional QR or camera props improve storytelling but do not determine correctness.

**Q10. What happens when the algorithm cannot meet the deadline?**  
It reports infeasible, identifies the stage bottleneck and proposes honest alternatives for group and buyer discussion. It never silently overloads a member or guarantees delivery.

**Q11. What is your technical moat?**  
The hard combination of offline integrity, production-stage optimization, consent and versioned member earnings. We will validate this against existing SHG enterprise tools and actual producer workflows instead of claiming no competition.

**Q12. What evidence do you have that this works?**  
Show versioned source code, passing tests, two-phone offline demonstration, scenario fixtures and signed/consented user walkthrough findings. Where evidence is missing, label a proposed feature honestly.

---

## 22. Pitch-deck outline (eight crisp slides)

1. **The human problem:** 12 women, one order, missed date and disputed earnings.
2. **Why current tools miss the execution gap:** marketplace ≠ stage-wise reliable production.
3. **Our breakthrough:** Cooperative Proof Layer + production digital twin.
4. **Live proof:** one stage-based plan, offline work record and reallocation.
5. **Live proof:** ledger dispute, group approval, Order Passport.
6. **Architecture and engineering:** solver, PWA event outbox, deterministic finance, bounded agent.
7. **Impact, evidence, and risk:** actual tests and pilot observations vs targets; honest limitations.
8. **Startup case and ask:** beachhead users, partner hypothesis, next pilot milestone.

**Presentation principle:** one diagram or three proof screenshots per slide, not paragraphs of buzzwords. During the live demo, show the actual application rather than repeating the same slides.

---

## 23. Final acceptance checklist — do not submit without checking

### Product completeness

- [ ] A buyer can create a valid order.
- [ ] A leader can cost, plan and approve an order.
- [ ] At least two members can receive and accept distinct stage-specific assignments.
- [ ] Work and quality events update a single authoritative record.
- [ ] A member can work offline and sync without double counting.
- [ ] A late task triggers a **feasible, consensual** recovery proposal.
- [ ] An earnings dispute is visible and resolved without erasing history.
- [ ] Group approval checks the correct payroll snapshot.
- [ ] A buyer can inspect a privacy-safe Order Passport.

### Technical credibility

- [ ] Capacity, costing and wage formulas reconcile on seeded data.
- [ ] Correct status shown for infeasible, conflict and insufficient evidence.
- [ ] No fabricated bank settlement, lab certification or real deployment claim.
- [ ] Automated tests and E2E demo are reproducible.
- [ ] Local hardware/browser capabilities are actually tested.
- [ ] Secrets, tenant boundaries and authorization checks are in place.

### User and startup credibility

- [ ] At least one real SHG/member workflow is validated, or all data marked illustrative.
- [ ] Target buyer and value proposition are specified.
- [ ] No unverified market share, wage or income-growth statements.
- [ ] Pilot and pricing are explicitly labelled hypotheses until tested.
- [ ] Demo works with a documented offline fallback.

---

## 24. Source register and what's verified

**Uploaded basis:** `README (13).md` — original Sahakari AI concept, 12-member scenario, multi-factor allocation, costing, Tamil audio passbook, assistive vision and listed tests. The supplied file **did not contain application or test source code**, so technical implementation/pass claims are **not independently verified** here.

**Official market context:**
- Ministry of Rural Development / PIB (2 Sep 2026), SHGs and women mobilized: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2305947&lang=1&reg=3
- PIB eSaras capabilities (2026): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2283704
- Official eSaras marketplace: https://www.esaras.in/marketplace

**Official engineering references:**
- OR-Tools CP-SAT: https://developers.google.com/optimization/cp
- OR-Tools job-shop constraints: https://developers.google.com/optimization/scheduling/job_shop
- PWA offline data/IndexedDB: https://web.dev/learn/pwa/offline-data
- PWA service-worker mechanics: https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers
- Browser speech-recognition limitations: https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

**Evidence classification:**
- **Official problem description:** supplied screenshots and original README.
- **Verified external facts:** above government/developer documentation.
- **Calculated from disclosed inputs:** ₹260.55 cost, ₹291.82 minimum target quote, 58.67 gross daily bottleneck, ₹810/₹610 member example.
- **Illustrative assumptions:** all demo product rates, member hours, stage durations, assumed members, quote inputs and late-work events.
- **Proposed but not implemented by this document:** application architecture, API endpoints, offline sync, agent, tests, reports and user interfaces.

---

## 25. Final answer to the judges

> **“Sahakari AI isn't another marketplace for women entrepreneurs. It's the missing execution and trust layer for their businesses. We turn a group order into an explainable plan, let members record and verify work even offline, identify delays before they break the promise, and ensure that every proposed earning can be inspected and challenged. Our demo proves the whole journey — from the buyer's order to the member's statement and a traceable delivery record. The group retains control of work, quality and payments.”**

### The winning-strategy rule

**Do not maximize feature count. Maximize the number of consequential claims you can prove live.**

A defensible SHG order lifecycle, tested on two phones and backed by actual user feedback, is worth far more than a complex slide deck claiming “100% fairness” or “guaranteed winning.”

**PS 8.1 recommendation:** Build the **Cooperative Proof Layer + production digital twin + consent-based recovery + auditable earnings** as one complete product. **Mandatory custom hardware: none.**
