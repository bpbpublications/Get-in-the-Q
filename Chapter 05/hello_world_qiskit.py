from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate to qubit 0
qc.cx(0, 1)  # Apply CNOT gate with qubit 0 as control and qubit 1 as target
qc.measure_all()
qc.draw('mpl')
