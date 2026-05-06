# Sentinel Core

Sentinel Core is my local-first household infrastructure watch partner.

This project started as a vibe coding session, but the vision behind it was serious from the beginning.

Every major decision, workflow, security boundary, UI direction, and monitoring philosophy came from me. AI was not the architect. AI was my paint brush.

I used AI to iterate faster, prototype faster, and refine ideas faster, but the ideas, research, expectations, and standards were always mine.

The goal was never to build another generic AI dashboard.

The goal was to create a private, local-first household monitoring system that helps me understand what is happening inside my own environment without depending on cloud surveillance or reckless automation.

---

# What Sentinel Core Is

Sentinel Core is a Python-based local monitoring and network awareness system designed for:

- local-first monitoring
- local knowledge-aware AI assistance
- browser-based operational awareness
- household network visibility
- troubleshooting workflows
- local reports and operational memory
- strict internet boundaries

The system is designed to:

- identify visible LAN devices
- monitor gateway and DNS behavior
- summarize active connections
- monitor listening ports
- store local reports
- surface unusual changes
- support troubleshooting workflows
- maintain long-term household infrastructure awareness

This is not intended to replace professional SIEM, EDR, or enterprise monitoring platforms.

This is a personal infrastructure watch partner for my own environment.

Use it only on networks you own or are authorized to monitor.

---

# AI-Assisted Build Philosophy

I vibe coded this.

That does not mean careless.

It means I used AI intentionally to accelerate development while I focused on architecture, security boundaries, operational thinking, UX direction, and product vision.

AI helped me move faster.

But:

- the ideas were mine
- the research was mine
- the expectations were mine
- the product direction was mine
- and the standards were mine

I did not stop until the system behaved the way I wanted.

---

# Local Knowledge System

The `knowledge/` folder is the heart of Sentinel Core.

The most important idea behind this project was creating a structured local knowledge environment that the AI can pull from.

This knowledge is not only for troubleshooting.

It is also for:

- long-term monitoring
- device awareness
- operational memory
- historical understanding
- known-services tracking
- household infrastructure context

Instead of acting like a generic chatbot with no memory of the environment, Sentinel Core uses local context to understand the home it is monitoring.

```text
knowledge/
├── index.md
├── device-registry.md
├── known-services.md
├── runbook.md
├── troubleshooting-notes.md
└── troubleshooting-pack.md
```

---

# Security Model

Sentinel Core is intentionally conservative.

Current security boundaries:

- local-only binding by default (`127.0.0.1`)
- no direct public internet exposure
- no autonomous internet browsing
- no reckless scanning behavior
- optional token-based LAN access
- generated local reports ignored by Git
- online research requests written to an outbox instead of automatically executed

Example local-only startup:

```bash
python3 -m homenet_agent serve --host 127.0.0.1 --port 8773
```

Do not expose Sentinel Core directly to the public internet.

---

# Browser Control Room

Sentinel Core includes a premium-style browser control room inspired by Velvet Core principles:

- dark premium interface
- charcoal surfaces
- brass accents
- teal highlights
- operational clarity over clutter

The dashboard may include:

- system health
- total signals
- completed checks
- active connections
- failed checks and alerts
- critical alert tracking
- operational summaries
- reports and logs
- knowledge access

The goal is not to talk to a chatbot.

The goal is to interact with a household infrastructure partner.

---

# Project Structure

```text
.
├── README.md
├── knowledge/
├── reports/
├── data/
├── outbox/
└── homenet_agent/
```

---

# Roadmap

Things I want next:

- trusted device naming
- stronger device identity mapping
- alert trend analysis
- encrypted local notes
- deeper knowledge search
- macOS notifications
- stricter LAN auth sessions
- cleaner package naming
- improved operational summaries
- stronger dashboard polish

---

# My Rule For Sentinel

Sentinel Core should be useful without being reckless.

It should help me understand my environment without overwhelming me.

It should surface what matters.

It should stay quiet when things are normal.

And it should ask for outside help carefully instead of pretending autonomy is intelligence.

That is the Velvet Core standard.
