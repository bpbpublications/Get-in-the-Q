import math
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(operational=True, simulator=False)

def create_grover_oracle(marked_states):
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    num_qubits = len(marked_states[0])
    qc = QuantumCircuit(num_qubits)
    for target_state in marked_states:
        reversed_target = target_state[::-1]
        zero_indices = [index for index in range(num_qubits) if reversed_target[index] == "0"]
        qc.x(zero_indices)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        qc.x(zero_indices)
    return qc

target_states = ["011", "100"]
grover_oracle_circuit = create_grover_oracle(target_states)
grover_operator = GroverOperator(grover_oracle_circuit)

optimal_num_iterations = math.floor(
    math.pi / (4 * math.asin(math.sqrt(len(target_states) / 2**grover_operator.num_qubits)))
)

quantum_circuit = QuantumCircuit(grover_operator.num_qubits)
quantum_circuit.h(range(grover_operator.num_qubits))
quantum_circuit.compose(grover_operator.power(optimal_num_iterations), inplace=True)
quantum_circuit.measure_all()
