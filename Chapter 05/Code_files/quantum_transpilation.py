from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

backend_target = backend.target
pass_manager = generate_preset_pass_manager(target=backend_target, optimization_level=3)
optimized_circuit = pass_manager.run(quantum_circuit)
