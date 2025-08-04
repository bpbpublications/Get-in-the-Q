from qiskit.quantum_info import SparsePauliOp 
observable_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"] 
observables = [SparsePauliOp(label) for label in observable_labels]

from qiskit_ibm_runtime import EstimatorV2 as Estimator
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)

pass_manager = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pass_manager.run(qc)

estimator = Estimator(backend=backend)
estimator.options.resilience_level = 1
estimator.options.default_shots = 5000

aligned_observables = [observable.apply_layout(isa_circuit.layout) for observable in observables]
job = estimator.run([(isa_circuit, aligned_observables)])
job_result = job.result()
circuit_result = job_result[0]
