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
        self._ingressos_compr=[]  # Completo: chamar super().__init__ e criar lista vazia de ingressos
        
    def comprar_ingresso(self, ingresso: Ingresso):
        if isinstance(ingresso,Ingresso) !=True:
            raise ValueError("O ingresso adicionado nao e um objeto Ingressso")
        self._ingressos_compr.append(ingresso)    # Completo: adicionar ingresso à lista
        
    def listar_ingressos(self):
        for ingressos in self._ingressos_compr:
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
            self.capacidade=capacidade  # Completo: armazenar nome e capacidade?

    def __str__(self):
        return f"Palco {self.nome} - Capacidade de {self.capacidade} pessoas"

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
        if isinstance(cliente,Cliente) !=True:
            raise ValueError("O cliente adicionado nao e um objeto Cliente")
        if isinstance(ingresso,Ingresso) !=True:
            raise ValueError("O ingresso adicionado nao e um objeto Ingressso")
        if isinstance(self.palco,Palco) !=True:
            raise ValueError("O palco adicionado nao e um objeto Palco")
        
        for ingressos in cliente._ingressos_compr:
            if ingressos.codigo == ingresso.codigo:
                raise ValueError("O cliente já possui este ingresso.")
        
        ingressos_vend=0
        for clintes in self.clientes:
            ingressos_vend += len(clintes._ingressos_compr)

        if ingressos_vend + 1 > self.palco.capacidade:
            raise ValueError("O evento não tem mais capacidade para suportar pessoas.")
        
        cliente.comprar_ingresso(ingresso)
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def adicionar_funcionario(self, func:Funcionario):
        if isinstance(func,Funcionario) !=True:
            raise ValueError("O func adicionado nao e um objeto Funcionario")
        
        for funcionarios in self.equipe:
            if funcionarios==func:
                raise ValueError("Esse funcionário já está na equipe.")
        
        self.equipe.append(func)

    def listar_clientes(self):
        for clientes in self.clientes:
            print(clientes)

    def listar_equipe(self):
        for funcionario in self.equipe:
            funcionario.exibir_dados()

    def listar_ingressos(self):
        for clientes in self.clientes:
            for ingressos in clientes._ingressos_compr:
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
        if isinstance(festival,Festival) !=True:
            raise ValueError("O festival adicionado nao e um objeto Festival")

        self._festivais.append(festival)
        # Completo: adicionar festival à lista
       
    def buscar_festival(self, nome: str):
        for festivais in self._festivais:
            if festivais.nome == nome:
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
        print(f"O auditor {self.nome} entrou no horario {date.today()}")

    def auditar_festival(self,fest:Festival):
        if isinstance(fest,Festival) !=True:
            raise ValueError("O fest adicionado nao e um objeto Festival")

        a=len(fest.clientes)
        b=len(fest.equipe)
        c=0
        for clientes in fest.clientes:
            c+=len(clientes._ingressos_compr)
        print(f"= Relatório de Auditoria do Festival {fest.nome} =\n")
        print(f"Número de clientes:{a}\nIngressos vendidos:{c}\nCapacidade do palco:{fest.palco.capacidade}\nStatus da capacidade:","A capacidade máxima de pessoas está sendo respeitada\n" if c<=fest.palco.capacidade else "A capacidade máxima de pessoas não está sendo respeitada\n")
        print(f"Número de funcionários:{b}\nStatus dos funcionários:", "Está em conformidade\n" if b>0 else "Não está em conformidade\n")
    
    def __str__(self):
        return f"Auditor <{self.nome}> (ID:{self._id})"

# Completo: Implementar a classe Auditor

# -------------------------------------------------
# 11) Bloco de teste                              🡇
# -------------------------------------------------
#if __name__ == "__main__":
    """
    TODO:
      • Crie 1 empresa, 2 festivais, clientes, equipe e auditor.
      • Venda ingressos, liste participantes, audite festivais.
      • Mostre saídas no console para validar implementações.
    """
palc=Palco("Primeiro",5)
palc1=Palco("Segundo",5)

ing=Ingresso("1","normal",2.5)
ing1=Ingresso("2","normal",2.5)
ing2=Ingresso("3","normal",2.5)
ing3=Ingresso("4","normal",2.5)
ing4=Ingresso("5","normal",2.5)
ing5=Ingresso("6","normal",2.5)
ing6=Ingresso("7","normal",2.5)
ing7=Ingresso("8","normal",2.5)
ing8=Ingresso("9","normal",2.5)
ing9=Ingresso("10","normal",2.5)

festi=Festival("Musical",date.today(),"Pau dos Ferros",palc)
festi1=Festival("Musical 2",date.today(),"Àgua Nova",palc1)

f1=Funcionario('Fulano', "1112083974", "Faxineiro","registrado")
f2=Funcionario("Cicrano","222000888","Autor","registrado")

cli=Cliente("Murilo","111222333","aaaa@mail.com")
cli1=Cliente("Pedro","222111334","bbbb@mail.com")

aud=Auditor("Pedro")

emp=EmpresaEventos("XFest")

festi.adicionar_funcionario(f1)
festi.adicionar_funcionario(f2)
festi.vender_ingresso(cli,ing)
festi.vender_ingresso(cli,ing1)
festi.vender_ingresso(cli,ing2)
festi.vender_ingresso(cli,ing5)
festi.vender_ingresso(cli,ing6)


festi1.adicionar_funcionario(f1)
festi1.vender_ingresso(cli1,ing3)
festi1.vender_ingresso(cli1,ing4)
festi1.vender_ingresso(cli1,ing7)
festi1.vender_ingresso(cli1,ing8)
festi1.vender_ingresso(cli1,ing9)

emp.adicionar_festival(festi)
emp.adicionar_festival(festi1)

print("\n== Primeiro Festival ==")
festi.listar_clientes()

print("\n== Segundo Festival ==")
festi1.listar_clientes()

print("\n== Primeiro Festival ==")
aud.auditar_festival(festi)

print("\n== Segundo Festival ==")
aud.auditar_festival(festi1)

print("\n== Lista de Festivais ==")
emp.listar_festivais()