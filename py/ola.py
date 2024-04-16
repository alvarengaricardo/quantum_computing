from qiskit import QuantumCircuit, execute, Aer

# Cria um circuito quântico com 4 qubits e 4 bits clássicos
qc = QuantumCircuit(4, 4)

# Aplica uma porta Hadamard em todos os qubits para criar uma superposição
for qubit in range(4):
    qc.h(qubit)

# Mede os qubits
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

# Escolhe o simulador Aer para executar o circuito
simulator = Aer.get_backend('qasm_simulator')

# Executa o circuito quântico no simulador
job = execute(qc, simulator, shots=1)

# Obtém os resultados
result = job.result()

# Imprime o resultado
counts = result.get_counts(qc)
print("Olá, Mundo Quântico! Resultado: ", counts)
