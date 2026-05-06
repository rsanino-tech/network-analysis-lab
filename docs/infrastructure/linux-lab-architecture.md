# Linux Lab Architecture

## Purpose

This Ubuntu VM is part of the broader Sentinel Core ecosystem.

The goal was not to simply install Linux for the sake of saying I use Linux.

The goal was to intentionally build:

- a controlled cybersecurity learning environment
- a local-first infrastructure lab
- a safe testing space for Sentinel Core
- a networking and monitoring sandbox
- and a system that teaches operational awareness instead of reckless tooling usage

---

# Core Philosophy

One of the most important decisions in this project was understanding systems intentionally instead of blindly following tutorials.

This project is heavily AI-assisted, but every architectural direction, concern, security question, and implementation expectation came from me.

AI accelerated execution.
AI did not invent the vision.

I treated AI as a paint brush:
- accelerating iteration
- reducing friction
- helping explain infrastructure concepts
- and helping organize ideas into a real operational system

But the philosophy, standards, and reasoning were mine.

---

# Why Ubuntu Instead of Kali Linux

I intentionally chose Ubuntu first.

Reasoning:

- I wanted to learn Linux fundamentals before offensive tooling
- I wanted operational understanding over “hacker aesthetics”
- I wanted a stable environment for Python, networking, and Sentinel Core development
- I wanted to understand infrastructure before experimenting with advanced security tooling

This decision reflects a long-term engineering mindset instead of rushing directly into offensive security tools.

---

# Why UTM

UTM was selected because:

- it works well on Apple Silicon Macs
- it supports Apple Virtualization
- it provides isolated virtual environments
- and it creates a clean Linux lab without modifying the host operating system

The free direct-download version was intentionally chosen over the paid App Store version.

Reasoning:
- reduce unnecessary spending
- keep setup simple
- maintain direct control over tooling

---

# Virtualization vs Emulation

A major learning point during setup was understanding the difference between virtualization and emulation.

## Virtualization

Used for this Ubuntu VM.

Reasoning:
- Ubuntu ARM64 matches Apple Silicon architecture
- significantly better performance
- lower overhead
- more stable Linux experience

## Emulation

Not selected.

Reasoning:
- slower
- unnecessary for Ubuntu ARM64
- more useful for retro or incompatible systems

This distinction helped reinforce understanding of system architecture compatibility.

---

# Networking Decisions

The VM currently uses:

## Shared Network (NAT)

Reasoning:
- safer beginner configuration
- reduced exposure
- easier management
- internet access through the host Mac
- aligns with Sentinel Core’s local-first and controlled-access philosophy

An important observation during setup was that the VM reported a “wired” connection even though the Mac host uses Wi‑Fi.

This became a useful infrastructure learning moment:

Mac Wi‑Fi → UTM virtual adapter → Ubuntu virtual Ethernet interface

The VM sees a virtual Ethernet connection created by the hypervisor.

---

# Security Concerns and Questions

A major part of this project was documenting security reasoning during setup.

Questions raised during the process included:

- How trustworthy are package managers?
- How do I know packages are not malicious or corrupted?
- Why should I trust Homebrew?
- What are the risks of installing third-party tools?
- Why use virtualization instead of emulation?
- Why does the VM show a wired connection?
- What networking mode is safest initially?
- Should disk encryption be enabled?
- What should remain isolated during early learning?

These questions became part of the architecture process itself.

The goal was not just “getting Linux running.”

The goal was understanding:
- trust boundaries
- infrastructure layers
- virtualization behavior
- package ecosystems
- networking models
- and operational security decisions

---

# VM Configuration

## Virtual Machine

- Ubuntu Desktop ARM64
- Apple Virtualization enabled
- 4 GB RAM
- 2 CPU cores
- 64 GB virtual storage
- OpenGL acceleration enabled
- No shared folders initially
- NAT/shared networking enabled
- No disk encryption initially

## Hostname

`sentinel-lab`

This VM acts as:
- a Linux learning environment
- a Sentinel Core testing node
- and a local infrastructure sandbox

---

# Sentinel Core Integration Vision

The VM is part of the broader Sentinel Core infrastructure ecosystem.

Planned future integrations include:

- network monitoring
- local reporting
- Nmap-based awareness tooling
- device inventory tracking
- operational logging
- local AI summaries
- troubleshooting automation
- knowledge-base integration

The long-term goal is not aggressive scanning.

The goal is calm, contextual, local-first operational awareness.

---

# Builder Philosophy

This project represents another way to demonstrate capability beyond a resume.

The documentation intentionally preserves:
- decisions
- reasoning
- architecture tradeoffs
- and security concerns

because those details demonstrate systems thinking.

The objective is not to appear like someone who copied tools.

The objective is to demonstrate:
- intentional infrastructure design
- operational awareness
- thoughtful security reasoning
- and persistent execution.
