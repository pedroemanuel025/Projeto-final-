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
        self._id=uuid.uuid4()

    def get_id(self):
        return self._id   
        

class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        print(f"[LOG] <{evento}>")    # Completo: imprimir no formato  [LOG] <evento>
        

# -------------------------------------------------
# 3) Classe base Pessoa                           🡇
# -------------------------------------------------
class Pessoa:
    """Classe base para pessoas do sistema."""
    def __init__(self, nome: str, cpf: str):
        self._nome=nome
        self._cpf=cpf    # Completo: armazenar nome e cpf como atributos protegidos
        
    @property
    def nome(self):
        return self._nome    # Completo: retornar o nome
        
    def __str__(self):
        return f"{self._nome} ({self._cpf})"  # Completo: "Maria (123.456.789-00)"
        

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
        super().__init__(nome,cpf)  
        self._email=email
        self._ingresos_compr=[]  # Completo: chamar super().__init__ e criar lista vazia de ingressos
        
    def comprar_ingresso(self, ingresso: Ingresso):
        self._ingresos_compr.append(ingresso)    # Completo: adicionar ingresso à lista
        
    def listar_ingressos(self):
        for ingressos in self._ingresos_compr:
            print (ingressos)   # Completo: imprimir os ingressos
        

# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)      🡇
# -------------------------------------------------
class Funcionario(Pessoa,IdentificavelMixin,Logavel):
    def __init__(self, nome:str, cpf:str, cargo:str, registro:str):
        Pessoa.__init__(self, nome, cpf)
        IdentificavelMixin.__init__(self)
        self.auditavelmixin=AuditavelMixin()
        self._cargo=cargo
        self._registro=registro

    def exibir_dados(self):
        print(f"{self._nome} [{self._cargo}] ({self._registro}) <{self._id}>")
    
    def logar_entrada(self):
        return f"O funcionario {self._nome} logou no  {date.today()}"
    
# Completo: Implementar a classe Funcionario

# -------------------------------------------------
# 7) Palco (objeto de composição)                 🡇
# -------------------------------------------------
class Palco:
    """Objeto que compõe o Festival."""
    def __init__(self, nome: str, capacidade: int):
            self.nome=nome 
            self.capacidade=capacidade
            self._capacidade_us=0  # Completo: armazenar nome e capacidade?

    def resumo(self):
        return f"Palco {self.nome} - cap. {self.capacidade} pessoas"    # Completo: retornar string "Palco X – cap. Y pessoas"
       

# -------------------------------------------------
# 8) Festival (composição com Palco)              🡇
# -------------------------------------------------
class Festival:
    def __init__(self,nome:str, data:date, local:str, palco:Palco):
        self.nome=nome
        self.data=data
        self.local=local
        self.palco=palco
        self.clientes=[]
        self.equipe=[]

    def __str__(self):
        return f"[{self.nome}] -{self.data}- ({self.local}) <{self.palco}>"

    def vender_ingresso(self, cliente:Cliente ,ingresso:Ingresso):
        for clientes in self.clientes:
            c
            if clientes==cliente:
                c+=True
            for ingressos in clientes._ingresos_compr:
                if ingressos == ingresso:
                    raise ValueError("O cliente já possui este ingresso.")
                else:
                    a=len(clientes._ingresos_compr)
                    self.palco._capacidade_us+=a

        if self.palco.capacidade<self.palco._capacidade_us:
            raise ValueError("O evento não tem mais capacidade para suportar pessoas.")
        
        else:
            if c:
                raise ValueError("O cliente já possui este ingresso.")
            else:
                cliente.comprar_ingresso(ingresso)
                self.clientes.append(cliente)

    def adicionar_funcionario(self, func:Funcionario):
        for funcionarios in self.equipe:
            c
            if funcionarios==func:
                c+=True
            
        if c:
            raise ValueError("Esse funcionário já está na equipe.")
        
        else:
            self.equipe.append(func)

    def listar_clientes(self):
        for clientes in self.clientes:
            print(clientes)

    def listar_equipe(self):
        for funcionario in self.equipe:
            funcionario.exibir_dados()

    def listar_ingressos(self):
        for clientes in self.clientes:
            for ingressos in clientes._ingresos_compr:
                print(ingressos)      
      
# Completo: Implementar a classe Festival

# -------------------------------------------------
# 9) EmpresaEventos                               🡇
# -------------------------------------------------
class EmpresaEventos:
    """Agrupa seus festivais (has‑a)."""
    def __init__(self, nome:str):
        self._nome=nome
        self._festivais=[]
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome: str):
        if not self._nome.strip():
            raise ValueError("O nome da empresa não pode estar vazio.")
        self._nome=novo_nome
        # Completo: validar + atualizar nome
        
    def adicionar_festival(self, festival:Festival):
        self._festivais.append(festival)
        # Completo: adicionar festival à lista
       
    def buscar_festival(self, nome: str):
        for festivais in self._festivais:
            if festivais._nome == nome:
                return festivais
        return
        # Completo: retornar festival ou None
        
    def listar_festivais(self):
        for festivais in self._festivais:
            print(festivais)
        # Completo: imprimir todos os festivais
        

# -------------------------------------------------
# 10) Auditor (Identificável + Logável)           🡇
# -------------------------------------------------
class Auditor(IdentificavelMixin,Logavel):
    def __init__(self,nome:str):
        super().__init__()
        self.nome=nome
    
    def logar_entrada(self):
        print(f"O auditor {self.nome} entrou no horario {date.today}")

    def auditar_festival(fest:Festival):
        a=len(fest.listar_clientes)
        b=len(fest.listar_equipe)
        c=0
        for clientes in fest.listar_clientes:
            c+=len(clientes._ingresos_compr)
        print("= Relatório de Auditoria do Festival =")
        print(f"Número de clientes:{a}\nIngressos vendidos:{c}\nCapacidade do palco:{fest.palco.capacidade}\nStatus da capacidade:","A capacidade máxima de pessoas está sendo respeitada" if c<=fest.palco.capacidade else "A capacidade máxima de pessoas não está sendo respeitada")
        print(f"Número de funcionários:{b}\nStatus dos funcionários:", "Está em conformidade" if b>0 else "Não está em conformidade")
    
    def __str__(self):
        return f"Auditor <{self.nome}> (ID:{self._id})"

# Completo: Implementar a classe Auditor

# -------------------------------------------------
# 11) Bloco de teste                              🡇
# -------------------------------------------------
if __name__ == "__main__":
    """
    TODO:
      • Crie 1 empresa, 2 festivais, clientes, equipe e auditor.
      • Venda ingressos, liste participantes, audite festivais.
      • Mostre saídas no console para validar implementações.
    """
    pass

f1=Funcionario('Fulano', "1112083974", "Lixeiro","registrado")
f1.exibir_dados()