# Traceability Matrix

| Req ID | Inferred Functional Requirement | Architecture Component | Code File / Module |
|--------|---------------------------------|------------------------|--------------------|
| FR-001 | Initialize and configure Julia engine server | JuliaEngineServer | src\run_julia_engine.py |
| FR-002 | Setup custom logging for Julia engine server | JuliaEngineServer | src\run_julia_engine.py |
| FR-003 | Run Julia server with restart capability | JuliaEngineServer | src\run_julia_engine.py |
| FR-004 | Warm up connection for Julia engine server | JuliaEngineServer | src\run_julia_engine.py |
| FR-005 | Start services for Julia engine server | JuliaEngineServer | src\run_julia_engine.py |
| FR-006 | Initialize and configure Python engine server | PyEngineServer | src\run_py_engine.py |
| FR-007 | Setup custom logging for Python engine server | PyEngineServer | src\run_py_engine.py |
| FR-008 | Run gRPC server for Python engine | PyEngineServer | src\run_py_engine.py |
| FR-009 | Start services for Python engine server | PyEngineServer | src\run_py_engine.py |
| FR-010 | Initialize and configure Gateway server | GatewayServer | src\run_server.py |
| FR-011 | Setup custom logging for Gateway server | GatewayServer | src\run_server.py |
| FR-012 | Run Gateway server | GatewayServer | src\run_server.py |
| FR-013 | Run Gateway server with multiprocessing | GatewayServer | src\run_server.py |
| FR-014 | Compute dictionary from payload | Controller | src\api\controllers.py |
| FR-015 | Compute RecordBatch from payload | Controller | src\api\controllers.py |
| FR-016 | Decode request from Arrow table | Flat Arrow Schema | src\api\flat_arrow_schema.py |
| FR-017 | Encode response to Arrow table | Flat Arrow Schema | src\api\flat_arrow_schema.py |
| FR-018 | Encode error message to Arrow table | Flat Arrow Schema | src\api\flat_arrow_schema.py |
| FR-019 | Compute JSON payload | Routers | src\api\routers.py |
| FR-020 | Convert ArrowModel to Python dictionary | ArrowModel | src\model\base_model.py |
| FR-021 | Perform sanity check on ArrowModel | ArrowModel | src\model\base_model.py |
| FR-022 | Initialize LPModel with model dictionary | LPModel | src\model\lp_model.py |
| FR-023 | Perform sanity check on LPModel | LPModel | src\model\lp_model.py |
| FR-024 | Create model based on type and data | ModelFactory | src\model\model_factory.py |
| FR-025 | Initialize QPModel with model dictionary | QPModel | src\model\qp_model.py |
| FR-026 | Perform sanity check on QPModel | QPModel | src\model\qp_model.py |
| FR-027 | Initialize SolverModel with solver dictionary | SolverModel | src\model\solver_model.py |
| FR-028 | Perform sanity check on SolverModel | SolverModel | src\model\solver_model.py |
| FR-029 | Validate request input as Arrow table | API Utils | src\utils\api_utils.py |
| FR-030 | Write Arrow table to IPC bytes | API Utils | src\utils\api_utils.py |
| FR-031 | Load configuration section from file | Load Config | src\utils\load_config.py |
| FR-032 | Check Arrow COO matrix | Model Sanity Check | src\utils\model_sanity_check.py |
| FR-033 | Check variable bounds | Model Sanity Check | src\utils\model_sanity_check.py |
| FR-034 | Check objective sense | Model Sanity Check | src\utils\model_sanity_check.py |
| FR-035 | Check network socket | Network Check | src\utils\network_check.py |
| FR-036 | Create solver configuration | Pyomo Utils | src\utils\pyomo_utils.py |
| FR-037 | Monitor processes | Watcher | src\utils\watcher.py |
| FR-038 | Compute optimization using base service | BaseOptService | src\service\optimization_service\base_opt_service.py |
| FR-039 | Compute optimization using gRPC service | GrpcComputeService | src\service\optimization_service\compute_grpc_service.py |
| FR-040 | Compute optimization using Julia service | JuliaComputeService | src\service\optimization_service\compute_julia_service.py |
| FR-041 | Create optimization service based on name | OptServiceFactory | src\service\optimization_service\opt_service_factory.py |
| FR-042 | Serve gRPC server for Arrow RPC | FlightServer | src\service\optimization_service\python\pyomo\controller\arrow_rpc_server.py |
| FR-043 | Build and solve base problem | BaseProblem | src\service\optimization_service\python\pyomo\objects\base_problem.py |
| FR-044 | Initialize and solve LP problem | LPProblem | src\service\optimization_service\python\pyomo\problems\lp_problem.py |
| FR-045 | Initialize and solve QP problem | QPProblem | src\service\optimization_service\python\pyomo\problems\qp_problem.py |
| FR-046 | Run Pyomo solver with parameters | PyomoSolver | src\service\optimization_service\python\pyomo\service\opt_solver.py |