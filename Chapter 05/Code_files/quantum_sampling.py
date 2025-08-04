from qiskit_ibm_runtime import SamplerV2 as Sampler

sampler_instance = Sampler(backend=backend)
sampler_instance.options.default_shots = 10_000

execution_result = sampler_instance.run([optimized_circuit]).result()
measurement_distribution = execution_result[0].data.meas.get_counts()
