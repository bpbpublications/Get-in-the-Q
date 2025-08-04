from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler

quantum_register = QuantumRegister(1)
classical_register = ClassicalRegister(1)
quantum_circuit = QuantumCircuit(quantum_register, classical_register)

qubit = quantum_register[0]
classical_bit = classical_register[0]

quantum_circuit.h(qubit)
quantum_circuit.measure(qubit, classical_bit)

with quantum_circuit.if_test((classical_bit, 1)):
    quantum_circuit.x(qubit)

quantum_circuit.measure(qubit, classical_bit)
quantum_circuit.draw("mpl")

quasi_dists = Sampler().run(quantum_circuit, shots=1000).result().quasi_dists[0]
