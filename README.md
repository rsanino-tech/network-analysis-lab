# Sentinel Core

Sentinel Core is a local-first infrastructure awareness and monitoring system designed to help understand, manage, and troubleshoot a personal network environment with clarity, restraint, and operational context.

The project combines:

- local network awareness
- browser-based operational visibility
- structured infrastructure memory
- AI-assisted troubleshooting
- and controlled automation

without depending on cloud surveillance, reckless scanning behavior, or fully autonomous decision-making.

---

# Why I Built It

Most consumer monitoring tools either:
- expose too much to the cloud,
- overwhelm users with noise,
- or prioritize automation over understanding.

Sentinel Core was built around a different philosophy:

> understand the environment first.

The goal was never to create another generic AI dashboard.

The goal was to build a local infrastructure partner that helps me:

- understand my network
- track operational changes
- preserve infrastructure knowledge
- and troubleshoot issues with context instead of guesswork

This repository also documents the reasoning behind architectural, networking, and security decisions throughout the build process.

---

# System Overview

Sentinel Core is designed for:

- local-first monitoring
- household network visibility
- device awareness
- operational summaries
- connection monitoring
- local report generation
- AI-assisted troubleshooting
- and long-term infrastructure context

Core capabilities include:

- identifying visible LAN devices
- monitoring gateway and DNS behavior
- summarizing active connections
- monitoring listening ports
- generating local operational reports
- surfacing unusual changes
- preserving known-service context
- maintaining operational memory over time

This is not intended to replace enterprise SIEM or EDR platforms.

Sentinel Core is intentionally personal, local, and operationally focused.

---

# Architecture Philosophy

The system follows a local-first model.

Current design principles include:

- local execution before cloud dependency
- operational clarity over aggressive automation
- explainable workflows over hidden decision-making
- infrastructure awareness over "AI magic"
- controlled security boundaries
- conservative network behavior

The objective is not to create an autonomous security system.

The objective is to create a trustworthy operational companion that helps surface meaningful information without creating unnecessary risk.

---

# AI-Assisted Development

This project was heavily AI-assisted.

I am still early in my journey within infrastructure, cybersecurity, and systems engineering, so part of this repository intentionally documents the learning process alongside the implementation.

AI accelerated:

- iteration
- prototyping
- interface refinement
- workflow organization
- and implementation speed

But the architecture, operational direction, monitoring philosophy, security concerns, and infrastructure decisions came from me.

I used AI as an accelerator — not as a replacement for judgment.

One of the goals of this repository is to document not only the tooling itself, but the reasoning, tradeoffs, questions, and security considerations behind the environment over time.

---

# Local Knowledge System

The `knowledge/` directory is one of the most important parts of Sentinel Core.

Instead of treating the AI like a stateless chatbot, the system uses structured local knowledge to maintain operational context about the environment it monitors.

The knowledge system supports:

- device awareness
- operational memory
- troubleshooting context
- historical tracking
- known-service awareness
- infrastructure understanding

```text
knowledge/
├── index.md
├── device-registry.md
├── known-services.md
├── runbook.md
├── troubleshooting-notes.md
└── troubleshooting-pack.md
```

The long-term vision is to create an environment-aware assistant that can reason about local infrastructure using preserved context instead of temporary conversations.

---

# Security Model

Sentinel Core is intentionally conservative.

Current security boundaries include:

- local-only binding by default (`127.0.0.1`)
- no direct public internet exposure
- no autonomous browsing behavior
- no uncontrolled scanning behavior
- optional token-based LAN access
- generated reports excluded from Git tracking
- online research requests written to an outbox instead of automatically executed

Example local-only startup:

```bash
python3 -m homenet_agent serve --host 127.0.0.1 --port 8773
```

This project is intended only for networks you own or are authorized to monitor.

---

# Browser Control Room

Sentinel Core includes a browser-based operational dashboard designed around clarity and infrastructure awareness.

Dashboard concepts include:

- system health
- active connections
- operational summaries
- failed checks and alerts
- device visibility
- reports and logs
- knowledge access
- monitoring workflows

The goal is not endless notifications.

The goal is awareness.

---

# Linux Infrastructure Lab

The project now includes a dedicated Ubuntu-based infrastructure lab running through UTM virtualization on Apple Silicon.

The Linux environment exists to support:

- network analysis
- operational testing
- infrastructure learning
- future Sentinel Core integrations
- and controlled experimentation

Architecture and infrastructure decisions are documented in:

```text
docs/infrastructure/linux-lab-architecture.md
```

This includes:

- virtualization decisions
- networking choices
- package trust concerns
- local-first reasoning
- and infrastructure design philosophy

---

# Project Structure

```text
.
├── README.md
├── knowledge/
├── reports/
├── data/
├── outbox/
├── docs/
└── homenet_agent/
```

---

# Roadmap

Planned future improvements include:

- trusted device naming
- stronger device identity mapping
- alert trend analysis
- encrypted local notes
- deeper knowledge search
- macOS notifications
- stricter LAN authentication
- cleaner package structure
- improved operational summaries
- expanded monitoring workflows
- stronger dashboard polish

---

# Final Principle

Sentinel Core should help explain the environment without becoming noise.

It should surface what matters.

It should stay quiet when systems are healthy.

And it should support informed decision-making instead of pretending autonomy is intelligence.
