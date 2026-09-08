# Software Architecture Overview for OptArrow

## 1. Introduction & Purpose of the System

OptArrow is a software system designed to facilitate optimization tasks using various computational engines. The system integrates different optimization models and services, providing a robust framework for solving linear and quadratic programming problems. The primary purpose of OptArrow is to offer a scalable and efficient solution for optimization tasks, leveraging both Python and Julia engines to perform computations.

## 2. High-Level Architecture

The architecture of OptArrow is organized into several main components, each encapsulated in its respective folder. These components include:

- **API**: Handles the external interface for clients to interact with the system.
- **Models**: Defines the data structures and models used for optimization tasks.
- **Services**: Implements the core logic for optimization computations and service management.
- **Pyomo**: Provides specific utilities and classes for optimization using the Pyomo library.

## 3. Component Descriptions

### API

The API component is responsible for managing incoming requests and outgoing responses. It includes controllers and routers that process client requests, decode and encode data, and ensure proper communication with the underlying services.

- **Controllers**: Manage the logic for processing requests and computing results.
- **Flat Arrow Schema**: Handles the encoding and decoding of data using Apache Arrow for efficient data interchange.
- **Routers**: Direct requests to the appropriate controller methods.

### Models

The Models component defines the various data structures used within the system. These models represent the optimization problems and their configurations.

- **BaseModel**: An abstract base class for all models, providing common functionality.
- **LPModel and QPModel**: Specific implementations for linear and quadratic programming models.
- **ModelFactory**: A factory class for creating model instances based on type.
- **RequestModel and SolverModel**: Represent the request and solver configurations.

### Services

The Services component contains the logic for executing optimization tasks. It includes different services for handling computations and managing engine interactions.

- **BaseOptService**: A base class for optimization services, providing common computation methods.
- **GrpcComputeService and JuliaComputeService**: Implementations for handling computations using gRPC and Julia engines, respectively.
- **OptServiceFactory**: A factory class for creating service instances based on configuration.

### Pyomo

The Pyomo component provides utilities and classes specific to optimization using the Pyomo library. It includes problem definitions, solver configurations, and service implementations.

- **FlightServer**: Manages gRPC communication for optimization tasks.
- **BaseProblem and ProblemFactory**: Define and create problem instances for optimization.
- **BaseSolver and SolverFactory**: Define and create solver instances for executing optimization tasks.
- **LPProblem and QPProblem**: Specific problem implementations for linear and quadratic programming.

## 4. Data Flow / Interactions

The data flow within OptArrow begins with the API receiving requests from clients. These requests are processed by the controllers, which decode the data and validate the input. The controllers then interact with the Services component to perform the necessary computations.

The Services component utilizes the Models to instantiate the appropriate optimization problem and solver configurations. Depending on the request, the service may use either the Python or Julia engine to execute the optimization task.

Once the computation is complete, the results are encoded and sent back through the API to the client. The system ensures efficient data interchange using Apache Arrow, facilitating high-performance communication between components.

Overall, OptArrow's architecture is designed to provide a modular and scalable solution for optimization tasks, leveraging the strengths of both Python and Julia computational engines.