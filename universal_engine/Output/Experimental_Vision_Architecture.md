```markdown
# OptArrow Optimization Integration Engine Architecture

## 1. System Boundaries & External Actors

### External Actors
- **Client**: 
  - Originates from MATLAB, Python, or other clients.
  - Sends Linear Programming (LP) or Quadratic Programming (QP) requests.
  - Communicates using JSON or Arrow IPC bytes.

## 2. Core Components

### HTTP Gateway
- **Technology**: FastAPI
- **Functionality**: 
  - Handles POST requests (`/compute`).
  - Parses HTTP payloads.
  - Returns responses in JSON or Arrow IPC format.

### Controller + Factories
- **Functionality**: 
  - Reads engine, solver, and model specifications.
  - Dispatches requests to the appropriate backend.
  - Creates model/service objects.

### Model Layer
- **Components**: 
  - LPModel
  - QPModel
- **Functionality**: 
  - Performs sanity checks.
  - Normalizes request models.

### Python Branch

#### Python Engine Adaptor
- **Component**: GrpcComputeService
- **Functionality**: 
  - Converts requests to Arrow tables.
  - Uses Python as the backend language.

#### Python Flight Server
- **Functionality**: 
  - Temporarily stores request tables.
  - Triggers solve operations.
  - Returns result tables.

#### Python/HiGHS Solver Layer
- **Functionality**: 
  - Builds solver-native models.
  - Solves LP/QP problems using `pyomo.ConcreteModel`.

### Julia Branch

#### Julia Engine Adaptor
- **Component**: JuliaComputeService
- **Functionality**: 
  - Converts requests to Arrow IPC.
  - Uses Julia as the backend language.

#### Julia Socket Server
- **Functionality**: 
  - Reads Arrow IPC bytes.
  - Converts data to Julia format.

#### JuMP Solver Layer
- **Functionality**: 
  - Builds JuMP models.
  - Executes Julia solver operations.

## 3. Data Flows & Protocols

### Data Flows
- **Client to HTTP Gateway**: 
  - HTTP Request body containing `arrow.tabular.RecordBatch`.
- **HTTP Gateway to Controller + Factories**: 
  - FastAPI request body as `pyarrow.Table`.
- **Controller + Factories to Model Layer**: 
  - HTTP Request body as Python dictionary.
- **Model Layer to Python Engine Adaptor**: 
  - Python dictionary to `pyarrow.Table`.
- **Python Engine Adaptor to Python Flight Server**: 
  - Arrow Flight stream carrying `pyarrow.Table` and Arrow record batches.
- **Python Flight Server to Python/HiGHS Solver Layer**: 
  - Python dictionary to `pyomo.ConcreteModel`.
- **Model Layer to Julia Engine Adaptor**: 
  - Python dictionary to `pyarrow.Table` to Arrow IPC.
- **Julia Engine Adaptor to Julia Socket Server**: 
  - TCP payload as Arrow IPC bytes with a 4-byte length prefix.
- **Julia Socket Server to JuMP Solver Layer**: 
  - Julia dictionary to `JuMP.Model`.

### Protocols
- **HTTP**: Used for initial client requests to the HTTP Gateway.
- **Arrow IPC**: Used for data serialization and transport between components.
- **Arrow Flight gRPC**: Used for streaming data in the Python branch.
- **TCP Socket**: Used for data transport in the Julia branch.
```
