graph TD
    subgraph "External Input"
        News[News Article / URL Seed]
    end

    subgraph "AI & Intelligence Layer"
        LLM[Spring AI Model via Gemini/Ollama]
    end

    subgraph "Project 1: Seed Ingestor"
        Ingestor[Graph Extraction Service]
    end

    subgraph "Project 2: Persona Factory"
        Factory[Agent Generation Service]
    end

    subgraph "Project 3: The Arena"
        Arena[Simulation Engine]
        VThreads((Java 21 Virtual Threads))
    end

    subgraph "Project 4: The Oracle"
        Oracle[Reporting Service]
        Report[Final Predictive Report]
    end

    subgraph "Data Storage Layer"
        Neo4j[(Neo4j: Knowledge Graph)]
        Redis[(Redis: Fast Persona Cache)]
        PG[(PostgreSQL + pgvector: Social Memory)]
    end

    %% Phase 1: Ingestion
    News --> Ingestor
    Ingestor -->|1. Extract Entities| LLM
    Ingestor -->|2. Save Graph| Neo4j

    %% Phase 2: Persona Creation
    Factory -->|3. Read Stakeholders| Neo4j
    Factory -->|4. Generate Personas| LLM
    Factory -->|5. Cache Active Agents| Redis

    %% Phase 3: Swarm Simulation
    Arena -->|6. Fetch Active Agents| Redis
    Arena -->|7. Orchestrate Concurrency| VThreads
    VThreads <-->|8. Agent Debates| LLM
    VThreads -->|9. Save Interaction Logs| PG

    %% Phase 4: Reporting
    Oracle -->|10. Read Full History| PG
    Oracle -->|11. Summarize Consensus| LLM
    Oracle -->|12. Output PDF/JSON| Report
    
    %% Styling
    classDef project fill:#0a5c36,stroke:#333,stroke-width:2px,color:#fff;
    class Ingestor,Factory,Arena,Oracle project;
