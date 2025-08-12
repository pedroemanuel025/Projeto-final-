#python
#Copy
from abc import ABC, abstractmethod
import uuid
from datetime import date

# -------------------------------------------------
# 1) Interface                                    🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass

# -------------------------------------------------
# 2) Mixins                                       🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine‑o com outras classes."""
    def __init__(self):
        # TODO: gerar e armazenar um ID usando uuid.uuid4()
        id_unico = uuid.uuid4()
        pass
    def get_id(self):
        # TODO: retornar o ID
        return  uuid.uuid4

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        # TODO: imprimir no formato  [LOG] <evento>
        print(f"[LOG] {evento}")

# -------------------------------------------------
# 3) Classe base Pessoa                           🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
        # TODO: armazenar nome e cpf como atributos protegidos
    @property
    def nome(self):           
        return self._nome 
    
    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("Nome invalido")
        self._nome = valor
       # "Maria (123.456.789-00)"
        pass

# -------------------------------------------------
# 4) Ingresso — classe simples                    🡇
# -------------------------------------------------
class Ingresso:
    def __init__(self, codigo: str, tipo: str, preco: float):
        self.codigo = codigo
        self.tipo = tipo  # ex.: 'Pista', 'VIP', 'Backstage'
        self.preco = preco
    def __str__(self):
        return f"[{self.codigo}] {self.tipo} – R$ {self.preco:.2f}"

# -------------------------------------------------
# 5) Cliente                                      🡇
# -------------------------------------------------
class Cliente(Pessoa):
    """Herda de Pessoa e possui ingressos."""
    def __init__(self, nome: str, cpf: str, email: str):
        super().__init__
        self.nome = nome
        self.cpf = cpf
        self.email = email
lista_de_ingressos = []
        # TODO: chamar super().__init__ e criar lista vazia de ingressos
def comprar_ingresso(self, ingresso: Ingresso):
        lista_de_ingressos.append(ingresso)
        # TODO: adicionar ingresso à lista

def listar_ingressos(self):
        # TODO: imprimir os ingressos
        pass

# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)      🡇
# -------------------------------------------------

class Funcionario(Pessoa, IdentificavelMixin, Logavel):
    def __init__(self, nome, cargo, registro):
        self.nome = nome
        self.cargo = cargo
        self.registro = registro
        
    def dados(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Registro: {self.registro}")
    def logar_entrada(self):
        self.log(f"Entrada registrada para {self.nome} ({self.cargo})")
# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, registro
# - Métodos:
#   • exibir_dados()    → imprime nome, cargo, registro e ID
#   • logar_entrada()   → registra no log

# -------------------------------------------------
# 7) Palco (objeto de composição)                 🡇
# -------------------------------------------------
class Palco:
    """Objeto que compõe o Festival."""
    def __init__(self, nome: str, capacidade: int):
        self.nome = nome
        self.capacidade = capacidade
        # TODO: armazenar nome e capacidade
        pass
    def resumo(self):
        print(f"Palco {self.nome} - cap {self.capacidade} Pessoas")
        # TODO: retornar string "Palco X – cap. Y pessoas"
        pass

# -------------------------------------------------
# 8) Festival (composição com Palco)              🡇
# -------------------------------------------------
class Festival:
    def __init__(self, nome, data, local, palco):
        self.nome = nome
        self.data = data
        self.local = local
        self.palco = palco

    lista = ["clientes","equipe","ingressos"]

# TODO: Implementar a classe Festival
# - Atributos: nome, data, local, palco
# - Listas: clientes, equipe, ingressos
# - Métodos:
#   • vender_ingresso(cliente, ingresso)  (checar duplicidade & capacidade)
#   • adicionar_funcionario(func)
#   • listar_clientes()
#   • listar_equipe()
#   • listar_ingressos()

# -------------------------------------------------
# 9) EmpresaEventos                               🡇
# -------------------------------------------------
class EmpresaEventos:
    """Agrupa seus festivais (has‑a)."""
    def __init__(self, nome: str):
        self._nome = nome
        if len(nome) >= 3:
            print("Nome valido")
        else:
            print("Nome invalido")
        self.festivais = []
                    # TODO: validar nome (≥ 3 letras) e criar lista vazia de festivais
        pass
    @property
    def nome(self):
        self._nome
        return
        # TODO: retornar nome
    
    @nome.setter
    def nome(self, novo_nome: str):

        # TODO: validar + atualizar nome
        pass
    def adicionar_festival(self, festival):
        self.festivais.append(festival)
        # TODO: adicionar festival à lista
        pass
    def buscar_festival(self, nome: str):
        # TODO: retornar festival ou None
        pass
    def listar_festivais(self):
        for fest in self.festivais:
        # TODO: imprimir todos os festivais
         print(f" {fest.nome} ({fest.data}) em {fest.local}")
        pass

# -------------------------------------------------
# 10) Auditor (Identificável + Logável)           🡇
# -------------------------------------------------

class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome):
        self.nome = nome
        IdentificavelMixin.__init__(self)
        
    def auditor_festival(self, festival):
        if len(festival.clientes) >= festival.aplco.capacidade:
            print("Festival {festival.nome}: Capacidade completa")
        else:
            print(f"Festival {festival.nome}: OK ({len(festival.clientes)}/{festival.palco.capacidade}")
        pass

        
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_festival(fest) → verifica:
#         ▸ Nº de clientes ≤ capacidade do palco
#         ▸ existe ao menos 1 funcionário
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"

# -------------------------------------------------
# 11) Bloco de teste                              🡇
# -------------------------------------------------
if __name__ == "__main__":
    
    empresa = EmpresaEventos("Produções Musicais LTDA")

    # Criar festivais
    palco1 = Palco("paloco mundo", 10000)
    palco2 = Palco("Palco mundo2", 15000)

    festival1 = Festival("Rock In Rio", "2025-09-10", "Rio de Janeiro", palco1)
    festival2 = Festival("Lollapalooza", "2025-10-05", "São Paulo", palco2)

    empresa.adicionar_festival(festival1)
    empresa.adicionar_festival(festival2)


    # Criar clientes
    cliente1 = Pessoa("João","123.456.789-00")
    cliente2 = Pessoa("Maria","123.856.189-00")
    cliente3 = Pessoa("Pedro", "025.255.179-00")

    equipe = [Funcionario("Carlos", "Segurança", "REG001"),
              Funcionario("Ana", "Produção", "REG002")]
    # Criar auditor
    auditor = Auditor("Fiscal do Evento")
    
    festival1.vender_ingresso(cliente1)
    festival1.vender_ingresso(cliente2)
    festival2.vender_ingresso(cliente3)

    # Listar participantes
    print("\nParticipantes do Rock In Rio:", festival1.listar_participantes())
    print("Participantes do Lollapalooza:", festival2.listar_participantes())

    # Auditar festivais
    print("\n--- Auditoria ---")
    auditor.auditar_festival(festival1)
    auditor.auditar_festival(festival2)

    """
    TODO:
      • Crie 1 empresa, 2 festivais, clientes, equipe e auditor.
      • Venda ingressos, liste participantes, audite festivais.
      • Mostre saídas no console para validar implementações.
    """
    
