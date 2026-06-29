<div align="center">
  <!-- Cabecera GIF Tech -->
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDQwdzI3cW16Z3E3c2p4NWx2aGF6eWNwaHpxYnF5ZjZ5eTh4a2V2ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L1R1tvI9svkIWwpVYr/giphy.gif" width="100%" alt="Data Engineering Pipeline Animation" style="border-radius: 10px;" />

  <br><br>

  <a href="https://github.com/Niltra">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=00FF41&center=true&vCenter=true&width=800&lines=System.out.println(%22Data+Engineering+Zoomcamp%22);Orchestrating+Robust+Data+Workflows;Batch+%26+Streaming+Data+Processing;Building+Scalable+Data+Warehouses" alt="Typing SVG" />
  </a>
</div>

---

### 📡 System Overview 
> *Translating raw datasets into reliable analytical assets through automated, reproducible infrastructure.*

This repository documents my architectural solutions and pipeline deployments developed during the **DataTalks.Club Data Engineering Zoomcamp**. It serves as a living portfolio of my ability to design highly available data infrastructure, emphasizing clean orchestration, containerization, and scalability.

---

### ⚙️ Core Infrastructure Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,docker,postgres,gcp,terraform,apache,kafka,bash&perline=8" alt="Tech Stack" />
  </a>
</p>

---

### 📊 Deployment Roadmap & Progress

<table border="0" width="100%">
  <tr>
    <td width="30%"><b>Module 1: Infrastructure & IaC</b></td>
    <td width="70%"><img src="https://geps.dev/progress/100?color=00FF41" alt="100%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Dockerized environments and programmatic Cloud Infrastructure (GCP) deployment via <b>Terraform</b>.</i></td>
  </tr>
  
  <tr>
    <td width="30%"><b>Module 2: Workflow Orchestration</b></td>
    <td width="70%"><img src="https://geps.dev/progress/100?color=00FF41" alt="100%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Automated complex ETL/ELT pipelines using Mage/Prefect, ensuring data freshness.</i></td>
  </tr>

  <tr>
    <td width="30%"><b>Module 3: Data Warehousing</b></td>
    <td width="70%"><img src="https://geps.dev/progress/100?color=00FF41" alt="100%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Optimized schemas in <b>Google BigQuery</b> with advanced partitioning and clustering.</i></td>
  </tr>

  <tr>
    <td width="30%"><b>Module 4: Analytics Engineering</b></td>
    <td width="70%"><img src="https://geps.dev/progress/80?color=ED8B00" alt="80%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Modular data modeling for downstream BI consumption using <b>dbt (Data Build Tool)</b>.</i></td>
  </tr>

  <tr>
    <td width="30%"><b>Module 5: Batch Processing</b></td>
    <td width="70%"><img src="https://geps.dev/progress/30?color=ff0000" alt="30%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Distributed processing of massive datasets utilizing <b>Apache Spark</b>.</i></td>
  </tr>

  <tr>
    <td width="30%"><b>Module 6: Streaming Data</b></td>
    <td width="70%"><img src="https://geps.dev/progress/10?color=ff0000" alt="10%" /></td>
  </tr>
  <tr>
    <td colspan="2"><i>Real-time data ingestion and processing pipelines leveraging <b>Apache Kafka</b>.</i></td>
  </tr>
</table>

---

### 💻 Architecture Topology (Capstone Project)

```bash
# [STATUS: ARCHITECTURE IN DEVELOPMENT]

[Data Sources] (APIs / CSVs / Event Streams)
       │
       ▼
[Ingestion Layer] ──> Apache Kafka (Real-time) / Python Scripts (Batch)
       │
       ▼
[Data Lake] ────────> Google Cloud Storage (GCS)
       │
       ▼
[Orchestration] ────> Mage / Prefect (Triggering ETL jobs)
       │
       ▼
[Transformation] ───> dbt (Data Build Tool) / Apache Spark
       │
       ▼
[Data Warehouse] ───> Google BigQuery (Partitioned & Clustered)
       │
       ▼
[BI & Analytics] ───> Looker Studio / Metabase
