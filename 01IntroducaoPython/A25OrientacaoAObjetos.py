"""
CLASSE ('molde')
    *Agrupamento de objetos similares que apresentam os mesmos atributos e
    métodos
    * Molde de bonecos de gesso
        * Define o formato e o tamanho
        * O molde é sempre o mesmo, porém, os objetos gerados podem ter
        características variadas, respeitando a estrutura básica do molde
        
    Classe: Cachorro Cor, Raca
        Objeto1: Cor:preto, Raca:tal
        Objeto2: Cor:marrom, Raca:poodle
        Objeto3: Cor:branco, Raca:sla
        
    Caracteristicas Cachorro (ATRIBUTOS)
        Cor, Tamanho, N de patas, Raça
    Ações Cachorro (MÉTODOS)
        Latir, Correr, Morder, Brincar
  
    Características Calculadora (ATRIBUTOS)
        Cor, Marca, Tamanho, Data de Fabricação
    Ações Calculadora (MÉTODOS)
        Somar, Subtrair, Dividir, Multiplicar
    
OBJETOS
    CARACTERÍSTICAS -> ATRIBUTOS
        Strings, Listas, Tuplas
    AÇÕES -> MÉTODOS
        Funções
    
MUNDO                     | PROGRAMAÇÃO
Molde de boneco de gesso  | Classe
Bonecos de gesso          | Objetos

"""

# ORIENTAÇÃO A OBJETOS

class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'Não é um triângulo'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'Triângulo isósceles' # Pelo menos dois lados iguais
        else:
            return 'Outro tipo de triângulo'
        
t1 = Triangulo(5, 1, 3, 4, 3)

print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)

t2 = Triangulo(8, 8, 8, 16, 9)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)

print()
print(t1.area(), t2.area())
print()
print(t1.tipo())
print(t2.tipo())
