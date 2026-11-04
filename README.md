<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Süleyman Gencay Coşkun — Computer Engineering · Autonomous UAVs · Computer Vision · Product Engineering" src="assets/banner-light.svg" width="100%">
</picture>

<br>

I'm a final-year **Computer Engineering** student at Sakarya University and a **Platform Analyst** at Duosis, where I build enterprise products end to end — web, mobile, infrastructure and security.

Outside work I captain **[ESCO-UAV](https://esco-uav.space)**, a four-person team building an autonomous fixed-wing aircraft for the TEKNOFEST Fighting UAV competition. I wrote its telemetry stack, ground station, target detector and lock-on guidance. I also ship my own iOS apps and games.

<br>

## ✈️ ESCO-UAV — autonomous fixed-wing UAV

**Role:** Team captain & software lead · 04/2026 – present

- **Telemetry & ground station** built to the competition spec: Python companion computer, FastAPI service and a Next.js live map. The companion talks MAVLink to ArduPilot.
- **Target detection:** a YOLO11 detector trained on **41,891 images**. It reached **96.5 % detection** with **zero false locks** in validation.
- **Lock-on guidance** validated end to end in ArduPlane SITL, with safety gates for area limits, altitude floors and separation from rival aircraft.
- **Airframe** designed with engineering analysis and parametric CAD, then built with laser cutting and 3D printing.

```text
camera ─▶ YOLO11 detector ─▶ tracker ─▶ guidance ─▶ MAVLink ─▶ ArduPilot
                                                                   │
competition server ◀─ FastAPI ◀─ companion computer ◀── telemetry ─┘
                         │
                         └─▶ Next.js ground station (live map, permits, tasks)
```

**Stack:** Python · FastAPI · MAVLink · ArduPilot · YOLO11 · OpenCV · Next.js · CadQuery

🌐 [esco-uav.space](https://esco-uav.space) · 📦 [esco-uav-landing](https://github.com/coskungencay/esco-uav-landing)

Earlier I worked on machine learning, image processing and data labelling with Sakarya University's **İLGERU-UAV** team, and competed in TEKNOFEST Fighting UAV 2024.

<br>

## 🏢 Work — Duosis Information Systems

**Platform Analyst** · 10/2025 – present · Istanbul (joined as a software intern in 07/2025)

| Project | What I do |
|---|---|
| **HERMES** | I'm building the company's work and support request platform end to end: web, mobile, infrastructure and security. It is in daily use by the company and its customers. |
| **LogiSlot** | I'm building a multi-tenant SaaS that digitises goods receiving and dock-appointment scheduling for factories and warehouses, across web, mobile and cloud. |
| **Consulting** | I advise enterprise customers on observability and IT process automation (Instana, Datadog, OpenText OO/SA, Kubernetes). |
| **DATALAKE** | I worked on an enterprise data-lake project. |

<br>

## 📱 Independent iOS development

I design and build my own apps in Swift and publish them on the App Store.

| App | About |
|---|---|
| **Thunder Blast: OLYMPUS** | Premium match-3 game built with SwiftUI and SpriteKit. No energy timers and no subscriptions. |
| **BALLROWS: Neon Blast** | Puzzle game. |
| **AssetFlow AI** | AI-assisted generator for App Store screenshots and marketing images. |

More at **[coskungencay.github.io](https://coskungencay.github.io)**.

<br>

## 🧰 Open source

| Repository | About |
|---|---|
| [**teknofest-ktr-olcer**](https://github.com/coskungencay/teknofest-ktr-olcer) | Pre-checks TEKNOFEST rocket design reports (KTR) against the official rubric: 95 requirements, disqualification-risk flags and HTML/JSON reports. Includes a CLI and a web dashboard. *Python* |
| [**besiktas-carsisi**](https://github.com/coskungencay/besiktas-carsisi) | Multilingual website with an admin panel for the Grand Beşiktaş Bazaar. *Next.js 15* |
| [**tarsau**](https://github.com/coskungencay/tarsau) | Command-line archiver that bundles ASCII text files into a single `.sau` archive; a systems programming course project. *C* |
| [**ci-cd-sau**](https://github.com/coskungencay/ci-cd-sau) | CI/CD and DevSecOps demo: FastAPI with GitHub Actions, Semgrep and Trivy. |

<br>

## 🛠️ Toolbox

| Area | Tools |
|---|---|
| **Languages** | Python · TypeScript · JavaScript · Swift · C |
| **Web & backend** | Next.js · React · React Native · FastAPI |
| **UAV & autonomy** | ArduPilot · MAVLink · SITL · telemetry / ground control |
| **Vision & ML** | YOLO · OpenCV · dataset building and labelling |
| **Data & infra** | PostgreSQL · Kafka (Confluent) · Docker · Kubernetes · Cloudflare |
| **Observability** | Instana · Datadog · OpenText OO / SA |
| **Design & fabrication** | Parametric CAD (CadQuery) · 3D printing · laser cutting |
| **AI-assisted dev** | Claude Code · Cursor · MCP · AI agents |

<br>

## 🎓 Education & community

- **Sakarya University**, B.Sc. Computer Engineering (final year) · 2023 – present
- **ultrAslan UNI Sakarya**, management team member · 2024 – 2026

<br>

## 📫 Contact

<a href="mailto:gencay.coskun.en@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-gencay.coskun.en%40gmail.com-F26B1D?style=flat-square&logo=gmail&logoColor=white"></a>
<a href="https://esco-uav.space"><img alt="ESCO-UAV" src="https://img.shields.io/badge/ESCO--UAV-esco--uav.space-111827?style=flat-square"></a>
<a href="https://coskungencay.github.io"><img alt="Apps" src="https://img.shields.io/badge/iOS%20apps-coskungencay.github.io-111827?style=flat-square&logo=apple&logoColor=white"></a>

Istanbul, Türkiye · I work in English and Turkish.
